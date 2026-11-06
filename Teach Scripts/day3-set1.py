# print hello 10 times using while loop

# variable declaration
text = "hello" 
count = 1

# while loop - we have to set stop condition

while (count <= 10):
    print(text, count, sep="-")
    count += 1

# for loop - stop condition is default behaviour

for i in range(1,11):
    print(text, count, sep="-")