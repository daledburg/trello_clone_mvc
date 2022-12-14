from init import db, ma
from marshmallow import fields

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    status = db.Column(db.String)
    priority = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='cards')
    comments = db.relationship('Comment', back_populates='card', cascade='all, delete')

class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['card']))

    class Meta:
        fields = ('id', 'title', 'description', 'status', 'priority', 'date', 'user', 'comments')
        ordered = True
