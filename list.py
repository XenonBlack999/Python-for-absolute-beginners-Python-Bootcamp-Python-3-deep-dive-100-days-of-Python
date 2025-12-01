name : str = "Alice"
age : int = "25"
city : str = "Bangkok"

a = [name,age,city]

print(a)

def list_update(name, age , city):
    a.append(name)
    a.append(age)
    a.append(city)
    print(a)
    return a 

def main():
    name : str = input(str("Please tell me your name:"))
    age : int = int(input("Please tell  me your age :"))
    city : str = input(str(" Please tell me your city: "))
    list_update(name,age, city)
    
    
if __name__  == "__main__":
    while 1 == 1:
        main()
