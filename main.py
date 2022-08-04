from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do you want to search for? ")
url = f"https://www.newegg.ca/p/pl?d={gpu}"
