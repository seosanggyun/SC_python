## WS 1번

# 함수 정의
# 인자는 리스트 하나

def list_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(list_sum([1, 2, 3, 4, 5])) # => 15

## WS 2번

# def dict_list_sum(infos):
#     # 모든 age들을 더할 변수
#     result = 0
#     # 순회
#     for info in infos:
#         result += info['age']
        
#     return result

# print(info = [{'name': 'harry', 'age': 5}, {'name': 'sang', 'age': 29}]) # => 34

## 키값 찾기 
## 해리의 age 찾고싶을 때
## dict_list_sum[0]['age']
## sang의 name 찾고싶을 때
## dict_list_sum[1]['name']


## 2차원 리스트 연습

numbers = [ [0,1,2],
            [3,4,5],
            [6,7,8],]

for i in range(3):
    for j in range(3):
        print(numbers[i][j])

for x in range(3):
    for y in range(3):
        print(numbers[y][x])        


## WS 3번
def all_list_sum(numbers):
    result = 0
    for number in numbers:
        for num in number:
            result += num
    return result, num

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))

print(sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]], []))

print(sum(*[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
## 언패킹해도 안됨
## TypeError: sum() takes at most 2 arguments (4 given)
## 두개만 받을건데 왜 네개나 주냐고 짜증냄


