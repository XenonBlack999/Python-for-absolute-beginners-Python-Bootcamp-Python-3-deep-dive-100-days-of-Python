# binary to decimal changer function 

def binary_to_decimal(b):
    num = b
    dec = 0
    base = 1 # because 2^0=1
    temp = num
    while(temp): 
        digit = temp%10 
        temp = int(temp/10)
        dec += digit * base
        base = base * 2
    return dec
        
bnum = 101010

print(binary_to_decimal(bnum))


# binary to decimal changer function 

def decimal_to_binary(n):
    binary = [0] * n 
    i = 0
     
    while (n>0):
        binary[i] = n % 2
        n = int(n/2)
        i += 1
    for x in range (i-1,-1,-1):
        print(binary[x], end="")
        
x = int(input("Please enter your decimal number:"))
decimal_to_binary(x)



