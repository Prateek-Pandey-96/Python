from .subscriber import Subscriber

class NotificationService(Subscriber):
    
    def processEvent(self, event):
        print(f"sending a notificatione: {event.name}")