def scenario2(): 
#     print()
#     print("****************************** SCENARIO 2: ******************************")
#     columnScenario2 = Column(1, ColumnStatus.ACTIVE, 10, 2)
#     columnScenario2.display()  
#     columnScenario2.elevatorsList[0].floor = 10
#     columnScenario2.elevatorsList[1].floor = 3
    
#     print()
#     print("Person 1: (elevator 2 is expected)")
#     columnScenario2.requestElevator(1, ButtonDirection.UP)
#     columnScenario2.elevatorsList[1].requestFloor(6, columnScenario2)
#     print("----------------------------------")
#     print()
#     print("Person 2: (elevator 2 is expected)")
#     columnScenario2.requestElevator(3, ButtonDirection.UP)
#     columnScenario2.elevatorsList[1].requestFloor(5, columnScenario2)
#     print("----------------------------------")
#     print()
#     print("Person 3: (elevator 1 is expected)")
#     columnScenario2.requestElevator(9, ButtonDirection.DOWN)
#     columnScenario2.elevatorsList[0].requestFloor(2, columnScenario2)
#     print("==================================")
# scenario2()