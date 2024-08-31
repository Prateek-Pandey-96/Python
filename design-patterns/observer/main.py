from user import User
from userService import UserService
from subscribers.cacheService import CacheService
from subscribers.notificationService import NotificationService
from subscribers.loggerService import LoggerService

if __name__ == '__main__':
    """
    Saving a user to database required three additonal events
    1> logging the save action
    2> sending a notification
    3> updating the cache
    """
    userService = UserService()
    
    userService.addSubscriber(CacheService())
    userService.addSubscriber(NotificationService())
    userService.addSubscriber(LoggerService())
    
    userService.saveUser(User("user1", "user1@gmail.com"))


