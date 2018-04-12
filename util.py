import pymysql
from json_connection import database

class cl_insert_student_info(object):

    def __init__(self,sl_no,scholar_id , mail_id , name , codeforces_h , earth_h,spoj_h,codechef_h,github_h,validate,processed):
        self.sl_no=sl_no
        self.scholar_id=scholar_id
        self.mail_id=mail_id
        self.name=name
        self.codeforces_h=codeforces_h
        self.earth_h=earth_h
        self.spoj_h=spoj_h
        self.codechef_h=codechef_h
        self.github_h=github_h
        self.validate=validate
        self.processed=processed

    def insert_student_info(self):
        ob_db=database()
        ob_db.connect("coding_club")
        
        #print (self.scholar_id,self.mail_id,self.name,self.codeforces_h,self.earth_h,self.spoj_h,self.codechef_h,self.github_h), "taken+p"  '''
        ob_db.cursor.execute('''INSERT INTO student_info (sl_no,scholar_id,mail_id,name,codeforces_h,earth_h,spoj_h,codechef_h,github_h,validate,processed) VALUES
                          (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''',
                          (self.sl_no,self.scholar_id,self.mail_id,self.name,self.codeforces_h,self.earth_h,self.spoj_h,self.codechef_h,
                            self.github_h,self.validate,self.processed))
        ob_db.close()


class cl_insert_contribution(object):

    def __init__(self,scholar_id,score,start_date_of_contest,type_of_contest,id_of_contest):
        self.scholar_id=scholar_id
        self.score=score
        self.start_date_of_contest=start_date_of_contest
        self.type_of_contest=type_of_contest
        self.id_of_contest=id_of_contest

    def insert_contribution(self):
        ob_db=database()
        ob_db.connect("coding_club")
        ob_db.cursor.execute('''INSERT INTO contribution (scholar_id,score,start_date,type_of_contest,id) VALUES
          (%s,%s,
          %s,%s,
          %s) ''',
          (self.scholar_id,self.score,self.start_date_of_contest,self.type_of_contest,self.id_of_contest))
        ob_db.close()

class gen_ins(object):

    def __init__(self,table_name,**kwargs):
        self.num=len(kwargs)
        self.table_name=table_name
        print self.num
        self.placeholder = ', '.join(['%s'] *len(kwargs))
        self.columns = ', '.join(kwargs.keys())

    def ins(self):

        ob_database=database()
        ob_database.connect("coding_club")
        print "p: ", self.placeholder
        for key,value in kwargs.iteritems():
                        print key,value
        self.st1="INSERT INTO %s (%s) VALUES (%s) " % (self.table_name,self.columns,self.placeholder)
        ob_database.cursor.execute(self.st1,kwargs.values())
        ob_database.close()

class extract_git_identification():

    def me_data(self,data,j):
        self.data=data
        self.j=j
        self.str_date_time=data[j]['payload']['pull_request']['created_at']
        self.git_id=data[j]['id']
        self.req_url=data[j]['payload']['pull_request']['url']

    def me_data1(self,data1):
        self.data1=data1
        self.stars=int(data1['base']['repo']['stargazers_count'])
        self.name_of_repo=data1['head']['repo']['name']

class cl_insert_git_repos(object):

    def __init__(self,sl_no,name_of_repos):
        self.sl_no=sl_no
        self.name_of_repos=name_of_repos

    def cl_insert_git_repos(self):
        ob_db=database()
        ob_db.connect("coding_club")
        ob_db.cursor.execute('''INSERT INTO git_repos VALUES
          (%s,%s) ''',
          (self.sl_no,self.name_of_repos))
        ob_db.close()



