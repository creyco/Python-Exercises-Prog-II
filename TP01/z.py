# Python3 code to demonstrate
# string intersection
# using naive method

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using naive method to
# get string intersection
res = ""
for i in test_str1:
	if i in test_str2 and not i in res:
		res += i
		
# printing intersection
print ("String intersection is : " + res)




# Python3 code to demonstrate
# string intersection
# using set() + intersection()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using set() + intersection() to
# get string intersection
res = set(test_str1).intersection(test_str2)
		
# printing intersection
print ("String intersection is : " + str(res))


# Python3 code to demonstrate
# string intersection
# using join()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using join() to
# get string intersection
res = ''.join(sorted(set(test_str1) &
		set(test_str2), key = test_str1.index))
		
# printing intersection
print ("String intersection is : " + str(res))
