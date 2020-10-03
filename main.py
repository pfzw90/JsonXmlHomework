import xml, json
import pprint from pprint

def get_top_json(file):
    with open(file, encoding = "utf-8") as f:
      news = json.read(f)
      pprint(news)

get_top_json("newsafr.json")