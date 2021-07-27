from src.bus_stop import BusStop


class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.passengers =[]
        self.takings = 0

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers = []

    def ticket_sale(self, person, price):
        person.cash -= price
        self.takings += price
        self.pick_up(person)

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            self.pick_up(person)
        
        BusStop.clear(bus_stop)
            
    def remaining_capacity(self):
        return int(self.capacity) - len(self.passengers)
        
        #queue for the bus
        #check if the bus is the right bus
        #pay for the bus
        #passenger money goes down
        #bus money goes up
        #get on the bus
        #bus capacity decreases
        # self.ticket_sale(person.person, self.price)
        # self.capacity -= 1