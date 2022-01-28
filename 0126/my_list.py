class MyList:
    
    def __init__(self,*args):
        self.value = [*args] 
        # 언패킹 후 리스트로 감싸서 집어넣자

    def __len__(self):
        result = 0
        for i in self.value:
            result += 1
        return result


a = MyList(1,2,3,4)
print(a.value)
print(len(a))
print(dir(MyList))
