# SIS.co Innovacion acsanchez 20200124 1155 - 1 days - 20200124 1156
import graphene

# 1. Models
# 1.1 Interface


class Estandar(graphene.Interface):
    fecha_registro = graphene.String()
    estado = graphene.String()
