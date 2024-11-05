#przykład 1 - użycie TypedDict

from typing import TypedDict

class User(TypedDict):
    name:str
    age:int
    email:str

def print_user_info(user:User) -> None:
    print(f"Name: {user['name']}, Age: {user['age']}, e-mail: {user['email']}")

user_data = {'name':'Leon','age':40,'email':'leonion@abc.pl'}
print_user_info(user_data)
