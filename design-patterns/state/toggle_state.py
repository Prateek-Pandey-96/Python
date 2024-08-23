from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context) -> None:
        pass

class OffState(State):
    def handle(self, context):
        print("moving from off state to on state")
        context.state = OnState()

class OnState(State):
     def handle(self, context):
        print("moving from on state to off state")
        context.state = OffState()

class Context:
    def __init__(self, state: State) -> None:
        self.state = state
    
    def toggleSwitch(self):
        self.state.handle(self)

if __name__=="__main__":
    context = Context(OffState())

    context.toggleSwitch()
    context.toggleSwitch()
    context.toggleSwitch()
    context.toggleSwitch()
    context.toggleSwitch()

# Practice problem

# implement an elevator running between ground floor and nth floor
# at each floor you have two options, go up or down
# you can't go belor ground floor and above nth floor