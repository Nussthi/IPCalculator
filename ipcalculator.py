from ip import IPAdress
from baseconverter import Converter

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

    def get_netid(self, ip_binary, mask_binary):
        '''Create an IPAdress object with the netID value
        
        Parameters:
            - ip_binary (IPAdress Object): the ip adress
            - mask_binary (IPAdress Object): the mask adress

        Returns:
            - netid (IPAdress Object)       
        '''
        netid = IPAdress()
        #Retrieving the list containing the binary bytes
        ip_binary_bytes = ip_binary.bytes_bin
        mask_binary_bytes = mask_binary.bytes_bin

        #Index for the netid byte
        netid_byte = 0

        #Looping each byte of the list
        for ip_byte, mask_byte in zip(ip_binary_bytes, mask_binary_bytes):
            #Loop each bit of the byte
            for ip_bit, mask_bit in zip(ip_byte, mask_byte):

                #Determining the bit value with a logic gate AND
                if ip_bit == 1 and mask_bit == 1:
                    netid.bytes_bin[netid_byte].append(1)
                elif ip_bit == 0 or mask_bit == 0:
                    netid.bytes_bin[netid_byte].append(0)

            netid_byte += 1
        return netid
    