#!/usr/bin/env python
#Learn how this works here: http://youtu.be/pxofwuWTs7c
 
import urllib2
import json
import pymysql
from json_connection import database
from json_connection import json_l
conn=database()
conn.connect('coding_club')
conn.cursor.execute("SELECT name_of_repos FROM git_repos ")
list_of_repos=set()
repos=conn.cursor.fetchall()
for r in repos:
    list_of_repos.add(r[0])
conn.cursor.execute("SELECT scholar_id,github_h FROM student_info ")
repo_q=conn.cursor.fetchall()
for q in repo_q:
	repo_scholar_id=q[0]
	repo_handle=q[1]
	points=0
	repo_url="https://api.github.com/users/"+q[1]+"/repos"
	repo_ob=json_l()
	repo_data=repo_ob.fetch_data_from_api(repo_url)
	for i in range(len(repo_data)):
		repo_name=repo_data[i]['name']
		repo_stars=int(repo_data[i]['stargazers_count'])
		fork_status=repo_data[i]['fork']
		print repo_name, fork_status
		if fork_status==False:
			if repo_name in list_of_repos or repo_stars>=100:
				points+=25
				print q[1],repo_name
	print q[1], points
