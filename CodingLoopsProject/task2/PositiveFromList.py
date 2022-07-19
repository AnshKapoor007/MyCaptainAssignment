list_input = [int(item) for item in input("Enter the list elements: ").split()] #Taking list from user
print("Positive Elements:", end=" ")
for ele in list_input: #Printing Positive elements of the list
    if (ele > 0):
        print(ele, end=" ")