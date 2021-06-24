class Person(object):
    __slots__ = ('_name')
    def __init__(self,name):
        self._name  = name 
    # @property TypeError: 'NoneType' object is not callable
    def po(self):
        print('i am %s'%self._name)
p = Person('xiaoming')
p.po()