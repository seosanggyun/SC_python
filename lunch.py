# import 시 주의할 점...
# import 가지고 오는 행위
# 이 이후로 활용할 코드를 가지고 올 거시기 때무네
# import는 항상 최 상단에 작성한다.
# 필요할때마다 등록한다.


import random

menu = ['짜장면', '짬뽕', '탕수육', '깐풍기', '토달볶']
print(menu)

# menu 중에 하나를 무작위로 선택
# like f(x)할 때 x 를 안에 넣듯이
choice = random.choice(menu)
print(choice)


