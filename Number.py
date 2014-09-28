import math

def SinglePrime(SingleNumber):
    
    sqrt = int(math.sqrt(SingleNumber) + 1)    
    try:   
        for n in range(2, sqrt):
           if SingleNumber % n == 0:
              # print SingleNumber, "/", n, " = ", SingleNumber / n, "; therefore it is not prime"
                break
        else:
            print (SingleNumber, " is prime")
    except (MemoryError, OverflowError):
        print ("I am sorry but that number is too large. Please select a new number")
        print ("")

def FibMax(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print (a),
         a, b = b, a+b
     print ("")
     print( "")

def FibNth(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     with open('report.txt', 'w') as results:    
         for c in range(n):
#             results.write("########################## Fibonacci(" + str(c + 1) + ") #################\n")
             results.write(str(a) + " ")
             a, b = b, a+b
#             print ""
#             print ""
     
choice = 1               

while choice <> 4:
    print ("[1] Search a number range for primes")
    print ("[2] Test a single Number for primality")
    print ("[3] Fibonacci series")
    print ("[4] Quit")
    print ("")
    try:    
        choice = int (raw_input ("enter you choice: "))
        print ("")
        if choice == 1:        
            StartNum = int (raw_input("Please enter the 1st number in the range: "))
            EndNum = int (raw_input("Please enter the last number in the range: "))
            for n in range(StartNum, (EndNum + 1)):
                SinglePrime(n)
        if choice == 2:
            TestNum = int (raw_input("Please enter the number you wish to test: "))
            SinglePrime(TestNum)
        if choice == 3:
            choice2 = 1
            while choice2 != 3:
                try:                
                    print ("[1] Serach Fibonacci numbers up to (n)")
                    print ("[2] Search for the (n)th Fibonacci number")
                    print ("[3] Quit")
                    choice2 = int (raw_input("Enter your choice: "))
                    if choice2 == 1:
                        fib1 = int(raw_input("Please enter the highest Fibonacci you want to find: "))            
                        FibMax(fib1)
                    if choice2 == 2:
                        fib1 = int(raw_input("Please enter the (n)th Fibonacci you want to find: "))
#                        FibNth(fib1)
                        FibNth(fib1)
                except ValueError:
                    print ("Please enter a valid number")
                    print ("")
    except ValueError:
        print ("Please enter a valid number")
        print ("")
          
