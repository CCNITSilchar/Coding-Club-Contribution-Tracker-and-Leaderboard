import urllib2
import json
import pymysql
from json_connection import json_l
from json_connection import database
from util import cl_insert_contribution
from cl_calculation import calculation
from util import gen_ins
from class_contribution import contribution
from contest_list import cl_contest_list

conn=database()
conn.connect("coding_club")
ob_contest_list=cl_contest_list()
ob_contest_list.insert_contest_list()
ob_con=contribution()
ob_con.fetch_id_of_contest()
for current_contest in ob_con.id_contest:
    print("enter")
    ob_con.assign_contest_details(current_contest)
    if ob_con.process=="0":
        ob_con.generate_complete_url(ob_con.id_of_contest)
        print ob_con.url
        ob_data=json_l()
        data=ob_data.fetch_data_from_api(ob_con.url)
        length_of_row=len(data['result']['rows'])
        if length_of_row==0:
            ob_con.update_processed_of_contest(ob_con.id_of_contest)
            continue
        for i in range(length_of_row):
            handle= data['result']['rows'][i]['party']['members'][0]['handle']
            ob_calc=calculation()
            score=ob_calc.cal_points(data,i)
            print handle
            ob_con.select_scholar_id_of_a_handle(handle)
            ob_insert_contribution=cl_insert_contribution(ob_con.scholar_id,score,ob_con.start_date_of_contest,"cf",ob_con.id_of_contest)
            ob_insert_contribution.insert_contribution()
        ob_con.update_processed_of_contest(ob_con.id_of_contest)
conn.close()