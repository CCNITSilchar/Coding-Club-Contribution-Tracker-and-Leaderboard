import urllib2
import json
import pymysql
from json_connection import json_l
from json_connection import database
from util import cl_insert_contribution
from cl_calculation import calculation
from util import gen_ins

class contribution:
    conn=database()
    conn.connect("coding_club")
    def fetch_scholar_id_and_handle(self):
        self.conn.cursor.execute("SELECT scholar_id,codeforces_h  FROM student_info")
        self.scholar_id_and_handle =self.conn.cursor.fetchall()

    def fetch_scholar_id_and_handle_for_new_user(self):
        self.conn.cursor.execute("SELECT scholar_id,codeforces_h  FROM student_info WHERE validated_user=(%s) AND new_user=(%s)",("1","1"))
        self.scholar_id_and_handle_new =self.conn.cursor.fetchall()

    def fetch_id_of_contest(self):
        self.conn.cursor.execute("SELECT id ,start_date, processed FROM codeforces_contests ")
        self.id_contest = self.conn.cursor.fetchall()

    def generate_complete_url(self,id_of_contest,status):
        if(status=="old"):
            self.fetch_scholar_id_and_handle()
            self.list_of_scholar_id_and_handle=self.scholar_id_and_handle
        else:
            self.fetch_scholar_id_and_handle_for_new_user()
            self.list_of_scholar_id_and_handle=self.scholar_id_and_handle_new

        self.id_of_contest=id_of_contest
        self.url="http://codeforces.com/api/contest.standings?contestId="
        self.url+=(self.id_of_contest+'&handles=')
        self.e=0
        for self.row in self.list_of_scholar_id_and_handle:
            self.scholar_no = self.row[0]
            self.c_h=str(self.row[1])
            if self.c_h!=None:
                if self.e==0:
                    self.url=self.url+self.c_h
                    self.e=self.e+1
                else:
                    self.url=self.url+';'+self.c_h
        self.url+='&showUnofficial=false'; 

        
    def update_processed_of_contest(self,id_of_contest):
        self.conn.cursor.execute('''UPDATE codeforces_contests SET processed=
                  (%s) WHERE id=(%s)''',
                  (True,self.id_of_contest))
        self.conn.db.commit()

    def update_user_status(self):
        self.fetch_scholar_id_and_handle_for_new_user();
        for self.rows in self.scholar_id_and_handle_new :
            self.conn.cursor.execute('''UPDATE student_info SET new_user=
                      (%s) WHERE scholar_id=(%s)''',
                      ("0",self.rows[0]))
        self.conn.db.commit()
    
    def select_scholar_id_of_a_handle(self,handle):
        self.handle=handle
        self.conn.cursor.execute("SELECT scholar_id from student_info WHERE codeforces_h=(%s)",(str(self.handle)))
        self.scholar_id=self.conn.cursor.fetchone()

    def assign_contest_details(self,current_contest):
        self.current_contest=current_contest
        self.process=self.current_contest[2]
        self.id_of_contest=str(self.current_contest[0])
        self.start_date_of_contest=self.current_contest[1]
