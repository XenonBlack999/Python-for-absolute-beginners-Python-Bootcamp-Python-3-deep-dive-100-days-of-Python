list = [1,2,3,4,5,6]

def sum(x1,y1):
    return x1+y1

def multi(x3, x4):
    return x3*x4

def myreduce(sum, seq):# sequence
    first = seq[0]
    for i in seq[1:]:
        first = sum(first, i)
    return first
        
        
print(myreduce(sum, list))

print(myreduce(multi, list))
