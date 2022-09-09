my_list = ['Real', ' Python']
x=my_list

func = lambda x: ''.join(i for i in x)
print(func(my_list))