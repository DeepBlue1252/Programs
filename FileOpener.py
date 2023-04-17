import os
import openai

def splitChunks(text):
    tokens = text.split()
    chunks = []
    chunk = ""
    for token in tokens:
        if len(chunk) + len(token) < 4096:
            chunk += token + " "
        else:
            chunks.append(chunk.strip())
            chunk = token + " "
    if chunk != "":
        chunks.append(chunk.strip())

    return chunks

def splitEntities(text):
    characters = {}
    places = {}
    if '{' not in text:
        return characters, places
    

    brackOpenInd = text.index('{')
    brackCloseInd = text.index('}')

    charactersDict = text[brackOpenInd+1:brackCloseInd]

    text = text[brackCloseInd+1:]
    brackOpenInd = text.index('{')
    brackCloseInd = text.index('}')

    placesDict = text[brackOpenInd+1:brackCloseInd]


    # Split the text string into individual key-value pairs
    pairs = charactersDict.split("', ")

    # Loop through each pair and split it into key-value components
    for pair in pairs:
        # Remove any leading or trailing whitespace and single quotes from the key and value
        key, value = pair.split(": ")
        # Add the key-value pair to the dictionary
        characters[key] = value
    
    # Split the text string into individual key-value pairs
    pairs = placesDict.split("', ")

    # Loop through each pair and split it into key-value components
    for pair in pairs:
        # Remove any leading or trailing whitespace and single quotes from the key and value
        key, value = pair.split(": ")
        # Add the key-value pair to the dictionary
        places[key] = value
    return characters, places

def parsePages(chunks):
    characterList = {}
    placeList = {}
    for chunk in chunks[:5]:
        #print(chunk)
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": f"You are to define only the characters that have dialogue and \
                    places/settings that have descriptions within the story and be sure to return 2 \
                    dictionaries specifically labeled 'characters' and 'places' respectfully and using {{}} notation. \
                    Also do not use '\n'. Be very sure to not return any text besides the dictionaries. The key \
                    should be the name of the person or place and the value should be a description of their \
                    appearance. If there are no characters or places return empty dictionaries. The section is{chunk}"}
            ],
            temperature = 0
        )
        #print(completion['choices'][0]["message"]["content"])
        sectionList = completion['choices'][0]["message"]["content"]
        if sectionList == chunk:
            continue
        characters, places = splitEntities(sectionList)
        for key,value in characters.items():
            if key not in characterList:
                characterList[key] = value
        for key,value in places.items():
            if key not in placeList:
                placeList[key] = value
    return characterList, placeList

def main():
    f = open("HarryPotterTesting.txt",'r', encoding="utf8")
    fs = open("SmallerStory.txt",'r', encoding="utf8")

    openai.organization = "org-uqp71zJlH9G3BhGunVAStNc0"
    openai.api_key = "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"
    #openai.Model.list()

    
    text = f.read()
    chunks = splitChunks(text)
    #print(len(chunks))
    allCharacters, allPlaces = parsePages(chunks)
    print(allCharacters, allPlaces)

    

    #print(completion['choices'][0]["message"]["content"])


main()