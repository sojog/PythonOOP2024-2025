
# def fun(x,y,z):
#     return x + y**2 + z//2

# print(fun(z=2, x=3, y=6))

# print(fun(2, 3, 6))


# def fun(x,y,*z):
#     return (x + sum(z))**y
# print(fun(1,2,1,1,2))


# def fun(**kargs):
#     print(kargs)
#     print(min(kargs))
#     return (min(kargs.values())+min(kargs.values()))*2
# print(fun(cheie1=11,cheie2=29,cheie3=51,cheie4=-31,cheie5=20))




# def functie(*args, **kargs):
#     print(args, type(args))
#     print(kargs, type(kargs))

# functie(3, 1, 4, 32, cheie=32, p3 = 4)

# def fun(*b, **a):
#     print("b", b)
#     print("a", a)
#     return sum(b)/len(b)
# print(fun(11,29))

# def fun(*b, **a):
#     print("b", b)
#     print("a", a)
#     return sum(b)/len(b)
# print(fun(a=11,b=29))


def fun(x = 3, y = 3):
    print("x local", x)
    y -= 1
    z = x * y * 1
    x *= 2 
    return z


x  = 1
print("x global=", x)
print(fun())
print("x global=", x)