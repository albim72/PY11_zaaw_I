from funcwraps import dekorator
from cache import fibonacci

def main():
    print("przykład użycia dekoratora z @wraps! ")

    @dekorator
    def wrapsprzyklad():
        return "prosta funkcja"

    print(wrapsprzyklad())

    print("przykład użycia lru_cache!")

    print(fibonacci(10))


if __name__ == '__main__':
    main()
