import pandas as pd
import urllib.parse
import subprocess
import os
import random

def street_view(latitude, longitude, heading=0, pitch=0, fov=90):
    base_url = "https://www.google.com/maps/@?api=1&map_action=pano"

    prams = {
        "viewpoint": f"{latitude}, {longitude}",
        "heading": heading,
        "pitch": pitch,
        "fov": fov
    }   

    url = f"{base_url}&{urllib.parse.urlencode(prams)}"

    subprocess.run(["open", url])

df = pd.read_csv("lost_rawdata.csv")

random = random.randint(0, 999)

lat, long, city, country = df.iloc[(random)]


print(random)
print(f"The lat is {lat}")
print(f"The long is {long}")
print(f"The city is {city}")
print(f"The country is {country}")

input("Press any key to get lost...")

street_view(latitude=lat, longitude=long, heading=220, pitch=10)

os.system('clear')

print("Where are you? Guess the City or Country. Correct City for 10 points or Country for 5 points\n")
input("I'm in... ")