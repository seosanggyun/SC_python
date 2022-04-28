from random import choice

print('#########################################################')
print('####################SSAFY Sorting Hat####################')
print('#########################################################')

Gryffindor = []
Slytherin = []
Hufflepuff = []
Ravenclaw = []

wizards = ['김동욱', '권나은', '김누리', '김대영', '김지현', '김혜라', '김효근', '박정현', '박제학', '박지현', '배준식',  '석민형', '오하민', '윤영진', '윤호준', '이재준', '이호준', '전현우', '홍성목']

houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']

while len(wizards) > 0:
    selected = choice(wizards)
    
    blank = input()
    print('#########################################################')
    print()
    print(f'              {selected}이(가) 모자를 썼습니다.')
    print('             Sorting Hat : Hmm..teresting...')

    house = choice(houses)

    blank = input()

    if house == 'Gryffindor':
        print('         너는.. 누구보다 용감하고 희생정신이 크구나..')
    elif house == 'Slytherin':
        print('         너는.. 누구보다 수완이 좋고 야망이 크구나..')
    elif house == 'Hufflepuff':
        print('         너는.. 누구보다 정직하고 근성이 있구나..')
    elif house == 'Ravenclaw':
        print('         너는.. 누구보다 지혜롭고 독창적이구나..')

    blank = input()

    print(f'               {selected}은(는).. {house}!')
    print()
    print('#########################################################')

    if house == 'Gryffindor':
        Gryffindor.append(selected)
    elif house == 'Slytherin':
        Slytherin.append(selected)
    elif house == 'Hufflepuff':
        Hufflepuff.append(selected)
    elif house == 'Ravenclaw':
        Ravenclaw.append(selected)

    wizards.remove(selected)

    if len(Gryffindor) == 5 and 'Gryffindor' in houses:
        houses.remove('Gryffindor')
    elif len(Slytherin) == 5 and 'Slytherin' in houses:
        houses.remove('Slytherin')
    elif len(Hufflepuff) == 5 and 'Hufflepuff' in houses:
        houses.remove('Hufflepuff')
    elif len(Ravenclaw) == 5 and 'Ravenclaw' in houses:
        houses.remove('Ravenclaw')

blank = input()
print('               Sorting Hat : 배정 결과는..')

blank = input()
print('#########################################################')
print()
print(f'    Gryffindor 기숙사에는..')
print(f'  {Gryffindor}!')
print()
print(f'    Slytherin 기숙사에는..')
print(f'  {Slytherin}!')
print()
print(f'    Hufflepuff 기숙사에는..')
print(f'  {Hufflepuff}!')
print()
print(f'    Ravenclaw 기숙사에는..')
print(f'  {Ravenclaw}!')
print()
print('#########################################################')








