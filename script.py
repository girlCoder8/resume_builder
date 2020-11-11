import requests, json, urllib
from datetime import date

# Search for used Model 3 vehicles with FSD near Redmond, WA, excluding SR and Performance vehicles.
query = '{"query":{"model":"m3","condition":"used","options":{"TRIM":["MRRWD","LRRWD","LRAWD"],"AUTOPILOT":["AUTOPILOT_FULL_SELF_DRIVING"]},"arrangeby":"Price","order":"asc","market":"US","language":"en","super_region":"north america","lng":-122.1257,"lat":47.6722,"zip":"98052","range":0},"offset":0,"count":50,"outsideOffset":0,"outsideSearch":false}'

y = json.loads(requests.get('https://www.tesla.com/inventory/api/v1/inventory-results?query=' + urllib.parse.quote(query)).content)
toExport = ('"Found ' + y['total_matches_found'] + ' results."\n')
toExport += ('"Request date: ' + str(date.today()) + '"\n')
toExport += ('"VIN","MODEL","TRIM","MILAGE","AP","PRICE","LOCATION"\n')
for result in y['results']:
    toExport += ('"' + result['VIN'] + '","' + result['Model'] + '","' + result['TrimName'] + '","' + str(result['Odometer']) + ' ' + result['OdometerType'] + '","' + result['AUTOPILOT'][0] + '","$' + str(result['Price']) + '","' + result['MetroName'] + '"\n')
file = open(str(date.today()) + ".csv", "w")
file.write(toExport)
file.close()