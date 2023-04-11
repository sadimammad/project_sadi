import sys
import datetime

if '-' in sys.argv:
    a = sys.argv.index('-')
    if len(sys.argv) > a+1 and a>=2:
        print('Book name:', end=' ')
        for i in range(1, a):
            print(sys.argv[i], end=' ')
        print()
        print('Writer:', end=' ')
        for i in range(a+1, len(sys.argv)):
            print(sys.argv[i], end=' ')
        x = datetime.datetime.now()
        print()
        print('Added in: ', end=' ')
        print(x.strftime('%#d %B %Y'))
    else:
        print('Wrong input')
else:
    print('Wrong input')