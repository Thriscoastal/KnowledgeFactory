from robot_models import Robot, SmartRobot

def main():
    print("Starting Factory...")
    print(Robot.get_population())

    r1 = Robot("R2D2", 100)
    r2 = SmartRobot("ChatBot-9000", 85, "GPT-4")

    print("\n--- Testing Polymorphism ---")
    r1.speak() 
    r2.speak() 

    print("\n--- Testing Encapsulation ---")
    print(f"{r2.name}'s battery is at {r2.battery}%")

    print("\n--- Testing Static and Class Methods ---")
    print(f"Is 150 a valid battery? {Robot.is_valid_battery(150)}")
    print(Robot.get_population()) 

if __name__ == "__main__":
    main()