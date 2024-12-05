from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import re

def all_service(station):
    result = ''
    link = 'https://www.sbstransit.com.sg/service/sbs-transit-app?BusStopNo=' + station + '&ServiceNo='
    req = Request(link)
    page = urlopen(req).read()
    page_code = soup(page, 'html.parser')

    found = page_code.find_all('tr')

    found.remove(found[0])

    for i in found:
        service = i.find_all('td')
        for thing in service:
            result = result + re.sub('<.*?>', '', str(thing)) + '\n'
        result = result + '\n'
    return result

def a_service(station, service):
    result = ''
    link = 'https://www.sbstransit.com.sg/service/sbs-transit-app?BusStopNo=' + station + '&ServiceNo=' + service
    req = Request(link)
    page = urlopen(req).read()
    page_code = soup(page, 'html.parser')

    found = page_code.find_all('tr')

    found.remove(found[0])

    service = found[1].find_all('td')
    print(len(service))
    for thing in service:
        result = result + re.sub('<.*?>', '', str(thing)) + '\n'
    result = result + '\n'
    return result
