from urllib.request import urlopen
import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer


def is_industry_halal(industry):
    keywords = ['alcohol', 'pork', 'gambling', 'pornography', 'weapon']
    search_list = industry.split(",")

    for item in search_list:
        for val in keywords:
            if val in item:
                return False
    return True


def is_income_halal(revenue, interestIncome):
    return False if float(interestIncome) / float(revenue) >= 0.05 else True


def is_debt_halal(totalAssets, totalDebt):
    return False if float(totalAssets) / float(totalDebt) >= 0.33 else True


@api_view(['GET'])
def company_info(request):
    response = urlopen(
        "https://financialmodelingprep.com/api/v3/profile/{}?apikey=e7394146d80618dee7f07fb36f6d1126".format(
            request.query_params.get('symbol')))
    data_json = json.loads(response.read())

    return Response({
        'data': data_json[0],
        'industry': data_json[0]['industry'],
        'is_industry_halal': is_industry_halal(data_json[0]['industry'])
    })


@api_view(['GET'])
def company_income(request):
    response = urlopen(
        "https://financialmodelingprep.com/api/v3/income-statement/{}?apikey=e7394146d80618dee7f07fb36f6d1126".format(
            request.query_params.get('symbol')))
    data_json = json.loads(response.read())

    return Response({
        'data': data_json[0],
        'revenue': data_json[0]['revenue'],
        'interestIncome': data_json[0]['interestIncome'],
        'is_revenue_halal': is_income_halal(data_json[0]['revenue'], data_json[0]['interestIncome'])
    })

# 3. Total Debt calculation
@api_view(['GET'])
def company_debt(request):
    response = urlopen(
        "https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?apikey=e7394146d80618dee7f07fb36f6d1126".format(
            request.query_params.get('symbol')))
    data_json = json.loads(response.read())

    return Response({
        'data': data_json[0],
        'is_debt_halal': is_debt_halal(data_json[0]['totalAssets'], data_json[0]['totalDebt'])
    })


@api_view(['GET'])
def company_search(request):
    response = urlopen("https://ticker-2e1ica8b9.now.sh/keyword/{}".format(request.query_params.get('text')))
    data_json = json.loads(response.read())

    return Response(data_json)





#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class Company(APIView):
#     def get(self, request, format=None):
#         response = urlopen(
#             "https://financialmodelingprep.com/api/v3/profile/{}?apikey=e7394146d80618dee7f07fb36f6d1126".format(
#                 request.query_params.get('symbol')))
#         data_json = json.loads(response.read())
#
#         return Response(data_json)
#
#
# class CompanySearch(APIView):
#     def get(self, request, format=None):
#         response = urlopen("https://ticker-2e1ica8b9.now.sh/keyword/{}".format(request.query_params.get('text')))
#         data_json = json.loads(response.read())
#
#         return Response(data_json)
