import copy
from ip import IPAdress

class IPCalculator:
    '''Class to make calculation with IP adresses

    Attributes
        None

    Methods
        - get_netid(ip_binary, mask_binary):
            Returns an the netID as an IPAdress object
    
    '''

    def __init__(self):
        '''Constructs all the necessary attributes for the Converter object

        Parameters
            None
        '''
        pass

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

        last_adress.byte4 -= 1

        return last_adress