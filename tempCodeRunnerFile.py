t = Column(1, ColumnStatus.ACTIVE, 10, 2)
print(t.display())
print(t.requestElevator(1, ButtonDirection.UP))
print(t.findElevator(1, 1))

elevtesting = Elevator(1,ElevatorStatus.UP, 2, 4, SensorStatus.OFF, SensorStatus.OFF)
print(elevtesting.move())