import requests

url = 'http://localhost:9696/predict'

house = {
'area'  :                   6540,
'bedrooms'  :                  3,
'bathrooms'  :                 1,
'stories'    :                 1,
'mainroad'   :                 1,
'guestroom'   :                1,
'basement'    :                1,
'hotwaterheating'  :           0,
'airconditioning'  :           0,
'parking'      :               2,
'prefarea'     :               1,
'furnishingstatus'  :  'furnished'
}

response = requests.post(url, json=house).json()

print(response)

