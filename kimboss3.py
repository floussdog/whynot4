import requests

url = "https://d7sms.p.rapidapi.com/secure/sendbatch"

payload = "{\r
    \"messages\": [\r
        {\r
            \"content\": \"Bulk SMS Content\",\r
            \"from\": \"D7-Rapid\",\r
            \"to\": [\r
                \"Destination1\",\r
                \"Destination2\"\r
            ]\r
        }\r
    ]\r
}"
headers = {
    'content-type': "application/json",
    'authorization': "Basic Ym52aDM4NDA6cm1Cd1FQaWg=",
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "d7sms.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
