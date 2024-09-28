import json

from datetime import datetime

from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (
    CategorySerializer,
    MasterUnitSerializer,
    OtherUnitSerializer,
    ShowSerializer,
    ShowInfoSerializer,
    SourceWebSerializer,
    SubUnitSerializer,
    SupportUnitSerializer,
)

from .models import (
    Category,
    MasterUnit,
    OtherUnit,
    Show,
    ShowInfo,
    SourceWeb,
    SubUnit,
    SupportUnit,
)


# Create your views here.
class ShowViewSet(ModelViewSet):
    queryset = Show.objects.filter(uid=0)
    serializer_class = ShowSerializer

    @action(detail=False, methods=["GET"])
    def show(self, request):
        showList = Show.objects.using("showDB").all()
        context = {"showList": showList}
        return render(request, "show.html", context)

    @action(detail=False, methods=["GET"])
    def search(self, request):
        uid = request.GET.get("uid")

        showData = Show.objects.using("showDB").get(uid=uid)
        masterUnitData = MasterUnit.objects.using("showDB").filter(uid=uid)
        subUnitData = SubUnit.objects.using("showDB").filter(uid=uid)
        supportUnitData = SupportUnit.objects.using("showDB").filter(uid=uid)
        otherUnitData = OtherUnit.objects.using("showDB").filter(uid=uid)
        showInfoData = ShowInfo.objects.using("showDB").filter(uid=uid)

        # category = Category.objects.using("showDB").get(categoryid = showData.category.categoryid)
        # print(category.categoryname)

        context = {
            "uid": showData.uid,
            "title": showData.title,
            "category": showData.category,
            "showUnit": showData.showunit,
            "discountInfo": showData.discountinfo,
            "descriptionFilterHtml": showData.descriptionfilterhtml,
            "imageUrl": showData.imageurl,
            "webSales": showData.websales,
            "sourceWebPromote": showData.sourcewebpromote,
            "comment": showData.comment,
            "editModifyDate": showData.editmodifydate,
            "sourceWebID": showData.sourcewebid,
            "startDate": showData.startdate,
            "endDate": showData.enddate,
            "hitRate": showData.hitrate,
            "version": showData.version,
            "masterUnit": [i.unitname for i in masterUnitData],
            "subUnit": [i.unitname for i in subUnitData],
            "supportUnit": [i.unitname for i in supportUnitData],
            "otherUnit": [i.unitname for i in otherUnitData],
            "showInfo": showInfoData,
        }
        return render(request, "search.html", context)

    @action(detail=False, methods=["GET"])
    def editPage(self, request):
        uid = request.GET.get("uid")

        showData = Show.objects.using("showDB").get(uid=uid)
        masterUnitData = MasterUnit.objects.using("showDB").filter(uid=uid)
        subUnitData = SubUnit.objects.using("showDB").filter(uid=uid)
        supportUnitData = SupportUnit.objects.using("showDB").filter(uid=uid)
        otherUnitData = OtherUnit.objects.using("showDB").filter(uid=uid)
        showInfoData = ShowInfo.objects.using("showDB").filter(uid=uid)

        categoryData = Category.objects.using("showDB").all()
        sourceWebData = SourceWeb.objects.using("showDB").all()

        context = {
            "show": showData,
            "startDate": showData.startdate.replace("/", "-"),
            "endDate": showData.enddate.replace("/", "-"),
            "masterUnit": masterUnitData,
            "subUnit": subUnitData,
            "supportUnit": supportUnitData,
            "otherUnit": otherUnitData,
            "showInfo": showInfoData,
            "category": categoryData,
            "sourceWeb": sourceWebData,
        }
        return render(request, "edit.html", context)

    @action(detail=False, methods=["POST"])
    def editShow(self, request):
        if request.user.is_authenticated:
            try:
                data = request.data

                uid = data["uid"]
                title = data["title"]
                category = data["categoryID"]
                showUnit = data["showUnit"]
                descriptionFilterHtml = data["descriptionFilterHtml"]
                discountInfo = data["discountInfo"]
                imageUrl = data["imageUrl"]
                webSales = data["webSales"]
                sourceWebPromote = data["sourceWebPromote"]
                comment = data["comment"]
                sourceWebID = data["sourceWebID"]
                startDate = data["startDate"]
                endDate = data["endDate"]

                timeNow = datetime.now()
                editTime = timeNow.strftime("%Y/%m/%d %H:%M:%S")

                showRecord = Show.objects.using("showDB").filter(uid=uid)

                showRecord.update(
                    title=title,
                    category=int(category),
                    showunit=showUnit,
                    descriptionfilterhtml=descriptionFilterHtml,
                    discountinfo=discountInfo,
                    imageurl=imageUrl,
                    websales=webSales,
                    sourcewebpromote=sourceWebPromote,
                    comment=comment,
                    editmodifydate=editTime,
                    sourcewebid=int(sourceWebID),
                    startdate=startDate,
                    enddate=endDate,
                )

                return Response({"msg": "修該完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})

    @action(detail=False, methods=["POST"])
    def editMaster(self, request):
        if request.user.is_authenticated:
            try:
                data = request.data

                masterUnitID = data["masterUnitID"]
                unitName = data["unitName"]

                masterUnitRecord = MasterUnit.objects.using("showDB").filter(
                    masterunitid=masterUnitID
                )

                masterUnitRecord.update(unitname=unitName)

                return Response({"msg": "修改完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})

    @action(detail=False, methods=["POST"])
    def editSub(self, request):
        if request.user.is_authenticated:
            try:
                data = request.data

                subUnitID = data["subUnitID"]
                unitName = data["unitName"]

                subUnitRecord = SubUnit.objects.using("showDB").filter(
                    subunitid=subUnitID
                )

                subUnitRecord.update(unitname=unitName)

                return Response({"msg": "修改完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})

    @action(detail=False, methods=["POST"])
    def editSupport(self, request):
        if request.user.is_authenticated:
            try:
                data = request.data

                supportUnitID = data["supportUnitID"]
                unitName = data["unitName"]

                supportUnitRecord = SupportUnit.objects.using("showDB").filter(
                    supportunitid=supportUnitID
                )

                supportUnitRecord.update(unitname=unitName)

                return Response({"msg": "修改完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})

    @action(detail=False, methods=["POST"])
    def editOther(self, request):
        if request.user.is_authenticated:
            try:
                data = request.data

                otherUnitID = data["otherUnitID"]
                unitName = data["unitName"]

                otherUnitRecord = OtherUnit.objects.using("showDB").filter(
                    otherunitid=otherUnitID
                )

                otherUnitRecord.update(unitname=unitName)

                return Response({"msg": "修改完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})

    @action(detail=False, methods=["POST"])
    def editShowInfo(self, request):
        if request.user.is_authenticated:
            try:
                data = request.data

                showInfoID = data["showInfoID"]
                time = data["time"]
                location = data["location"]
                locationName = data["locationName"]
                onSales = data["onSales"]
                latitude = data["latitude"]
                longitude = data["longitude"]
                price = data["price"]
                endTime = data["endTime"]

                showInfoRecord = ShowInfo.objects.using("showDB").filter(
                    showinfoid=showInfoID
                )

                showInfoRecord.update(
                    time=time,
                    location=location,
                    locationname=locationName,
                    onsales=onSales,
                    latitude=latitude,
                    longitude=longitude,
                    price=price,
                    endtime=endTime,
                )

                return Response({"msg": "修改完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})

    @action(detail=False, methods="DELETE")
    def delete(self, request):
        if request.user.is_authenticated:
            try:
                uid = request.data["uid"]

                masterRecord = MasterUnit.objects.using("showDB").filter(uid=uid)
                masterRecord.delete()
                subRecord = SubUnit.objects.using("showDB").filter(uid=uid)
                subRecord.delete()
                supportRecord = SupportUnit.objects.using("showDB").filter(uid=uid)
                supportRecord.delete()
                otherRecord = OtherUnit.objects.using("showDB").filter(uid=uid)
                otherRecord.delete()
                showInfoRecord = ShowInfo.objects.using("showDB").filter(uid=uid)
                showInfoRecord.delete()
                showRecord = Show.objects.using("showDB").filter(uid=uid)
                showRecord.delete()

                return Response({"msg": "修改完成"})
            except:
                return Response({"msg": "失敗"})
        else:
            return Response({"msg": "please login"})
