from random import randint
from time import sleep


class Lift():
    def __init__(self):
        self.dir = 'up'
        self.free_place = 5
        self.current_floor = 0
        self.people_inside = []
        self.summ = 0
        self.work_is = True

    def pick_up(self):
        opportunity = True
        count = 0
        while opportunity:
            for i in house[self.current_floor].rezidents:
                if i.dir == self.dir and self.free_place:
                    count += 1
                    self.people_inside.append(i)
                    self.free_place -= 1
                    house[self.current_floor].rezidents.remove(i)
                    break
            else:
                opportunity = False
        if count != 0:
            print('На {} этаже зашло {} жителей'.format(self.current_floor + 1, count))
            sleep(1)

    def exit(self):
        opportunity = True
        count = 0
        while opportunity:
            for i in self.people_inside:
                if i.go_to == self.current_floor + 1:
                    count += 1
                    self.free_place += 1
                    self.summ -= 1
                    self.people_inside.remove(i)
                    break
            else:
                opportunity = False
        if count != 0:
            print('На {} этаже вышло {} жителей'.format(self.current_floor + 1, count))
            sleep(1)

    def check_dir(self):
        if self.free_place == 5 and len(house[self.current_floor].rezidents) != 0:
            up, down = 0, 0
            for i in house[self.current_floor].rezidents:
                if i.dir == 'up':
                    up += 1
                else:
                    down += 1
            else:
                if up > down:
                    self.dir = 'up'
                elif up < down:
                    self.dir = 'down'

    def work(self):
        while self.work_is:
            self.exit()
            self.check_dir()
            self.pick_up()
            self.move()
            if self.summ == 0:
                self.work_is = False
        else:
            print('Программа завершена')

    def move(self):
        if self.current_floor == max_floor - 1:
            self.dir = 'down'
        elif self.current_floor == 0:
            self.dir = 'up'
        if self.dir == 'up':
            self.current_floor += 1
        else:
            self.current_floor -= 1


class Floor():
    def __init__(self, number, rezidents):
        self.number = number
        self.rezidents = rezidents


class Rezident():
    def __init__(self, current_floor, go_to):
        self.current_floor = current_floor
        self.go_to = go_to
        self.dir = 'up' if go_to > current_floor else 'down'


house = []
max_floor = randint(5, 20)
print('В доме {} этажей'.format(max_floor))
sleep(1)

lift = Lift()

for i in range(1, max_floor + 1):
    rezidents = []
    for j in range(0, randint(0, 10)):
        requirement = True
        while requirement:
            go_to = randint(1, max_floor)
            if go_to != i:
                requirement = False
        rezidents.append(Rezident(i, go_to))
        lift.summ += 1
    print('На {} этаже {} жителей'.format(i, len(rezidents)))
    sleep(1)
    house.append(Floor(i, rezidents))

lift.work()