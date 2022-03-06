import requests

a = [0,1,2,3,12,13]
for value in a:
    apiFullUrl = 'https://reqres.in/api/users/'+str(value)
    r = requests.get(apiFullUrl)
    responseData = r.json()
    print("")
    print("**********start***************")
    print("api full url::"+apiFullUrl)
    print("for value "+str(value)+" responseData::", responseData)
    if value < 1 or value > 12:
        assert responseData == {}
    else:
        print(responseData.get('data').get('id'))
        print(responseData.get('data').get('email'))
        print(responseData.get('data').get('first_name'))
        print(responseData.get('data').get('last_name'))
        print(responseData.get('data').get('avatar'))
        assert responseData.get('data').get('id') == value
        print(responseData.get('support').keys())
        assert list(responseData.get('support').keys()) == ['url','text']
    print("**********end***************")
    print("")
