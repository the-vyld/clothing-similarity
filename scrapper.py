import pandas as pd
import requests

name = []
price = []
url = []
brand = []

# header params for the ajax query to fetch products
def getParams(i):
    return {
        "offset": str(i),
        "store": "ROW",
        "lang": "en-GB",
        "currency": "GBP",
        "rowlength": "4",
        "channel": "desktop-web",
        "country": "IN",
        "keyStoreDataversion": "ornjx7v-36",
        "limit": "72",
    }

# header cookies for the ajax query to fetch products
COOKIES = {
    "geocountry": "IN",
    "_abck": "0964C38D588870D3AB8A8A2AD61310FE~-0~YAAQB3UsMQcIugaIAQAAD08bMwlZG0wtE/Pw48gP3Z4nq6DtH9qpRwbONt11nDV5SnCpmPjBvTNcmaLEsVNNkSYBIlc+9CkRpqfWdyffWjKVD9n5FJZEw98JdVAy/wljB+UaZawPvweFcLc0p59FRYkT3RMxX42UHFkoTUaCXEkbQ3GoaXMLQT0W22vuAcWCGAIhOzuAcj0bEby8vuwPH6ZBRGHs7PH+UYXM5iD//2c3vzLq91nJRRBCdT/jNvnv7SRMp39E/HIMtg7Glz+ytyWcuzMqvKuN6J7cFLkptKjlG0BQgde19T6Y3UVPbM379H9t0JyPf31bVlSd32AMr90O95isGih93wSbwB+iOXrhjGuEOAX6itq4NWnoJS7L1CkmBi1Pv/nNXEXZsVAwSFK5dOePqK4=~-1~-1~-1",
    "AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg": "-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE",
    "s_pers": "%20s_vnum%3D1685557800077%2526vn%253D4%7C1685557800077%3B%20gpv_e231%3Dbea6d4df-3fab-4ec4-b80d-42cefde915e3%7C1684486407660%3B%20s_nr%3D1684484607677-Repeat%7C1716020607677%3B%20gpv_e47%3Dmen%257Cshirts%7C1684486407682%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C7616%2520refined%7C1684486407690%3B%20eVar225%3D40%7C1684486407742%3B%20s_invisit%3Dtrue%7C1684486407748%3B%20visitCount%3D4%7C1684486407755%3B",
    "browseCountry": "IN",
    "asos": "PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001",
    "browseCurrency": "GBP",
    "browseLanguage": "en-GB",
    "browseSizeSchema": "UK",
    "storeCode": "ROW",
    "currency": "1",
    "stc-welcome-message": "cappedPageCount=2",
    "featuresId": "2f6f608c-9479-4050-abf6-816c593452db",
    "asos-perx": "faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a",
    "AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg": "1",
    "s_cc": "true",
    "s_sq": "%5B%5BB%5D%5D",
    "floor": "1001",
    "plp_columsCount": "fourColumns",
    "_s_fpv": "true",
    "bm_sz": "56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689",
    "siteChromeVersion": "au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12",
    "keyStoreDataversion": "ornjx7v-36",
    "asos-b-sdv629": "ornjx7v-36",
    "ak_bmsc": "07F43D3170912B3E69F6D18CCE02AC30~000000000000000000000000000000~YAAQB3UsMVJuuAaIAQAA7VTFMhOeep1URQUCSBoS6voEviXkoDWiGIiWfZSkoUhmaf5ZTRokYbofaBZp/QuB371GKP7my0ehbgZDBp8+PciS/dYGTg+2vD5MlkwAYasUxDkjSFMgqdcjsRK751EDmst/WyUD+BP4pKeRplHbm8TfwoJo1bD3HPeiaabwXxeiHmFS/IaoXfMbBegePqLFX3eHtmjhnHLKeD4vC2zx+p7gDjdEPaBUerFnW5kPbiI0tYFnJwg576zoA11d3iceVAaY4fRm4zGQmxT0IkNMm8rfVEHMLuzYTWaGEtQJf/ae5cQqDJt7h//XQbCSaQJrTUx3/A3p4aEPds+fR5YMk+sS4MOC6eJEoVGy6wTFXR6jFWv0f1BE+aXdfj6iedep0lsd195TkzovBbUfRCtBYygT",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1",
}

# appends useful values from the product data in various lists
def appendResults(response):

    results_json = response.json()
    result_items = results_json["products"]
    base_url = "https://asos.com/"

    for item in result_items:
        name.append("men's " + item["name"])
        price.append(item["price"]["current"]["text"])
        url.append(base_url + item["url"])
        brand.append(item["brandName"])

# looping alters the headers according to our need which allows us to fetch all products as the source website is paginated
for i in range(0, 7560, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "b42b9344-6402-400e-9411-e5f271e7ccad",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/t-shirts-vests/cat/?cid=7616",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~-1~YAAQH3UsMQwm8jKIAQAAE4cSMwnDudblqvPt6WFpoJBAA+AUTaDng9J3L4shnZnhOVvPZdcTitlzDBxdo44jVDt7oPDre2oPynCLVRAE7UxfIE4Y/y5PsCLp+AlUt7e549nOG5A9jiLCmRJ24Xl86G703pDY/gjN4T1yRtbwNS8i5mqcqNLmhAid5UEeJUF1x+aDshYVEkQa5/3PVXPB30I9CKKyECwqdNeotX/U2a1tGTAJNmZ7GHW8/FnirYWTE7Av7+qJeJrHVbZmOhd/4v4cWAOKnPKGmzpXbMCFsDGNLVl/j8e/KwkTzORztp0NH3OfdKNG4PTZC9pizXGNQLy86dEck5QDz6xWFR0OXLqdVK5WLQ7WObPUYq14gFBhJ2RoMnmXb9k8CMbAv/9gz61hVbBceA==~0~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D4%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684484490027%3B%20gpv_e231%3De280284b-d2ce-45c9-a8c8-6ef6c7bb342c%7C1684485832443%3B%20s_nr%3D1684484032462-Repeat%7C1716020032462%3B%20gpv_e47%3Dmen%257Ct-shirts%2520%2526%2520vests%7C1684485832469%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C3602%2520refined%7C1684485832478%3B%20eVar225%3D39%7C1684485832526%3B%20s_invisit%3Dtrue%7C1684485832534%3B%20visitCount%3D4%7C1684485832541%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; _s_fpv=true; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; asos-b-sdv629=ornjx7v-36; ak_bmsc=07F43D3170912B3E69F6D18CCE02AC30~000000000000000000000000000000~YAAQB3UsMVJuuAaIAQAA7VTFMhOeep1URQUCSBoS6voEviXkoDWiGIiWfZSkoUhmaf5ZTRokYbofaBZp/QuB371GKP7my0ehbgZDBp8+PciS/dYGTg+2vD5MlkwAYasUxDkjSFMgqdcjsRK751EDmst/WyUD+BP4pKeRplHbm8TfwoJo1bD3HPeiaabwXxeiHmFS/IaoXfMbBegePqLFX3eHtmjhnHLKeD4vC2zx+p7gDjdEPaBUerFnW5kPbiI0tYFnJwg576zoA11d3iceVAaY4fRm4zGQmxT0IkNMm8rfVEHMLuzYTWaGEtQJf/ae5cQqDJt7h//XQbCSaQJrTUx3/A3p4aEPds+fR5YMk+sS4MOC6eJEoVGy6wTFXR6jFWv0f1BE+aXdfj6iedep0lsd195TkzovBbUfRCtBYygT; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/7616",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 4104, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "asos-cid": "0a0d6bd5-0691-407e-8748-7040e0f5ce6f",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/shirts/cat/?cid=3602",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/3602",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2160, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "88245ccc-4501-4dd4-9ebd-56d6406cc17a",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/shorts/cat/?cid=7078",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMV4UugaIAQAAiKwdMwnQWwp+0DqxC5Fs+L1fe4MBdcGwkmgx8C/YsEAgzehfeMU/NGM0kJeow29aCwCX8HBL8V1bLY7bCSKNRwbWkSIj5fYagTwMR/n2ourxbnE1TUNGM1tXIvJog3ztFxEwjgVblxmhxz1s/DUw8A4D7Y/hPMM1xOspCJ1T3wCrEvXpQzeyVSN1xE4tKWw2N8yWm8aGGft7mCwZMVRlCbiN7DBKq3OmYlHdM8e81VcKHj0u5Rsc6k0vINlc9DcyC8rQMcypdThaIx/5r6HdbVxHuhr3+B4vJEb+WH3QqhGB4jPdbdtaCtcSV18DE+LNqxfyDLp0ADTXqmlrpSjsPcLHREjzt1weUl20frKm3GVcZ1sX+HtWuXYEAZy/2LmRJ7n0ugEa5Q==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D4%7C1685557800077%3B%20gpv_e231%3Db98d0ca6-a5a9-4e1e-888d-99c1a669cfd3%7C1684486562857%3B%20s_nr%3D1684484762874-Repeat%7C1716020762874%3B%20gpv_e47%3Dmen%257Ct-shirts%2520%2526%2520vests%7C1684486562879%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C3602%2520refined%7C1684486562886%3B%20eVar225%3D41%7C1684486562928%3B%20s_invisit%3Dtrue%7C1684486562934%3B%20visitCount%3D4%7C1684486562940%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; _s_fpv=true; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; asos-b-sdv629=ornjx7v-36; ak_bmsc=07F43D3170912B3E69F6D18CCE02AC30~000000000000000000000000000000~YAAQB3UsMVJuuAaIAQAA7VTFMhOeep1URQUCSBoS6voEviXkoDWiGIiWfZSkoUhmaf5ZTRokYbofaBZp/QuB371GKP7my0ehbgZDBp8+PciS/dYGTg+2vD5MlkwAYasUxDkjSFMgqdcjsRK751EDmst/WyUD+BP4pKeRplHbm8TfwoJo1bD3HPeiaabwXxeiHmFS/IaoXfMbBegePqLFX3eHtmjhnHLKeD4vC2zx+p7gDjdEPaBUerFnW5kPbiI0tYFnJwg576zoA11d3iceVAaY4fRm4zGQmxT0IkNMm8rfVEHMLuzYTWaGEtQJf/ae5cQqDJt7h//XQbCSaQJrTUx3/A3p4aEPds+fR5YMk+sS4MOC6eJEoVGy6wTFXR6jFWv0f1BE+aXdfj6iedep0lsd195TkzovBbUfRCtBYygT; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/7078",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 3384, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "8d184aae-640e-4e65-8fcf-4e6edf7b0a4c",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/trousers-chinos/cat/?cid=4910",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~-1~YAAQB3UsMV8kugaIAQAARfsgMwk6+tDDCx+PK+XKJvk9sq9jsANufMolCZb5zaUEsBPE5jW2YJr/hwcKwqBvBEEjDDBtRJy72wswUz5r+jy5OV+MJaCAipx74LuWEk3WFb8MV+zA6hyoph9twUwMLcIuUZLlOh82WM43DngbrB41pGf9rgqChpk/88W6WAaIlC8DZ062u+6lueBtJnp5nai2Z538X+Mnc1nPTn4xQRYcnNWGyHe1caVSyHJVH5hZa/6bhFgQUo7Uk+xKsHGAmcN7sVrQfueZmFOHBzC2z0Ig/87iDsxWxyntRchZgVnaZ1lc2yH4bLTSqX3v4+2eAf7RCi0QLA1RdSbv5HO2aQQW7IDguVV1e63Ov/0GnOV0qKAJgqtCmuc9b3j+LtJkQ+5se0qfTw==~0~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D4%7C1685557800077%3B%20gpv_e231%3D582d13df-6378-4a55-89e7-8972a216073e%7C1684486779655%3B%20s_nr%3D1684484979671-Repeat%7C1716020979671%3B%20gpv_e47%3Dmen%257Cshirts%7C1684486779675%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C7078%2520refined%7C1684486779682%3B%20eVar225%3D42%7C1684486779733%3B%20s_invisit%3Dtrue%7C1684486779739%3B%20visitCount%3D4%7C1684486779744%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; _s_fpv=true; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; asos-b-sdv629=ornjx7v-36; ak_bmsc=07F43D3170912B3E69F6D18CCE02AC30~000000000000000000000000000000~YAAQB3UsMVJuuAaIAQAA7VTFMhOeep1URQUCSBoS6voEviXkoDWiGIiWfZSkoUhmaf5ZTRokYbofaBZp/QuB371GKP7my0ehbgZDBp8+PciS/dYGTg+2vD5MlkwAYasUxDkjSFMgqdcjsRK751EDmst/WyUD+BP4pKeRplHbm8TfwoJo1bD3HPeiaabwXxeiHmFS/IaoXfMbBegePqLFX3eHtmjhnHLKeD4vC2zx+p7gDjdEPaBUerFnW5kPbiI0tYFnJwg576zoA11d3iceVAaY4fRm4zGQmxT0IkNMm8rfVEHMLuzYTWaGEtQJf/ae5cQqDJt7h//XQbCSaQJrTUx3/A3p4aEPds+fR5YMk+sS4MOC6eJEoVGy6wTFXR6jFWv0f1BE+aXdfj6iedep0lsd195TkzovBbUfRCtBYygT; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4910",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 360, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "4808176b-344a-4d3a-b071-f344c195d371",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/trousers-chinos/cargo-trousers/cat/?cid=14273",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D4%7C1685557800077%3B%20gpv_e231%3D6e20aa4c-2491-4a75-9ecf-8a1528bc06e3%7C1684487133911%3B%20s_nr%3D1684485333931-Repeat%7C1716021333931%3B%20gpv_e47%3Dmen%257Ctrousers%2520%2526%2520chinos%7C1684487133937%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C14273%2520refined%7C1684487133945%3B%20eVar225%3D44%7C1684487133996%3B%20s_invisit%3Dtrue%7C1684487134008%3B%20visitCount%3D4%7C1684487134015%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/14273",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 1008, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "2e3d392c-f2ca-4951-8cc0-65afce29e6dc",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/co-ords/cat/?cid=28291",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20gpv_e231%3D344f01c6-66e3-4ee0-9b1f-8cc2ed612b9b%7C1684490756719%3B%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20s_nr%3D1684488956740-Repeat%7C1716024956740%3B%20gpv_e47%3Dmen%257Ctrousers%2520%2526%2520chinos%257Ccargo%2520trousers%7C1684490756744%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C28291%2520refined%7C1684490756750%3B%20eVar225%3D1%7C1684490756771%3B%20s_invisit%3Dtrue%7C1684490756778%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520row%25257Ccategory%252520page%25257C28291%252520refined%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/28291",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 5040, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "899b9355-f86f-4ed0-9961-9a2232250218",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/designer-brands/cat/?cid=27111",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20s_nr%3D1684488956740-Repeat%7C1716024956740%3B%20gpv_e47%3Dmen%257Ctrousers%2520%2526%2520chinos%257Ccargo%2520trousers%7C1684490756744%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C28291%2520refined%7C1684490756750%3B%20gpv_e231%3Db5aeb706-dc55-4ecd-9d48-85f4dc1b7baf%7C1684490763912%3B%20eVar225%3D1%7C1684490763952%3B%20s_invisit%3Dtrue%7C1684490763957%3B%20visitCount%3D5%7C1684490763964%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/27111",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 3240, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "32f058ef-c2bb-4d2a-a73d-c361e7b49f6a",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/hoodies-sweatshirts/cat/?cid=5668",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3Dae832629-b5b1-4963-bca9-4401c14cba05%7C1684490896084%3B%20s_nr%3D1684489096106-Repeat%7C1716025096106%3B%20gpv_e47%3Dmen%257Cco-ords%7C1684490896111%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C27111%2520refined%7C1684490896117%3B%20eVar225%3D2%7C1684490896164%3B%20s_invisit%3Dtrue%7C1684490896170%3B%20visitCount%3D5%7C1684490896176%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/5668",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2880, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "6469cb8e-7104-49df-9a85-9162eae7d322",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/jackets-coats/cat/?cid=3606",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D449d0a5e-a6b8-47c9-b6be-d0c4b143dc16%7C1684491020872%3B%20s_nr%3D1684489220896-Repeat%7C1716025220896%3B%20gpv_e47%3Dmen%257Cdesigner%2520brands%7C1684491020903%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C5668%2520refined%7C1684491020910%3B%20eVar225%3D3%7C1684491020961%3B%20s_invisit%3Dtrue%7C1684491020968%3B%20visitCount%3D5%7C1684491020977%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/3606",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2160, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "6c9628d9-ebce-4654-96a8-1bc16cfb1484",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/jeans/cat/?cid=4208",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D2edae830-2704-4265-af78-16c513d5dc48%7C1684491160668%3B%20s_nr%3D1684489360686-Repeat%7C1716025360686%3B%20gpv_e47%3Dmen%257Choodies%2520%2526%2520sweatshirts%7C1684491160693%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C3606%2520refined%7C1684491160701%3B%20eVar225%3D4%7C1684491160753%3B%20s_invisit%3Dtrue%7C1684491160761%3B%20visitCount%3D5%7C1684491160767%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4208",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 864, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "e0cc1a2d-3afa-4120-a341-6a5c14a59858",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/tracksuits/joggers/cat/?cid=14274",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3Dc2d28f4b-f75d-42cb-a3ea-ee72adf426a0%7C1684491246730%3B%20s_nr%3D1684489446745-Repeat%7C1716025446745%3B%20gpv_e47%3Dmen%257Cjackets%2520%2526%2520coats%7C1684491246751%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C4208%2520refined%7C1684491246760%3B%20eVar225%3D5%7C1684491246804%3B%20s_invisit%3Dtrue%7C1684491246809%3B%20visitCount%3D5%7C1684491246821%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/14274",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)


for i in range(0, 1440, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "5186a647-77e2-4cd9-8863-e2a87910c502",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/jumpers-cardigans/cat/?cid=7617",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D4802b1e1-4ecb-4ef1-b878-e8ce1ac1e4c1%7C1684491377612%3B%20s_nr%3D1684489577633-Repeat%7C1716025577633%3B%20gpv_e47%3Dmen%257Cjeans%7C1684491377637%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C14274%2520refined%7C1684491377645%3B%20eVar225%3D6%7C1684491377686%3B%20s_invisit%3Dtrue%7C1684491377694%3B%20visitCount%3D5%7C1684491377700%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/7617",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 576, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "4b1da3d7-2666-4d77-92c7-88b566f87e62",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/loungewear/cat/?cid=18797",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3Dea1891a4-0f2f-4c18-bae4-bdac8e83465b%7C1684491488622%3B%20s_nr%3D1684489688638-Repeat%7C1716025688638%3B%20gpv_e47%3Dmen%257Ctracksuits%257Cjoggers%7C1684491488643%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C7617%2520refined%7C1684491488650%3B%20eVar225%3D7%7C1684491488691%3B%20s_invisit%3Dtrue%7C1684491488697%3B%20visitCount%3D5%7C1684491488703%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/18797",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 1296, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "f7151377-da9a-4c1a-874c-6ed498235705",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/multipacks/cat/?cid=20831",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D6e7f5b39-6e48-4328-9c64-fc8c1e0dab6d%7C1684491590225%3B%20s_nr%3D1684489790241-Repeat%7C1716025790241%3B%20gpv_e47%3Dmen%257Cjumpers%2520%2526%2520cardigans%7C1684491590249%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C18797%2520refined%7C1684491590256%3B%20eVar225%3D8%7C1684491590298%3B%20s_invisit%3Dtrue%7C1684491590303%3B%20visitCount%3D5%7C1684491590310%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/20831",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 1296, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "85b1854e-c96f-4025-aa41-dbeac393ceb5",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/polo-shirts/cat/?cid=4616",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D529bbb83-8bbb-40e8-9a23-70985c6cf007%7C1684491674059%3B%20s_nr%3D1684489874080-Repeat%7C1716025874080%3B%20gpv_e47%3Dmen%257Cloungewear%7C1684491674084%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C20831%2520refined%7C1684491674093%3B%20eVar225%3D9%7C1684491674139%3B%20s_invisit%3Dtrue%7C1684491674145%3B%20visitCount%3D5%7C1684491674151%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4616",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 216, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "b2aaee20-f3c0-4af1-8f2a-573560b35ec7",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/underwear-socks/socks/cat/?cid=16329",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D25fc48dc-92dc-44bc-9647-9fb47f158140%7C1684492089171%3B%20s_nr%3D1684490289189-Repeat%7C1716026289189%3B%20gpv_e47%3Dmen%257Cmultipacks%7C1684492089196%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C4616%2520refined%7C1684492089203%3B%20eVar225%3D10%7C1684492089253%3B%20s_invisit%3Dtrue%7C1684492089259%3B%20visitCount%3D5%7C1684492089268%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/16329",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 4896, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "b1f221a7-ab75-46c9-b912-00839b1322e0",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/activewear/cat/?cid=26090",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D3a639ed3-3f30-4990-9f37-b17365a2d133%7C1684492169476%3B%20s_nr%3D1684490369494-Repeat%7C1716026369494%3B%20gpv_e47%3Dmen%257Cpolo%2520shirts%7C1684492169499%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C16329%2520refined%7C1684492169507%3B%20eVar225%3D11%7C1684492169552%3B%20s_invisit%3Dtrue%7C1684492169559%3B%20visitCount%3D5%7C1684492169566%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/26090",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 3960, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "8dbd4c84-6a5e-40cd-8a33-48a87375e419",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/suits/cat/?cid=5678",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D8f9bc059-c609-4a29-b685-01b99ba18f8d%7C1684492235939%3B%20s_nr%3D1684490435959-Repeat%7C1716026435959%3B%20gpv_e47%3Dmen%257Cunderwear%2520%2526%2520socks%257Csocks%7C1684492235966%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C26090%2520refined%7C1684492235973%3B%20eVar225%3D12%7C1684492236016%3B%20s_invisit%3Dtrue%7C1684492236022%3B%20visitCount%3D5%7C1684492236028%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/5678",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 864, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "6475949c-3276-49e5-9a34-657ccacde83c",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/swimwear/cat/?cid=13210",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3Db6afce6e-76cc-4579-9e2a-c09a26a90de5%7C1684492420875%3B%20s_nr%3D1684490620894-Repeat%7C1716026620894%3B%20gpv_e47%3Dmen%257Csportswear%7C1684492420901%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C5678%2520refined%7C1684492420908%3B%20eVar225%3D13%7C1684492420961%3B%20s_invisit%3Dtrue%7C1684492420969%3B%20visitCount%3D5%7C1684492420976%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/13210",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 1296, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "c899030c-2c7c-431b-8829-593e387442d6",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/tracksuits/cat/?cid=26776",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3Dc3a269f2-cd3f-4722-9e86-4bde2987b68a%7C1684492537861%3B%20s_nr%3D1684490737880-Repeat%7C1716026737880%3B%20gpv_e47%3Dmen%257Csuits%7C1684492537887%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C13210%2520refined%7C1684492537895%3B%20eVar225%3D14%7C1684492537953%3B%20s_invisit%3Dtrue%7C1684492537960%3B%20visitCount%3D5%7C1684492537968%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/26776",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 504, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "ea0c68a6-880d-456e-93b9-ab0dfd919bf0",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/underwear-socks/underwear/cat/?cid=20317",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D574b953a-5083-4beb-813a-450e7f4f82fd%7C1684492651410%3B%20s_nr%3D1684490851427-Repeat%7C1716026851427%3B%20gpv_e47%3Dmen%257Cswimwear%7C1684492651432%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C26776%2520refined%7C1684492651438%3B%20eVar225%3D15%7C1684492651484%3B%20s_invisit%3Dtrue%7C1684492651491%3B%20visitCount%3D5%7C1684492651496%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/20317",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 3600, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "cc729ce6-c98f-4b2d-9d45-0f9dd4922122",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/shoes-boots-trainers/cat/?cid=4209",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D5d8e097d-6d3b-4348-b98e-38207dde5328%7C1684492751653%3B%20s_nr%3D1684490951670-Repeat%7C1716026951670%3B%20gpv_e47%3Dmen%257Ctracksuits%7C1684492751675%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C20317%2520refined%7C1684492751683%3B%20eVar225%3D16%7C1684492751727%3B%20s_invisit%3Dtrue%7C1684492751733%3B%20visitCount%3D5%7C1684492751739%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4209",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 4320, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "2990d985-7145-45a3-8629-e095894e0bb6",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/men/accessories/cat/?cid=4210",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQB3UsMYYwugaIAQAAPrYjMwmgIBQkykUZ5Bbh7YwhZkaE/Ugi7FBFlglm2hrHpM5+cojqSVX3xxap1j37O9xqmpcHR3KIzLT36J1Dlh1gtFxq7K2V+Xf7Xd99knGn5u+VesNNVrAaDDU3mk8oTStTP4jEi0Cyj4jJiyktrN/C8+uyRVqJ3L2NzJAXIZIU4DxGKm+AlizKDIvL4ui4sXezC6VewU2mztrdA6k83xDEMXJ8fT4XvxAZ5n8n9/Tgyu64Srj9rtEJnQ2QW+H/w8SjczRi6cltpwA5LzwBrPs/xhiCLgRvmqBcZzc8zHvXHkn/MMLkvTAjoViwVwIDpDE3OWhIEIdpViNO+PQT06cvhElkAi2QtBA5JV/L6SfEYfyf8E4YzAihp38gc0dDWZaLmuCTbg==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684486172s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D25f3d4bc-c504-4245-9068-89b57d6e5f8f%7C1684492833958%3B%20s_nr%3D1684491033978-Repeat%7C1716027033978%3B%20gpv_e47%3Dmen%257Cunderwear%2520%2526%2520socks%257Cunderwear%7C1684492833984%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C4209%2520refined%7C1684492833991%3B%20eVar225%3D17%7C1684492834035%3B%20s_invisit%3Dtrue%7C1684492834041%3B%20visitCount%3D5%7C1684492834047%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1001; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1001; plp_columsCount=fourColumns; bm_sz=56ED2BA9BD4030881EE3A260EE75D478~YAAQB3UsMUNuuAaIAQAAPVHFMhOCGO2HFtGrGhCo4mBj20ndIf1nT3T6Xi6lHBWY1rTbSk4lS99RM5HReuOaJFSE0hhUHhILCxx8hiSZQPfVCK9xEi1na7d+JyrKs4x40Xx0Whp0chZUkrSLYGBVsm4ZJN338dy4Eoy+kHXRMpW4QC2h/2ypu+FKC40SGZwvKHCStCAuogeJ44Fv8YI8uyjqaHBSjqpOgLyBLb4Enyo7tI8gPIyQALL5IOkXvCQsAQLtPA5j6p16DE2440975IB4tlwFG5h3r3v2v5EKmc/U~3290949~3290689; asos-b-sdv629=ornjx7v-36; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+13%3A39%3A01+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4210",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

# create a pandas dataframe
male_df = pd.DataFrame({"Name": name, "Brand": brand, "Price": price, "Url": url})
print(male_df)

name = []
brand = []
price = []
url = []

COOKIES = {
    "geocountry": "IN",
    "_abck": "0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMWff+DKIAQAAp2yhMwnUuxk1zOZTZGDamN6Sn2xpq7qPw6M4rh1xKoh0GHmJ7/PziNveQ7tvcZx9HbGzRFj5CIegHa5IJEsERr61Lc6Vb2MnzqKWQYP0QwojsO4o3drhNdQ63JeOj4zUhYPmA+Bupd51jBE5fXzfN5vGufu5/S4gAmus57maJIw+o4pKdAT7PF883X9eaZ2EBzHsIhtegg3Yx2aVa/tzAKJ87CS8lnuOYyzN4aQF/WzX3CQbJep7k/Sbzu5D0FeCqgfpJ1qPBohVzS00tSeZcZlJRGfFpx8aESpOml9ww0HQZ4hvJhYc75juQTaL6XzOEXCZt7QwwzAUSNDvcj68QyH3zhjXFdxfK5VAyyU7y9w9ovvBmGDAkxx6Yd8Oe3kJfVrX9T7b5w==~-1~-1~-1",
    "AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg": "-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE",
    "s_pers": "%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20eVar225%3D25%7C1684495263632%3B%20visitCount%3D5%7C1684495263636%3B%20gpv_e231%3Dbec6371b-a8c9-4687-b832-fab28c0f9da3%7C1684495264178%3B%20s_invisit%3Dtrue%7C1684495264183%3B%20s_nr%3D1684493464188-Repeat%7C1716029464188%3B%20gpv_e47%3Dno%2520value%7C1684495264191%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C8799%2520refined%7C1684495264196%3B",
    "browseCountry": "IN",
    "asos": "PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000",
    "browseCurrency": "GBP",
    "browseLanguage": "en-GB",
    "browseSizeSchema": "UK",
    "storeCode": "ROW",
    "currency": "1",
    "stc-welcome-message": "cappedPageCount=2",
    "featuresId": "2f6f608c-9479-4050-abf6-816c593452db",
    "asos-perx": "faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a",
    "AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg": "1",
    "s_cc": "true",
    "s_sq": "asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520row%25257Ccategory%252520page%25257C8799%252520refined%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c",
    "floor": "1000",
    "plp_columsCount": "fourColumns",
    "asos-b-sdv629": "ornjx7v-36",
    "_s_fpv": "true",
    "ak_bmsc": "465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR",
    "siteChromeVersion": "au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12",
    "keyStoreDataversion": "ornjx7v-36",
    "bm_sz": "E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1",
}


def appendResults(response):

    results_json = response.json()
    result_items = results_json["products"]
    base_url = "https://asos.com/"

    for item in result_items:
        name.append("women's " + item["name"])
        price.append(item["price"]["current"]["text"])
        url.append(base_url + item["url"])
        brand.append(item["brandName"])


for i in range(0, 21600, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "9b85b8b4-f421-4950-97b1-7cee62b07bed",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/dresses/cat/?cid=8799",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMWff+DKIAQAAp2yhMwnUuxk1zOZTZGDamN6Sn2xpq7qPw6M4rh1xKoh0GHmJ7/PziNveQ7tvcZx9HbGzRFj5CIegHa5IJEsERr61Lc6Vb2MnzqKWQYP0QwojsO4o3drhNdQ63JeOj4zUhYPmA+Bupd51jBE5fXzfN5vGufu5/S4gAmus57maJIw+o4pKdAT7PF883X9eaZ2EBzHsIhtegg3Yx2aVa/tzAKJ87CS8lnuOYyzN4aQF/WzX3CQbJep7k/Sbzu5D0FeCqgfpJ1qPBohVzS00tSeZcZlJRGfFpx8aESpOml9ww0HQZ4hvJhYc75juQTaL6XzOEXCZt7QwwzAUSNDvcj68QyH3zhjXFdxfK5VAyyU7y9w9ovvBmGDAkxx6Yd8Oe3kJfVrX9T7b5w==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20eVar225%3D25%7C1684495263632%3B%20visitCount%3D5%7C1684495263636%3B%20gpv_e231%3Dbec6371b-a8c9-4687-b832-fab28c0f9da3%7C1684495264178%3B%20s_invisit%3Dtrue%7C1684495264183%3B%20s_nr%3D1684493464188-Repeat%7C1716029464188%3B%20gpv_e47%3Dno%2520value%7C1684495264191%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C8799%2520refined%7C1684495264196%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520row%25257Ccategory%252520page%25257C8799%252520refined%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/8799",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 14400, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "bc51854e-64c1-437f-9084-35ef2ba56ff9",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/tops/cat/?cid=4169",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMWff+DKIAQAAp2yhMwnUuxk1zOZTZGDamN6Sn2xpq7qPw6M4rh1xKoh0GHmJ7/PziNveQ7tvcZx9HbGzRFj5CIegHa5IJEsERr61Lc6Vb2MnzqKWQYP0QwojsO4o3drhNdQ63JeOj4zUhYPmA+Bupd51jBE5fXzfN5vGufu5/S4gAmus57maJIw+o4pKdAT7PF883X9eaZ2EBzHsIhtegg3Yx2aVa/tzAKJ87CS8lnuOYyzN4aQF/WzX3CQbJep7k/Sbzu5D0FeCqgfpJ1qPBohVzS00tSeZcZlJRGfFpx8aESpOml9ww0HQZ4hvJhYc75juQTaL6XzOEXCZt7QwwzAUSNDvcj68QyH3zhjXFdxfK5VAyyU7y9w9ovvBmGDAkxx6Yd8Oe3kJfVrX9T7b5w==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20s_nr%3D1684493464188-Repeat%7C1716029464188%3B%20gpv_e47%3Dno%2520value%7C1684495264191%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C8799%2520refined%7C1684495264196%3B%20gpv_e231%3Dda41a706-ddef-4d1a-b268-a8d48510fa0f%7C1684495319554%3B%20eVar225%3D26%7C1684495319595%3B%20s_invisit%3Dtrue%7C1684495319601%3B%20visitCount%3D5%7C1684495319608%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4169",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 6840, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "8beeda6e-9624-41c6-81d7-3d736919ecb0",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/swimwear-beachwear/cat/?cid=2238",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~-1~YAAQH3UsMT8D+TKIAQAAx0enMwl3cYsdnCzK5ctf4Kp2L1wweis/D9Nce4njjryXrGp7PHmFIkQZD93Er8vaS3/+XnOExFzWu4ldV+DU0MLlq3lMxzzl0ZfKg5Yf19KO/TtQz/yRLWc0JnaSrb5M8O5IO84qzbdgdaG2alWUOkzDx2e6AbmTs8QFr6BLfRlfob1XGz/sjOQLZxLC542QatZWfhmyl+uza+ARttuVqx/pXGxY/PxnnT3y0aD1nZNj+aQmYYp+MVS8FcGGAfEk5YAcFSGibc+2IA4Lf7AQKrR/7EiIs5al4IJyjevJA8joRvW8cj4wy4cNNTBJ5VrgRLVsiKvzVuXY6Ox96ktojIawVk/ziae/d9LZCLLDNZfVO5qBo1j7imo8EY2HL1ZEqh3EQUJJxg==~0~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3D081937c5-ab62-48aa-b660-e400933b8919%7C1684495580929%3B%20s_nr%3D1684493780954-Repeat%7C1716029780954%3B%20gpv_e47%3Dwomen%257Cdresses%7C1684495580960%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C4169%2520refined%7C1684495580974%3B%20eVar225%3D27%7C1684495581043%3B%20s_invisit%3Dtrue%7C1684495581052%3B%20visitCount%3D5%7C1684495581059%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/2238",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 3600, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "f1553b3e-fca7-4e25-a1c1-8d7d120382bd",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/skirts/cat/?cid=2639",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~-1~YAAQH3UsMdsJ+TKIAQAAMLWoMwk2pIL50tsfuqAFZp718tVaPxZr1CKbq4GTgNX7uOhSp/nIeqo0YK39b6+k6eenkPXwCnLIrIRd6Gse27HBFOrWsSSWZV6fGaYd4ZNVvpI8YOD67c9ORwoH33C83aKtQZA2csIRyhfkWe6q4S/26pw/sxL8PnuY66hK0cOAnuCGSTHD9+8YC8TRYIbyd7jL9dwwyoUrWBBd6d3V9ILxQFKrfqgmvo4tUyI4OA8UQ4yGLaCXxU4tOwbcGOlBUIAOOlHx6hFtMQNj0H3GI3+hpIH4W30b7pXOlTkU/aYfD7M0r4jBnGZINb65cX9sRb8fjGCUSlr/G1sB1UUdVTl+Lbfn9rIMdHYGfeti3K9C1zoZ5NjvU4F9qiiGZEye7p2ZxcBCGc4=~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3D19664490-8b78-4037-a3c6-d61ee5f0c3f2%7C1684495675955%3B%20s_nr%3D1684493875974-Repeat%7C1716029875974%3B%20gpv_e47%3Dwomen%257Ctops%7C1684495675981%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C2238%2520refined%7C1684495675991%3B%20eVar225%3D28%7C1684495676050%3B%20s_invisit%3Dtrue%7C1684495676059%3B%20visitCount%3D5%7C1684495676066%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/2639",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2880, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "b90b0870-3195-418b-ad17-ab8b67eebb60",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/shorts/cat/?cid=9263",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3D8eec7d0b-81f2-4a00-8a96-8995ae9757d2%7C1684495787445%3B%20s_nr%3D1684493987466-Repeat%7C1716029987466%3B%20gpv_e47%3Dwomen%257Cswimwear%2520%2526%2520beachwear%7C1684495787473%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C2639%2520refined%7C1684495787481%3B%20eVar225%3D29%7C1684495787534%3B%20s_invisit%3Dtrue%7C1684495787542%3B%20visitCount%3D5%7C1684495787550%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/9263",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 1440, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "77927d32-240e-4b89-b4e4-a29ce2cb752b",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/suits-separates/blazers/cat/?cid=11896",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3D56ae102a-5855-4988-b88e-a15e42a8b24e%7C1684495872829%3B%20s_nr%3D1684494072850-Repeat%7C1716030072850%3B%20gpv_e47%3Dwomen%257Cskirts%7C1684495872857%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C9263%2520refined%7C1684495872867%3B%20eVar225%3D30%7C1684495872921%3B%20s_invisit%3Dtrue%7C1684495872929%3B%20visitCount%3D5%7C1684495872938%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/11896",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 6840, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "60b76766-1593-41bd-a4f5-f103a2725c79",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/co-ords/cat/?cid=19632",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3Df67b04d6-e4da-4376-af0a-9de161bf2cba%7C1684495964847%3B%20s_nr%3D1684494164866-Repeat%7C1716030164866%3B%20gpv_e47%3Dwomen%257Cshorts%7C1684495964873%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C11896%2520refined%7C1684495964883%3B%20eVar225%3D31%7C1684495964940%3B%20s_invisit%3Dtrue%7C1684495964949%3B%20visitCount%3D5%7C1684495964959%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/19632",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 3960, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "dc91c776-1562-4c7f-ae1c-9ded0820f625",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/coats-jackets/cat/?cid=2641",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3D1e078c17-9524-41e7-92c6-3a35d53b471e%7C1684496058735%3B%20s_nr%3D1684494258753-Repeat%7C1716030258753%3B%20gpv_e47%3Dwomen%257Csuits%2520%2526%2520separates%257Cblazers%7C1684496058758%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C19632%2520refined%7C1684496058767%3B%20eVar225%3D32%7C1684496058818%3B%20s_invisit%3Dtrue%7C1684496058824%3B%20visitCount%3D5%7C1684496058831%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/2641",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 6480, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "930bfaa2-f7f6-4cb0-a899-5e432963b2e3",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/designer-brands/cat/?cid=15210",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684495197008%3B%20gpv_e231%3D0286ae1d-7193-4ef5-ac14-7d46c1ea2ac2%7C1684496179427%3B%20s_nr%3D1684494379453-Repeat%7C1716030379453%3B%20gpv_e47%3Dwomen%257Cco-ords%7C1684496179459%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C2641%2520refined%7C1684496179469%3B%20eVar225%3D33%7C1684496179526%3B%20s_invisit%3Dtrue%7C1684496179537%3B%20visitCount%3D5%7C1684496179545%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A21%3A04+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/15210",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 792, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "e3f04731-3f89-4c15-8519-3fc6b9db964c",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/exclusives/cat/?cid=16979",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20eVar225%3D38%7C1684496407597%3B%20visitCount%3D5%7C1684496407601%3B%20gpv_e231%3Db4522d39-6b45-44fb-a75d-abe55df5a5aa%7C1684496407962%3B%20s_invisit%3Dtrue%7C1684496407968%3B%20s_nr%3D1684494607973-Repeat%7C1716030607973%3B%20gpv_e47%3Dno%2520value%7C1684496407977%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C16979%2520refined%7C1684496407980%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520row%25257Ccategory%252520page%25257C16979%252520refined%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/16979",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 1800, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "d879a821-c860-4672-b2a3-16c2f51f41a2",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/hoodies-sweatshirts/cat/?cid=11321",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20s_nr%3D1684494607973-Repeat%7C1716030607973%3B%20gpv_e47%3Dno%2520value%7C1684496407977%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C16979%2520refined%7C1684496407980%3B%20gpv_e231%3D5ee37dca-5d79-461c-ae90-4473c7e4f51b%7C1684496438597%3B%20eVar225%3D39%7C1684496438638%3B%20s_invisit%3Dtrue%7C1684496438646%3B%20visitCount%3D5%7C1684496438652%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/11321",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 4320, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "ca3c21c2-6056-4ef9-b9d3-56f83a3a45a5",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/jeans/cat/?cid=3630",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3Da26e6159-0ca5-4d34-b5ad-7281cde3af05%7C1684496531358%3B%20s_nr%3D1684494731381-Repeat%7C1716030731381%3B%20gpv_e47%3Dwomen%257Cexclusives%7C1684496531388%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C11321%2520refined%7C1684496531399%3B%20eVar225%3D40%7C1684496531464%3B%20s_invisit%3Dtrue%7C1684496531475%3B%20visitCount%3D5%7C1684496531483%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/3630",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2160, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "491d6b40-e47b-4b5e-a180-d9a525af148c",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/jumpers-cardigans/cat/?cid=2637",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3De6179648-694b-466d-a601-4bf0639622e2%7C1684496655184%3B%20s_nr%3D1684494855203-Repeat%7C1716030855203%3B%20gpv_e47%3Dwomen%257Choodies%2520%2526%2520sweatshirts%7C1684496655210%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C3630%2520refined%7C1684496655217%3B%20eVar225%3D41%7C1684496655268%3B%20s_invisit%3Dtrue%7C1684496655275%3B%20visitCount%3D5%7C1684496655282%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        "offset": str(i),
        "store": "ROW",
        "lang": "en-GB",
        "currency": "GBP",
        "rowlength": "4",
        "channel": "desktop-web",
        "country": "IN",
        "keyStoreDataversion": "ornjx7v-36",
        "limit": "72",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/2637",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2160, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "19297983-f7ff-4ac4-b533-0880c8c0d815",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/jumpsuits-playsuits/cat/?cid=7618",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3Db3849426-288b-4037-8418-2e1797ee8045%7C1684496755219%3B%20s_nr%3D1684494955242-Repeat%7C1716030955242%3B%20gpv_e47%3Dwomen%257Cjeans%7C1684496755249%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C2637%2520refined%7C1684496755258%3B%20eVar225%3D42%7C1684496755315%3B%20s_invisit%3Dtrue%7C1684496755324%3B%20visitCount%3D5%7C1684496755338%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/7618",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 5040, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "29e36d92-e8b9-463e-b951-b9b4400c704b",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/lingerie-nightwear/cat/?cid=6046",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3D900d5526-7bab-482c-9a14-e815486f723a%7C1684496861081%3B%20s_nr%3D1684495061101-Repeat%7C1716031061101%3B%20gpv_e47%3Dwomen%257Cjumpers%2520%2526%2520cardigans%7C1684496861107%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C7618%2520refined%7C1684496861116%3B%20eVar225%3D43%7C1684496861165%3B%20s_invisit%3Dtrue%7C1684496861173%3B%20visitCount%3D5%7C1684496861181%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/6046",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 504, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "3d2c25b9-a5da-417f-88e1-292d6a4c8366",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/loungewear/cat/?cid=21867",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3D6368677e-0cd6-4752-9241-220a48cdfed7%7C1684497166008%3B%20s_nr%3D1684495366029-Repeat%7C1716031366029%3B%20gpv_e47%3Dwomen%257Clingerie%2520%2526%2520nightwear%7C1684497166036%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C21867%2520refined%7C1684497166044%3B%20eVar225%3D45%7C1684497166099%3B%20s_invisit%3Dtrue%7C1684497166107%3B%20visitCount%3D5%7C1684497166116%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/26416",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 864, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "119248d1-58a8-4b20-968f-57fe4dedd754",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/multipacks/cat/?cid=19224",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3D6368677e-0cd6-4752-9241-220a48cdfed7%7C1684497166008%3B%20s_nr%3D1684495366029-Repeat%7C1716031366029%3B%20gpv_e47%3Dwomen%257Clingerie%2520%2526%2520nightwear%7C1684497166036%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C21867%2520refined%7C1684497166044%3B%20eVar225%3D45%7C1684497166099%3B%20s_invisit%3Dtrue%7C1684497166107%3B%20visitCount%3D5%7C1684497166116%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/19224",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2880, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "951058c7-8660-4ed3-a9d7-55c2ec454821",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/tops/shirts-blouses/cat/?cid=11318",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3D266fb898-bb8b-4473-ba0b-069928cb789f%7C1684497311072%3B%20s_nr%3D1684495511091-Repeat%7C1716031511091%3B%20gpv_e47%3Dwomen%257Cloungewear%7C1684497311097%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C19224%2520refined%7C1684497311106%3B%20eVar225%3D46%7C1684497311158%3B%20s_invisit%3Dtrue%7C1684497311165%3B%20visitCount%3D5%7C1684497311176%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; ak_bmsc=465D2C284A7876B2D29CC1BAD51D2F1B~000000000000000000000000000000~YAAQH3UsMT+69TKIAQAAFYRbMxPjfYvbyqVs3rrGHCRxBeJben8oFcOGPLXFVz20IhdKW+bukA7qsRD0ReY7gvQ8UK74I2zgN8mXXh8POcunAmy2JZuT72gcOcYPbAwAOL4OoxR7v5MSiVFc6PX6S9Hi+FF/o6jYjP7ccy8vOJ7usVMORw23179jrvpnDqbdCxm9jRWXQo0HPoPLu89Rvp5CH0IB6RigDpwO592YyBMAgpr6/TWzUGKAe7tjDkHGwI/3Bzi5q+/BrHqVgcjSohYC5Ppaa7HvU5NDrDKchodufQ9Ao2v7X87cwH0pMcsFQkvxhRy2NjHMwve9jPgl2A96PTxECiVLGwqsP8+HCWxYLz9AdGJaI4Eq8HylzJW4J3czTLPS2jugOk1Cz0ryU92S6RARI1AolHJGivb+pzcR; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/11318",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 288, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "97afa0b8-f539-40aa-926b-ca9a36b2edfc",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/socks-tights/cat/?cid=7657",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3D792ccecf-f8e2-4229-b893-c0b34f6957ae%7C1684497407776%3B%20s_nr%3D1684495607797-Repeat%7C1716031607797%3B%20gpv_e47%3Dwomen%257Cmultipacks%7C1684497407803%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C11318%2520refined%7C1684497407811%3B%20eVar225%3D47%7C1684497407872%3B%20s_invisit%3Dtrue%7C1684497407881%3B%20visitCount%3D5%7C1684497407894%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/7657",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2480, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "98451df6-1c42-4638-a4cb-c3cf70346894",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/sportswear/cat/?cid=26091",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_p6%3D%2520%7C1684496387771%3B%20gpv_e231%3Db539d050-dc1e-4e4d-82b9-b4ed9c6110de%7C1684498108871%3B%20s_nr%3D1684496308889-Repeat%7C1716032308889%3B%20gpv_e47%3Dwomen%257Ctops%257Cshirts%2520%2526%2520blouses%7C1684498108896%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C7657%2520refined%7C1684498108904%3B%20eVar225%3D48%7C1684498108961%3B%20s_invisit%3Dtrue%7C1684498108969%3B%20visitCount%3D5%7C1684498108976%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/26091",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 2160, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "8453af10-4536-4009-be7f-ba2350c8230f",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/suits-separates/cat/?cid=13632",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D7e5ded0d-68b4-488a-a4c0-bfd0aa2141c3%7C1684498198215%3B%20s_nr%3D1684496398233-Repeat%7C1716032398233%3B%20gpv_e47%3Dwomen%257Csocks%2520%2526%2520tights%7C1684498198238%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C26091%2520refined%7C1684498198250%3B%20eVar225%3D49%7C1684498198302%3B%20s_invisit%3Dtrue%7C1684498198310%3B%20visitCount%3D5%7C1684498198318%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/13632",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 720, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "3614317e-1f43-4fec-b5b8-b78a74311401",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/tracksuits/cat/?cid=27953",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3De45388da-9b35-40c7-ae66-ae275e0a955b%7C1684498284246%3B%20s_nr%3D1684496484265-Repeat%7C1716032484265%3B%20gpv_e47%3Dwomen%257Csportswear%7C1684498284271%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C13632%2520refined%7C1684498284280%3B%20eVar225%3D50%7C1684498284338%3B%20s_invisit%3Dtrue%7C1684498284347%3B%20visitCount%3D5%7C1684498284357%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/27953",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 6840, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "83567d83-8815-4ee5-8fac-9e7b1b7348a5",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/trousers-leggings/cat/?cid=2640",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D04cafd78-68fc-4482-903b-ffb307d86997%7C1684498371034%3B%20s_nr%3D1684496571056-Repeat%7C1716032571056%3B%20gpv_e47%3Dwomen%257Csuits%2520%2526%2520separates%7C1684498371062%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C27953%2520refined%7C1684498371071%3B%20eVar225%3D51%7C1684498371122%3B%20s_invisit%3Dtrue%7C1684498371130%3B%20visitCount%3D5%7C1684498371139%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/2640",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 7920, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "84c78ddf-ce63-4430-835f-0756eb0bc6e9",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/shoes/cat/?cid=4172",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D6778174b-bca2-459c-a207-2872400f7f1f%7C1684498558917%3B%20s_nr%3D1684496758937-Repeat%7C1716032758937%3B%20gpv_e47%3Dwomen%257Ctrousers%2520%2526%2520leggings%7C1684498558944%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C8799%2520refined%7C1684498558952%3B%20eVar225%3D53%7C1684498559008%3B%20s_invisit%3Dtrue%7C1684498559015%3B%20visitCount%3D5%7C1684498559021%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520row%25257Ccategory%252520page%25257C8799%252520refined%2526link%253DView%252520all%2526region%253Db2598144-62bd-4b68-804d-4cb894f853a1%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4172",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 5400, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "b1bb5be9-866e-44ef-88d8-3a1f8e958a6a",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/accessories/cat/?cid=4174",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3D28be34f5-bff3-4ed2-a5e9-f89bda405628%7C1684498573399%3B%20s_nr%3D1684496773419-Repeat%7C1716032773419%3B%20gpv_e47%3Dwomen%257Cdresses%7C1684498573425%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C4172%2520refined%7C1684498573433%3B%20eVar225%3D54%7C1684498573489%3B%20s_invisit%3Dtrue%7C1684498573496%3B%20visitCount%3D5%7C1684498573505%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/4174",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)

for i in range(0, 5040, 72):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        # 'Accept-Encoding': 'gzip, deflate, br',
        "asos-cid": "52901e97-56d4-484e-a21b-2ca9b00068c2",
        "asos-c-plat": "web",
        "asos-c-name": "@asosteam/asos-web-product-listing-page",
        "asos-c-ver": "1.2.0-d7bef89a42ea-8963",
        "Connection": "keep-alive",
        "Referer": "https://www.asos.com/women/face-body/cat/?cid=1314",
        # 'Cookie': 'geocountry=IN; _abck=0964C38D588870D3AB8A8A2AD61310FE~0~YAAQH3UsMdIS+TKIAQAAdGqqMwnOXVsIpYIcrcVaSOkVtq4iuVgoQsGXqwVxL2MDo765pVeaXDsLxdZPeEQqG3do+eRvVH4cGiA4j3/x0jxcveiNVT9ViYx0BUmbwAB3QnnRBKYIoeLRazwyBZXL1FSV18d/ftPdZSDjANAzZFMqZfENkI51K2sd9sDVkPr5zRaiVk+38Gx3ji3oh9oxJ7brz5X0+d3vCOcESkoIbObXvCBYGuaI/KSxwjSdgGgnht0b7gnmvq5PwuoS+E3+SrZYJdzv/I6zeEJHrpvXMz7T2ST4HxHW9V1cd+/kb4oh5HeRNGQ6CDDG7mH8OfvhX7wwVHiJopE33OIQ3gtSmctWe87y48BpdgakuY036v9Aqlen1nxjxSHpvtZcZZtSMJbb6rYYtA==~-1~-1~-1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C60069574564088357800626577175423412725%7CvVersion%7C3.3.0%7CMCAID%7CNONE%7CMCOPTOUT-1684498964s%7CNONE; s_pers=%20s_vnum%3D1685557800077%2526vn%253D5%7C1685557800077%3B%20gpv_e231%3Db88193d0-7ff8-4d8a-94b9-61653f5a9e4a%7C1684498707203%3B%20s_nr%3D1684496907222-Repeat%7C1716032907222%3B%20gpv_e47%3Dwomen%257Cshoes%7C1684498707229%3B%20gpv_p10%3Ddesktop%2520row%257Ccategory%2520page%257C4174%2520refined%7C1684498707236%3B%20eVar225%3D55%7C1684498707299%3B%20s_invisit%3Dtrue%7C1684498707306%3B%20visitCount%3D5%7C1684498707314%3B; browseCountry=IN; asos=PreferredSite=&customerguid=faf8d120b9f74c3bbbb75e88c6b2f10f&topcatid=1000; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=1; stc-welcome-message=cappedPageCount=2; featuresId=2f6f608c-9479-4050-abf6-816c593452db; asos-perx=faf8d120b9f74c3bbbb75e88c6b2f10f||f75b1ed39966481a85519cad3d49bd1a; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; floor=1000; plp_columsCount=fourColumns; asos-b-sdv629=ornjx7v-36; _s_fpv=true; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=ornjx7v-36; bm_sz=E19C8B4FC364AAA076ED9DB82ADBDE87~YAAQH3UsMTvf+DKIAQAAZmahMxMfoIBwTe1VCpo//CPaUdqU37sPbXb6zFqePPxEx0L21w0b83cjS/l2kuBnN/GKnfxfoj/VnqFa0hAJ0jxQD4hBJq5RzNdfHcPOarv9qi0kKSd0VEHZz5tzbDCqBF6JsOU4FyyY/Hmy9iT6oJxV72Q9vgT+nDAJ7n3ioDWzzEX8vij4rmJbWndU0Gqc5qqPEW/gEobgbztxaIBNCM+Yf+x9+Bqi+EepZSjPanl5/71XPX4+mZrjzCv44Fzn6VL9g83P5CkhNvQLClIVZ0uK~3556404~4408129; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+16%3A40%3A08+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&hosts=&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; ak_bmsc=93E6DF982B26D8BC6605172B2BD7FF84~000000000000000000000000000000~YAAQH3UsMRoc+jKIAQAAZdrNMxMsNCWuIUz4kEpApTDbTQr/Bob/zbOMJML8WyEUqElDdx8rwSnJSDtzv2HkkD4GM5+24aHYZke1W57EndvzSeosQ5U7Fh0Oc+P5IQQ2Rr77bbzjsQ/mBE7kG+sA9/rmixyzqErA+hgxJL9umhiZNqYuhIBSXjArL7YppE4KiZhmMZkLmnAAtQmZrz8+/v8EdnrmvSr4C/jlhhmVyY/s1Rssy76Kz98ZH5RCKC4442+dcE5LFg7RbCmIB2pVgaMAXY8jd4IBdHZwo6Ne7cv8lOFO+85Nx6m70lInX1tMGQa3aUxd1Q8+8DeHnyxdmEpWGuBkTPzGWSL7ICYB8nBkNflybYEDpmic9Y7lYgm7K4TFSfCMW/dIbcnoymA+pyV4zhsTEHFGhymXId59VISP',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(
        "https://www.asos.com/api/product/search/v2/categories/1314",
        params=getParams(i),
        cookies=COOKIES,
        headers=headers,
    )

    appendResults(response)


female_df = pd.DataFrame({"Name": name, "Brand": brand, "Price": price, "Url": url})
df = male_df.append(female_df, ignore_index=True)
df.to_csv('data.csv', index=False)
