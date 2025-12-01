# Calculate are of triangle using Heron's Formula
# area = sqrt(s * (s - a) * (s - b) * (s - c))

a = float(input("Enter the first side of Triangle(cm):"))
b = float(input("Enter the 2nd side of Triangle(cm):"))
c = float(input("Enter the 3rd side of Triangle(cm):"))
s = (a + b + c) /2
print("The value of s :", s)
area = s * (s - a) * (s - b) * (s - c)** 0.5
print("Area using Heron's Formula was :", area,"cm²")