


def ham():
    a = 'spam'
    return a

# 1.
# print(a) # NameError: name 'a' is not defined

# 2.
# ham()
# print(a) # NameError: name 'a' is not defined

# 함수는 가장 기본 : local scope!
# 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용하는 것!
# 블랙박스 밖으로 결과를 주고 싶을 수 있어요! => return 해야 함

def add(x, y):
    print(x)
    print(y)

add(y=2, x=4)

print(1, end='')

def add(*args, a):
    return args, a 
print(add(1,2,3,4, a = 7))

def another_add(a, *args):
    return a, args

print(another_add(1,2,3,4,5))


def add( a, **kwargs):
    return a, kwargs

print(add(a=1, b=2, c=3, d=4))


global_a = 1

def enclosed():
    a = 20

    def local():
        a = 300
        print(a)
    local()
    print(a)

enclosed()
print(global_a)


PI= 3.141592

first_name = 'tak'
student = '상균'
students = ['', '']

def get_first_name():
    pass

def foo(*args):
    pass



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))
