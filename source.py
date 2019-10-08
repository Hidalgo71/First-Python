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
print(suM)
print("2nd add:", int(int1) + int(int2))


def test_func():
    print("This is a Test function")
    return


test_func()
for j in range(0, 5):
    print(j)
print('For loop finished.')


def my_func():
    num = input("Enter a number: ")
    num = int(num)
    for count in range(num):
        if count < num:
            print(count)
        count += 1


my_func()

print("After my_func. \n")
# iterating list
my_list = ["a", "b", 71, "c"]
for i in my_list:
    print(i)
# iterating Tuple
myTuple = ("x", "y", 71, "z")
for t in myTuple:
    print(t)
