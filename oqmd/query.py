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


sql_select = ''' SELECT cc.id, cc.path, cp.formula
                   FROM calculations cc
             INNER JOIN compositions cp
                     ON cc.composition_id = cp.formula
                  WHERE cc.composition_id = 'Ba1 O3 Ti1' 
             '''

sql_columns = ''' SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                   WHERE TABLE_NAME = 'calculations'
              '''


conn = get_conn()
    
with conn:
        
    cur = conn.cursor()
    cur.execute(sql_columns)
    rows = cur.fetchall()
    pprint([row for row in rows])