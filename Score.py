def score(x):
    if x >= 90 and x <= 100:
        print 'A'
    elif x >= 70:
        print 'B'
    elif x >= 60:
        print 'C'
    elif x>=0:
        print 'D'
    else:
        print 'Individal Score'

print score(9)