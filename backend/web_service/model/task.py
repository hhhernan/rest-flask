from model.init_db import db
from marshmallow import Schema, fields

class Task( db.Model ):

    id_task = db.Column( db.Integer , primary_key = True )
    name = db.Column( db.String(100) , nullable= False  ) 
    description = db.Column( db.String(5) , nullable= False  ) 

    def __init__(self , name , description , id_task = 0 ):
        self.name = name
        self.id_task = id_task
        self.description = description

    def __repr__(self):
        return '<Task %r>' % self.name

    def add( self  ):
        try:
            db.session.add( self )
            db.session.commit()
            return 'success'
        except Exception as e:
            return 'Failed'

    def delete( self ):
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


class TaskSchema( Schema ):
    class Meta:
        model = Task
        ordered = True

    name = fields.String(required=True)
    id_task = fields.Integer( strict=True )
    description = fields.String( required=True)

