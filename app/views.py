from django.shortcuts import render
import os 
import csv
import pandas as pd
from django.http import JsonResponse, HttpResponse
from .models import *

# Create your views here.

def index(request):
    data = request
    print(data)
    return render(request, 'index.html')

def supplier(request):
    currentPath = os.getcwd()
    csvPath = os.path.join(currentPath, 'app', 'export.csv')
    csvfile = pd.read_csv(csvPath, encoding='cp1252')
    # print(csvfile['PO Number'])
    supplierName = filterData(csvfile['Supplier'])
    
    return JsonResponse({'supplier':supplierName})

def purchase(request):
    if request.method == 'POST':
        supplier = request.POST['supplierName']
        currentPath = os.getcwd()
        csvPath = os.path.join(currentPath, 'app', 'export.csv')
        csvfile = open(csvPath, 'r')
        getData = csv.DictReader(csvfile)

        tempPONumber = list()
        for i in getData:
            if i['Supplier'] == supplier:
                tempPONumber.append(i['PO Number'])    
    return JsonResponse({'purchase':tempPONumber})

def poNumberData(request):
    data = request.POST['purchaseNumber']
    currentPath = os.getcwd()
    csvPath = os.path.join(currentPath, 'app', 'export.csv')
    csvfile = open(csvPath, 'r')
    getData = csv.DictReader(csvfile)
    poInfo = []
    for i in getData:
        if i['PO Number'] == data:
            poInfo.append([i['PO Number'], i['Description']])

    return JsonResponse({'poInfo':poInfo})

def submit(request):
    data = request.POST
    name = data['name']
    startTime = data['startTime']
    endTime = data['endTime']
    hourWorked = data['hourWorked']
    ratePerHour = data['ratePerHour']
    supplierName = data['supplierName']
    purchaseNumber = data['purchaseNumber']
    Purchase.objects.create(name = name, starttime = startTime, endtime = endTime,
                                         hourworked = hourWorked, rateperhour = ratePerHour, 
                                         suppliername = supplierName, purchasenumber = purchaseNumber)
    return HttpResponse('successfully inserted')

def filterData(data):
    newData = list()
    for i in data:
        # print(str(i) == 'nan')
        if i == '' or str(i) == 'nan':
            continue
        else:
            newData.append(i)
    unique_data = list(dict.fromkeys(newData))
    return unique_data
            
            
            
    
    
    
     
