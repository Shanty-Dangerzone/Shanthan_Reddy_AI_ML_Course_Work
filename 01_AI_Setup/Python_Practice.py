print("Hello, World!")  # This line prints a greeting message to the console.
blah1 = "blah"
blah2 = 2
blah3 = True
blah4 = 4.0
blah5 = [1, 2, 3, 4, 5]
blah6 = {'a': 1, 'b': 2, 'c': 3}

print(blah1, blah2, blah3, blah4, blah5, blah6)
print(blah2+blah4) #Result of addition of integer and float is float
#print(blah1+blah2) #This will give error as we cannot add string and integer
print(blah1*blah2) #But this will print string blah 2 times as we are multiplying string with integer
print(blah2+blah3) #Result of addition of integer and boolean is integer as True is considered as 1bbv 
#print(blah2+blah5) #This will give error as we cannot add integer and list
print(blah2+blah5[0]) #This will print addition of integer and first element of list
print(blah5[1:4]) #This will print elements from index 1 to 33..(4 is excluded)
print(blah6['b']) #This will print value corresponding to key 'b' in dictionary
blah5.append(6) #This will append 6 to the list
print(blah5)