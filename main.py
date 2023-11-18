import requests
import time
import random
import webbrowser
import helper

gamesCount = 1

# some steam html classes

goodReviewElement = "game_review_summary positive"

t1 = time.time()

urls = []
titles = []


urlCount = 5

while gamesCount <= urlCount:
    """
    This is main loop, what generate steam links and adding good ones to urls
    Idk how to generate more working links, so feel free to contribute
    """
    url = 'https://store.steampowered.com/app/' + str(random.randint(1, 1300000)) + "/"  # random url
    print("Sending request to", url)
    r = requests.get(url)
    rtext = r.text
    # print(r.text)
    isGame = helper.detectGame(rtext) and not helper.detectDLC(rtext)
    title = rtext[rtext.find('<title>') + 7 : rtext.find('</title>')]
    print(title)
    if isGame:
        isGood = goodReviewElement in rtext
        gamesCount += 1
        print(f"Game found: {url} | Good reviews: {isGood}")
        urls.append(url)
        titles.append(title)

print(f"Finished in {time.time() - t1} seconds")
print("Generating webpage...")


helper.generateweb("template.html", urls, titles)


print("Successfully generated webpage :)")
webbrowser.open_new_tab("generated.html")
print(urls)
