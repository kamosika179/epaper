"""
toggl_python.py

Copyright kamosika
Released under the MIT liense
https://opensource.org/licenses/MIT

Date: 2022-08-15
"""

import os
import requests
import pprint
import datetime
import makeImage

def get_total_time_per_day_and_create_image():
    toggl_api_key = os.environ['TOGGL_API']

    target_url = "https://api.track.toggl.com/reports/api/v2/weekly"

    headers = {"Content-Type" : "application/json"}
    
    f = open(os.path.dirname(os.path.abspath(__file__))+'/settingfile.txt',"r").readlines()
    
    today = datetime.date.today()
    td = datetime.timedelta(days = today.weekday())
    since = today - td

    querys = {"since" : since,
              "user_agent" : f[0],
              "workspace_id" : f[1],}


    response = requests.get(target_url,params=querys,headers=headers,auth=requests.auth.HTTPBasicAuth(toggl_api_key,"api_token"))
    #秒数*1000した値がweek_totalsに入っている？

    prev_minutes_per_day = [ 0 if x==None else x for x in response.json()['week_totals']]
    minutes_per_day = [ float(format(x/(3600*1000), '.1f')) for x in prev_minutes_per_day]
    
    makeImage.print_image(working_hours = minutes_per_day[:-1])
    #pprint.pprint(minutes_per_day[:-1])

get_total_time_per_day_and_create_image()

