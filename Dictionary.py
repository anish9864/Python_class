#Accessing values from Dictionary

# car = {
    
#     "brand" : "toyota",
#     "color" : ["black","white","red"],
#     "model" : 2025,
#     "price" : 2000000
    
# }
#print(car)     


# a = car["brand"]
# b = car["color"]
# a = car.get("brand")
# b = car.get("price")
# print(a)
# print(b)

# a = car.keys()
# print(a)
# b = car.values()
# print(b)



# Changing values of dictionary
# car["model"] = 2027
# car["price"] = 5000000
# print(car)


# 2025/12/14
# using update() method to change the values of dictionary
car = {
    
    "brand" : "toyota",
    "color" : ["black","white","red"],
    "model" : 2025,
    "price" : 2000000
    
}
# car.update({"brand":"tesla", "model" : 2026, "color" : ["black","white","red","brown", "blue"]})
# car.update({"engine_type" : "electric"})

# print(car)



# Removing data from dictionary:
# car = {
    
    "brand" : "toyota",
    "color" : ["black","white","red"],
    "model" : 2025,
    "price" : 2000000
    
}
# 1. using the pop() method to remove the specific item from dictionary
# car.pop("color")
#2. using popitem() method to remove the last inserted item from dictionary
# car.popitem()
#3. using del keyword to remove specific item from dictionary
# del car #a
# del car["model"] #b
# car.clear() #c
# print(car)


#use of loops in dictionary
# car = {
    
    "brand" : "toyota",
    "color" : ["black","white","red"],
    "model" : 2025,
    "price" : 2000000
    
}
# for i in car:
#     print(i)
# for i in car:
#     print(car[i])
# for i in car.keys():
#     print(i)
# for i in car.values():
#     print(i)
# for i,j in car.items():
#     print(i,j)



# Nested Dictionary

#key1 = key2 : value
# variable = key1


# car1 = {  "brand" : "toyota",  "color" : "black",  "model" : 2025,  "price" : 2000000 }
# car2 = {  "brand" : "tesla",  "color" : "white",  "model" : 2026,  "price" : 3000000 }
# car3 = {  "brand" : "bmw",  "color" : "red",  "model" : 2027,  "price" : 4000000 }
# cars = {
#     "car1st": car1,
#     "car2nd": car2,
#     "car3rd": car3
# }
# print(cars)


#Alternative and short

#variable = key1 : key2 : value
cars = {
    "car1": {  "brand" : "toyota",  "color" : "black",  "model" : 2025,  "price" : 2000000 },
    "car2": {  "brand" : "tesla",  "color" : "white",  "model" : 2026,  "price" : 3000000 },
    "car3": {  "brand" : "bmw",  "color" : "red",  "model" : 2027,  "price" : 4000000 }
}
print(cars)

print(cars["car3"] ["brand"])
print(cars["car3"] ["color"])