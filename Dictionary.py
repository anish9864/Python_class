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
car.update({"engine_type" : "electric"})

print(car)