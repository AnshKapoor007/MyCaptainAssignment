number_of_ele = int(input("Enter number of elements in the fibonacci series: ")) #Taking user input
fibonacci = [0,1]
if (number_of_ele <= 0): #Checking for invalid inputs
    print("Invalid Value")
elif (number_of_ele == 1): #Printing Fibonacci if number_of_elements is equal to 1
    print(0)
else: #Printing Fibonacci if number_of_elements is greater than 1
    for i in range(2, number_of_ele): #Generating the Fibonacci Series
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    for i in fibonacci:
        print(i, end = " ")