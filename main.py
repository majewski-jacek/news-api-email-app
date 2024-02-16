import requests
from send_email import send_email

api_key = "e3b4598a90914c73b75d145ac48f4f17"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "e3b4598a90914c73b75d145ac48f4f17"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        raw_title = article["title"].replace("\n", "")
        raw_description = article["description"].replace("\n", "")
        body = body + raw_title + "\n" + raw_description + 2*"\n"

send_email(body)