fruit=["apple", "banana", "cherry", "kiwi", "grapes"]
print(fruit)
print("the length of list is",len(fruit))
print("the first fruit is",fruit[0])
print("the last fruit is",fruit[-1])
fruit.append("orange")
print("updated list",fruit)
fruit.insert(2,"mango")
print("updated list",fruit)
fruit.remove("kiwi")
print("the updated list",fruit)
fruit.pop()
print("updated list",fruit)
print("multiplication of list",fruit*2)
fruit=fruit[:4]
print("sliced of list",fruit)
fruit.clear()
print("updated list",fruit)


students=["Ali",123,"address",45.5]
print(students)
 

mydict={}
mydict={1:"apple",2:"banana"}
print(mydict)

mydict_2={"name":"ali","marks":234}
print(mydict_2)

mydict_3={"name":"codingal", 2:[1,2,3]}
print(mydict_3)

mydict_4=dict({1:"apple",2:"banana"})
print(mydict_4)

print(mydict[1])
print(mydict_["name"])
print(mydict_2[2][1])
print(mydict_4.get(2))
mydict_4[3]="orange"
print(mydict_4)
mydict_4.pop(1)
print(mydict_4)
mydict_4.clear()
print(mydict_4)

def test(list1):
    result={}
    for i in list1:
        result[i[0]]=i[:1]
    return result

students1=[[1,'ali','cl'],[2,'usman','c2'],[3,'saad','c1'],[4,'omar','c3'],[5,'ayesha','c4']]
print("the students are",students1)
print("after convrsion")
print(test(students1))