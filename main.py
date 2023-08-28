import requests
import time
import random
import webbrowser
import helper

gamesCount = 1

# some steam html classes
isGameElement = "game_purchase_action"
goodReviewElement = "game_review_summary positive"

t1 = time.time()

urls = []

urlCount = 5

while gamesCount <= urlCount:
    """
    This is main loop, what generate steam links and adding good ones to urls
    Idk how to generate more working links, so feel free to contribute
    """
    url = 'https://store.steampowered.com/app/' + str(random.randint(1, 1300000)) + "/"  # random url
    print("Sending request to", url)
    r = requests.get(url)
    # print(r.text)
    isGame = isGameElement in r.text
    if isGame:
        isGood = goodReviewElement in r.text
        gamesCount += 1
        print(f"Game found: {url} | Good reviews: {isGood}")
        urls.append(url)

print(f"Finished in {time.time() - t1} seconds")
print("Generating webpage...")


helper.generateweb("template.html", urls)


print("Successfully generated webpage :)")
webbrowser.open_new_tab("generated.html")
print(urls)
