##PATTERN 1
# rows=int(input("Enter number of rows:"))
# #each_number will be 1 in first iteration and then 2 and so on
# for each_number in range(1,rows+1):	
# #printing number will be in range (1 , i+1) i.e  (1,2) but 2 is excluded so only 1 will be printed , likewise the rest	
# 	for printing_pattern in range(1,each_number+1):		
# 		print(printing_pattern,end=" ")				#The print() function inserts a new line at the end, by default In Python 3, end =" " appends space instead of newline.			
# 	print()
	
# 	OUTPUT:
# 	Enter number of rows:5
# 	1 
# 	1 2 
# 	1 2 3 
# 	1 2 3 4 
# 	1 2 3 4 5 






##PATTERN 2
# rows=int(input("Enter number of rows:"))	
# for each_number in range(1,rows+1):	
# 	for printing_pattern in range(1,each_number+1):		
# 		print(each_number,end="")			
# 	print()

#OUTPUT:
# Enter number of rows:5
# 1
# 22
# 333
# 4444
# 55555




##PATTERN 3
# rows=int(input("Enter number of rows:"))	
# for each_number in range(rows,0,-1):	
# 	for printing_pattern in range(1,each_number+1):		
# 		print(each_number,end="")			
# 	print()

# OUTPUT:
# Enter number of rows:5
# 55555
# 4444
# 333
# 22
# 1




##PATTERN 4
# rows=int(input("Enter number of rows:"))
# for each_number in range(1,rows+1):
# 	for printing_pattern in range(1,each_number+1):
# 		print("*", end=" ")
# 	print()

# OUTPUT:
# Enter number of rows:5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 




##PATTERN 5 , this pattern is reverse of the above program but the for loop is different compared to it ,it has one step included more in it  i.e  step
# rows=int(input("Enter number of rows:"))
# for each_number in range(rows,0,-1):
#the -1 is used for decremented loop 
# 	for printing_pattern in range(1,each_number+1):
# 		print("*", end=" ") 
# 	print()

# OUTPUT:
# Enter number of rows:5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 



##PATTERN 6
# rows=int(input("Enter number of rows:"))
# for each_number in range(1,rows+1):
# 	for empty_space in range(1,rows +1- each_number):
# 		print(" ", end=" ")
# 	for printing_pattern in range(1,each_number+1):
# 		print("*", end=" ")
# 	print()

# OUTPUT:
# Enter number of rows:5
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 






##PATTERN 7
# rows=int(input("Enter number of rows:"))
# for each_number in range(rows,0,-1):
# 	for empty_space in range(1,rows +1-each_number):
# 		print(" ", end=" ")
# 	for printing_pattern in range(1,each_number+1):
# 		print("*", end=" ")
# 	print()

# OUTPUT:
# Enter number of rows:5
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 







##PATTERN 8
# rows=int(input("Enter number of rows:"))
# for each_number in range(1,rows+1):
# 	for empty_space in range(1,rows +1- each_number):
# 		print(" ", end=" ")
# 	for printing_pattern in range(1, ( 2*each_number-1)+1):
# 		print("*", end=" ")
# 	print()


# OUTPUT:
# 	Enter number of rows:5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 




##PATTTERN 9
# rows=int(input("Enter number of rows:"))
# for each_number in range(rows,0,-1):
# 	for empty_space in range(1,rows +1- each_number):
# 		print(" ", end=" ")
# 	for printing_pattern in range(1, ( 2*each_number-1)+1):
# 		print("*", end=" ")
# 	print()

# OUTPUT:
# Enter number of rows:5
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 






