# rest-flask
Este es un ejemplo de cómo construir un servicio web (RESTful) con las siguientes librerías:

|Api | Versión |
|----------------------------|-----------------|
| Flask  | 2.0.1 |
| Flask-RESTful |  0.3.9  |
| Flask-SQLAlchemy  | 2.5.1 |
| marshmallow | 3.13.0 |


En este caso utilizamos **Flask-RESTful** para aprovechar los mecanismos que incorpora, como es el metodo **add_resource**, 
que permite redactar en una clase la definición de los métodos **get, post , put, delete , etc**. de la consulta HTTP, 
 y colocar la ruta como un argumento . Esto ayuda a comprender mejor la funcionalidad de una api y permite trabajar con archivos pequeños.

por ejemplo:
```
api.add_resource( ClaseConLosMetodosDeConsultaHTTP , '/ruta' )
```

**Flask-SQLAlchemy**  es una api que permite definir el modelado de datos almacenados en una base de datos SQL 
y soporta **PostgreSQL , MySQL , MariaDB , SQLite , Oracle y Microsoft SQL** Server. En este ejemplo hicimos 
uso de esta api ya que permite adjuntar el manejo de la sesión a la aplicación, pero considero que cuando en 
la implementación es necesario incorporar mecanismos que no tienen como disparador una consulta HTTP, es mejor
utilizar **SQLAlchemy**  ya que la definición del modelado se podrá importar en cualquier modulo.  

**Marshmallow** es una api que permite **serializar y deserializar estructuras de datos**. En este ejemplo 
fue utilizado para la validación de los datos de entrada y la serialización  de objetos  creados por 
Flask-SQLAlchemy , esto con el fin de incorporar un mecanismo que revise la integridad de los datos y 
debido a que en la documentación de flask-restful menciona que **reqparse será remplazado** y 
recomiendan utilizar marshmallow , se consideró como la mejor alternativa. 
