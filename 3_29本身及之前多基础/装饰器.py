class Person(object):
    #装饰器导出都是坑

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法 getter == propery 
    @property # 包装器
    def nam(self):
        return self._name
        print('ssss%s'%self._name) # 我方法里面刚写错了执行不报错
    # 访问器@property和修改器@setter都是对类中的方法的改变
    # 访问器 - getter方法 访问器可以使外界访问类的方法
    @property # get报错
    def age(self):
        return self._age

    # 修改器 - setter方法 修改器可以从外部改变类里面方法的值
    @age.setter # 去掉访问器@propety报错
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    
    person = Person('王大锤', 12)
    person.nam() # 不能调用方法，我靠
    person.play()
    person.age = 22 # 去掉修改器则修改不了，但没报错
    # person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()