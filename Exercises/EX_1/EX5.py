class temperatureSensor:
    def __init__(self, sensorName, SensorID, fabricationDate, sensorMeasurements):
        self.sensorName = sensorName
        self.SensorID = SensorID
        self.fabricationDate = fabricationDate
        self.sensorMeasurements = sensorMeasurements
    def asDictionary(self):
        sensorDict = {
            "sensorID ":  self.SensorID,
            "sensorName ":  self.sensorName,
            "fabricationDate ":  self.fabricationDate,
            "sensorMeasurements ":  self.sensorMeasurements
        }
        print(sensorDict)
        return sensorDict
if __name__ == "__main__":
    sensorName = input("Enter sensor name: ")
    SensorID = input("Enter sensor ID: ")
    fabricationDate = input("Enter fabrication date: ")
    sensorMeasurements = []
    stringVersion = open("Exercises\\EX_1\\sensorMeasurements.txt").read().split(",")
    for item in stringVersion:
        item = int(item)
        sensorMeasurements.append(item)
    sensor1 = temperatureSensor(sensorName, SensorID, fabricationDate, sensorMeasurements)
    sensor1.asDictionary()