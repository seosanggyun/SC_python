import random
"""



MADE BY CHOI JI WON




"""
members = ['김동욱', '강현준', '권나은', '김건효', '김누리', '김대영', '김상훈', '김수진', '김지현', '김혜라', '김효근', '박정현', '박제학', '박지현', '배준식', '서상균', '석민형', '오하민', '윤영진', '윤호준', '이재준', '이호준', '장지선', '전현우', '최지원', '홍성목']
pairs = random.sample(members, len(members))
for i in range(len(pairs)//2):
    blank = input()
    print(f'{i + 1:^3d}조 : {pairs[i]}, {pairs[-1 - i]}')