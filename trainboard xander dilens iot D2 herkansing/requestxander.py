import http.client
import json
import ssl #had issue with desktop and ssl certification expired
ssl._create_default_https_context = ssl._create_unverified_context


def request():

    a = 0

    con = http.client.HTTPSConnection("api.irail.be")
    con.request("GET", "/liveboard/?id=BE.NMBS.008892007&arrdep=departure&format=json")
    test1 = con.getresponse()
    test2 = test1.read()
    dataTest1 = json.loads(test2)
    departureList = dataTest1["departures"]["departure"]

    return(departureList)

if __name__ == "__main__" :
    kaka = request()

    print(kaka)
