# car = { "brand": "Ford", "model": "Mustang", "year": 1964, }
# print(car.get('model'))

# quiz = {"Do you help out at home? ":"no it is not correct"      }

# D = dict() 
# for x in enumerate(range(2)): 
#     D[x[0]] = x[1] 
#     D[x[1]+7] = x[0] 
# print(D) 

# D = {1 : 1, 2 : '2', '1' : 1, '2' : 3} 
# D['1'] = 2
# D = {1 : 1, 2 : '2', '1' : 2, '2' : 3} 
# print(D[D[D[str(D[1])]]]) 

# D = {1 : {'A' : {1 : "A"}, 2 : "B"}, 3 :"C", 'B' : "D", "D": 'E'} 
# print(D[D[D[1][2]]], end = " ") 
# print(D[D[1]["A"][2]]) 

tuple1 = (1, 2, 4, 3) 
tuple2 = (1, 2, 3, 4) 
print(tuple1 < tuple2) 