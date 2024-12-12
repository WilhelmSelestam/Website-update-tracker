import pywhatkit
import time
from datetime import datetime
from datetime import timedelta

# pywhatkit.sendwhatmsg("+46734184838", "Message 2", 19, 44, 15, True, 2)

pywhatkit.sendwhatmsg_instantly("+46734184838", "Ju jävlar händer det, köp bijett för faan", 15, True, 3)

now = datetime.today()
print(now) 

result = now + timedelta(seconds=30)
print(result)