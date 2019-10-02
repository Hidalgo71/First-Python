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
    print("This is a function")
    return


test_func()


def my_func():
    count = 0
    num = input("Enter a number: ")
    num = int(num)
    for count in num:
        if count < num:
            print(count)
        count += 1


my_func()

# iterating list
my_list = ["a", "b", 71, "c"]
for i in my_list:
    print(i)
# iterating Tuple
myTuple = ("x", "y", 71, "z")
for t in myTuple:
    print(t)
