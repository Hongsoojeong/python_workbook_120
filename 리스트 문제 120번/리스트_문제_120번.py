#연습 120번
def find_ascending_sorted(list):#오름차순 판단 함수
    Fact=True
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
            Fact=False
            return Fact
    return Fact

def find_descending_sorted(list):
    Fact=True
    for i in range(0,len(list)-1):
        if list[i]<list[i+1]:
            Fact=False
            return Fact
    return Fact

def make_list():
    list=[]
    while True:
        num=input("숫자를 입력해주세요: ")
        if num=="":
            return list
        else:
            list.append(int(num))

list=make_list()
print(list)
if find_ascending_sorted(list)==True:
    print("오름차순 순입니다.")
elif find_descending_sorted(list)==True:
    print("내림차순 순입니다.")
else:
    print("아무런 순서도 아닙니다.")