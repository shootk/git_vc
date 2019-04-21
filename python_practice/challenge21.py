class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == {}
    
    def push(self,value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
#1
"""
s = "& i 0 u"
word = Stack()
for w in s:
    word.push(w)
s=""
while word.size() >0:
    s += str(word.pop())
print(s)
"""

#2
num = [1,2,3,4,5]
num_r = []
s = Stack()
for n in num:
    s.push(n)
for i in range(len(num)):
    num_r.append(s.pop())
print(num_r)