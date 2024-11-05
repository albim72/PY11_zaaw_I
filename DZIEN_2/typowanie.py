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

#przykład 2 - złożone aliasy typów

from typing import List,Tuple,Union

Coordinate = Tuple[float,float]
Path = List[Coordinate]
CoordinateError = Union[Coordinate,str]

def validate_coordinate(coord:CoordinateError)->bool:
    if isinstance(coord,str):
        print(f"Error: {coord}")
        return False
    return True

example_path = [(0.0,1.0),(2.5,3.5),(4.0,-1.2),('True',True)]
print(validate_coordinate(example_path[0]))
print(validate_coordinate("invalide coordinate"))
print("_"*70)
print(validate_coordinate(example_path[3][0]))
print(validate_coordinate(example_path[3][1]))

#przykład 3 - użycie Protocol do definiowania interfejsów

from typing import Protocol

class Runner(Protocol):
    def run(self)->str:
        ...

    def finish_time(self)->float:
        ...

class Athlete:
    def run(self)->str:
        return "Athlete is running!"

    def finish_time(self)->float:
        return 1.15

class Robot:
    def run(self)->str:
        return "Robot is running!"

    def finish_time(self)->float:
        return 1.12

def start_race(participant:Runner)->None:
    print(participant.run())
    print(participant.finish_time())

athlete = Athlete()
robot = Robot()
start_race(athlete)
start_race(robot)

#przykład 4  użycie Generic dla funkcji z typami ogólnymi
from typing import TypeVar,Generic,List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self)->None:
        self._container: List[T] = []

    def push(self,item:T)->None:
        self._container.append(item)

    def pop(self)->T:
        return self._container.pop()


stack = Stack[int]()
stack.push(10)
stack.push(12)
stack.push(8.8)
stack.push("abcv")
print(stack.pop())
