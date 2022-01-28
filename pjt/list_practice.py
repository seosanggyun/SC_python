from curses import keyname
from pprint import pprint

def movie_info(movie):
    title = movie.get('title')
    result = {
        '제목': title
    }
    return result


def movie_info2(movie, genres):
    genres[0].get('name')

    
for stock in stocks:
    print(stock.get('price, '비상장주식'))



numbers = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ]

for number in numbers:
    print(number)
    for num in number:
        print(num)


lidict = [
            {'items': [1,2,3,'철수']}
            {'items': [1,2,3,'영희']}
            ]
            
for i in lidict:
    print(i)
    for key in lidict:
        print(key)
        print(lidict[key])
        for j in lidict[key]:
            print(j)