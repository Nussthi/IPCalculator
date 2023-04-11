import copy
from models.ip import IPAdress
from models.inputcleaning import InputCleaning
from views.view import View

class IPCalculator:
    '''Class to make calculation with IP adresses

    Attributes
        None

    Methods
        - get_netid(ip_binary, mask_binary):
            Returns an the netID as an IPAdress object
    
    '''

    def get_IPadress(self, ip_name):
        '''Ask the IP adress to the user
        
        Parameters:
            - ip_name (string): determine the sentence to write on the screen

        Returns:
            - bytes_list (list of integers): the list containing the 4 bytes       
        '''
        input_cleaner = InputCleaning()
        input_view = View()

        #Determine which sentence to print 
        if ip_name == "hostid":
            ip_adress = input_view.ask_ip_adress()
        elif ip_name == "mask":
            ip_adress = input_view.ask_subnet_mask()

        #Retrieving the 4 bytes of the IP adress
        try:
            bytes_list = input_cleaner.byteParser(ip_adress)
        except Exception:
            print("IP adress format should be : xxx.xxx.xxx.xxx")
            return None

        #Checking if the IP contains only digital values
        try:
            input_cleaner.byteValueCheck(bytes_list)
        except Exception:
            print("IP adress contains a character other than an integer")
            return None

        bytes_list = input_cleaner.bytes_list_to_string(bytes_list)

        return bytes_list
        
    def assign_ip_bytes(self, bytes_list):
        '''Assign the bytes to the IPAdress object
        
        Parameters:
            - bytes_list (list of integers): the list containing the 4 bytes

        Returns:
            - ip_adress (IPAdress Object): the object with the user IP      
        '''
        ip_adress = IPAdress()

        ip_adress.byte1 = bytes_list[0]
        ip_adress.byte2 = bytes_list[1]
        ip_adress.byte3 = bytes_list[2]
        ip_adress.byte4 = bytes_list[3]

        return ip_adress



    def calculate_ips(self):
        '''Calculate and show the result on the prompt'''

        while True:
            hostid_bytes = self.get_IPadress("hostid")
            if hostid_bytes is not None:
                break

        while True:
            mask_bytes = self.get_IPadress("mask")
            if mask_bytes is not None:
                break

        hostid_adress = IPAdress()
        mask_adress = IPAdress()

        hostid_adress = self.assign_ip_bytes(hostid_bytes)
        mask_adress = self.assign_ip_bytes(mask_bytes)
        
        netid_adress = IPAdress()
        wildcard_adress = IPAdress()
        broadcast_adress = IPAdress()
        first_adress = IPAdress()
        last_adress = IPAdress()
        usable_adresses = 0

        hostid_adress.ip_to_binary()
        mask_adress.ip_to_binary()

        usable_adresses = self.get_number_adresses(mask_adress)

        netid_adress = self.get_netid(hostid_adress,mask_adress)
        netid_adress.binary_ip_to_decimal()

        wildcard_adress = self.get_wildcard_mask(mask_adress)
        wildcard_adress.binary_ip_to_decimal()

        broadcast_adress = self.get_broadcast(netid_adress, mask_adress)
        broadcast_adress.binary_ip_to_decimal()

        first_adress = self.get_first_adress(netid_adress)
        last_adress = self.get_last_adress(broadcast_adress)

        print("\n----------------Result----------------")
        print("Host ID              : ", hostid_adress.display_decimal())
        print("Subnet Mask          : ", mask_adress.display_decimal())
        print("Net ID               : ", netid_adress.display_decimal())
        print("Wildcard             : ", wildcard_adress.display_decimal())
        print("Broadcast            : ", broadcast_adress.display_decimal())
        print("Usable adresses      : ", usable_adresses)
        print("First adress         : ", first_adress.display_decimal())
        print("Last adress          : ", last_adress.display_decimal())
        print("--------------------------------------\n")


    def get_netid(self, ip_adress, mask_adress):
        '''Create an IPAdress object with the netID adress values
        
        Parameters:
            - ip_adress (IPAdress Object): the ip adress
            - mask_adress (IPAdress Object): the mask adress

        Returns:
            - netid (IPAdress Object)       
        '''
        netid = IPAdress()
        #Retrieving the list containing the binary bytes
        ip_binary_bytes = ip_adress.bytes_bin
        mask_binary_bytes = mask_adress.bytes_bin

        #Index for the netid byte
        netid_byte = 0

        #Looping each byte of the list
        for ip_byte, mask_byte in zip(ip_binary_bytes, mask_binary_bytes):
            #Loop each bit of the byte
            for ip_bit_value, mask_bit_value in zip(ip_byte, mask_byte):

                #Determining the bit value with a logic gate AND
                if ip_bit_value == 1 and mask_bit_value == 1:
                    netid.bytes_bin[netid_byte].append(1)
                elif ip_bit_value == 0 or mask_bit_value == 0:
                    netid.bytes_bin[netid_byte].append(0)

            netid_byte += 1
        return netid
    
    def get_wildcard_mask(self, mask_adress):
        '''Create an IPAdress object with the wildcard mask adress values
        
        Parameters:
            - mask_adress (IPAdress Object): the mask adress

        Returns:
            - wildcard_mask (IPAdress Object): the wildcard mask adress
        '''
        wildcard_mask = IPAdress()

        #Retrieving the list containing the binary bytes
        mask_binary_bytes = mask_adress.bytes_bin


        wildcard_byte = 0
        #Looping each byte of the list
        for mask_byte in mask_binary_bytes:
            #Looping each bit of the byte
            for mask_bit_value in mask_byte:
                #The wildcard bit value will be 0 if the mask bit value is 1
                # and vice versa
                if mask_bit_value == 1:
                    wildcard_mask.bytes_bin[wildcard_byte].append(0)
                else:
                    wildcard_mask.bytes_bin[wildcard_byte].append(1)
            wildcard_byte += 1

        return wildcard_mask

    def get_broadcast(self, netid_adress, mask_adress):
        '''Create an IPAdress object with the broadcast adress values
        
        Parameters:
            - netid_adress (IPAdress Object): the netid adress
            - mask_adress (IPAdress Object): the mask adress

        Returns:
            - broadcast_adress (IPAdress Object): the broadcast adress
        '''
        #Deepcopying  netid_adress to avoid references
        broadcast_adress = copy.deepcopy(netid_adress)
        wildcard_mask = self.get_wildcard_mask(mask_adress)
        wildcard_binary_bytes = wildcard_mask.bytes_bin

        broadcast_byte = 0
        #Looping each byte of the wilcard
        for wildcard_byte in wildcard_binary_bytes:
            broadcast_bit = 0
            #Looping each bit of the byte
            for wildcard_bit_value in wildcard_byte:
                #If the bit value is 1, then the broadcast adress bit value will
                # also be 1
                if wildcard_bit_value == 1:
                    broadcast_adress.bytes_bin[broadcast_byte][broadcast_bit] = 1
                broadcast_bit += 1
            
            broadcast_byte += 1

        return broadcast_adress
        
    def get_number_adresses(self, mask_adress):
        '''Calculate the number of usable adresses

        Parameters:
            - mask_adress (IPAdress Object): the mask adress

            
        Returns:
            - usable_adresses (int): Number of usable adresses
        '''

        usable_adresses = 0
        number_of_zero = 0
        mask_binary_bytes = mask_adress.bytes_bin

        #The number of adresses is determined by the number
        # of 0 in the subnet mask
        for mask_byte in mask_binary_bytes:
            number_of_zero += mask_byte.count(0)

        #The number of usable adresses is calculated like this :
        # 2 ^ "number of zeros in the subnet mask" - 2
        # -2 because we can't use Broadcast and NetID adresses
        usable_adresses = (2**number_of_zero)-2

        return usable_adresses
    
    def get_first_adress(self, netid_adress):
        '''Calculate the first host adress

        Parameters:
            - netid_adress (IPAdress Object): the NetID adress

            
        Returns:
            - first_adress (IPAdress Object): the first host adresss
        '''
        first_adress = copy.deepcopy(netid_adress)

        #Just adding 1 on the last byte
        first_adress.byte4 += 1

        return first_adress

    def get_last_adress(self, broadcast_adress):
        '''Calculate the last host adress

        Parameters:
            - mask_adress (IPAdress Object): the mask adress

            
        Returns:
            - last_adress (IPAdress Object): the last host adress
        '''
        last_adress = copy.deepcopy(broadcast_adress)

        #Just removing 1 on the last byte
        last_adress.byte4 -= 1

        return last_adress