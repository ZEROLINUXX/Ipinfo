import requests as req

domain=input("Enter ip or domain: ")
ip"https://{}".format(domain)

data=req.get(ip)
print(data.text)
