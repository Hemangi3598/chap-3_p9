# wapp to find the rev of the given number

num = int(input("enter the number")) 
if num < 0:
	print("invalid number")
else:
	print("num = ", num)
	rev = 0
	while num > 0:
		digit = num % 10                     # get the last digit
		rev =   (rev * 10) + digit                       # use the last digit
		num =   num // 10                    # remove the last digit
	print("rev= ", rev)