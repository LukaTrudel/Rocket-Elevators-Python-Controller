# def scenario2():
#     print()
#     print("______________________________________________________________________________________________")
#     print()
#     print("--------------------SCENARIO #2--------------------")
#     column = Column(1, ColumnStatus.ACTIVE, 10, 2)
#     column.display()
#     column.elevatorList[0].currentFloor = 10
#     column.elevatorList[1].currentFloor = 3
#     print()
#     print("-----[REQUEST #1]-----")
#     print()
#     elevator = column.requestElevator(1, ButtonDirection.UP)
#     elevator.requestFloor(6)
#     print()
#     print()
#     print("-----[REQUEST #2]-----")
#     print()
#     print()
#     column.elevatorList[1].currentFloor = 6
#     elevator = column.requestElevator(3, ButtonDirection.UP)
#     elevator.requestFloor(5)
#     print()
#     print()
#     print("-----[REQUEST #3]-----")
#     print()
#     print()
#     elevator = column.requestElevator(9, ButtonDirection.DOWN)
#     elevator.requestFloor(2)
#     print()
#     print("______________________________________________________________________________________________")
#     print()

# scenario2()