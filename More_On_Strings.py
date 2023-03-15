# my_str = 'python'
# len(my_str)

# my_str[0]

# my_str[1]

# #slicing
# my_str[0:4]
# #zero na likhleo hoy
# my_str[:4]
# #minus indexing -1 is the last letter
# my_str[-1]
# my_str[-2]
# #we can take a char out of a string
# letter=my_str[-3]
# letter

# my_str.upper()
# my_str.lower()

#practice Problem

#multiassignments

int1 = int(input('Please enter the 1st integer -> '))
int2 = int(input('Please enter the 2nd integer -> '))

print("Before Swapping int_1 = ",int1," and int2 = ",int2);
int1,int2 = int2,int1
print("After Swapping int_1 = ",int1," and int2 = ",int2);