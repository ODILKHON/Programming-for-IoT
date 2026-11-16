import json
class temperatureSensor:
    def __init__(self, sensorID,sensorName, yearFabrication, calibrated):
        self.sensorID = sensorID
        self.sensorName = sensorName
        self.yearFabrication = yearFabrication
        self.calibrated = calibrated
    def asDictionary(self):
        sensorDict = {
            "sensorID": self.sensorID,
            "sensorName": self.sensorName,
            "yearFabrication": self.yearFabrication,
            "calibrated": self.calibrated
        }
        print(sensorDict)
        return sensorDict
if __name__ == "__main__":
    tempDict = json.load(open("Exercises\\EX_1\\temperatureSensor.json"))
    sensor1 = temperatureSensor(**tempDict)
    sensor1.asDictionary()
    sensor2 = temperatureSensor("s-002", "DHT22", 2023, "no")

    json.dump(sensor2.asDictionary(), open("Exercises\\EX_1\\Exercise_6th_json.json", "w"))