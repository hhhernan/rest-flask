from model.init_db import db
from marshmallow import Schema, fields
from datetime import datetime

class Users( db.Model ):

    id_user = db.Column( db.Integer , primary_key = True )
    nombre = db.Column( db.String(100) , nullable= False  ) 
    rol = db.Column( db.String(100) , nullable= False  ) 
    equipo = db.Column( db.String(100) , nullable= False  ) 
    fecha_registro = db.Column( db.DateTime , nullable= True , default=datetime.now()  ) 

    # def __init__(self , nombre , rol , equipo , fecha_registro , id_user = 0 ):
    #    self.id_user =  id_user
    #    self.nombre = nombre
    #    self.rol = rol
    #    self.equipo = equipo
    #    self.fecha_registro = fecha_registro

    def __repr__(self):
        return '<USer %r>' % self.nombre

    def serialize( self ):
        return {
            "nombre" : self.nombre,
            "rol" : self.rol
        }

    def add( self  ):
        try:
            db.session.add( self )
            db.session.commit()
            return 'success'
        except Exception as e:
            return 'Failed'

    def borrar( self ):
        try:
            db.session.delete( self )
            db.session.commit()
            return 'success '
        except Exception as e:
            return 'Failed'

    def update( self ):
        try:
            db.session.commit()
            return 'success'
        except Exception as e:
            return 'failed'


class UserSchema( Schema ):
    class Meta:
        model = Users
        ordered = True

    id_user = fields.Integer( strict=True )
    nombre = fields.String(required=True)
    rol = fields.String(required=True) 
    equipo = fields.String(required=True) 
    fecha_registro = fields.DateTime( required=False )

