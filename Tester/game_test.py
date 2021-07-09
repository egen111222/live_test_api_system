import random
import requests

class Walker:
    def __init__(self,position = 0,id=0):
        self.good = 0
        self.position = position
        self.coins = 200
        self.id = id
    def move_right(self):
        if self.position < len(plants)-1:
            self.position += 1
            requests.post("http://127.0.0.1:8000/game/set_events",
              data={"name":"move_right","place":self.position})
    def move_left(self):
        if self.position > 1:
            self.position -= 1
            requests.post("http://127.0.0.1:8000/game/set_events",
              data={"name":"move_left","place":self.position})
            
    def profit(self,middle_price):
        if plants[self.position].price < middle_price and self.coins > plants[self.position].price:
            self.good += 1
            self.coins -= plants[self.position].price
            plants[self.position].set_price()
            requests.post("http://127.0.0.1:8000/game/set_events",
              data={"name":"buy","place":self.position})
        elif self.good > 0 and plants[self.position].price > middle_price:
            self.coins += plants[self.position].price
            self.good -= 1
            plants[self.position].set_price()
            requests.post("http://127.0.0.1:8000/game/set_events",
              data={"name":"sell","place":self.position})


        

class Plant:
    def __init__(self,good = 50):
        self.good = good
        self.set_price()
    def set_price(self):
        self.price  = 200/self.good
        

walkers = []
plants = []


for i in range(100):
    plants.append(Plant(random.randint(20,100)))


for i in range(10):
    walkers.append(Walker(random.randint(0,len(plants)),i))



def set_middleprice():
    tmp = 0
    for i in plants:
        tmp += i.price
    tmp /= len(plants)
    return tmp


while True:
    middle_price = set_middleprice()
    for walker in walkers:
        choose = random.randint(1,3)
        if choose == 1:
            walker.move_left()
        elif choose == 2:
            walker.move_right()
        elif choose == 3:
            walker.profit(middle_price)
        requests.post("http://127.0.0.1:8000/game/set_notes",
              data={"number_user":walker.id,"coins":walker.coins,"goods":walker.good})






