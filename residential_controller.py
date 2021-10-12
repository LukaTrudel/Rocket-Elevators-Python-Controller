from enum import Enum
import time
import math
import random

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
        
        
        
    def display(self):
        print("Created column " + str(self.id))
        print("Number of floors: " + str(self.amountOfFloors))
        print("Created Number of elevators: " + str(self.amountOfElevators))
        print("----------------------------------")


    def createCallButtons(self, _amountOfFloors):
        #buttonFloor = 1
        print('patate')
        #print(buttonFloor)
        for x in range(self.amountOfFloors -1):
            if x < _amountOfFloors: #'//If it's not the last floor
                callButton = CallButton(x + 1, ButtonStatus.OFF, x + 1, ButtonDirection.UP) #'//id, status, floor, direction
                self.callButtonsList.append(callButton) 
                #x += 1
            
            if x > 1: #'//If it's not the first floor
                callButton = CallButton(x + 1, ButtonStatus.OFF, x + 1, ButtonDirection.DOWN) #'//id, status, floor, direction
                self.callButtonsList.append(callButton) 
                #x += 1
            
            #buttonFloor += 1
            print("call button " + str(self.callButtonsList[x].id) + " has been created")


    def createElevators(self, _amountOfFloors, _amountOfElevators):
        print("hello")
        for x in range(_amountOfElevators):
            elevator = Elevator(x + 1, ElevatorStatus.IDLE, _amountOfFloors, 1, SensorStatus.OFF, SensorStatus.OFF) #'//id, status, amountOfFloors, currentFloor
            self.elevatorsList.append(elevator)
            #self.elevatorID += 1
            print("elevator " + str(self.elevatorsList[x].id) + " has been created")
        

    #'//Simulate when a user press a button outside the elevator
    def requestElevator(self, floor, direction):
        for x in (self.elevatorsList):
            print("Elevator" + str(x.id) + " | " + "Floor: " + str(x.currentFloor) + " | " + "Status: " + str(x.status.value))
        elevator = self.findElevator(floor, direction) 
        self.callButtonsList.append(floor)
        print("requestElevatortest")
        elevator.move()
        elevator.operateDoors()

        print("ARE WE MAKING IT PAST THE FUNCTION CALLS")
        
        return elevator
        
       
    print("trying")
    
    def findElevator(self, currentFloor, direction):
        print('deez')
        activeElevatorList = []
        idleElevatorList = []
        sameDirectionElevatorList = []
        for x in (self.elevatorsList):
            if x.status != ElevatorStatus.IDLE: 
                if x.status == ElevatorStatus.UP and x.floor <= currentFloor or x.status == ElevatorStatus.DOWN and x.floor >= currentFloor:
                    activeElevatorList.append(x)
            else:
                idleElevatorList.append(x)
        
        if len(activeElevatorList) > 0: 
            sameDirectionElevatorList = [elevator for elevator in activeElevatorList if elevator.status == direction]
        
        if len(sameDirectionElevatorList) > 0:
            bestElevator = self.findNearestElevator(currentFloor, sameDirectionElevatorList)
        else:
            bestElevator = self.findNearestElevator(currentFloor, idleElevatorList)
        
        
        print('were having a good time')
        return bestElevator
        
        
            
    def findNearestElevator(self, currentFloor, selectedList):
        bestElevator = selectedList[0]
        bestDistance = abs(selectedList[0].currentFloor - currentFloor) 
    
        for elevator in selectedList:
            if abs(elevator.currentFloor - currentFloor) < bestDistance:
                bestElevator = elevator
        
        print()
        print("ELEVATOR " + str(bestElevator.id) + " WAS CALLED")            
        return bestElevator

    

            

class Elevator:
    def __init__(self, _id, _status, _amountOfFloors, _currentFloor, _weightSensorStatus, _obstructionSensorStatus):
        self.id = _id
        self.status = _status
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = _currentFloor
        self.direction = None
        self.weightSensor = _weightSensorStatus
        self.obstructionSensor = _obstructionSensorStatus
        self.door = Door(_id, DoorStatus.CLOSED)
        self.floorRequestsButtonsList = [] 
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors)

        
    def createFloorRequestButtons(self, _amountOfFloors):
        #buttonFloor = 1
        for x in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(x + 1, ButtonStatus.OFF, x + 1) #'//id, status, floor
            self.floorRequestsButtonsList.append(floorRequestButton)
            #buttonFloor += 1
            #self.floorRequestButtonID += 1
        

    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    def move(self): 
        print("movefunction")
        while len(self.floorRequestList) != 0:
            _requestedFloor =  self.floorRequestList[0]
            self.status = ElevatorStatus.MOVING
            print('end of the move function')
            if self.currentFloor < _requestedFloor:
                self.status = ElevatorStatus.UP
                self.sortFloorList()
                print('end of the move function')
            while self.currentFloor < _requestedFloor:
                self.currentFloor += 1
                self.screenDisplay = self.currentFloor
            
            if self.currentFloor > _requestedFloor:
                self.status = ElevatorStatus.DOWN
                self.sortFloorList()
                print('end of the move function')
            while self.currentFloor > _requestedFloor:
                self.currentFloor -= 1
                self.screenDisplay = self.currentFloor
                
            
            self.status = ElevatorStatus.IDLE
            self.floorRequestList.pop(0)
        
            self.status = ElevatorStatus.IDLE
            print('end of the move function')
            

    def sortFloorList(self):
        if self.direction(ElevatorStatus.UP):
            self.floorRequestList.sort()
        else:
            self.floorRequestList.sort(reverse=True)

    def operateDoors(self):
        self.door = DoorStatus.OPENED
        #time.sleep(waiTime)
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
    def __init__(self, _id, _status, _floor):
        self.id = _id
        self.status = _status
        self.foor = _floor


class Door:
    def __init__(self, _id, _status):
        self.id = _id
        self.status = _status



class ColumnStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


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




t = Column(1, ColumnStatus.ACTIVE, 10, 2)
print(t.display())
print(t.requestElevator(1, ButtonDirection.UP))
print(t.findElevator(1, 1))

elevtesting = Elevator(1,ElevatorStatus.MOVING, 10, 4, SensorStatus.OFF, SensorStatus.OFF)
print(elevtesting.move())
