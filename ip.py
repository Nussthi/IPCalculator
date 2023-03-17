from baseconverter import Converter

class IPAdress:
    '''Class to create IPAdresses

    Attributes
        - byte1 : int
            first byte (from the left)
        - byte2 : int
            second byte (from the left)
        - byte3 : int
            third byte (from the left)
        - byte4 : int
            fourth byte (from the left)
        - byte1_bin : list
            first byte in binary (from the left)
        - byte2_bin : list
            second byte in binary (from the left)
        - byte3_bin : list
            third byte in binary (from the left)
        - byte4_bin : list
            fourth byte in binary (from the left)
        - bytes_bin : list
            list of byte1_bin, byte2_bin etc...

    Methods
        - display_decimal():
            Display the decimal bytes attributes
        - display_binary():
            Display the binary bytes attributes
        - ip_to_binary():
            Convert the decimal bytes to binary bytes
        - binary_ip_to_decimal():
            Convert the binary bytes to decimal bytes

    '''


    def __init__(self, byte1=0, byte2=0, byte3=0, byte4=0):
        """Constructs all the necessary attributes for the IPAdress object

        Parameters
            - byte1 : int
                first byte (from the left)
            - byte2 : int
                second byte (from the left)
            - byte3 : int
                third byte (from the left)
            - byte4 : int
                fourth byte (from the left)
        """

        self.byte1 = byte1
        self.byte2 = byte2
        self.byte3 = byte3
        self.byte4 = byte4
        self.byte1_bin = []
        self.byte2_bin = []
        self.byte3_bin = []
        self.byte4_bin = []
        self.bytes_bin = [self.byte1_bin, self.byte2_bin, self.byte3_bin, self.byte4_bin]


    def display_decimal(self):
        '''Display the the object IP adress in decimal on the terminal'''
        print(f"{self.byte1}.{self.byte2}.{self.byte3}.{self.byte4}")

    def display_binary(self):
        '''Diplay the object IP adress in binary on the terminal'''
        print(f"{self.byte1_bin}.{self.byte2_bin}.{self.byte3_bin}.{self.byte4_bin}")

    def ip_to_binary(self):
        '''Convert the ip byte in decimal into byte in binary'''
        converter = Converter()

        self.byte1_bin = converter.convert_to_binary(self.byte1)
        self.byte2_bin = converter.convert_to_binary(self.byte2)
        self.byte3_bin = converter.convert_to_binary(self.byte3)
        self.byte4_bin = converter.convert_to_binary(self.byte4)

        self.byte1_bin = converter.binary_byte_format(self.byte1_bin)
        self.byte2_bin = converter.binary_byte_format(self.byte2_bin)
        self.byte3_bin = converter.binary_byte_format(self.byte3_bin)
        self.byte4_bin = converter.binary_byte_format(self.byte4_bin)

        self.bytes_bin = [self.byte1_bin,
                          self.byte2_bin,
                          self.byte3_bin,
                          self.byte4_bin]

    def binary_ip_to_decimal(self):
        '''Convert the the binary bytes into decimal bytes'''
        converter = Converter()

        self.byte1 = converter.convert_to_decimal(self.byte1_bin)
        self.byte2 = converter.convert_to_decimal(self.byte2_bin)
        self.byte3 = converter.convert_to_decimal(self.byte3_bin)
        self.byte4 = converter.convert_to_decimal(self.byte4_bin)

    def get_bytes(self):
        '''Return the bytes of the IP adress'''
        return self.bytes_bin