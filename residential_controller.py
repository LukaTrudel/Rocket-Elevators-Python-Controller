from enum import Enum
import time

elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1
waitTime = 5

print("testing")
print("testing")

class Column:
    def __init__(self, _id, _status, _amountOfFloors, _amountOfElevators):
        self.id = _id
        self.status = _status
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.elevatorsList = []
        self.callButtonsList = []

        self.createElevators(_amountOfFloors, _amountOfElevators) 
        self.createCallButtons(_amountOfFloors)

        def createCallButtons(self, _amountOfFloors):
            buttonFloor = 1
        
            for _amountOfFloors in self.callButtonsList:
                if buttonFloor < _amountOfFloors: #'//If it's not the last floor
                    callButton = CallButton(callButtonID, ButtonStatus.OFF, ButtonDirection.UP) #'//id, status, floor, direction
                    self.callButtonsList.append(callButton) 
                    self.callButtonID += 1
                

                if buttonFloor > 1: #'//If it's not the first floor
                    callButton = CallButton(callButtonID, ButtonStatus.OFF, ButtonDirection.DOWN) #'//id, status, floor, direction
                    self.callButtonsList.append(callButton) 
                    self.callButtonID += 1
                
                buttonFloor += 1

        def createElevators(self, _amountOfFloors, _amountOfElevators): 
            for elevator in range(self._amountOfElevators):
                elevator = Elevator(elevatorID, ElevatorStatus.IDLE, _amountOfFloors, 1) #'//id, status, amountOfFloors, currentFloor
                self.elevatorsList.append(elevator)
                self.elevatorID += 1
        

       # '//Simulate when a user press a button outside the elevator
        def requestElevator(self, floor, direction):
            elevator = self.findElevator(floor, direction) 
            elevator.addFloorToFloorList(floor) 
            elevator.move()
            elevator.operateDoors()
            return elevator
       

        def findElevator(self, currentFloor, direction):
            activeElevatorList = []
            idleElevatorList = []
            sameDirectionElevatorList = []
            for x in (self.elevatorsList):
                if x.status != ElevatorStatus.IDLE: #verify if elevator is active and if the request is on the elevator way
                    if x.status == ElevatorStatus.UP and x.floor <= currentFloor or x.status == ElevatorStatus.DOWN and x.floor >= currentFloor:
                        activeElevatorList.append(x)
                else:
                    idleElevatorList.append(x)
            
            if len(activeElevatorList) > 0: #Create new list for elevators with same direction that the request
                sameDirectionElevatorList = [elevator for elevator in activeElevatorList if elevator.status == direction]
            
            if len(sameDirectionElevatorList) > 0:
                bestElevator = self.findNearestElevator(currentFloor, sameDirectionElevatorList)
            else:
                bestElevator = self.findNearestElevator(currentFloor, idleElevatorList)
                
            return bestElevator

                
        def findNearestElevator(self, currentFloor, selectedList):
            bestElevator = selectedList[0]
            bestDistance = abs(selectedList[0].floor - currentFloor) #abs() returns the absolute value of a number (always positive).
        
            for elevator in selectedList:
                if abs(elevator.floor - currentFloor) < bestDistance:
                    bestElevator = elevator
            
            print()
            print("ELEVATOR " + str(bestElevator.id) + " WAS CALLED")            
            return bestElevator




class Elevator:
    def __init__(self, _id, _status, _amountOfFloors, _currentFloor):
        self.id = _id
        self.status = _status
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = _currentFloor
        self.direction = None
        self.door = Door(_id, DoorStatus.CLOSED)
        self.floorRequestsButtonsList = [] 
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors)

        
        
        def createFloorRequestButtons(self, _amountOfFloors):
            buttonFloor = 1
            for buttonFloor in (_amountOfFloors):
                floorRequestButton = FloorRequestButton(floorRequestButtonID, ButtonStatus.OFF, buttonFloor) #'//id, status, floor
                self.floorRequestsButtonsList.append(floorRequestButton)
                buttonFloor += 1
                self.floorRequestButtonID += 1
        

        def requestFloor(self, floor):
            self.floorRequestList.append(floor)
            self.move()
            self.operateDoors()

        def move(self, _requestedFloor): 
            while len(self.floorRequestList) != 0:
                _requestedFloor =  self.floorRequestList[0]
                self.status = ElevatorStatus.MOVING

                if self.currentFloor < _requestedFloor:
                    self.status = ElevatorStatus.UP
                    self.sortFloorList()
                
                while self.currentFloor < _requestedFloor:
                    self.currentFloor += 1
                    self.screenDisplay = self.currentFloor
               
                if self.currentFloor > _requestedFloor:
                    self.status = ElevatorStatus.DOWN
                    self.sortFloorList()

                while self.currentFloor > _requestedFloor:
                    self.currentFloor -= 1
                    self.screenDisplay = self.currentFloor
                    
                
                self.status = ElevatorStatus.IDLE
                self.floorRequestList.pop(0)
            
            self.status = ElevatorStatus.IDLE

        def sortFloorList():
            if self.direction(ElevatorStatus.UP):
                self.floorRequestList.sort()
            else:
                self.floorRequestList.sort(reverse=True)

        def operateDoors(self, waiTime):
            self.door = DoorStatus.OPENED
            time.sleep(waitTime)
            if self.weightSensor == SensorStatus.OFF and self.obstructionSensor == SensorStatus.OFF:
                self.door = DoorStatus.CLOSED
            else:
                self.operateDoors()
           

class CallButton:
    def __init__(self, _id, _buttonStatus, _floor, _direction):
        self.id = _id
        self.status = _buttonStatus
        self.foor = _floor
        self.direction = _direction


class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.id = _id
        self.foor = _floor


class Door:
    def __init__(self, _id):
        self.id = _id


class ElevatorStatus(Enum):
    IDLE = 'idle'
    UP = 'up'
    DOWN = 'down'
    MOVING = 'moving'

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