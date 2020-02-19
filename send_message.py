import requests
url = "https://api.ciscospark.com/v1/messages"
access_token = "Bearer  " + "NWQ2MTgwMWEtNDQwOC00MWE5LThmN2EtZGJiOTkwMTJhYzBkNGQ2Y2I1OWItZWJl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

#Header
headers  = {
    "Content-type":"application/json",
    "Authorization" : access_token
}


#Body
body = {
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNDhkN2M3MjAtNTI1NS0xMWVhLWFlOGItYjFmN2RmOGE0Nzdl",
    "text": "Chúc ngủ ngon"
}

#Creating a post request
r  = requests.post(url, headers = headers, json = body)

print(r.status_code)
print(r.text)
