def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam_1(divideBy):
    return 42 / divideBy

try:
    print(spam_1(2))
    print(spam_1(12))
    print(spam_1(0))
    print(spam_1(1))
except ZeroDivisionError:
    print('Error : Invalid argument')