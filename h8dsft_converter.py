def celsius_kelvin(): # celsius and kelvin conversion functions
    power_cels_kelv = True # variable to keep looping if invalid input being passed
    while power_cels_kelv == True:
        print("Celsius to Kelvin choose A \nKelvin to celsius choose B\n")
        celc_or_kelv = input("A or B: ").lower() # choose which conversion to use
        if celc_or_kelv == "a": # choices a, celcius to kelvin conversion
            
            # check input whether its valid or not using "try except"
            try:
                celsius_degree = float(input("input degree(C): "))
            except:
                print("Please enter a valid value in the correct format.")
                return
            celsius_to_kelvin = celsius_degree + 273.15 # formula for conversion from celsius to kelvin
            print(f"{celsius_degree} °C converted to kelvin is {celsius_to_kelvin} K") # print results
            return celsius_to_kelvin # return results if needed
        elif celc_or_kelv == "b": # choices b, kelvin to celsius conversion

            # check input whether its valid or not using "try except"
            try:
                kelvin_degree = float(input("input degree(K): "))
            except:
                print("Please enter a valid value in the correct format.")
                return
            kelvin_to_celsius = kelvin_degree - 273.15 # formula for conversion from kelvin to celsius
            print(f"{kelvin_degree} K converted to kelvin is {kelvin_to_celsius} °C") # print results
            return kelvin_to_celsius # return results if needed
        else:
            print("\n---------Invalid input, please enter a valid input.----------\n")



# celsius_kelvin() # uncomment to use this function



def convert_fahrenheit(celsius, kelvin): # fahrenheit conversion from celsius and kelvin, with celsius and kelvin as kwargs
    celsius_fahrenheit = round((celsius * 9/5) + 32, 2) # celsius to fahrenheit formula
    kelvin_fahrenheit = round(((kelvin-273.15) * 9/5) + 32, 2) # kelvin to fahrenheit formula
    return celsius_fahrenheit, kelvin_fahrenheit # return results


celsius_results, kelvin_results = convert_fahrenheit(23, 245) # make variable from results
print(f"23 celsius converted to fahrenheit is {celsius_results} °F") # print results
print(f"245 celsius converted to fahrenheit is {kelvin_results} °F") # print results



def convert_fahrenheit(fahrenheit): # celsius and kelvin conversion from fahrenheit, with celsius and kelvin as kwargs
    fahrenheit_celsius = round((fahrenheit - 32) / 1.8, 2) # fahrenheit to celsius formula
    fahrenheit_kelvin = round(((fahrenheit - 32) / 1.8) + 273.15, 2) # fahrenheit to kelvin formula
    return fahrenheit_celsius, fahrenheit_kelvin

f_to_c, f_to_k = convert_fahrenheit(78)

print(f"23 °F converted to celsius is {f_to_c} °C") # print results
print(f"245 °F converted to kelvin is {f_to_k} K") # print results