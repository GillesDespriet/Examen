import urllib.request
import json

response = urllib.request.urlopen("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5")
output = json.loads(response.read())
facts = output
for fact in facts:
    print(fact["text"])