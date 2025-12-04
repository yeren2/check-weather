import requests
from twilio.rest import Client

account_id="****"
auth_token="****"


KEY="****"

LAT="YOUR_LATITUDE"
LONG="YOUR_LONGITUDE"


weather_data=f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={KEY}"
weather_info=requests.get(weather_data)

if weather_info.status_code==200:
    data=weather_info.json()
    temp=data["main"]["temp"]
    wind=data["wind"]["speed"]
    weather=data["weather"][0]["main"]
    if temp<288.15 and wind>10 and weather=="Clouds":
        client=Client(account_id,auth_token)
        message=client.messages.create(
            body="Hava kapali ve esiyor,bir ceket al istersen",
            from_="whatsapp:+14155238886",
            to="whatsapp:+905313185664",
        )
    elif temp>288.15 and wind<10 and weather=="Clear":
        client = Client(account_id, auth_token)
        message = client.messages.create(
            body="Bugun baya iyi giy tisort cik disari",
            from_="whatsapp:****",
            to="whatsapp:YOUR_PHONE_NUMBER",
        )
    else:
        client = Client(account_id, auth_token)
        message = client.messages.create(
            body="Ceket alsan iyi olur ama almazsan da canin sagolsun",
            from_="whatsapp:****",
            to="whatsapp:RECEIVER_PHONE_NUMBER",
        )
    print("islem basarılı")

else:
    print("mesaj gonderilemedi")
