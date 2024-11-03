import base64

from bs4 import BeautifulSoup
import requests

def get_image(query: str) -> str:
    response = requests.get(f"https://www.google.com/search?q={query}&tbs=isz:i&udm=2")
    soup = BeautifulSoup(response.text, "html.parser")
    img = soup.find("img", attrs={"class": "DS1iW"}).get("src")
    response = requests.get(img)
    return img

if __name__ == "__main__":
    print(get_image("apple"))
