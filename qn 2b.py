 #Python program to print odd Numbers in given range
  
start, end = 0, 50
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 != 0:
        print(num, end = " \n")



#alternative

  
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
  
#create a list that contains only odd numbers in given range
odd_list = range(start, end + 1) #this is an odd list conytain all number in range
newodd=[] 
for num in odd_list:
    if num % 2 != 0:
        print(num, end = " ")


print("\n")

#