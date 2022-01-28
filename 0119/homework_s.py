
## 0119 HW 2번

# 정중앙 문자를 반환 하는 함수
# 만약 문자열의 길이가 짝수라면 중앙의 2개를 반환
# 함수를 정의
# 전달인자를 받을 매개변수

# ctrl + / => 내가 선택한 줄 모두 주석 처리

# 코드
# 순서
# 바꾸기
# alt + 위/아래


def get_middle_char(word):
    length = 0
    # 단어 전부 순회
    for i in word:
        # 한개씩 개수를 세어보자.
        length += 1
    # 정 중앙값
    center = length // 2

    # 만약 홀수라면
    if length % 2:
        result = word[center]
    # 만약 짝수라면
    else:
        # result = word[center-1] + word[center]
        result = word[center-1:center+1]
        ## 슬라이싱 0 1 // 2 3 // 4 5
        ## 이렇게 되어야 하니까 2부터 4까지로 범위 정해야 함
    return result

print(get_middle_char('ssafy')) # => a
print(get_middle_char('coding')) # => di


## 0119 HW 3번

def ssafy(name, location='부울경'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')

# (4)
# ssafy(name= '길동', '구미')
# 키워드 인자를 사용한 뒤에는 위치 인자를 사용할 수 없다.

## 0119 HW 4번

def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3,7)
print(result)

## 0119 HW 5번
def my_avg(*numbers):
    # 평균값을 구하기
    length = 0
    count = 0
    for i in numbers: # (77, 83, ...)
        length += 1
        count += i
    return count // length

print(my_avg(77, 83, 95, 80, 70)) # => 81.0

## 언패킹 예시
def test (list_a, list_b):
    print(list_a, list_b)

# test([['첫번째 인자'], ['두번째 인자']])
# 이렇게 하면 list_b에 들어갈 인자가 없으니까 오류 뜸
# 근데 *를 앞에 붙이면
test(*[['첫번째 인자'], ['두번째 인자']])
# 이러면 언팩 해줘서 오류 안남