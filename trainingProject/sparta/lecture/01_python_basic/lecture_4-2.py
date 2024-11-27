# 클래스 만들기

def test_function():
    pass

if True:
    pass

class Ai_studnet1:
    def __init__(self):
        print("Ai_studnet1 sparta")

Ai_studnet1()

class Ai_studnet2:
    def __init__(self, input_name):
        self.name = input_name

    def greet(self):
        print(f"My name is {self.name}")

    def speak(self):
        print("Hello")

sparta = Ai_studnet2("스파르타")

sparta.greet()
sparta.speak()

# print()안에 파라미터가 없을시 위에서 mystock이 print()안의 파라미터로 들어가기 때문에 
# 메서드에서 파라미터를 지정해주지 않았음에도 파라미터가 1개 들어갔다고 인식하게 된다.
# 그러므로 메서드안에 self(또는 아무런 변수)를 넣어서 파라미트가 무조건 들어올 객체를 받아줘야 한다.

# 위 에러 문구는 파이썬에서 클래스를 다루다보면 굉장히 쉽게 접할 수 있는 오류이다. 
# 글자 그대로 인자를 요구하지 않는 함수에다가 1개의 인자를 전달해버려서 오류가 났다는 뜻이다. 
# 하지만 위의 예시 코드에서는 분명히 say_a() 라고 호출했기 때문에 인자를 넣지 않았다! 
# 그럼에도 위와 같은 오류가 나는 것은 파이썬 인터프리터가 자동으로 메소드를 호출할 때 인자를 넣어버리기 때문이다.

class Ai_studnet3:
    def __init__(self, name=None, age=None):
        if name == None:
            name = "스파르타"
        if age == None:
            age = 30
        
        self.name = name
        self.age = age

    def getStudent(self):
        print(f"이름: {self.name} 나이 : {self.age}")

sparta3 = Ai_studnet3()          
sparta3.getStudent()