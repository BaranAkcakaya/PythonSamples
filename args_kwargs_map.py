#kwargs
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
     
# Now we can use *args or **kwargs to
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks")
myFun(*args)
 
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)

#args
# Python program to illustrate 
# *args for variable number of arguments
def myFun(*args): 
	for arg in args: 
		print (ars)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

#map
# Python program to demonstrate working 
# of map. 

# Return double of n 
def addition(n): 
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

#filter
# function that filters vowels 
def fun(variable): 
	letters = ['a', 'e', 'i', 'o', 'u'] 
	if (variable in letters): 
		return True
	else: 
		return False


# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

# using filter function 
filtered = filter(fun, sequence) 

print('The filtered letters are:') 
for s in filtered: 
	print(s) 


