# coding: utf-8

# ## Using URL

import json  # library for json operations
import urllib  # library for fetching internet resources

title = raw_input("Enter word to search: ")  # Input word to search dictionary

# stores the json formatted output to a variable
url = 'http://glosbe.com/gapi/translate?from=eng&dest=guj&format=json&phrase=' + title + '&pretty=true'

# json representation of url is stored in variable result
result = json.load(urllib.urlopen(url))

# get the first text in "meaning" in "tuc" from result
print "Meaning: ", result["tuc"][0]["meanings"][0]["text"]






# ## Using JSON

import json
from difflib import get_close_matches  # import library and its methods

data = json.load(open("data.json", 'r'))  # loads the json data file


def translate(word):
    """
    Provide the definition of the given word.
    """
    word = word.lower()
    if word.lower() in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yesno = raw_input(
            "Did you mean %s instead?Enter Y if Yes, N otherwise :" % get_close_matches(word, data.keys())[0])
        if yesno.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno.lower() == 'n':
            return "Word doesn't exist. Please double check it."
        else:
            return "We didn't recognize your input."
    else:
        return "Word doesn't exist. Please double check it."


word = raw_input("Enter keyword: ")
result = translate(word)
if type(result) is list:
    for item in result:
        print item
else:
    print result
