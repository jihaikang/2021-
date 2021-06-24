class Person():  # __slots__魔法

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender') # __为私有属性

    def __init__(self, name, age):
        self._name = name # self.name = name 可以    实例.name  外部访问。这个不是私有属性
        # self._name =name _只是个约定，变量或方法仅供内部使用。但外部依然可以调用它
        self._age = age
        # self._gender = gender

    @property
    def name(self):
        return self._name
        print(self._name) # 我就想知道如何把name答应出来

    @property
    def age(self):
        return self._age
    # @property
    # def gender(self):
    #     return self._gender

    @age.setter
    def age(self, age):
        self._age = age
    # @classmethod
    def play(self):
        if self._age <= 16: # 这种统一命名跟本没法用类属性啊,搞死人
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22) # 把类绑定为一个对象
    person.play()
    person._gender = '男' # 给类添加属性
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True

a= main()# 方法能被调用，能再创造一个对象
print(type(a))
# b = Person('dd',11,11) # NameError: name 'djj' is not defined我这个类不能导入参数,我忘了字符串要用引号括起来
# b.name
# b.age
# b.gender
