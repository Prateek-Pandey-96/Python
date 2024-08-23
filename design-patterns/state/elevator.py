from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def movingUp(self, elevator) -> None:
        pass
    
    @abstractmethod
    def movingDown(self, elevator) -> None:
        pass

class GoingUp(State):
    def movingUp(self, elevator) -> None:
        print("going up")
        elevator.curr_floor += 1
        
    def movingDown(self, elevator) -> None:
        print("was going up, need to change state")
        elevator.state = GoingDown()
        elevator.curr_floor -= 1

class GoingDown(State):
    def movingUp(self, elevator) -> None:
        print("was goind down, need to change state")
        elevator.state = GoingUp()
        elevator.curr_floor += 1

    def movingDown(self, elevator) -> None:
        print("going down")
        elevator.curr_floor -= 1


class Elevator:
    def __init__(self, floors: int, state: State) -> None:
        self.floors = floors
        self.curr_floor = 0
        self.state = state

    def pressUpButton(self):
        if elevator.curr_floor == elevator.floors:
            print("stop this nuisance")
            return
        self.state.movingUp(self)
    
    def pressDownButton(self):
        if elevator.curr_floor == 0:
            print("stop this nuisance")
            return
        self.state.movingDown(self)
    
if __name__=="__main__":
    elevator = Elevator(3, GoingUp())

    elevator.pressUpButton()
    print(elevator.curr_floor)
    elevator.pressUpButton()
    print(elevator.curr_floor)
    elevator.pressUpButton()
    print(elevator.curr_floor)
    elevator.pressDownButton()
    print(elevator.curr_floor)
    elevator.pressUpButton()
    print(elevator.curr_floor)



