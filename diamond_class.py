#the use of super in diamond class inherite question;in sup=True condition,
# base_class's call_me run one time,
# in sup=False condition,base_class's call_me run two times.
class BaseClass():
    num_base_calls = [0]
    def call_me(self):
        print('calling base class')
        self.num_base_calls[0] += 1


class LeftClass(BaseClass):
    num_left_calls = [0]
    def call_me(self,sup=True):
        if sup==True:
            super().call_me()
        else:
            BaseClass.call_me(self)
        print('calling left class')
        self.num_left_calls[0] += 1


class RightClass(BaseClass):
    num_right_calls = [0]
    def call_me(self,sup=True):
        if sup==True:
            super().call_me()
        else:
            BaseClass.call_me(self)
        print('calling right class')
        self.num_right_calls[0] += 1


class SubClass(LeftClass,RightClass):
    num_sub_calls = [0]
    def call_me(self,sup=True):
        if sup==True:
            super().call_me(sup=True)
        else:
            LeftClass.call_me(self,sup=False)
            RightClass.call_me(self,sup=False)
        print('calling sub class')
        self.num_sub_calls[0] += 1


if __name__=='__main__':
    s = SubClass()
    s.call_me(sup=False)
    print('base-num:%s'%(s.num_base_calls))
    print('left_num:%s'%(s.num_left_calls))
    print('right_num:%s'%(s.num_right_calls))
    print('sub_num:%s'%(s.num_sub_calls))

