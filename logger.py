import datetime


def decorator(path):
    def _decorator(some_func):


        def record(*args, **kwargs):
            with open(path, 'a') as f:
                date = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
                result = some_func(*args, **kwargs)
                name = some_func.__name__
                f.write(f'{date} \n')
                f.write(f'Имя: {name}, Аргументы: {args} , {kwargs}\n')
                f.write(f'Результат: {result}')
                return result
        return record
    return _decorator

