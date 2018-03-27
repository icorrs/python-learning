#test mothod of class
class RoundFloat(float):
    'round float with baseobjct float'

    def __new__(cls,val):
        assert isinstance(val,float),\
        "value must be a float"
        return float(round(val,2))


class RoundFloat1():
    'round float without baseobjct'

    def __init__(self):
        pass

    def __call__(self,val):
        'call'
        return round(val,2)
    

def pow1(a,b):
    return pow(b,a)


class Factorial:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n-1)
        return self.cache[n]

print(__name__)