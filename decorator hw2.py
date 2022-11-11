from datetime import datetime
from functools import wraps

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        my_list = []
        value = func(*args, **kwargs)
        my_list.append(datetime.now())
        my_list.append(wraps)
        my_list.append(args)
        my_list.append(value)
        with open('log.txt', 'w') as file:
            file.writelines(str(my_list))
        return value

    return wrapper


@log_function
def greet(name):
    print(f"Hello {name}")


@log_function
def sum_number(a, b):
    return a + b


@log_function
def wrapper_do_twice(name):
    print(name)
    print(name)


if __name__ == '__main__':
    greet('Everybody')
    print(sum_number(3, 4))
    wrapper_do_twice('Yay!')