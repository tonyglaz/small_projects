from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()


# дамп в словарь
user = User(id=1, name="Ilya", age=19)
user_schema = UserSchema()
result = user_schema.dump(user)
print(type(result))
print(result["name"])

# дамп в строку
user = User(id=1, name="Ilya", age=19)
user_schema = UserSchema()
result = user_schema.dumps(user)
print(type(result))
print(result)

# дамп списка
u2 = User(id=2, name="Dima", age=20)
u3 = User(id=3, name="Petya", age=50)
u4 = User(id=4, name="Vasya", age=24)
user_schema = UserSchema(many=True)
print(user_schema.dump([u2, u3, u4]))
print(user_schema.dumps([u2, u3, u4]))

# десериализация
user_json_str = '{"name":"Petya","age":54}'
user_schema_01 = UserSchema()
user_dict = user_schema_01.loads(user_json_str)
user = User(**user_dict)
print(user.age, user.name)
