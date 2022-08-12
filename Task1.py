def fib(number):
    fibonacci=[0,1]                           
    i=0
    if number==0:
        print("No numbers")

    elif number == 1:
        print(fibonacci[0]) 
    else: 
        while i < number-2 :
            i+=1
            fibonacci.append (fibonacci[i]+fibonacci[i-1])
        print (fibonacci)

    
def main():
    insertednumber = int(input("insert how many fibonacci numbers do you need "))
    fib(insertednumber)

main()