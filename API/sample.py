import requests 

location = input ("Enter City: ")

url = f"https://api.weatherapi.com/v1/current.json?key=396d6a3b84264868a2b95855262410&q={location}"
response = requests.get(url)
print (response.status_code)

if response.status_code == 200:
    data = response.json()

    print(f"ln {location} the temperature is {data["current"]["temp_c"]}, and the weather  is {data["current"]["condition"]["text"]}"  )
