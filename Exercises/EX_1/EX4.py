class temperatureSensor: 
    def __init__(self,sensorName,sensorID,sensorMeasurements):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.sensorMeasurements = sensorMeasurements
    def computeAverage(self):
            sum = 0
            counter = 0
            for i in self.sensorMeasurements:
                sum +=i
                counter+=1
            return "Average of the sensor measurements is: " + str(sum/counter) 
    def computeMax(self):
            max = 0
            for i in self.sensorMeasurements:
                if(i>max):
                    max =i
            return "Max for this measurement is: " + str(max) 
    def computeMin(self):
            min = self.sensorMeasurements[0]
            for i in self.sensorMeasurements:
                if(i<min):
                    min =i          
            return "Min for this measurement is: " + str(min)
if __name__ == "__main__":
    sensorName = input("Enter sensor name: ")
    sensorID = input("Enter sensor ID: ")
    sensorMeasurements = []
    stringVersion = open("Exercises\\EX_1\\sensorMeasurements.txt").read().split(",")
    for item in stringVersion:
        item = int(item)
        sensorMeasurements.append(item)
    sensor1 = temperatureSensor(sensorName,sensorID,sensorMeasurements)
    print(sensor1.computeAverage())
    print(sensor1.computeMax())
    print(sensor1.computeMin())
    

    
