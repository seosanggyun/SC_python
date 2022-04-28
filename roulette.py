from random import choice


roulette = ['1. Wealth', '2. Robbery', '3. Noblesse Oblige', '4. Equalizer']


while True:
    prize = choice(roulette)
    blank = input()
    print('###################')
    print(f'{prize}')
    print('###################')