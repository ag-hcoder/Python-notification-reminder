from plyer import notification
import time
while(1):
    notification.notify(
        title = "This is a reminder",
        message = "This can be used for any notification",
        app_icon = "/home/hardik/Desktop/icon.ico",
        timeout = 10
    )
    time.sleep(10)
