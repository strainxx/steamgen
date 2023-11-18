import requests
import helper
import time

gameCount = 99110
games_id = open("games_id.txt", "a")
while gameCount < 2508760:
    url = f"https://store.steampowered.com/app/{gameCount}/"
    r = requests.get(url).text
    print(f"Request {gameCount}")
    if helper.detectGame(r) and not helper.detectDLC(r):
            games_id.write(str(gameCount))
            games_id.write("\n")
            print(f"GAME FOUND: {url}")
    gameCount+=10
    #time.sleep(1)

games_id.close()
