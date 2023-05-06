def name_case(func):
    def name(name_1):
        x_ = name_1.capitalize()
        ok = func(x_)
        return ok
    return name
@name_case
def real_name(x):
    print(x)
real_name('nitesh')