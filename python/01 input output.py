'''a=input()
print(a)
name = input("Enter your name: ")
print(name, " ", type(name))

a=int(input())
print(a, " type is ", type(a))
a=float(input())
print(a, " type is ", type(a))
'''




# MULTIPLE INPUTS FROM USER
'''
print("""Today,
	we will learn about 
	input().split(separator, maxsplit)
	""")

x,y=input("Enter two values ").split()
print("number of boys are ", x)
print("number of girls are ", y)

a,b=input("Enter two values: ").split()
print("first number is {} and second number is {}".format(a,b))

x=list(map(int, input("Enter multiple values: ").split()))
print("list of students: ", x)

x,y=[int(x) for x in input("Enter two values: ").split()]
print("First number is: ", x)
print("Second number is: ", y)


x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))


x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)

x = [int(x) for x in input("Enter multiple value which you need to put , assign: ").split(",")]
print("Number of list is: ", x) 
'''




# OUTPUT USING PRINT FUNCTION
'''
name = 'Khusniddin' # if we do not put last quotes it means SyntaxError
age = 22
print("Name: ", name) # print(nme) NameError
print("Age: ", age)
# print(name+age) here TypeError

print("Hello, may name is ", name, " and I am ", age, " years old")

print("Hello ", end="salom")
print(" again and again")

print(name,age, sep=" is ")
# a=1
# print(name,age,sep='-',a)//sytax error
import io
dummy_file = io.StringIO()
print("Hello Khusniddin!!!", file=dummy_file)
print(dummy_file.getvalue())

# this is another example
# a=input()
# print("welcome again", file=open('Testfile.txt','w'))
# print("welcome again",a, file=open('Testfile.txt', 'w'))
'''



# HOW TO PRINT WITHOUT NEWLINE
'''
print("just learning")
print('awesome')


print("just learning", end=' ')
print('awesome')

a=[1,2,3,4]

for i in range(4):
	print(a[i], end=" ")

print(*a)

import sys
sys.stdout.write("My name is Khusniddin")
sys.stdout.write(" and what is your name bro") 	
'''




# OUTPUT FORMATTING

print('{0} and {1}'.format('Geeks', 'Portal'))
 
print('{1} and {0}'.format('Geeks', 'Portal'))
 
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

print('Number one portal is {0}, {1}, and {other}.'.format('Geeks', 'For', other ='Geeks'))

data = dict(fun='Khusniddin',adj="vulnerable")
print("I love {fun} computer {adj}".format(**data))


cstr = "I love geeksforgeeks"
print(cstr.center(40, '#'))
print(cstr.ljust(40,'-'))
print(cstr.rjust(40,'+'))
