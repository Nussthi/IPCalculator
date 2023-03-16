import math

class Converter:
    def __init__(self):
        pass

    def convert_to_binary(self, number):
        quotient = number #Saving the number as a quotient
        listNombre = [] #List to save the binary result for further manipulation in the program
        base = 2 #Base of conversion, binary

        #As long as the quotient doesn't hit 0, we continue
        while quotient != 0:
            
            #Flooring the result of the quotient divided by 2
            division_result = math.floor(quotient / 2)

            #Calculating the bit (0 or 1) depending on the modulo result
            modulo_result = quotient % base
        
            #Adding the bit at the begining of the list
            listNombre.insert(0,modulo_result)

            #Modifying the quotient for the next loop
            quotient = division_result

        return listNombre

