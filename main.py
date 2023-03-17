from ip import IPAdress
from baseconverter import Converter
from ipcalculator import IPCalculator

def main():
    ip_adress = IPAdress(192,168,1,213)
    mask_adress = IPAdress(255,255,255,0)
    net_id_adress = IPAdress()
    ip_calculator = IPCalculator()

    print("\n----IP et masque----")
    ip_adress.display_decimal()
    mask_adress.display_decimal()
    print("--------------------\n")

    ip_adress.ip_to_binary()
    mask_adress.ip_to_binary()
    
    print("----IP et Masque binaire----")
    print(ip_adress.bytes_bin)
    print(mask_adress.bytes_bin)
    print("----------------------------\n")

    net_id_adress = ip_calculator.get_netid(ip_adress,mask_adress)
    net_id_adress.binary_ip_to_decimal()

    print("----Net ID----")
    net_id_adress.display_decimal()
    print("--------------")
    


if __name__ == "__main__":
    main()