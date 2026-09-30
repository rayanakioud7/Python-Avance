def F1(n):
    for i in range(n):
        print("bonjour")

def F2(n):
    if (n%10)==0:
        print(f'{n} est divisible par 10')

def F3(s):
    voyelles = ['a','e','u','i','o']
    count =0
    for char in s:
        if char.lower() in voyelles:
            count+=1
    return count

def F4(n):
    if n == 0:
        return 1
    else:
        return F4(n-1)*n

def F5(n):
    for i in range(1,11):
        print(f'{i} x {n} = {i*n}')

def F6(s):
    return len(s)

def F7(n):
    if n<=1:
        return (n,0)
    else:
        (a, b) = F7(n-1)
        return (a+b, a)
    '''
    if n <= 1:
        return n
    else:
        return F7(n - 2) + F7(n - 1)
    '''

if __name__ == '__main__':
    print(F1(3))
    print(F2(60))
    print(F3('bonjour'))
    print(F4(4))
    print(F5(2))
    print(F6('test'))
    print(F7(8))