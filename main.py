import requests

api_key = "e3b4598a90914c73b75d145ac48f4f17"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-16&sortBy=publishedAt&apiKey=" \
      "e3b4598a90914c73b75d145ac48f4f17"

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])