str ="andrew"
#str[0] = "A"
str = "A" + str[1:]
print(str)

names = ['thiyagarajan','udhayakumar','thiru']
age = [20,19,18]
print(zip(names,age))
print(" ")
print(" ")
for x,y in zip(names,age):
    print("name is",x ," age is", y)


name = "udhay"

if name == "thiru":
    print("he is boy")
elif name == "udhay":
    print("he is super boy")
else:
    raise TypeError("Unknown mode")

store = ["hello","hai","language","tamil","english","french","deutsch"]
print(store[::2])
print(store[1::2])

numbers = [1,2,3,4,5,6,7,8,9,10]
for z in range(len(numbers)):
    if(numbers[z]%2==0):
        print("even number at ",z,"indice","value is",numbers[z])
    else:
        print("odd number",numbers[z])


cd = open("C:\Users\Administrator\Desktop\hello.txt")

print(cd.readline())

lst = [x for x in open("C:\Users\Administrator\Desktop\hello.txt","r").readlines()]
print(lst)

count = {
    "Chen":'3',
    "Ben" :'3',
    "yasqin":'5'
}

for name,count in count.items():
    print(name,count)