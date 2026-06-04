import requests
url = url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()


    print("\n random joke")
    print("-------------------------")
    print("setup      :", data["setup"])
    print("punchaline   :", data["punchline"])

else:
    print("request failed")