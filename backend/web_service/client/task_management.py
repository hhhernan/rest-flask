from flask_restful import Resource, reqparse
from model.task import Task
from model.task import TaskSchema

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='nombre de la tarea')
parser.add_argument('description', type=str, help='detalle de a tarea')

schema = TaskSchema()

class TaskManagemet( Resource ):
    def get( self , id_task):
        task = Task.query.get( id_task ) 
        return schema.dump( task )

    def put( self , id_task ):
        args = parser.parse_args()

        error = schema.validate( args )
        if error:
            return {'status':'failed', 'message':error } , 400

        task = Task.query.get( id_task )

        task.name = args['name']
        task.description = args['description']

        return { 'status' : task.update() }, 200

    def delete( self , id_task ):
        task = Task.query.get( id_task )
        return { 'status' : task.delete() } 


class NewTask( Resource ):
    def post( self ):
        args = parser.parse_args()
        error = schema.validate( args )

        if not error:
            task = Task( name= args['name'] , description = args['description'] )
            return { 'status' : task.add() } , 200
        else:
            return { 'status' : 'failed' , 'message':error } , 400
            

class TaskList( Resource ):
    def get( self ):
        return schema.dump( Task.query.all() , many=True )

