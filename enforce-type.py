#Nested Functions 
def enforce(*types):
    def decotator(f):
        def new_func(*args, **kwargs):
            new_args = []
            for (a, t) in zip(args, types):
                new_args.append( t(a))
            return f(*new_args, **kwargs)
        return new_func
    return decotator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a, b):
    print(a/b)

repeat_msg("Hello", '5')
divide('1', '4')

