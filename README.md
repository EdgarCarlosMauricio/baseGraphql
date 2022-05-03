# baseGraphql
Modelobase de una mutacion y una query en graphql en el servidor .37 de DATASIS https://data.sis.co:334/

# Contexto
### El encargado de ejecutar el mod_wsgi para que al entrar a la carpeta se ejecute el codigo PYTHON es el archivo .htaccess
### Los archivos que se encuentran en la carpeta modulo, realmente no van hay sino en la carpeta /usr/lib/python3/dist-packages
### Y todas las API se encuentran en carpetas en el directorio /var/www/html/
## Se llama en https://data.sis.co:334/baseGraphql/base

# QUERY
```
query consultaBase($tipoFilter: String!, $dataFilter: String!){
  usuarios(tipoFilter: $tipoFilter, dataFilter: $dataFilter) {
    total
  }
}

```
### Variables, tenemo datafilter y tipofilter, pero no las usamos
```
{
  "tipoFilter": "",
  "dataFilter": ""
}       
```
# MUTACION
### En Altair, Postman, Insomnia, Thunder o Cualquier Framework De Front
```
mutation  pepe($ans: String!, $numradicado: String!){
  insertPqrs(pqrsData: {ans:$ans  numradicado: $numradicado }) {
    ok
    pqrsNew {
      numradicado
      ans
    }
 }
}
```
### Variables
```
{
  	"ans": "8",
    "numradicado": "225874/2021*pepe"
}
```