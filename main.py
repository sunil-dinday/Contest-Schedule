import requests
from datetime import datetime
import json
#Used to get list of all active codeforces contest
def codeforces():
	data=requests.get("http://codeforces.com/api/contest.list?gym=false&count=10")
	contests=[]
	data=data.json();
	if data['status']=="OK":
		result=data['result']
		for rslt in result:
			if rslt['phase']=="BEFORE":
				contests.append(rslt)
			if rslt['phase']=="FINISHED" :
				break;			
	with open("Contest.txt","w") as file:
		#if len(contests)!=0:
		for item in contests:
			file.write("Contest Name: ")
			file.write((item['name'].encode('utf8')+"\n"))
			file.write("Duration: "+str((item['durationSeconds']/(60*60)))+" Hours\n")
			file.write("Start time: "+ datetime.fromtimestamp(int(item['startTimeSeconds'])).strftime('%Y-%m-%d %H:%M:%S'))
			file.write("\n\n")


codeforces()