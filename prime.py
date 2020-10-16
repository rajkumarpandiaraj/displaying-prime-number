nValue = int(input('Enter the N value : '))
i = 2
while i < nValue :
    isPrime = True
    j = 2
    while j < nValue :
        if i != j :
            if i % j == 0 :
                isPrime = False
        j = j + 1
    if isPrime :
        print(i)
    i = i + 1