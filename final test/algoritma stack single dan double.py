#single stack
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


# Contoh penggunaan
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack:", s.data)
    print("Pop:", s.pop())
    print("Peek:", s.peek())
    print("Stack now:", s.data)

#double stack
class DoubleStack:
    def __init__(self, size):
        self.data = [None] * size
        self.top1 = -1               # Stack 1 dimulai dari kiri
        self.top2 = size             # Stack 2 dimulai dari kanan
        self.size = size

    def push1(self, value):
        if self.top1 + 1 == self.top2:   # penuh
            raise Exception("Stack Overflow")
        self.top1 += 1
        self.data[self.top1] = value

    def push2(self, value):
        if self.top2 - 1 == self.top1:   # penuh
            raise Exception("Stack Overflow")
        self.top2 -= 1
        self.data[self.top2] = value

    def pop1(self):
        if self.top1 == -1:
            return None
        value = self.data[self.top1]
        self.top1 -= 1
        return value

    def pop2(self):
        if self.top2 == self.size:
            return None
        value = self.data[self.top2]
        self.top2 += 1
        return value


# Contoh penggunaan
if __name__ == "__main__":
    ds = DoubleStack(10)

    ds.push1(1)
    ds.push1(2)
    ds.push2(99)
    ds.push2(88)

    print("Array:", ds.data)
    print("Pop stack1:", ds.pop1())
    print("Pop stack2:", ds.pop2())
    print("Array now:", ds.data)
