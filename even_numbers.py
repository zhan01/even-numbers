list1 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num = 0

print("\nPython program to print even numbers in a list")
print(list1) 
print("Even numbers\n")
while(num < len(list1)): 

	if num % 2 == 0: 
	    print(list1[num], end = " ") 
	
	num += 1