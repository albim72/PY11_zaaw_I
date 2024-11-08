from pydantic import Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List,Optional

@dataclass
class User:
    id:int
    name:str = "Jan Kowalski"
    friends:List[int] = dataclasses.field(default_factory=lambda :[0])
    age:Optional[int] = dataclasses.field(default=None,metadata=dict(title='Wiek użytkownika',
                                                                     description='Nie kłam!'))
    height:Optional[int] = Field(None,title='wzrost w cm',ge = 50, le=260)


user = User(id='33')
print(user)

us1 = User(64,"Olga Kot",[7,],38,170)
print(us1)

us2 = User(75,"Piot Kamyk",[34,63,3],17,209)
print(us2)
