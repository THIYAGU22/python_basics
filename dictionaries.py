d={
    'user' : 'thiyagu',
    'password' : 1234,
    'aoi' : 'python'
}
print(d['user'])
print(d)

d['user'] ='thiyagarajan'

print(d['user'])
print(d)

d['password'] = 123456
print(d['password'])
print(d)


for key,value in d.items():
    print("key in dictionary is :",key,"value in dictionary is ",value)

del d['user']

print(d)

for key in d.keys():
    print(key)

for values in d.values():
    print(values)

#print(d.clear())

#def fun(a):
    #assert a>1
    #print("assert")
#fun(0)

def func(a,b,c=100,d=122):
    print(a,b,c,d)

print(func(1,2))

print(func(1,2,3,4))

