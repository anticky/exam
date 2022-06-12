import logging
import random
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')
class Bebrik:
    def __init__(self, name="Bebrik", job=None, game=None, home=None, car=None):
        self.name = name
        self.job = job
        self.game = game
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.zavisimost = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_game(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.game = Game(game_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        if manage == "fuel":
            print("I bought fuel")
            logging.info('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "sweets":
            print("Yummy yummy!")
            self.money -= 15
            self.satiety += 2
            self.gladness += 10

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        bebrik_indexes = self.name + "'s indexes"
        print(f"{bebrik_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        print(f"Zavisimost – {self.zavisimost}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")


    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            logging.critical('depression')
            return False
        if self.satiety < 0:
            print("Dead…")
            logging.critical('dead')
            return False
        if self.money < -500:
            print("Bankrupt…")
            logging.warning('bankrupt')
            return False
        if self.zavisimost > 90:
            print("Igromaniya...")
            logging.critical('igromania')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
            logging.info('bought a car')
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        if self.game is None:
            self.get_game()
            print(f"I don't like any games, going to get a game {self.game.game} with zavisimost {self.game.zavisimost}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house ")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="sweets")


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


brands_of_car = {
    "plot": {"fuel": 100, "strength": 100, "consumption": 6},
    "paketik": {"fuel": 50, "strength": 40, "consumption": 10},
    "derevyaska": {"fuel": 70, "strength": 150, "consumption": 8},
    "karton": {"fuel": 80, "strength": 120, "consumption": 14}

}


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car can not move")
            return False


job_list = {
    "solomnik": {"salary": 50, "gladness_less": 10},
    "coker": {"salary": 40, "gladness_less": 3},
    "derevyashkin": {"salary": 45, "gladness_less": 25},
    "Ploter": {"salary": 70, "gladness_less": 1}
}


class Job:
    def __init__(self, list_of_jobs):
        self.job = random.choice(list(list_of_jobs))
        self.salary = list_of_jobs[self.job]["salary"]
        self.gladness_less = list_of_jobs[self.job]["gladness_less"]


game_list = {
    "CS:GO": {"zavisimost": 60, "gladness_less": 25},
    "Fortnite": {"zavisimost": 90, "gladness_less": 34},
    "Dota 2": {"zavisimost": 50, "gladness_less": 1},
    "Rust": {"zavisimost": 120, "gladness_less": 25}
}


class Game:
    def __init__(self, list_of_games):
        self.game = random.choice(list(list_of_games))
        self.zavisimost = list_of_games[self.game]["zavisimost"]
        self.gladness_less = list_of_games[self.game]["gladness_less"]


nick = Bebrik(name="Bababoi")


for day in range(1, 8):
    if nick.live(day) == False:
        break
