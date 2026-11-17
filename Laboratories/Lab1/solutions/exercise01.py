import json
from datetime import datetime
"""
Develop in OOP a program for managing a list of devices The full list of devices is
stored in the file “catalog.json” (available at this link)
The program needs to load the file and manage the catalog, providing the following
features:
• searchByName: print all the information about the devices for the given
• searchByID: print all the information about the devices for the given
• searchByService: print all the information about the devices that provides the
given
• searchByMeasureType: print all the information about the device that
provides such measure
• insertDevice: insert a new device it that is not already present on the list (the
ID is checked). Otherwise ask the end-user to update the information about the
existing device with the new parameters. Every time that this operation is
performed the “last_update” field needs to be updated with the current date and
time in the format “yyyy-mm-dd hh:mm”. The structure of the parameters of
the file must follow the one of the ones that are already present
• printAll: print the full catalog
• exit: save the catalog (if changed) in the same JSON file provided as input.
Finally, once the update file has been saved, validate the new JSON with jsonlint
(http://jsonlint.com/)
"""
#Defines an OOP class that groups all the data and functions(methods)
#required to manage our devices in one clean structure.
class DeviceManager:
    def __init__(self):
#opens catalog.json file, loads its content, and stores it inside 
# self.catalog as a python dictionary.
        self.catalog=json.load(open("Laboratories\\Lab1\\solutions\\catalog.json"))
    
    def searchByName(self):
        user_input_name=input("Enter the desired Device Name: ")
        devices_list=self.catalog["devicesList"]
#["devicesList"]: Tells Python to ignore everything else in self.catalog and grab only the value attached to the key "devicesList"
        devices_found=[]
        found=False
        
        for device in devices_list:
            if device["deviceName"]==user_input_name:
                devices_found.append(device)
                found=True
        
        if found:
            print(devices_found)
        else:
            print("No Devices found with that name")
    
    def searchById(self):
        user_input_id = int(input("Enter id: "))
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False
        for device in devices_list:
            if(device["deviceID"]==user_input_id):
                devices_found.append(device)
                found = True
        if found:
            print(devices_found)
        else:
            print("No device with given ID found!")
    def searchByService(self):
        user_input_service = input("Enter the service: ")
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False
        for device in devices_list:
            if user_input_service in device["availableServices"]:
                devices_found.append(device)
                found = True
        if found:
            print(devices_found)
        else: 
            print("No device with given service was found!")
    def searchByMeasureType(self):
        user_input_MeasureType = input("Enter measure type: ")
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False
        for device in devices_list:
            if user_input_MeasureType in device["measureType"]:
                devices_found.append(device)
                found = True
        if found:
            print(devices_found)
        else:
            print("No device with given measure type was found!")
        
    
    def printAll(self):
        print(self.catalog)
    



    def insertDevice(self):
        user_input_id=int(input("Enter the new Device ID: "))
        devices_list=self.catalog["devicesList"]
        found=False
        for device in devices_list:
            if device["deviceID"]==user_input_id:
                found=True
                break
        if found:
            #print("What section of the device do you want to change?\nEnter one: name, measure, service")
            user_input_change = input("What section of the device do you want to change?\nEnter one: name, measure, service")
            if(user_input_change=="name"):
                user_input_name = input("what name do you want: ")
                device["deviceName"] = user_input_name
                device["lastUpdate"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                json.dump(self.catalog,open('catalog.json', 'w'))
        else:
            user_input_name=input("Please enter the Device Name:")
            #available_services
            available_services=[]
            available_measureTypes = []
            while True:
                measure_type_enter = input("Enter Measure type: (enter 'ok' to finish)")
                if(measure_type_enter == "ok"):
                    break
                else:
                    available_measureTypes.append(measure_type_enter)
            while True:
                service_to_enter=input("Please add the serviceName available. When finish type 'ok' ")
                if service_to_enter=="ok":
                    break
                else:
                    available_services.append(service_to_enter)
            # other code for the other attributes of the device
            #
            #
            #
            device_dict={"deviceID":user_input_id,"deviceName":user_input_name,"measureType":available_measureTypes,"availableServices":available_services}
            self.catalog["devicesList"].append(device_dict)
            json.dump(self.catalog,open('catalog.json','w'))
        




    
if __name__=="__main__":
    welcome_message="Hello, welcome to the Device Manager."
    available_actions_message="The available actions are: \n 'sName' to search by name \n'sId' to search by Id \n'sService' to search by Service \n'sMeasure' to search by measure type \n'insert' to insert or update the device \n 'print' to print full catalog \n 'e' exit"
    condition_iterate=True
    device_manager_instance= DeviceManager()
    print(welcome_message)
    while True:
        print(available_actions_message)
        user_input=input("\n Please enter the action to be performed: ")
        if user_input == "sName":
            device_manager_instance.searchByName()
        elif user_input == "sId":
            device_manager_instance.searchById()
        elif user_input =="sService":
            device_manager_instance.searchByService()
        elif user_input == "sMeasure":
            device_manager_instance.searchByMeasureType()
        elif user_input =="insert":
            device_manager_instance.insertDevice()
        elif user_input == "print":
            device_manager_instance.printAll
        elif user_input == "e" or user_input=="exit":
            condition_iterate=False
            break
        
