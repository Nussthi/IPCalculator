import re

class InputCleaning:

    def byteParser(self, ip_adress):
        '''Retrieve the four bytes of the IP adress

        Parameters:
            - ip_adress (string): the ip adress typed by the user

        Returns:
            - bytes_list (list): a list containing the four bytes
        '''

        #Split the IP adress into a list
        bytes_list = ip_adress.split(".")

        #The IP adress should match a 4 bytes format
        if len(bytes_list) != 4 :
            raise Exception("Bytes list doesn't match 4 bytes format")

        return bytes_list
    
    def byteValueCheck(self, bytes_list):
        '''Check the value of each bytes

        Parameters:
            - bytes_list (list of strings): list containing each byte of the ip adress

        Returns:
            - None
        '''

        for byte in bytes_list:

            byte_integers = re.findall("\d",byte)

            if len(byte_integers) != len(byte) :
                raise Exception("A byte contains a character other than an integer")

    def bytes_list_to_string(self, bytes_list_str):
        '''Turn the bytes_list items to integers

        Parameters:
            - bytes_list_str (list of strings): list containing each byte of the ip adress

        Returns:
            - bytes_list_int (list of integers): list containing each byte of the ip adress
        '''

        bytes_list_int = []

        #Convert each byte to an integer
        for byte in bytes_list_str:
            bytes_list_int.append(int(byte))

        return bytes_list_int

'''
cleaner = InputCleaning()

try:
    bytess = cleaner.byteParser("192.168.1.200")
    print(bytess)
except Exception:
    print("IP adress format should be : xxx.xxx.xxx.xxx")

try:
    cleaner.byteValueCheck(bytess)
except Exception:
    print("IP adress contains a character other than an integer")
'''