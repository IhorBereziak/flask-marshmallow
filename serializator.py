from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Length, Range

class User():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

user = User('Sergio', 'PSM', 32)

class UserSchemma(Schema):
     name = fields.String(required=True, validate=Length(min=3, max=6))
     surname = fields.String(required=True)
     age = fields.Integer()

user_schema = UserSchemma()
dump_result = user_schema.dump(user)

# print(dump_result)
user_dict = {'name': 'patiallll', 'surname': 'Popov', 'age': 26}
# try:
#     result = user_schema.load(user_dict)
#     print(result)
# except ValidationError as err:
#     print(err)
error = user_schema.validate(user_dict)
if error:
    print(error)
else:
    print(user_schema.load(user_dict))
