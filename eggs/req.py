from urllib import parse

import requests
search_str = "экн"
search_url = parse.quote(search_str)
print(search_url)
response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/search?term={search_url}&type=group")

for group in response.json():

    print(group, type(group), group["id"])
