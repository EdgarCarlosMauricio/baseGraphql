import config_sis
import os
import sys
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import re
import string
import graphene
from collections import namedtuple
import requests

# 1. Import Config
import sis_t_config

# 19042022
__version__ = "1.0"

# 0. Global
pg_conn = None
response_body = ""

# 0.1 PgSql


def pg_connect():
    global pg_conn, response_body
    try:
        pg_conn = config_sis.pgsis_analytics()
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check DB Conn"

# 1. Models

# 1.2 Input


class TotalUsuarios(graphene.ObjectType):
    total = graphene.String()

# 2. Data


def get_usuarios(pg_conn, tipo_filter, data_filter):
    global response_body
    gql = []

    try:
        query = "SELECT count(*) AS total FROM pqrs_new_sch.pqrs_vw A"
        cur = pg_conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        pg_conn.commit()
        resultado = cur.fetchall()
        for y in resultado:
            gql.append(TotalUsuarios(total=y["total"]))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check gets"
        gql = TotalUsuarios(total=str(error))
    return gql
