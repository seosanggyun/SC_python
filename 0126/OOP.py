# class 대문자로 시작하는 이름
class Person:
    # 클래스 속성
    __population = 0

    # 생성자
    # 특별한 데코레이터가 없는 메서드는
    # 인스턴스 메서드고,
    # 인스턴스의 속성을 혹은 값을 조작하는 행위를 위한 메서드
    # 첫번째 인자로는 인스턴스 자신이 오게 될 것이다.
    # self라는 이름은 관례적인 것이고, 바뀌어도 문제는 없다.
    # 하지만 바꾸지는 않을 것이다.
    def __init__(self, name):
        # 인스턴스 속성
        self.name = name
        # self.population += 1
        # Person.population += 1 # 되긴 되는데 문제가 있다
        self.increase()

    def __del__(self):
        print('억')

        
    @classmethod
    def increase(cls):
        cls.__population += 1
        print(cls.__population)
    
    @staticmethod
    def decrease():
        # Person.population -= 1
        return '인구 감소가 일어나고 있엉'

    # 이렇게 했을때 만약에
    # 휴먼 클래스가 decrease()를 호출했을 때
    # 휴먼 클래스의 population을 건드리는게 아니라
    # Person 클래스의 population을 건드려버림
    # 딱히 이런거에 제약을 두진 않는데
    # 스태틱메서드를 쓰는 올바른 방법이 아님

class Human(Person):
    pass

# a = Human('휴먼')

# seo = Person('서상균')
# seo 인스턴스는 name 속성을 처음 생성할 때 할당되어서 가지게 된다.
# print(kim.name)
# print(type(kim))
# print(Person.name)
# hong = Person('홍길동')
# print(hong.name)
# print(kim.population, hong.population)
# print(Person.population)
# 클래스 메서드지만 호출 가능
# seo.increase()
# print(Person.population)

# # 클래스 메서드는 클래스로 호출 해라잉
# Person.increase()
# print(Person.population)

# print(a.name)
# print(a.population)
# a.increase()
# print(a.population)
# print(Person.population)

# 클래스 메서드는 분명히 인스턴스에서도 호출할 수 있고
# 다른데서도 다 호출할 수 있지만
# 클래스 속성에 관련된 상황에서만 써라
# 그렇게 약속했으니까.

p1 = Person('p1')
# p1.decrease()
# Person.__population += 1
# 변수앞에 __붙이면 다른데서 못건드리게 할 수 있음


# if __name__ == '__main__':


