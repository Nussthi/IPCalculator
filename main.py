from controllers.ipcalculatorcontroller import IPCalculatorController

def main():
    ip_calculator = IPCalculatorController()
    
    ip_calculator.view.run()
    

if __name__ == "__main__":
    main()