
#program that converts from celsious to fahrenheit
#get user choice
check = input("What do you want to convert. Use c2f for celsius to farenheit and f2c for fahrenheit to celsius \n")

if check == 'c2f':
    #get user input
   celsius = input("please input the temperature in degrees celsius to be converted \n")
   #conversion
   toCelsius = (((int(celsius)/ 5) * 9 ) + 32)
   print("The conversion is " + str(toCelsius) + " degrees Fahrenheit")

elif check == 'f2c':
    #get user input
    fahrenheit = input("Please input the temp in degrees Fahrenheit \n")
    #conversion
    tofahrenheit = ((int(fahrenheit) - 32) * 5/9)
    print("The conversion is " + str(tofahrenheit) + " degrees Celsius")
else:
    print("try again and type either c2f or f2c")
