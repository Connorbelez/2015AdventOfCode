# --- Day 2: I Was Told There Would Be No Math ---

# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

# For example:

# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?


def calc(l,w,h):
    SA = 2*l*w + 2*w*h + 2*h*l
    smallestSide = min(l*w, w*h, h*l)
    return SA + smallestSide

def calc1(l,w,h):
    volume = l*w*h
    l = [l,w,h]
    l.sort()
    s1,s2 = l[0],l[1]
    perimater = 2*s1 + 2*s2
    return volume + perimater



if __name__ == '__main__':
    total = 0
    x = [4,3,5]
    x.sort()
    print(x)
    with open('data.txt') as f:
        for line in f:
            l,w,h = map(int, line.split('x'))
            total += calc(l,w,h)
    print(total)
    total1 = 0
    with open('data.txt') as f:
        for line in f:
            l,w,h = map(int, line.split('x'))
            total1 += calc1(l,w,h)
    print(total1)