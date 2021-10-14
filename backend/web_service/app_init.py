from flask import Flask
from flask_restful import Api
from waitress import serve
from flask_sqlalchemy import SQLAlchemy

from model.init_db import db

from client.task_management import TaskManagemet
from client.task_management import NewTask
from client.task_management import TaskList

from client.user_management import UserManager
from client.user_management import NewUser
from client.user_management import UserList

app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test@localhost:3305/systemdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api( app )
db.init_app(app)

api.add_resource( TaskManagemet , '/task/<string:id_task>' )
api.add_resource( NewTask , '/newtask' )
api.add_resource( TaskList , '/tasklist' )

api.add_resource( UserManager , '/user/<int:id_user>')
api.add_resource( NewUser , '/newuser')
api.add_resource( UserList , '/userlist' )

serve(app, host='0.0.0.0', port=8011, threads=2)

