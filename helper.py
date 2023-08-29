def generateweb(templateFile: str, urls: list, titles: list):
    """This function generates webpage"""
    with open(templateFile, "r") as temp:
        tempText = temp.read()
        finalText = tempText
        t = 1
        for i in urls:
            finalText = finalText.replace(f"GAME_{t}_LOCATION", i)
            t += 1
        t = 1
        for i in titles:
            finalText = finalText.replace(f"GAME_{t}_NAME", i)
            t += 1
        with open("generated.html", "w") as generated:
            generated.write(finalText)
