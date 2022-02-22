# stack 은 새로운 데이터 타입이기 때문에 class

class Stack:
    def __init__(self,size):
        # 맨 처음 size , top , item 등이 필요
        self.size = size
        self.top = -1
        self.items = [None] * self.size

    # 스택의 연산 구현하기
    def is_empty(self):
        return True if self.top == -1 else False

    def is_full(self):
        return True if self.top == self.size else False

    def push(self,item):
        if self.is_full():                  # 스택이 꽉 차 있는 상태에서 push 하려고 하면
            raise Exception("It is full!")  # Error 발생
        else:
            self.top += 1
            self.items[self.top] = item

    def peek(self):
        if self.is_empty():
            raise Exception("It is empty!")
        return self.items[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception("It is empty!")
        else:
            value = self.items[self.top]    # 가장 위에 있는 데이터를 가져온다
            self.items[self.top] = None     # 아이템 삭제
            self.top -= 1                   # top 위치 변경
            return value                    # 저장 해 뒀던 값을 리턴




my_stack = Stack(size=5)
my_stack.push(1)
my_stack.push(2)
my_stack.pop()


print(my_stack)