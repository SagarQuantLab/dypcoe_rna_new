# def my_function():
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise ValueError(f"First position input argument must be Int, but supplied : {args[0], type(args[0])}")
        if not isinstance(args[1], int):
            raise ValueError(f"Second position input argument must be Int, but supplied : {args[1], type(args[1])}")
        
        if len(kwargs) > 0:
            key_list = list(kwargs.keys())
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError(f"first keyword input argument must be Int, but supplied : {kwargs[key_list[0]], type(kwargs[key_list[0]])}")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError(f"second keyword input argument must be Int, but supplied : {kwargs[key_list[1]], type(kwargs[key_list[1]])}")
        else:
            kwargs.setdefault('c', 0)
            kwargs.setdefault('d', 0)
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def addition(a, b, c, d):
    sum = a + b + c + d
    return sum

sum = addition(2, 3)
sum = addition(2, 3, c=4, d= 5)
# sum = addition(2, 3, c='c', d= 5)

print(sum)