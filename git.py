#!/usr/bin/env python
#Learn how this works here: http://youtu.be/pxofwuWTs7c
 
import urllib2
import json
import pymysql
from json_connection import database
from json_connection import json_l
from util import cl_insert_contribution
from date_time_git import cl_date_time_git
from util import extract_git_identification

conn=database()
conn.connect('coding_club')
conn.cursor.execute("SELECT name_of_repos FROM git_repos ")
list_of_repos=set()
repos=conn.cursor.fetchall()
for r in repos:
    list_of_repos.add(r[0])
conn.cursor.execute("SELECT scholar_id, github_h FROM student_info ")
handles=conn.cursor.fetchall()
for i in handles:
    if i[1]!=None:
        scholar_id=i[0]
        url = 'https://api.github.com/users/'+str(i[1])+'/events/public' 
        d=json_l()
        data=d.fetch_data_from_api(url)
        points=0
        for j in range(len(data)):
            if data[j]['type']=="PullRequestEvent" :
                ob_git=extract_git_identification()
                ob_git.me_data(data,j)
                ob_date_time_git=cl_date_time_git(ob_git.str_date_time)
                start_date=ob_date_time_git.convert_into_date()
                commit_time=ob_date_time_git.convert_into_epoch()
                current_time=ob_date_time_git.current_epoch_time()
                yesterday_time=current_time-86400
                data1=d.fetch_data_from_api(ob_git.req_url)
                ob_git.me_data1(data1)
                if data1['state']=="closed" or ob_git.name_of_repo in list_of_repos:
                    points=25
                    ins=cl_insert_contribution(i[0],points,start_date,"gt",ob_git.git_id)
                    ins.insert_contribution()


                    
                '''if(commit_time>yesterday_time):
                    data1=d.fetch_data_from_api(ob_git.req_url)
                    ob_git=extract_git_identification(data,j,data1)
                    if data1['state']=="closed" or name_of_repo in list_of_repos:
                            points=25
                            print i[1],name_of_repo,i[0],points,start_date,"gt",git_id
                            ins=cl_insert_contribution(i[0],points,start_date,"gt",ob_git.git_id)
                            ins.insert_contribution()
                else:
                    break'''