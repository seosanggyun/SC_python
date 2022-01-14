dust = 61

if(dust > 150):
    print('미세먼지 매우 나쁘지롱')
elif(80 < dust <= 150):
    print('미세먼지 나쁘지롱')
elif(30 < dust <= 80):
    print('미세먼지 보통이지롱')
else:
    print('미세먼지 좋지롱')

# 문자열 보관법 f-스트링 방법 외에도 있음
# print(f'{dust} 따옴표로 감싸서 사용한다.')
# print('{} 따옴표로 감싸서 사용한다.'.fomat(dust))

dusty = [59, 25, 102]
for i in dusty:
    print(i)

