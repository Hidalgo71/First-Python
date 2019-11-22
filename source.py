print("Hello Python")
word = 'word'
sent = "This is sentence"
paragraph = """This is 
     paragraph"""
print(word)
print(sent)
print(paragraph)
print(word, sent, paragraph)
i = 3 + 6
print("i=", i)

int1 = input("1st number:")
int2 = input("2nd number:")
suM = int(int1) + int(int2)
print("Printing Sum Variable Result: ", suM)
print("Product of int1 * int2:", int(int1) * int(int2))


def test_func():
    print("This is a Test Function Calling")
    return


test_func()
for j in range(0, 5):
    print(j)
print('For loop finished.')

countWhile = 5
myList = []
while countWhile > 0:
    if countWhile == 0:
        break
    else:
        myList.append(str(countWhile)) # This for not printing last comma
    countWhile -= 1
print(', '.join(myList))
print("While Loop Finished.")


def my_func():
    num = input("Enter a number: ")
    num = int(num)
    for count in range(num):
        if count % 2 == 0:
            print(count)


my_func()

print("After my_func. \n")
# iterating list
my_list = ["a", "b", 71, "c"]
for i in my_list:
    print(i, end=', ')
print("\n")
# iterating Tuple
myTuple = ("x", "y", 71, "z")
for t in myTuple:
    print(t)

# Dictionaries
newDict = {"Yekta": 71,
           "LeBron": 23,
           "Kobe": 25,
           "Jordan": 9}
print("\n", newDict)  # it's print one line like {...}
# print(newDict.items())
""" for x in newDict:
    print(x)
    for y in newDict[x]:
        print(y, ':', newDict[x][y]) """
newDict["Kobe"] = 24
print("Kobe's New Number:\n", newDict)
newDict["Cedi"] = 10
print("Adding New Player:\n", newDict)
del newDict["LeBron"]
print("After Deleting LeBron:\n", newDict)
newDict.clear()
print("After Clear Dict:\n", newDict)