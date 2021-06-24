from abc import ABCMeta, abstractmethod # 还有abc模块的
"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。


"""
# 多态可以调用 from abc import ABCMeta,abstractmethod实现 其中metaclass=ABCMeta当成参数传入类中 

class Pet(object, metaclass=ABCMeta): # ABCMeta难道是可以调用多个参数
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod # 指出抽象化的方法，不用传递实参，就可以调用元类的参数 这里的就是 self._nickname = nickname
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()