from itertools import chain
for i in chain(range(0,10), range(30,40)):
    print(i)
stopped = False
print(stopped)

def imcool(name):
    print(name)
    return (5,8,name)

a = imcool("Hello" + '7')
print(a)
(l,m,n) = imcool("Hello" + '7')
print("l:" + str(l))
print(l)
print(f"l:{l}, m:{m}, n:{n}")