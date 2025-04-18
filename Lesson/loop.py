# 1. Any Symbol with new lines

name = "Hello Lianna"

for i in name:
    print(i)

# 2. Repetitively print

name = "Hello Lianna"

for i in range(1, 6):
    print(name)

# 3. +1
i = 1
while i <= 10:
    print(i)
    i = i + 1
    # break

# 4 option

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in range(3):
    print(x)


my_list = [ 1, 2, 4, 5, 6, 7, 9 , 0 ]
x = 5
my_list.append( 3 , 11 )

for y in my_list:
    print(y)


    if y == x:
    print(x)

shop = {
    products [
        type: "y"
        price: 1
    ],
    [ type: "a"
     price: 2
     ]
    }

for x in shop["products"]:
    if x["type"] == "y":
        print
