class PostiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped = 0
        pos_numbers = []
        for x in numbers:
            if x >= 0:
                pos_numbers.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls,pos_numbers)
        instance._skipped = skipped
        return instance

posnb = PostiveTuple(9,6,22,5,0,-3,-45,13,46,79,-64,-2,6,-99)
print(type(posnb))
print(posnb)
print(posnb._skipped)
