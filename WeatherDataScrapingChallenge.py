from requests_html2 import HTMLSession

s= HTMLSession()

query = input ('Enter city: ')
url= f'https://www.google.com/search?q=weather+{query}'
r=s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
temp= r.html.find('span#wob_tm',first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
desc = r.html.find('div.VQF4g',first=True).find('span#wob_dc',first= True).text
wind = r.html.find('div.wtsRwe',first=True).find('span#wob_tws',first= True).text
humidity = r.html.find('div.wtsRwe',first=True).find('span#wob_hm',first= True).text

print("City: ",query)
print("temp: ", temp, unit)
print("Weather Condition: ",desc)
print("Wind: ", wind)
print("humidity: ",humidity)
#print(r.html.find('div.VQF4g',first=True).find('span#wob_dc',first= True).text)