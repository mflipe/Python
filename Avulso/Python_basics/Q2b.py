# Q2b) Returns True/False - two strings are same irrespective of lowercase/uppercase

def str_cmp(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 == p2:
        print(True)
    else:
        print(False)

str_cmp('nice', 'nice')
str_cmp('Hi there', 'hi there')
str_cmp('GoOd DaY', 'gOOd dAy')
str_cmp('foo', 'food')

"ABCD"
"A", "B", "C", "D", "A"
"DCBA"
"D", "C", "B", "A", "C"