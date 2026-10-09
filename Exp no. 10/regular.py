import re

text = "BGMI Player Jonthan has 16 kills and rank Ace"

print("Player:", re.findall(r"Player (\w+)", text))
print("Kills:", re.findall(r"\d+", text))
print("Replace:", re.sub("Jonthan", "Mortal", text))
print("Search:", re.search("Ace", text).group())