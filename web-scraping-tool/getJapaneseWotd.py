from bs4 import BeautifulSoup
import requests as req
import json
from json import loads


webhookUrl = "https://hooks.slack.com/services/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"

kanas = {} #List to store kana of the words
romajis = {} #List to store romaji of the words
english = {} #List to store english translations

resp = req.get("https://www.japanesepod101.com/japanese-phrases/")
html = resp.text

soup = BeautifulSoup(html, 'html.parser')


wotd_img = soup.find_all(attrs={'class':'r101-wotd-widget__image'})

jap_char = soup.find_all(attrs={'class':'r101-wotd-widget__word'})
print(jap_char)

rom_char = soup.find_all(attrs={'class':'r101-wotd-widget__additional-field romaji'})
print(rom_char)

eng_char = soup.find_all(attrs={'class':'r101-wotd-widget__english'})
print(eng_char)


translations = []
zipped_translations = list(zip(jap_char, rom_char, eng_char))
for i, x in enumerate(zipped_translations):
            jap = x[0]
            rom = x[1]
            eng = x[2]
            translations.append({
                f"japanese_word-{i}": jap.get_text().strip(),
                f"romaji_word-{i}": rom.get_text().strip(),
                f"english_word-{i}": eng.get_text().strip()
            })

for image in wotd_img:
    translations.append({
                f"img-src": image['src'],
                f"img-alt": image['alt']
            })
# translations.append(wotd_img)
with open("wotd.json", 'w') as json_file:
    json.dump(translations, json_file)
