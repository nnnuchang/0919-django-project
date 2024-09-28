from datetime import datetime

import urllib.request, json, ssl, pymongo

from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    mongoClient = pymongo.MongoClient("mongodb://35.236.151.253:27017/")
    updateDB = mongoClient["updateDB"]
    fishing = updateDB["fishing"]

    url = "https://data.moa.gov.tw/Service/OpenData/FaRss.aspx?key=013&IsTransData=1&UnitId=723"
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as response:
        data = json.loads(response.read().decode("utf-8"))

        test = {
            "field001": "基隆市政府",
            "field002": "一等",
            "field003": "船長",
            "field004": "59",
        }

        for i in data:
            newData = {
                "city": i["field001"],
                "level": i["field002"],
                "position": i["field003"],
                "people": i["field004"],
                "updateTime": datetime.now(),
            }

            fishing.insert_one(newData)

        return JsonResponse({"msg": 'saved'})

