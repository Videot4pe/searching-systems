from natasha import DatesExtractor, MorphVocab
from yargy import Parser
from person import PERSON
from weaponName import WEAPON_NAME
from weapon import WEAPON

text = open('src.txt').read()

morphVocab = MorphVocab()
datesExtractor = DatesExtractor(morphVocab)

datesMatches = datesExtractor(text)
# for match in datesMatches:
#     print(match)

parser = Parser(PERSON)

personMatches = [match.fact for match in parser.findall(text)]

for match in personMatches:
    print(match)

parser = Parser(WEAPON_NAME)

weaponNameMatches = [match.fact for match in parser.findall(text)]

for match in weaponNameMatches:
     print(match)

parser = Parser(WEAPON)

weaponMatches = [match.fact for match in parser.findall(text)]

for match in weaponMatches:
    print(match)