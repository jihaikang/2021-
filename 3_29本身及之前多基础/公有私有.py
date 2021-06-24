class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __ar(self): # 私有属性__
        print(self.__foo)
        print('__bar')

# 私有属性是 def __bar(私有属性__),一般向平常调用方法是无法调用的，会报错该类对象没有该属性，调用须在类后加_Test才可以

def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test._Test__ar) # 可以这样调用私有属性,但这是调用类
# 调用方法 他还返回了个None 不知

if __name__ == "__main__":
    main()