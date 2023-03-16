

class IPAdress:
    def __init__(self, byte1, byte2, byte3, byte4):
        self.byte1 = byte1
        self.byte2 = byte2
        self.byte3 = byte3
        self.byte4 = byte4
        self.byte1_bin = ""
        self.byte2_bin = ""
        self.byte3_bin = ""
        self.byte4_bin = ""

    def display_decimal(self):
        print(f"{self.byte1}.{self.byte2}.{self.byte3}.{self.byte4}") 
        
    def display_binary(self):
        print(f"{self.byte1_bin}.{self.byte2_bin}.{self.byte3_bin}.{self.byte4_bin}")    