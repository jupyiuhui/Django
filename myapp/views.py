from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls.conf import path
from django.db import models
from .models import Employee
from django.http import HttpResponse
import xlwt
import csv
from django.core.paginator import Paginator
import pymongo
from django.conf import settings
from bson.objectid import ObjectId
from pymongo import MongoClient
import re
from .my_thread import MyThread
from django.http import HttpResponseRedirect
my_client = pymongo.MongoClient(settings.DB_NAME)
dbname = my_client['123a']
collection_name = dbname["myapp_employee"]

employee = Employee.objects.all

def welcome(request):
    return render(request, "template1/pages/tables/data.html")

def form(request):
    return render(request, 'template1/pages/forms/form.html')

def show(request):
    return render(request, 'template1/pages/tables/data.html',{'employee':employee})

def search(request):
    social_network = request.POST['Social_Network']
    key = request.POST['Key_word']
    re_pat = re.compile(social_network)
    re_pat1 = re.compile(key)
    if (social_network!=None and key ==''):
        myquery = {"Social_Network":{"$regex": re_pat}} 
    elif(key != None and social_network != ""):
        myquery = {"Social_Network":{"$regex": re_pat},"Key_word":{"$regex": re_pat1}}
    elif(social_network != None and social_network == "" and key != None):
        myquery={"Key_word":{"$regex": re_pat1}}
        
    mydoc = collection_name.find(myquery)
    employee = []
    for i in mydoc:
        employee.append(i)
    return render(request, 'template1/pages/tables/data.html', {'employee': employee})

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True 
    columns = ['STT','Key_word','Names','Link_post','post','comment','device','time']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()

    rows = Employee.objects.all().values_list('STT','Key_word','Names','Link_post','post','comment','device','time')
    
    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,row[col_num],font_style)

    wb.save(response)

    return response

def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
  
    writer = csv.writer(response)
    writer.writerow(['STT','Key_word','Names','Link_post','post','comment','device','time'])
  
    users = Employee.objects.all().values_list('STT','Key_word','Names','Link_post','post','comment','device','time')
    for user in users:
        writer.writerow(user)
 
    return response

def my_thread(request):
    thread = MyThread()
    thread.start()
    msg = 'Start thread...'
    print(msg)