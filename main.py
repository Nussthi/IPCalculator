from ip import IPAdress
from ipcalculator import IPCalculator

def main():
    ip_calculator = IPCalculator()
    
    ip_adress = IPAdress(10,40,150,89)
    mask_adress = IPAdress(255,0,0,0)
    netid_adress = IPAdress()
    wildcard_adress = IPAdress()
    broadcast_adress = IPAdress()
    first_adress = IPAdress()
    last_adress = IPAdress()
    usable_adresses = 0

    ip_adress.ip_to_binary()
    mask_adress.ip_to_binary()

    usable_adresses = ip_calculator.get_number_adresses(mask_adress)

    netid_adress = ip_calculator.get_netid(ip_adress,mask_adress)
    netid_adress.binary_ip_to_decimal()

    wildcard_adress = ip_calculator.get_wildcard_mask(mask_adress)
    wildcard_adress.binary_ip_to_decimal()

    broadcast_adress = ip_calculator.get_broadcast(netid_adress, mask_adress)
    broadcast_adress.binary_ip_to_decimal()

    first_adress = ip_calculator.get_first_adress(netid_adress)
    last_adress = ip_calculator.get_last_adress(broadcast_adress)

    print("\n----------------Result----------------")
    print("Host ID              : ", ip_adress.display_decimal())
    print("Subnet Mask          : ", mask_adress.display_decimal())
    print("Net ID               : ", netid_adress.display_decimal())
    print("Wildcard             : ", wildcard_adress.display_decimal())
    print("Broadcast            : ", broadcast_adress.display_decimal())
    print("Usable adresses      : ", usable_adresses)
    print("First adress         : ", first_adress.display_decimal())
    print("Last adress          : ", last_adress.display_decimal())
    print("--------------------------------------\n")

if __name__ == "__main__":
    main()