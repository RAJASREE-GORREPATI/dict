# Write a program get all error codes from the below dict
http_client_errors = [
                      {
                       "errorText":  "Bad Request: The request body was not formatted",
                       "errorCode": 400
                       },
                      {
                       "errorText":  "Unauthorized: You are not authorized to access the resource",
                       "errorCode": 401
                       },
                      {
                       "errorText":  "Forbidden: You are authenticated but not authrized to access the requested resource",
                       "errorCode": 403
                      },
                     {
                       "errorText":  "Not Found: The URL Path not found or change from server side",
                       "errorCode": 404
                     }
                  ]
l=[]
for e in range(len(http_client_errors)):
    for k in http_client_errors[e]:
        if k!="errorCode":
            continue
        else:
            l.append(http_client_errors[e][k])
print(f"Error codes from the dict:{l}")

