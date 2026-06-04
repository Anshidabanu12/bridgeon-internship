# import requests
# url = "https://api.github.com/users/octocat"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print("\nGitHub user information")
#     print("----------------------------")
#     print(f"name           :{data,['name']}")
#     print(f"location        :{data,['location']}")
#     print(f"public repos   :{data,['public_repos']}")
#     print(f"created at        :{data,['created at']}")


# else: 
#     print("request file")

import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nGitHub User Information")
    print("----------------------------")
    print(f"Name          : {data['name']}")
    print(f"Location      : {data['location']}")
    print(f"Public Repos  : {data['public_repos']}")
    print(f"Created At    : {data['created_at']}")

else:
    print("Request failed")