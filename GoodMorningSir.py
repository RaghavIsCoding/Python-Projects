import time

hour = int(time.strftime('%H'))
if hour >= 0 and hour <= 12:
    print("Good Morning Sir")

elif hour >= 13 and hour <= 17:
    print("Good Afternoon Sir")

elif hour >= 18 and hour <= 24:
    print("Good Night Sir")