from ip import IPAdress
from baseconverter import Converter

def main():
    ip = IPAdress(127,730,120,90)
    ip.display_decimal()

    base_converter = Converter()
    print(base_converter.convert_to_binary(40))



if __name__ == "__main__":
    main()