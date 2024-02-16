import requests
from send_email import send_email

topic = "tesla"

api_key = "e3b4598a90914c73b75d145ac48f4f17"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=e3b4598a90914c73b75d145ac48f4f17&" \
      "language=pl"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        raw_title = article["title"].replace("\n", "")
        raw_description = article["description"].replace("\n", "")
        raw_link = article["url"].replace("\n", "")
        body = body + raw_title + "\n" + raw_description \
               + "\n" + raw_link + 2*"\n"

send_email(body)