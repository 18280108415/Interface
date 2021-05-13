import logging
#不带参数
def debug(func):
    def test(*args,**kwargs):
        logger = logging.getLogger(__name__)
        print('--> %s', func._name__)
        ret = func(*args,**kwargs)
        print('<-- %s, %s\n', ret.__name__, 'Success111111')

        print ('<-- %s, %s\n',"[DEBUG]: enter {}()".format(func.__name__))
        return func(*args,**kwargs)

    return test

#带参数
def debug1(func):
    def test(one):

        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func(one)

    return test

#可变参数*args和关键字参数**kwargs
def debug2(func):
    def test(*args,**kwargs):

        print ('<-- %s, %s\n',"[DEBUG]: enter {}()".format(func.__name__))
        return func(*args,**kwargs)

    return test



@debug2
def say_hello(one,two):
    print ("print1"+one+two)


if __name__ == '__main__':
    say_hello("23567ijndffsdwf","1+2")

