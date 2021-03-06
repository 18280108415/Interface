class logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print
            ("[{level}]: enter function {func}()".format(
                level=self.level,
                func=func.__name__))
            func(*args, **kwargs)

        return wrapper  # 返回函数


@logging(level='INFO')
def say(something):
    print
    ("say {}!".format(something))
if __name__ == '__main__':
    say("23567ijndffsdwf")