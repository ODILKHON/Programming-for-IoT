import datetime
class TemperatureSensor:
    #Defining the constructor for the TemperatureSensor class
    def __init__(self,sensorName,sensorID,sensorFabricationYear):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.sensorFabricationYear = sensorFabricationYear
        #age =  datetime.datetime.now().year - self.sensorFabricationYear
        #init cannot return a value, so we will not return age here
        #return age
    #printing the sensor details by method
    def show_sensorID(self):
        print(f"Sensor Name: {self.sensorName}, Sensor ID: {self.sensorID}")
    
    def printAge(self):
        currentYear = datetime.datetime.now().year
        age = currentYear - self.sensorFabricationYear
        print(f"Sensor Age: {age} years")

#Main of our program
if __name__ == "__main__":
    sensorName = input("Enter the sensor name: ")
    sensorID = input("Enter the sensor ID: ")
    sensorFabricationYear = int(input("Enter the sensor fabrication year: "))
    sensor1 = TemperatureSensor(sensorName, sensorID, sensorFabricationYear)
    sensor1.show_sensorID()
    sensor1.printAge()
    age = datetime.datetime.now().year - sensor1.sensorFabricationYear
    file1 = open("SensorDetails.txt","w")
    file1.write(f"SensorName: {sensor1.sensorName}\nSensorID: {sensor1.sensorID}\nSensorAge: {age}")
    file1.close()