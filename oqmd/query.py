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

def get_data():
    conn = get_conn()
    with conn:
            
        cur = conn.cursor()
        cur.execute(sql_columns_join)
        column_names = cur.fetchall()
        column_list = [name[0] for name in column_names]
        # print(len(column_list)) 27

        cur.execute(sql_select)
        data = cur.fetchall()
        data_list = [d for d in data]

    return column_list, data_list

def output(column_list, data_list):
    for data in data_list:
        result = {}
        print('-----------------------------------')

        for i, d in enumerate(data):
            column = column_list[i]
            output = d
            result[column] = output
        pprint(result)
        

# sql_select = ''' SELECT cc.*, cp.*
#                    FROM calculations cc
#              INNER JOIN compositions cp
#                      ON cc.composition_id = cp.formula
#                   WHERE cc.composition_id = 'Ba1 O3 Ti1' 
#                   LIMIT 10
#              '''

sql_select = ''' SELECT cc.*, cp.*
                   FROM calculations cc
             INNER JOIN compositions cp
                     ON cc.composition_id = cp.formula
                  WHERE cc.composition_id = 'Fe1 Ni1' 
                  LIMIT 10
             '''

sql_columns_join = ''' SELECT COLUMN_NAME
                         FROM INFORMATION_SCHEMA.COLUMNS
                        WHERE TABLE_NAME = 'calculations'
                        UNION ALL
                       SELECT COLUMN_NAME
                         FROM INFORMATION_SCHEMA.COLUMNS
                        WHERE TABLE_NAME = 'compositions'
                    '''

column_list, data_list = get_data()
output(column_list, data_list)