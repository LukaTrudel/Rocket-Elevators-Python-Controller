from enum import Enum

elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1


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
       

       
    




class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.id = _id
        self.amountOfFloors = _amountOfFloors


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



''' ELEVATOR STATUS '''
class ElevatorStatus(Enum):
    IDLE = 'idle'
    UP = 'up'
    DOWN = 'down'

''' BUTTON STATUS '''
class ButtonStatus(Enum):
    ON = 'on'
    OFF = 'off'

''' BUTTON DIRECTION '''
class ButtonDirection(Enum):
    UP = 'up'
    DOWN = 'down'