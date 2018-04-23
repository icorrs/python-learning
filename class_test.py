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

    def ab(self,a,b):
        return a+b*a

class Singleton(object):
    'singleton'
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(Singleton,cls).__new__(cls)
        return cls.instance

class SingletonSon(Singleton):
    def add(self,num):
        return num+2


class SingletonSon2(Singleton):
    def add(self,num):
        return num+3

class SingletonFactory():
    def add(self,object_type,num):
        return object_type().add(num)
        
