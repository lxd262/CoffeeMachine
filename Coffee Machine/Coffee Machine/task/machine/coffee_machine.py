# Write your code here
class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9

    def check_water(self, req_amount):
        if self.water - req_amount >= 0:
            self.water -= req_amount
            return False
        else:
            return True

    def check_milk(self, req_amount):
        if self.milk - req_amount >= 0:
            self.milk -= req_amount
            return False
        else:
            return True

    def check_coffee_beans(self, req_amount):
        if self.coffee_beans - req_amount >= 0:
            self.coffee_beans -= req_amount
            return False
        else:
            return True

    def check_disposable_cups(self, req_amount):
        if self.disposable_cups - req_amount >= 0:
            self.disposable_cups -= req_amount
            return False
        else:
            return True

    def machine_status(self):
        return (
            "The coffee machine has:\n{0} of water\n{1} of milk\n{2} of coffee beans\n{3} of disposable cups\n${4} of money\n".format(
                str(self.water), str(self.milk), str(self.coffee_beans), str(self.disposable_cups), str(self.money)))

    def buy(self):
        coffee_type = input(
            "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee_type == "1":
            if self.check_water(250):
                return "Sorry, not enough water!"
            if self.check_coffee_beans(16):
                return "Sorry, not enough coffee beans!"
            if self.check_disposable_cups(1):
                return "Sorry, not enough disposable cups!"
            self.money += 4
        elif coffee_type == "2":
            if self.check_water(350):
                return "Sorry, not enough water!"
            if self.check_milk(75):
                return "Sorry, not enough milk!"
            if self.check_coffee_beans(20):
                return "Sorry, not enough coffee beans!"
            if self.check_disposable_cups(1):
                return "Sorry, not enough disposable cups!"
            self.money += 7
        elif coffee_type == "3":
            if self.check_water(200):
                return "Sorry, not enough water!"
            if self.check_milk(100):
                return "Sorry, not enough milk!"
            if self.check_coffee_beans(12):
                return "Sorry, not enough coffee beans!"
            if self.check_disposable_cups(1):
                return "Sorry, not enough disposable cups!"
            self.money += 6
        elif coffee_type == "back":
            return
        else:
            return "Invalid input, please try again\n"
        return "I have enough resources, making you a coffee!\n"

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        return

    def take(self):
        money_taken = self.money
        self.money = 0
        return "I gave you $" + str(money_taken) + "\n"

    def use(self, user_action):
        while user_action != "exit":
            if user_action == "buy":
                print(self.buy())
            elif user_action == "fill":
                print(self.fill())
            elif user_action == "take":
                print(self.take())
            elif user_action == "remaining":
                print("\n" + self.machine_status())
            user_action = input("Write action (buy, fill , take, remaining, exit):")


my_coffee_machine = CoffeeMachine()
my_coffee_machine.use(input("Write action (buy, fill , take, remaining, exit):\n"))
