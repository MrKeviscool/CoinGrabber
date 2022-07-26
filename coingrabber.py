import random
import time
bg = [1]*9
screen = [0]*9
char = 4
coin = random.randrange(0, 8)
for x in range(9):
    screen[x] = bg[x]
screen[char] = 8
screen[coin] = 0
keypress = ''
points = 0
print("Coin Grabber by Daniel.S \n")
if input("do you want to know how to play the game? (y/n): ").lower() == "y":
    print("""you are the eight (8), your goal is to collect the coins that are zeroes (0) in the fastest time possible.
to move you press either 'a' or 'd' and press enter. any other combonations will not move you.
if the coin dosent show up than it is under you and you can press enter for a free coin.
your points are shown above the map.
Good Luck Have Fun!
""")
highfile = open(r"C:\ProgramData\coingrabberhigh.txt", "a")
highfile.close
highfile = open(r"C:\ProgramData\coingrabberhigh.txt", "r")
high = highfile.read()
if high == "":
    high = "999.99"
oghigh = high
print("time to beat: ",high)
input("\nPress Enter To Ready")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GOOO!")
starttime = time.time()
print(screen)
while True: 
    keypress = input().lower()
    if keypress == 'd' and char != 8:
        char = char + 1
    elif keypress == 'a' and char != 0:
        char = char - 1
    if char == coin:
        points = points + 1
        coin = random.randrange(0, 8)
    if points != 20:
        for x in range(9):
            screen[x] = bg[x]
        screen[coin] = 0
        screen[char] = 8
        print(points)
        print(screen)
    else:
        print("Game Over")
        print("You Got 20 coins!")
        endtime = time.time()
        print("your time was: ",endtime-starttime)
        if endtime - starttime < float(high):
            highfile.close
            highfile = open(r"C:\ProgramData\coingrabberhigh.txt", "w+")
            highfile.write(str(endtime - starttime))
            highfile.close()
            print("High Score: ",endtime-starttime)
            highfile.close()
        else:
            print("High Score:")
            print(high)
            highfile.close()
        break
        exit()
