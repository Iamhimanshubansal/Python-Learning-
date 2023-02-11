#Rule1: A variable name never starts with number

a=10
print(id(a))

1a=10               #it shows error because a variable name can't start with number
print(id(1a))

a1=10               #it will not show error because a variable name can end with number
print(id(a1))


#Rule2: A variable never contains special character except underscore(_)

a_=10
print(a_)

a_Himanshu =20
print(a_Himanshu)

_=100
print(_)


#Rule3: A variable must be readable.

a=24
Himanshu_age=24

