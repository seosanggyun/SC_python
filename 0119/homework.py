A = input()

def get_middle_char(A):
    length = 0
    for i in A:
        length += 1

    if length % 2 == 1:
        center = length // 2
        print(A[center])
    else:
        center = length // 2
        print(A[center-1], end='')
        print(A[center])

get_middle_char(A)

def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')

# (4)
# ssafy(name='길동', '구미')

def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
print(result)

A = list(map(int, input().split()))

def my_avg(*args):
    total = 0
    for n in A:
        total += n
    avg = total // len(A)
    print(avg)
my_avg(A)