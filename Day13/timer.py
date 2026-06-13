import time

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print(seconds)
    #waits for one second
    time.sleep(1)  
    #decrements the time by 1 second.
    seconds -= 1

print("Time's up!")