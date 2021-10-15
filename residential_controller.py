from enum import Enum

class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.status = ColumnStatus.ONLINE
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.elevatorList = []
        self.callButtonList = []

        self.createElevators(_amountOfFloors, _amountOfElevators) 
        self.createCallButtons(_amountOfFloors)
        
        
        
    def display(self):
        print("Created column " + str(self.ID))
        print("Number of floors: " + str(self.amountOfFloors))
        print("Created Number of elevators: " + str(self.amountOfElevators))
        print("----------------------------------")
    

    def createCallButtons(self, _amountOfFloors):
        for x in range(self.amountOfFloors):
            if x < _amountOfFloors: #'//If it's not the last floor
                callButton = CallButton(x + 1, x + 1, 'up') #'//id, status, floor, direction
                self.callButtonList.append(callButton) 
            
            if x > 1: #'//If it's not the first floor
                callButton = CallButton(x + 1, x + 1, 'down') #'//id, status, floor, direction
                self.callButtonList.append(callButton) 
                
            
            #buttonFloor += 1
            #print("call button " + str(self.callButtonList[x].ID) + " has been created")


    def createElevators(self, _amountOfFloors, _amountOfElevators):
        #print("hello")
        for x in range(_amountOfElevators):
            elevator = Elevator(x + 1, _amountOfFloors) #'//id, status, amountOfFloors, currentFloor
            self.elevatorList.append(elevator)
            #self.elevatorID += 1
            print("elevator " + str(self.elevatorList[x].ID) + " has been created")
        

    #'//Simulate when a user press a button outside the elevator
    def requestElevator(self, _floor, _direction):
        print("-CLIENT CALLS THE ELEVATOR AT FLOOR " +
                str(_floor) + " TO GO " + str(_direction) + "-")
        elevator = self.findElevator(_floor, _direction)
        elevator.floorRequestList.append(_floor)
        elevator.sortFloorList()
        print()
        print("ELEVATOR " + str(elevator.ID) + " MOVING FROM FLOOR " +
                str(elevator.currentFloor) + " TO FLOOR " + str(_floor))
        elevator.move()
        elevator.operateDoors()
        return elevator


    def findElevator(self, requestedFloor, requestedDirection):
        bestElevatorInformations = {
            "bestElevator": None,
            "bestScore": 5,
            "referenceGap": 10000000
        }

        for elevator in self.elevatorList:
            if requestedFloor == elevator.currentFloor and elevator.status == 'stopped' and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    1, elevator, bestElevatorInformations, requestedFloor)

            elif requestedFloor > elevator.currentFloor and elevator.direction == 'up' and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    2, elevator, bestElevatorInformations, requestedFloor)

            elif requestedFloor < elevator.currentFloor and elevator.direction == 'down' and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    2, elevator, bestElevatorInformations, requestedFloor)

            elif elevator.status == 'idle':
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    3, elevator, bestElevatorInformations, requestedFloor)

            else:
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    4, elevator, bestElevatorInformations, requestedFloor)

            #bestElevator = bestElevatorInformations["bestElevator"]
            #bestScore = bestElevatorInformations["bestScore"]
            #referenceGap = bestElevatorInformations["referenceGap"]
        print()
        print(">>[ELEVATOR SENT]:")
        print(bestElevatorInformations["bestElevator"])
        return bestElevatorInformations["bestElevator"]

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, floor):
        if scoreToCheck < bestElevatorInformations["bestScore"]:
            bestElevatorInformations["bestScore"] = scoreToCheck
            bestElevatorInformations["bestElevator"] = newElevator
            bestElevatorInformations["referenceGap"] = abs(
                newElevator.currentFloor - floor)
        elif bestElevatorInformations["bestScore"] == scoreToCheck:
            gap = abs(newElevator.currentFloor - floor)
            if (bestElevatorInformations["referenceGap"] > gap):
                bestElevatorInformations["bestScore"] = scoreToCheck
                bestElevatorInformations["bestElevator"] = newElevator
                bestElevatorInformations["referenceGap"] = gap
        return bestElevatorInformations

            

class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = 'idle'
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = 1
        self.direction = None
        self.overweight = None
        self.obstruction = None
        self.door = Door(_id)
        self.floorRequestButtonList = [] 
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors)

        
    def createFloorRequestButtons(self, _amountOfFloors):
        #buttonFloor = 1
        for x in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(x + 1, x + 1) #'//id, status, floor
            self.floorRequestButtonList.append(floorRequestButton)
            #buttonFloor += 1
            #self.floorRequestButtonID += 1

    def requestFloor(self, _floor):
        print()
        print("||-PASSENGER NOW INSIDE ELEVATOR REQUESTS TO GO TO FLOOR " +
              str(_floor) + "-||")
        self.floorRequestList.append(_floor)
        self.sortFloorList()
        print()
        print("ELEVATOR " + str(self.ID) + " MOVES FROM FLOOR " +
              str(self.currentFloor) + " TO GO TO FLOOR " + str(_floor))
        self.move()

    def move(self): 
        #print("movefunction")
        while len(self.floorRequestList) != 0:
            destination = self.floorRequestList[0]
            self.status = 'moving'
            if self.currentFloor < destination:
                self.direction = 'up'
                while self.currentFloor < destination:
                    self.currentFloor += 1

            elif self.currentFloor > destination:
                self.direction = 'down'
                while self.currentFloor > destination:
                    self.currentFloor -= 1

            self.status = 'stopped'
            self.floorRequestList.pop()

        if len(self.floorRequestList) == 0:
            self.status = 'idle'

    def sortFloorList(self):
        if self.direction == 'up':
            sorted(self.floorRequestList)
        else:
            sorted(self.floorRequestList, reverse=True)
          

    def operateDoors(self):
        #print("operate Doors")
        self.doorStatus = 'opened'
        #WAIT 5 SECONDS
        if not self.overweight:
            self.door.status = 'closing'

            if not self.door.obstruction:
                self.door.status = 'closed'

            else:
                self.door.obstruction = False
                self.operateDoors()
        else:
            while self.overweight:
                self.overweight = False
                self.operateDoors()
           

class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.status = ButtonStatus.OFF
        self.floor = _floor
        self.direction = _direction


class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.status = ButtonDirection.UP
        self.floor = 1


class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = DoorStatus.OPENED
        self.obstruction = None



class ColumnStatus(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'


# class ElevatorStatus(Enum):
#     IDLE = 'idle'
#     UP = 'up'
#     DOWN = 'down'
#     MOVING = 'moving'
#     STOPPED = 'stopped'

class ButtonStatus(Enum):
    ON = 'on'
    OFF = 'off'

class ButtonDirection(Enum):
    UP = 'up'
    DOWN = 'down'


class DoorStatus(Enum):
    OPENED = 'opened'
    CLOSED = 'closed'


class SensorStatus(Enum):
    ON = 'on'
    OFF = 'off'



def scenario1():
    print()
    print("______________________________________________________________________________________________")
    print()
    print("--------------------SCENARIO #1--------------------")
    column = Column(1, 10, 2)
    column.display()
    column.elevatorList[0].currentFloor = 2
    column.elevatorList[1].currentFloor = 6
    print()
    elevator = column.requestElevator(3, 'up')
    elevator.requestFloor(7)
    print()
    print("______________________________________________________________________________________________")
    print()



# ----------------------SCENARIO 2---------------------//

# Elevator 1 is Idle at floor 10
# Elevator 2 is idle at floor 3
# Someone is on the 1st floor and requests the 6th floor.
# Elevator 2 should be sent.
# 2 minutes later, someone else is on the 3rd floor and requests the 5th floor. Elevator 2 should be sent.
# Finally, a third person is at floor 9 and wants to go down to the 2nd floor.
# Elevator 1 should be sent.

def scenario2():
    print()
    print("______________________________________________________________________________________________")
    print()
    print("--------------------SCENARIO #2--------------------")
    column = Column(1, 10, 2)
    column.display()
    column.elevatorList[0].currentFloor = 10
    column.elevatorList[1].currentFloor = 3
    print()
    print("-----[REQUEST #1]-----")
    print()
    elevator = column.requestElevator(1, 'up')
    elevator.requestFloor(6)
    print()
    print()
    print("-----[REQUEST #2]-----")
    print()
    print()
    column.elevatorList[1].currentFloor = 6
    elevator = column.requestElevator(3, 'up')
    elevator.requestFloor(5)
    print()
    print()
    print("-----[REQUEST #3]-----")
    print()
    print()
    elevator = column.requestElevator(9, 'down')
    elevator.requestFloor(2)
    print()
    print("______________________________________________________________________________________________")
    print()

# ----------------------SCENARIO 3---------------------//

# Elevator A is Idle at floor 10
# Elevator B is Moving from floor 3 to floor 6
# Someone is on floor 3 and requests the 2nd floor.
# Elevator A should be sent.
# 5 minutes later, someone else is on the 10th floor and wants to go to the 3rd. Elevator B should be sent.

def scenario3():
    print()
    print("______________________________________________________________________________________________")
    print()
    print("--------------------SCENARIO #3--------------------")
    column = Column(1, 10, 2)
    column.display()
    column.elevatorList[0].currentFloor = 10
    column.elevatorList[1].currentFloor = 3
    column.elevatorList[1].status = 'moving'
    print()
    print("-----[REQUEST #1]-----")
    print()
    elevator = column.requestElevator(3, 'down')
    elevator.requestFloor(2)
    print()
    print("-----[REQUEST #2]-----")
    print()
    column.elevatorList[1].currentFloor = 6
    column.elevatorList[1].status = 'idle'
    elevator = column.requestElevator(10, 'down')
    elevator.requestFloor(3)
    print()
    print("______________________________________________________________________________________________")
    print()



# scenario1()
# scenario2()
scenario3()


