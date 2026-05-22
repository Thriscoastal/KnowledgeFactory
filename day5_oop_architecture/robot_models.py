from abc import ABC, abstractmethod
class Machine(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Robot(Machine):
    population_count = 0 

    def __init__(self, name, battery_level):
        self.name = name 
        
        self.__battery_level = battery_level 

        Robot.population_count += 1

    def start_engine(self):
        print(f"{self.name} is booting up its OS...")

    @property
    def battery(self):
        return self.__battery_level

    def speak(self):
        print("Beep boop. I am a standard robot.")

    @classmethod
    def get_population(cls):
        return f"Total robots manufactured: {cls.population_count}"

    @staticmethod
    def is_valid_battery(level):
        return 0 <= level <= 100

class SmartRobot(Robot):
    def __init__(self, name, battery_level, ai_model):
        super().__init__(name, battery_level)
        self.ai_model = ai_model


    def speak(self):
        print(f"Hello! I am {self.name}, powered by {self.ai_model}. How can I help you today?")

