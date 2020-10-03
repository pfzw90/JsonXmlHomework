import os, xml, json, xml.etree.ElementTree as ET
from pprint import pprint


def get_list(file, minlength):
    news_words_list = []
    
    if os.path.splitext(file)[1] == ".json":
      with open(file, encoding = "utf-8") as f:
        news = json.load(f)  
      for news_item in news["rss"]["channel"]["items"]:
        news_words_list.extend(news_item["description"].strip().split(' '))
    
    
    if os.path.splitext(file)[1] == ".xml":
      parser = ET.XMLParser(encoding="utf-8")
      tree = ET.parse(file, parser)
      root = tree.getroot()
      
      for news_item in root.findall("channel/item"):
        news_words_list.extend(news_item.find("description").text.strip().split(' '))
    
    
    return [w for w in news_words_list if len(w) >= minlength]
      
def get_sorted(unsorted_list):
    words = {}
    for word in unsorted_list:
      if word not in words.keys():
        words.update({word : 1})
      else:
        words[word] += 1
    return sorted(list(words.items()),key=lambda x: -x[1])

def print_sorted(file, minlength, number_of_words):   
  i = 1
  for word in get_sorted(get_list(file, minlength))[:number_of_words]:
    print(f'{i}. "{word[0]}" - {word[1]} repetitions')
    i += 1


def start():
 print_sorted(input('File name: '), int(input('Minimal length: ')), int(input('Number of words for output: ')))

start()

