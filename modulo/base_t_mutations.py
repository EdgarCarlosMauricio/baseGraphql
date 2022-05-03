# import config_sis
import os
import sys
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import re
import string
import graphene
from collections import namedtuple
# Librerias para enviar emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Import Config
import sis_t_config

__version__ = "2.0.0"

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

# 1.2 Input Models
# De la Mutacion


class PqrsNumRadicadoInputx(graphene.InputObjectType):
    numradicado = graphene.String(required=True)
    ans = graphene.String(required=True)

# 1.3 Rta Models

class PqrsNumRadicadox(graphene.ObjectType):
    numradicado = graphene.String()
    ans = graphene.String()


# 1.5 Llamada De Mutation Principal
class ModifyPqrsNewxx(graphene.Mutation):
    class Arguments:
        pqrs_data = PqrsNumRadicadoInputx(required=True)

    ok = graphene.Boolean()
    pqrs_new = graphene.Field(lambda: PqrsNumRadicadox)

    def mutate(self, info, pqrs_data):
        pqrs_new = set_pqrs_numradicado(pqrs_data.ans, pqrs_data.numradicado)

        if pqrs_new == 'ok':
            ok = True
        else:
            ok = False

        return ModifyPqrsNewxx(pqrs_new=pqrs_new, ok=ok)

# 1.6 Funcion De Ejecucion De La Mutacion
#  insertPqrs(pqrsData: { numradicado: $numeroradicado, ans: $ans }) { ok pqrsNew { numradicado ans } } }
def set_pqrs_numradicado(ans, numradicado):
    pg_connect()
    global pg_conn, response_body

    try:
        pg_q = "INSERT INTO pqrs_new_sch_v1.pqrs (numero_siniestro, ans) values ('" + \
            numradicado+"', '"+ans+"')"
        pg_cursor = pg_conn.cursor(cursor_factory=RealDictCursor)
        pg_cursor.execute(pg_q)
        pg_conn.commit()
        if pg_cursor.rowcount == 1:
            pqrs_new = 'ok'
        else:
            pqrs_new = 'error'
        pg_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        response_body = "Notice: check set"
        pqrs_new = 'errorX'
    return pqrs_new