class RangeValidator:
    def __init__(self,min_value,max_value):
        self.min_value = min_value
        self.max_value = max_value
        
    def __call__(self, value):
        if self.min_value <= value <=self.max_value:
            print(f'wartośc {value} mieści się w przedziale (min:{self.min_value}, max:{self.max_value})')
            return True
        else:
            print(f'wartośc {value} jest poza przedziałem (min:{self.min_value}, max:{self.max_value})')
            return True
