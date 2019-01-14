def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print (result)
    return result

print ('Enter number:')
result_value=collatz(int(input()))

while True:
    if result_value is not 1:
        result_value=collatz(result_value)
        continue
    break#else:
            #break
