from sys import exit
def collatz(number):
    if number > 0:
        if number % 2 == 0:
            result = number // 2
        else:
            result = 3 * number + 1
        print (result)
        return result
    else:
        print ('You didn\'t enter a positive integer.')
        exit(0)
print ('Enter a positive integer:')
try:
    user_input=int(input())
except ValueError:
    print ('You didn\'t enter a positive integer.')
    exit(0)
result_value=collatz(user_input)

while True:
    if result_value is not 1:
        result_value=collatz(result_value)
        continue
    break#else:
            #break
