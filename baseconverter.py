import math

class Converter:
    '''Class to make conversions of numbers

    Attributes
        None

    Methods
        - convert_to_binary(number):
            Returns the number as a binary list of integers
        - binary_byte_format(number):
            Returns a formatted binary list matching a byte format
    
    '''

    def __init__(self):
        '''Constructs all the necessary attributes for the Converter object

        Parameters
            None
        '''

     
    def convert_to_binary(self, number):
        '''Convert a number to binary
        
        Parameters:
            - number (int): the number to convert

        Returns:
            - binary_list (list of integers): each index is a bit 
        '''
        #Saving the number as a quotient
        quotient = number
        #List to save the binary result for further manipulation in the program
        binary_list = []
        #Base of conversion, binary
        base = 2

        #As long as the quotient doesn't hit 0, the loop goes on
        while quotient != 0:
           
            #Flooring the result of the quotient divided by 2
            division_result = math.floor(quotient / 2)

            #Calculating the bit (0 or 1) depending on the modulo result
            modulo_result = quotient % base
   
            #Adding the bit at the begining of the list
            binary_list.insert(0,modulo_result)

            #Modifying the quotient for the next loop
            quotient = division_result

        return binary_list

    def binary_byte_format(self, binary_number):
        '''Format a binary list to match a byte format
        
        Parameters:
            - binary_number (list of integers) : the list to match a byte format
        
        Returns:
            - binary_byte (list of integers) : with a length of 8
        '''

        binary_byte = binary_number

        #As long as the list doesn't match a length of 8 (bit)
        #We had 0 at the begining of it to have a byte format
        while len(binary_byte) < 8:
            binary_byte.insert(0,0)


        return binary_byte
    
    def list_to_string(self, list):
        '''Convert a list to a string'''
        string_list = ""

        for index in list:
            string_list += str(index)

        return string_list