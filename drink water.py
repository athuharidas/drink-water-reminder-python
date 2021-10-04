import time
from plyer import notification

if __name__ == "__main__":
   while True:
    notification.notify(
        title = "PLEASE DRINK WATER",
        message = " The amount of drinking water required to maintain good health varies, and depends on physical activity level, age, health-related issues, and environmental conditions",
        
        timeout = 10
        
    )
    time.sleep(60*60)

