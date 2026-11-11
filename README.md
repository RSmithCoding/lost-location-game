# Lost

A geography guessing game. It drops you at a random location somewhere in the world in Google Street View, and you have to work out where you are. Guess the city or the country to win.

## Why I built it

I mainly wanted a project to practise using pandas and working with a CSV file. While looking through available datasets, I noticed many of them included coordinates. I'd been exploring Street View and looked into opening it directly from Python, and the idea for the game grew from there.

## How it works

1. The game picks a random location from a list of 1,000 places across 127 countries.
2. It opens Google Street View at that spot in your browser.
3. Look around, then type your guess back in the terminal: either the city or the country.
4. Keep guessing until you get it right, or type `q` to give up and see the answer.

## Features

- 1,000 locations stored in a CSV file, each with coordinates, city and country
- Opens Street View directly at the location, with the camera angle already set
- Accepts either the city or the country as a correct answer, in any combination of capitals
- Unlimited guesses, or quit at any time and the game reveals where you were

## Built with

- Python 3
- [pandas](https://pandas.pydata.org/) for reading the location data
- `urllib.parse` for building the Google Maps Street View link
- `subprocess` for opening the link in your browser

## Running it

You need Python 3 and pandas:

```
pip3 install pandas
python3 lost.py
```

Keep `lost_rawdata.csv` in the same folder as `lost.py`.

**Note:** it currently only runs on macOS, because it uses the Mac `open` command to launch the browser. Windows support is planned.

## Data

The 1,000 locations in `lost_rawdata.csv` were generated with [Mockaroo](https://mockaroo.com), a tool for creating realistic test data. Each row has a latitude, longitude, city and country.

## What I learned

- Loading and reading data from a CSV file with pandas
- Building a URL with query parameters using `urllib.parse`
- Opening a browser from Python with `subprocess`
- Using Google Maps URLs to open Street View at a set location and angle

## Ideas for improvement

- Make it work on Windows and Linux as well as macOS
- Keep score over several rounds