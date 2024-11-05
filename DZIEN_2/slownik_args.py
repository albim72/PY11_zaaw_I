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

#przykład 4 - dekoratory przyjmujące argumenty!

def logging_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Wołana funkcja: {func.__name__} z argumentami {args} "
              f"i argumentami słownikowymi: {kwargs}")
        return func(*args,**kwargs)
    return wrapper

@logging_decorator
def add(a,b,**kwargs):
    result = a*2+b*3
    for key,value in kwargs.items():
        print(f"procesowanie dodatkowego argumentu {key} z wartością: {value}")
        if key == "add_to_result":
            result += value
        elif key == "multiply_result":
            result *= value
    return result

print("_"*70)
result = add(2,4)
print(f'wynik1: {result}')

res_with_kwargs = add(2,4,add_to_result=7)
print(f'wynik2: {res_with_kwargs}')

res_multi = add(2,4,add_to_result=7,multiply_result = 2)
print(f'wynik3: {res_multi}')

res_multi2 = add(2,4,multiply_result = 2)
print(f'wynik3: {res_multi2}')

res_multi_n = add(2,4,blabla = 2)
print(f'wynik4: {res_multi_n}')

res_multi_rev = add(2,4,multiply_result = 2,add_to_result=7)
print(f'wynik3: {res_multi_rev}')
