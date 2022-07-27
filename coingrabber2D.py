import random
import time
bg = [1]*9
screen = [0]*9
char = 4
coinheight = random.randrange(0, 8)
charheight = 0
coin = random.randrange(0, 8)
for x in range(9):
    screen[x] = bg[x]
screen[char] = 8
screen[coin] = 0
keypress = ''
points = 0
print("Coin Grabber 2D by Daniel.S \n")
if input("do you want to know how to play the game? (y/n): ").lower() == "y":
    print("""you are the eight (8), your goal is to collect the coins that are zeroes (0) in the fastest time possible.
to move you use WSAD and press enter.
on the unlikely chance that the coin does not show, it is under you and you can press enter for a free coin.
CTRL + C to exit at any time.
Good Luck Have Fun!
""")
highfile = open(r"C:\ProgramData\coingrabber2Dhigh.txt", "a")
highfile.close
highfile = open(r"C:\ProgramData\coingrabber2Dhigh.txt", "r")
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
for y in range(9):
    for x in range(9):
        screen[x] = bg[x]
        if coinheight == y:
            screen[coin] = 0
        if charheight == y:
            screen[char] = 8
while True: 
    keypress = input().lower()
    if keypress == 'd' and char != 8:
        char = char + 1
    elif keypress == 'a' and char != 0:
        char = char - 1
    elif keypress == 's' and charheight != 8:
        charheight = charheight + 1
    elif keypress == 'w' and charheight != 0:
        charheight = charheight - 1
    if char == coin and charheight - coinheight == 0:
        points = points + 1
        coin = random.randrange(0, 8)
        coinheight = random.randrange(0, 8)
    if points != 20:
        for y in range(9):
            for x in range(9):
                screen[x] = bg[x]
                if coinheight == y:
                    screen[coin] = 0
                if charheight == y:
                    screen[char] = 8
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

