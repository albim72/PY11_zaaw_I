"""
dekorator do logowanie zmian stanu obiektów
Można śledzic zmiany stanów i kontolowac jakie metody na nie wpływają
"""

def log_state_changes(cls):
    class Wrapped(cls):
        def __setattr__(self, name, value):
            if name in self.__dict__:
                # Use square brackets to access dictionary elements
                old_value = self.__dict__[name]  
                print(f"Zmieniono {name} z {old_value} to {value}")
            super().__setattr__(name,value)
    return Wrapped


@log_state_changes
class Document:
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def update_content(self,new_content):
        self.content = new_content


doc = Document("Python Tips","Content about Python!")
doc.update_content("new big content about Python libraries")
print(doc.content)
