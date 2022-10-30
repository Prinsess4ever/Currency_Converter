# write your code here!
from pathlib import Path
import requests

currency = input()

response = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
r = response.json()

cache_file = Path('name.cache')
with open(cache_file, "w") as f:
    if currency.lower() != "usd":
        f.write(str(r["usd"]["rate"]))

    if currency.lower() != "eur":
        f.write(str(r["eur"]["rate"]))
dict = {}

if currency.lower() != "usd":
    dict["usd"] = r["usd"]["rate"]
if currency.lower() != "eur":
    dict["eur"] = r["eur"]["rate"]


while True:
    to_ = input()
    if to_ == '':
        break

    how_much = int(input())

    print("Checking the cache...")

    if to_ in dict.keys():
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")

        with open(f"{to_}", "w") as f:
            f.write(str(r[to_]["rate"]))

        dict[to_] = r[to_]["rate"]


    print(f"You received {how_much * r[to_.lower()]['rate']} {to_}.")