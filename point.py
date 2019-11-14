#!/usr/bin/python

import sys,math

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self. y = float(y)

    def __repr__(self):
        c = (self.x, self.y)
        return c
    def __str__(self):
        point_s = "(%f, %f)" % (self.x, self.y)
        return point_s

class Line:
    def __init__(self, p1, p2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __str__(self):
        x1, y1 = self.p1.x,self.p1.y
        x2, y2 = self.p2.x,self.p2.y
        line = "((%f,%f),(%f,%f))" % (x1,y1,x2,y2)
        return line

    __repr__ = __str__

    def length(self):
        dx = abs(self.p2.x - self.p1.x)
        dy = abs(self.p2.y - self.p1.y)
        dx2 = dx ** 2
        dy2 = dy ** 2
        lineLen = math.sqrt(dx2 + dy2)
        return lineLen

    def slope(self):
        if p2.x - p1.x != 0:
            return ((self.p2.y - self.p1.y) / (self.p2.x - self.p1.x))
        return "undefined"

    def getEquation(self):
        b = (-self.slope() *self.p1.x) + self.p1.y
        if b < 0:
            return "y = %fx %f" % (self.slope(), b)
        return "y = %fx + %f" % (self.slope(), b)
#y = mx + b
#-b = mx - y
#b = -mx + y

if __name__ == '__main__':
    print "Creating a Line"

    x1 = raw_input("Enter a x1 value: ")
    y1 = raw_input("Enter a y1 value: ")
    p1 = Point(x1,y1)
    #print p1

    x2 = raw_input("Enter a x2 value: ")
    y2 = raw_input("Enter a y2 value: ")
    p2 = Point(x2,y2)
    #print p2

    line = Line(p1,p2)

    print "What are the lines attributes?"
    print "Select one:"
    print "1) Display line"
    print "2) Display line's length"
    print "3) Display line's slope"
    print "4) Display line's equaion"
    print "5) Quit program"
    choice_string = raw_input("Make a choice: ")

    active = True
    while active:

        try:
            choice = int(choice_string)
        except ValueError:
            sys.exit("Not an integer!  Goodbye!")
            active = False

        if choice == 1:
            print line
            choice_string = raw_input("What's your next choice?: ")
        elif choice == 2:
            line_length = line.length()
            print "Length is %f " % line_length
            choice_string = raw_input("What's your next choice?: ")
        elif choice == 3:
            line_slope = line.slope()
            if line_slope == 'undefined':
                print line_slope
            else:
                print "Slope is %f " % line_slope
            choice_string = raw_input("What's your next choice?: ")
        elif choice == 4:
            print line.getEquation()
            choice_string = raw_input("What's your next chocie?: ")
        elif choice == 5:
            print "Goodbye!"
            active = False
        else:
            print("I don't understand")
            choice_string = raw_input("What's your next choice?: ")


