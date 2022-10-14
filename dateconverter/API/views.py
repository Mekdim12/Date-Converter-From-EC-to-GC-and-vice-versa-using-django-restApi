from operator import imod
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from . import DateConverterViceVersa


# Create your views here.

@api_view(['GET'])
def api_Recview(request):
    
    value = {
        'API/get-date/mm-dd-yyyy/E(G)':'The date will be retrive back as a json'
    }
    return Response(value)






@api_view(['GET'])
def dateRetriver(request, dates, dateFormatted):

    dates = dates.split('-')
    day = int(dates[0])
    month = int(dates[1])
    year = int(dates[2])
    
    if dateFormatted == 'E':
        ConverterDate =DateConverterViceVersa.DateConverter().toGregorian(ethiopian_day=day, ethiopian_month=month, ethiopian_year= year)
        return Response(ConverterDate)

    elif dateFormatted == 'G':
        ConverterDate =DateConverterViceVersa.DateConverter().toEthiopianDateTime(euro_date=day ,euro_month= month ,euro_year= year)
        return Response(ConverterDate)

    else:
         return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })

    