from user import User
from subject.subject import Subject

class UserService(Subject):
    subscribers = set()
    
    def saveUser(self, user: User):
        print(f"user saved: {user.name}")
        # print(self.subscribers)
        self.notifyAll(user)

    def addSubscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def removeSubscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notifyAll(self, event: User):
        for sbr in self.subscribers:
            sbr.processEvent(event)