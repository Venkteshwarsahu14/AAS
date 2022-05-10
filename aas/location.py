
import requests
def local(lng,lat):
    
    URL = "https://discover.search.hereapi.com/v1/discover"
    latitude = lat   #21.222707
    longitude = lng  #81.622747
    # api_key = apikey
    api_key = 'y10YtokmvjPrk5TZHo6MXaF9-wzvh5EVjGaRWEq4y_Q' # Acquire from developer.here.com
    query = 'hospitals'
    limit = 5

    PARAMS = {
                'apikey':api_key,
                'q':query,
                'limit': limit,
                'at':'{},{}'.format(latitude,longitude)
             } 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    print(data)


    hospitalOne = data['items'][0]['title']
    hospitalOne_address =  data['items'][0]['address']['label']
    hospitalOne_latitude = data['items'][0]['position']['lat']
    hospitalOne_longitude = data['items'][0]['position']['lng']
    # hospitalOne_mobile = data['items'][0]['contacts'][0]["mobile"][0]["value"]
     

    hospitalTwo = data['items'][1]['title']
    hospitalTwo_address =  data['items'][1]['address']['label']
    hospitalTwo_latitude = data['items'][1]['position']['lat']
    hospitalTwo_longitude = data['items'][1]['position']['lng']
    # hospitalTwo_mobile = data['items'][1]['contacts'][0]["mobile"][0]["value"]


    hospitalThree = data['items'][2]['title']
    hospitalThree_address =  data['items'][2]['address']['label']
    hospitalThree_latitude = data['items'][2]['position']['lat']
    hospitalThree_longitude = data['items'][2]['position']['lng']


    hospitalFour = data['items'][3]['title']
    hospitalFour_address =  data['items'][3]['address']['label']
    hospitalFour_latitude = data['items'][3]['position']['lat']
    hospitalFour_longitude = data['items'][3]['position']['lng']
#     hospitalOne_mobile = data['items'][0]['contacts'][0]["mobile"][0]["value"]


    hospitalFive = data['items'][4]['title']
    hospitalFive_address =  data['items'][4]['address']['label']
    hospitalFive_latitude = data['items'][4]['position']['lat']
    hospitalFive_longitude = data['items'][4]['position']['lng']
    
#     print(hospitalOne_address)
    try:
        hospitalOne = data['items'][0]['title']
    except KeyError:
        hospitalOne = "none"
    
    try:
        hospitalOne_address =  data['items'][0]['address']['label']
    except KeyError:
        hospitalOne_address = "none"
    
    try:
        hospitalOne_mobile = data['items'][0]['contacts'][0]["mobile"][0]["value"]
    except KeyError:
        hospitalOne_mobile = "none"
    ######################################
    try:
        hospitalTwo = data['items'][1]['title']
    except KeyError:
        hospitalTwo = "none"
    
    try:
        hospitalTwo_address =  data['items'][1]['address']['label']
    except KeyError:
        hospitalTwo_address = "none"
    
    try:
        hospitalTwo_mobile = data['items'][1]['contacts'][0]["mobile"][0]["value"]
    except KeyError:
        hospitalTwo_mobile = "none"
        
    hos_one = [hospitalOne,hospitalOne_address,hospitalOne_mobile]
    hos_two = [hospitalTwo,hospitalTwo_address,hospitalTwo_mobile]
    
    print(hos_one,hos_two)
    return hos_one,hos_two
#     return data


def actual(lng,lat):

#     url = "https://revgeocode.search.hereapi.com/v1/revgeocode?at=21.222707%2C81.622747&lang=en-US"
    url= "https://revgeocode.search.hereapi.com/v1/revgeocode?at="+str(lat)+"%2C"+str(lng)+"&lang=en-US"

    payload = {}
    headers = {
      'Authorization': 'Bearer eyJhbGciOiJSUzUxMiIsImN0eSI6IkpXVCIsImlzcyI6IkhFUkUiLCJhaWQiOiI0bXk2bGtWcmNieExEYjN1QkkySSIsImlhdCI6MTU5NjQ0NTU1NCwiZXhwIjoxNTk2NTMxOTU0LCJraWQiOiJqMSJ9.ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJRMEpETFVoVE5URXlJbjAuLjZVU2dLLUNpQS00Z2U0VUhoMVBpTFEuTWVjX1NaVW1CTE1JeVltbk5fVFdYLVRZTHJRVGJtTEN0Z21FeC0xa1pWUTA1Skh3d25FYkdsTjRxMWZib1cyOXI4MnBhSjF5akVudDNUNkZaWTU3R1cwSkpVc0ZCWnh2ZlpTLUxIYlNhOFlHMUZWaG9XVmR5LVJzaVZBbm1BWjJCcGtsVDFzQl8tMzVDSF9kWXRwRU53LlJkSGw0QTdUQ1JJdUw4ZjlMdFBacFV0UkJBSVFpdFhFXzFKLTVGRGp1dnc.jsm6oVA954EUpI57OSB71WkKwibWoVMA3-UAPkVfvemnxHRRHudVGcioDje_D1dbUeXPPr_DaDetgNblFFzZkyrK1Y4_iT-sy91dlAu5tt2u_12PoR8oV2EoGx7WxSsTqxcjMhek7-DDPTYW5KqZZR87Zb6GKNXNl0cXOVK-I_g3Vcmo3DkR252eOugx6splq8x5PResiwGee2SLFIYU6xZUkIUxAkKD0D7iqShy3d9wdxSuyNYiCs0QGgQVWHv9WYknIYgnIQ54giwX9TZZaH_kVPLgdG_-i3w9qzkJ8LxTf1ovkY8ZfcDouU7qpXsKlam6y3PYG3_a08jEXcbo-Q'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
#     print(type(response)
    dic= response.json()
#     print(dic)
    # return dic
    return dic['items'][0]['title']


# d=actual(81.3418322,21.1562462)
# print(d)

    
# print(local(81.3418322,21.1562462))
# print(actual)