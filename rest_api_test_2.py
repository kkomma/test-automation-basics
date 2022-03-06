import requests

for page in range(1,3):
    apiFullUrl = 'https://reqres.in/api/users?page='+str(page)
    r = requests.get(apiFullUrl)
    responseData = r.json()
    print("")
    print("**********start***************")
    print("api full url::"+apiFullUrl)
    print("api responseData::", responseData)
    for element in responseData.get("data"):
        print("working on index:"+str(responseData.get("data").index(element)))
        print(element.get("id"))
    print("**********end***************")
    print("")
