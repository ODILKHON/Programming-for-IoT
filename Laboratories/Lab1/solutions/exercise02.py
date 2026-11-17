class ConditionRule:
#Creates the parent (super-class) blueprint that all rules share.
    def __init__(self, threshold):
#Runs automatically when a new rule is created, saving the limit number inside
        self.threshold = threshold

    def evaluate(self, value):
        return value > self.threshold
#Checks whether a sensor measurement (value) is greater than self.threshold, returning True or False.

class TemperatureRule(ConditionRule):

    def evaluate(self, temperature):
        return temperature > self.threshold


class LightRule(ConditionRule):

    def evaluate(self, light):
        return light > self.threshold
"""
class TemperatureRule(ConditionRule): and class LightRule(ConditionRule):: 
Putting (ConditionRule) in parentheses means both classes inherit 
from ConditionRule. They automatically get the __init__ method 
from ConditionRule without rewriting it, while defining their 
own specialized evaluate method for temperature or light readings.
"""

class RuleController:

    def __init__(self):
        self.rules = {}

    def add(self, name, rule):
        self.rules[name] = rule
    """
    self.rules = {}: Creates an empty Python dictionary to store all active rules. The rule's name (e.g., "AC_ON") acts as the key, and the rule object (TemperatureRule or LightRule) acts as the value.   def add(self, name, rule):: Saves a new rule into self.rules under its given name.  
    """
    def update(self, name, threshold):

        if name in self.rules:
            self.rules[name].threshold = threshold
            print("Rule updated.")
        else:
            print("Rule not found.")

    def delete(self, name):

        if name in self.rules:
            del self.rules[name]
            print("Rule deleted.")
        else:
            print("Rule not found.")

    def evaluate(self, temperature, light):

        for name, rule in self.rules.items():

            if isinstance(rule, TemperatureRule):
                result = rule.evaluate(temperature)
                print(name, ":", result)

            elif isinstance(rule, LightRule):
                result = rule.evaluate(light)
                print(name, ":", result)
    """
    for name, rule in self.rules.items():: Loops through every saved rule, unpacking both its name and its rule object.   isinstance(rule, TemperatureRule): Checks what type of object rule is. If it is a TemperatureRule, it passes temperature into rule.evaluate(...); if it is a LightRule, it passes light, then prints True or False.
    That rule.evaluate(...) call is invoking the evaluate method defined inside the TemperatureRule class.
    """
    def rulesList(self):

        for name, rule in self.rules.items():

            if isinstance(rule, TemperatureRule):
                print(
                    name,
                    "- Temperature - threshold:",
                    rule.threshold
                )

            elif isinstance(rule, LightRule):
                print(
                    name,
                    "- Light - threshold:",
                    rule.threshold
                )
"""
def rulesList(self):: Loops through all stored rules, checks whether each one is a temperature or light rule using isinstance(), and prints its name, type, and current threshold.
"""

# Main program

controller = RuleController()

while True:

    command = input(
        "\nEnter command (add/update/delete/evaluate/rules/exit): "
    )

    if command == "add":

        ruleType = input(
            "Enter rule type (temperature/light): "
        )

        name = input("Enter rule name: ")

        threshold = float(
            input("Enter threshold: ")
        )

        if ruleType == "temperature":

            rule = TemperatureRule(threshold)
            controller.add(name, rule)

        elif ruleType == "light":

            rule = LightRule(threshold)
            controller.add(name, rule)

        else:

            print("Invalid rule type.")


    elif command == "update":

        name = input("Enter rule name: ")

        threshold = float(
            input("Enter new threshold: ")
        )

        controller.update(name, threshold)


    elif command == "delete":

        name = input("Enter rule name: ")

        controller.delete(name)


    elif command == "evaluate":

        temperature = float(
            input("Enter current temperature: ")
        )

        light = float(
            input("Enter current light level: ")
        )

        controller.evaluate(
            temperature,
            light
        )


    elif command == "rules":

        controller.rulesList()


    elif command == "exit":

        break


    else:

        print("Invalid command.")