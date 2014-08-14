def digits(num):
    temp = num
    count = 0
    
    while temp > 0:
        digit = temp % 10
        if digit != 0:
            if num % digit == 0:
                count += 1
        temp /= 10

    print count

t = input()

for i in range(t):
    num = input()
    digits(num)
