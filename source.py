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
while countWhile > 0:
    if countWhile == 0:
        break
    else:
        print(countWhile, end=' ')
    countWhile -= 1
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
