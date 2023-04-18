import kivy
#from controllers.ipcalculatorcontroller import IPCalculatorController
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    #Initialize the inputs variables
    #Default None because the GridLayout is not loaded yet
    #The name of the variable is the same as in the kv file
    ipadress_input = ObjectProperty(None)
    maskadress_input = ObjectProperty(None)
    #Same for outputs variables
    hostid = ObjectProperty(None)
    maskadress_output = ObjectProperty(None)
    netid = ObjectProperty(None)
    wildcard = ObjectProperty(None)
    broadcast = ObjectProperty(None)
    usableadresses = ObjectProperty(None)
    firstadress = ObjectProperty(None)
    lastadress = ObjectProperty(None)

    #Initialize the Layout and giving it the controller
    #For interactions with IpCalculatorController
    def __init__(self, controller,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.controller = controller

    def calculate_ips(self):
        '''Calculate the subnets and show them on screen
        
        Parameters:
            - None

        Returns:
            - None     
        '''
        #Assign values from input text
        ip_adress = self.ipadress_input.text
        mask_adress = self.maskadress_input.text

        ip_adresses = (ip_adress,mask_adress)

        self.controller.calculate_ips(ip_adresses)

        self.display_result()

    def display_result(self):
        #Retrieve the subnets
        subnets_dict = self.controller.get_subnets()

        #Display the subnets on the outputs section
        self.hostid.text = subnets_dict["hostid"]
        self.maskadress_output.text = subnets_dict["mask"]
        self.netid.text = subnets_dict["netid"]
        self.wildcard.text = subnets_dict["wildcard"]
        self.broadcast.text = subnets_dict["broadcast"]
        self.usableadresses.text = str(subnets_dict["usableadresses"])
        self.firstadress.text = subnets_dict["firstadress"]
        self.lastadress.text = subnets_dict["lastadress"]        

class IPCalculator(App): 
    def __init__(self, controller=0, **kwargs):
        '''Initialize the class with the controller
        
        Parameters:
            - controller (IPCalculatorController Object): the controller to get informations

        Returns:
            - None     
        '''
        super().__init__(**kwargs)
        self.controller = controller
        
    def build(self):
        #Creating the Layout and givig it the controller
        return MyGrid(self.controller)


if __name__ == "__main__":
    ipcalculator = IPCalculator()
    ipcalculator.run()
 
'''
class MyGrid(GridLayout):
    #Initialize and create the interface
    def __init__(self,controller,**kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.controller = controller

        
        self.cols = 1

        #Making different layouts to separate each parts of the view
        self.inputslayout = GridLayout()
        self.inputslayout.cols = 2

        self.buttonlayout = GridLayout()
        self.buttonlayout.cols = 2

        self.outputslayout = GridLayout()
        self.outputslayout.cols = 2

        #Inputs layout
        self.inputslayout.add_widget(Label(text="IP Adress : "))
        self.ipadress = TextInput(multiline=False)
        self.inputslayout.add_widget(self.ipadress)

        self.inputslayout.add_widget(Label(text="Mask Adress : "))
        self.maskadress = TextInput(multiline=False)
        self.inputslayout.add_widget(self.maskadress)

        self.add_widget(self.inputslayout)

        #Button layout
        self.buttoncalculate = Button(text="Calculate")
        self.buttoncalculate.bind(on_press=self.calculate_ips)
        self.buttonlayout.add_widget(self.buttoncalculate)

        self.add_widget(self.buttonlayout)

        #Outputs layout
        self.outputslayout.add_widget(Label(text="Host ID : "))
        self.outputslayout.add_widget(Label(text="-")) 

        self.outputslayout.add_widget(Label(text="Subnet Mask : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.outputslayout.add_widget(Label(text="Net ID : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.outputslayout.add_widget(Label(text="Wildcard : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.outputslayout.add_widget(Label(text="Broadcast : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.outputslayout.add_widget(Label(text="Usable adresses : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.outputslayout.add_widget(Label(text="First adress : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.outputslayout.add_widget(Label(text="Last adress : "))
        self.outputslayout.add_widget(Label(text="-"))

        self.add_widget(self.outputslayout)
        

    def calculate_ips(self,instance):
        ipadress = self.ipadress.text
        maskadress = self.maskadress.text

        ip_adresses = (ipadress,maskadress)

        self.controller.calculate_ips(ip_adresses)

    def display_result(self):
        subnets_dict = self.controller.get_subnets()

    '''