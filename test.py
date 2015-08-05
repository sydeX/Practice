def swap(x,y):
    z = y
    y = x
    x = z
    # return x, y

def reverseString(a):
    start = 0
    end = len(a) - 2
    s = bytearray(a)

    while start < end:
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        start += 1
        end -= 1

    return s


class Test(object):
    def __init__(self):
        self.value = 1

    def printValue(self):
        print self.value

def changeTest(t):
    t.value = 2
    t.printValue()

def main():
    # a = 3
    # b = 2
    # print a,b
    # l = [a,b]
    # swap(l[0],l[1])
    # print a,b
    # print l

    t = Test()
    t.printValue()
    changeTest(t)
    t.printValue()
    print reverseString('abc0')


import pygame

if __name__ == '__main__':
    main()