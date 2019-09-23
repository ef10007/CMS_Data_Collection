import os
import requests
from pprint import pprint
import pymysql
import json

def get_conn():
    return pymysql.connect(
    host=os.getenv('gibbs_host'),
    user=os.getenv('oqmd_user'),
    password=os.getenv('oqmd_pw'),
    port=3306,
    db='oqdb',
    charset='utf8')

# print(os.getenv('oqmd_user'))

sql_select = 'select * from atoms limit 10'

conn = get_conn()
    
with conn:
        
    cur = conn.cursor()
    cur.execute(sql_select)
    rows = cur.fetchall()
    print([row for row in rows])