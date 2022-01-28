from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        # 오버라이드 할 때 순서 잘 지켜라
        # 안그러면 파괴 광선이 아니라
        # 몸통 박치기가 들어감
        self.skill = '파괴 광선'

    def attack(self):
        return '콰콰쾅'

    def walk(self):
        return '뽀쨕 뽀쨕'


class Metamong(Pokemon):
    no = 132

    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        self.skill = '변신'

    def eat(self):
        return '쫩쫩'


class Child(Pikatchu, Metamong):
    pass

class Brother(Metamong, Pikatchu):
    pass

b = Brother('메타몽?')
print(b.no, b.eat(), b.walk())
print(b.attack(), b.skill)

# c = Child('피카츄?')
# print(c.no, c.eat(), c.attack(), c.skill)

# pika = Pikatchu('피카츄')
# meta = Metamong('메타몽')
# print(meta.no, meta.attack())
# print(pika.name)
# print(pika.skill)
# print(pika.lv)
# print(pika.attack(), pika.walk())
# print(pika.no)
# print(Pokemon.population)
# print(Pikatchu.population)