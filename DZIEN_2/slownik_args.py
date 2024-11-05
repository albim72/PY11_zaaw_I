#przykład 1 - proste zastosowanie kwargs

def kw_function(**kwargs):
    print(kwargs)

kw_function(a=1,b=6,h=75)

#przykład 2 - tworzenie profilu użytkownika
def create_user_profile(**kwargs):
    profile = {
        "username":"Guest",
        "email":"guest1@firma.pl",
        "age":None,
        "is_active":True,
        "is_admin":False
    }
    profile.update(kwargs)
    return profile

user_profile = create_user_profile(username = "Jan Nowak",email="janek@abc.pl",
                                       age=45,city="Kraków")
print(user_profile)


#przykład 3 - przekazywanie argumentów do innych funkcji
def print_info(name,age,**kwargs):
    print(f"name: {name}, age: {age}")
    if kwargs:
        print("dodana informacja ->")
        for key,value in kwargs.items():
            print(f"{key}: {value}")

def user_details(**kwargs):
    print_info(**kwargs)

user_details(name="Alicja",age=27,location="Sopot",profession="inżynier sieci")
user_details(name="Leon",age=62,location="Opole")
user_details(name="Maciej",age=16,location="Lublin",eyes="niebieskie")
