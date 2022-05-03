# SIS.co Innovacion fjaramillo 20190129 1118 - 6 days - 20200422 1016
import psycopg2
#import pyodbc #Uncomment to 27


def pgsis_analytics():
    pg_conn = psycopg2.connect(host='172.30.0.27', database='sis_analytics',
                               user='sis_bigdata', password='F4llst4ck2020*')
    return pg_conn


def sssis_analytics():
    ss_conn = pyodbc.connect(Driver='{ODBC Driver 17 for SQL Server}', Server='172.30.0.39',
                             Database='soat_gruposis', UID='Bigdata', pwd='F8FM2h8foI*')
    return ss_conn


def pgsis_aes():
    key_aes = 'd4t41nn0v4c10ns1s'
    return key_aes


def pgsis_ip():
    key_ip = '172.30.0.253'
    return key_ip


def pgsis_token():
    key_ip = 'da2-57bklqvhtjd3lid2zr3vawzxh4'
    return key_ip
