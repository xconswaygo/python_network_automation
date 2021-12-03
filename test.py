dict = {
    'key1': 'value1',
    'key2': 'value2',
}

def function(param1, *args, **kwargs):
    print(param1)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key)
        print(value)

test = function('hello', 'arg1', 'arg2', test=dict)