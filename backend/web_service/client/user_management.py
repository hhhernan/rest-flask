from flask_restful import Resource, reqparse
from model.user import Users
from model.user import UserSchema

parser = reqparse.RequestParser()
parser.add_argument('nombre')
parser.add_argument('rol')
parser.add_argument('equipo' )
#parser.add_argument('fecha_registro',required=False )

schema = UserSchema()

class UserManager( Resource ):
    def get( self , id_user ):
        user = Users.query.get( id_user )
        return schema.dump( user )

    def put( self , id_user ):
        args = parser.parse_args()
        error = schema.validate(args)

        if error:
            return { 'status' : 'failed' , 'message' : error }

        user = Users.query.get( id_user )
        user.nombre = args['nombre']
        user.rol = args['rol']
        user.equipo = args['equipo']

        return { 'status' : user.add() }

    def delete( self , id_user ):
        user = Users.query.get( id_user )

        
        return { 'status' :  user.borrar( ) }

class NewUser( Resource ):
    def post( self ):
        args = parser.parse_args()
        
        error = schema.validate( args )
        if error:
            return {'status':'failed' , 'message' : error }

        user = Users( nombre = args['nombre'] , rol = args['rol'] , equipo=args['equipo'] )
        return { 'status' : user.add() }

class UserList( Resource ):
    def get( self ):
        return schema.dump( Users.query.all() , many=True )