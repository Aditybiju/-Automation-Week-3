import requests

API="https://api.zippopotam.us/"
country=str(input("Enter country code:"))
pincode = input("Enter Pincode:")
response = requests.get(API+country+'/'+pincode)

info = json.loads(response.text)

c=info['country']
s=info['places'][0]['state']
p=info['places'][0]['place name']
print("country:",c,"\nPlace Name:",p,"\nState:",s)






