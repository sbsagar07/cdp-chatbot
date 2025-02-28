import requests
from bs4 import BeautifulSoup
import json

# URLs of CDP documentation
docs_urls = {
    "Segment": "https://segment.com/docs/?ref=nav",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def fetch_documentation(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.text for p in soup.find_all("p")])  # Extract text from <p> tags
        return text
    return None

# Store extracted data
data = {}

for platform, url in docs_urls.items():
    content = fetch_documentation(url)
    if content:
        data[platform] = content

# Save to JSON
with open("cdp_docs.json", "w") as file:
    json.dump(data, file, indent=4)

print("Documentation saved successfully!")
