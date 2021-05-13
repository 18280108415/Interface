log.i('--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            log.i('<-- %s, %s\n', func.__qualname__, 'Success')