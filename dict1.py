# Get the status code from the below dict
response = {
    "message":  "Success",
    "code": 200
}
for k in response:
    if k!="code":
        continue
    else:
        print(response[k])
        break
