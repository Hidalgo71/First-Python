print('Hello EPL!')
num = 71
numSqrt = num ** 0.5
print('Sqr Root of %0.3f is %0.3f' % (num, numSqrt))

print("==========================")

# Area of triangle
# a = float(input('1st side: '))
# b = float(input('2nd side: '))
# c = float(input('3rd side: '))
#
# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('Area: %0.2f' % area)

print("==========================")

# Strings
var1 = 'Los Angeles'
var2 = "Lakers"
print("var1[0]", var1[0])
print("var2[1:5]", var2[1:5])
print(var1 + " " + var2 + " " + "Yesss")
print(var1.upper())
print(var1.capitalize())
print(var1.lower())

print("==========================")

# replace() = returns a copy of the string in which the values of old string replaced with the new value
oldStr = "I like programming"
newStr = oldStr.replace('like', 'love')
print(newStr)

print("==========================")

# Join
print(":".join("Python"))
str1 = "Big Data Analytics"
print(''.join(reversed(str1)))

print("==========================")

# Tuples = Enables you to assign more than one variable at a time!
tup1 = ('Martina Hingis', 'Monica Seles', 'Steffi Graf', 'Coco Gouf')
tup2 = (1, 2, 3, 4, 5, 6)
tup3 = (6, 5, 4, 3, 2, 1)
print(tup1[3])
print(tup2[1:3])
print(tup3[1:3])
print(tup2 + tup3)

tup4 = ("Yekta", "Ozdemir", 27, "Student")  # tuple packing
(name, surname, age, job) = tup4  # tuple unpacking
print(name)
print(job)

print("==========================")

# Comparison Operators = < >
# Tuples can be comp if 1st element each tuple

a = (3, 6)
b = (5, 4)

if a > b:
    print("A is bigger")
else:
    print("B is bigger")

c = (5, 6)

if c > b:
    print("C is bigger")
else:
    print("B is bigger")

e = (9, 4)
f = (9, 4)

if e > f:
    print("E is bigger")
else:
    print("F is bigger")

print("==========================")

# Search in a Tuple 'in'
primes = (2, 3, 5, 7, 11, 13, 17)

print(3 in primes)
print(71 in primes)

# Len function

print("total primes in tup: ", len(primes))

# Del function

# dummytup = (0, 1)
# del dummytup
# print(dummytup)

print("==========================")

# Tuple Loops
tup5 = ('Lakers',)
n = 5
for i in range(int(n)):
    tup5 = (tup5,)
    print(tup5)

print("==========================")


# FUNCTIONS
# def is a define for functions

def myArgsFun(username, greetings):  # Func definition
    print("Hello! %s, from my func! I wish 's"
          % username, greetings)


myArgsFun("yekta Ozdemir", "great year")  # Function calling

print("==========================")


def sumNum(numbers):
    total = 0
    for x in numbers:
        total += x

    return total


print(sumNum((33, 6, 9, 8, 78)))


# Tuple References
# *values = used in front of the last parameter name to donate it as a tuple reference.
# This * is not like a C syntax

def aritmethicMean(first, *values):
    return (first + sum(values)) / (1 + len(values))


print(aritmethicMean(2, 3, 5, 6))
