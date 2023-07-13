def f(*args, **kwargs):
    print('Named: ', kwargs)

#f(100, 50, 25)
f(gold=100, silver=50, copper=25)