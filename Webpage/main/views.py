# Create your views here.
import io
from django.shortcuts import render, redirect
from .utils import get_db_handle, get_collection_handle
from django.contrib import messages #import messages
from django.contrib.auth import login, authenticate, logout #import authenticate
from django.contrib.auth.forms import AuthenticationForm #import AuthenticationForm
from .forms import * 
from .models import *
import pandas as pd
import glob, os
from os import listdir
import json
import pymongo
from pandas import DataFrame
from django.http import HttpResponse
from rest_framework.views import APIView
from pyecharts.charts import Line
from pyecharts import options as opts

db_handle, mongo_client = get_db_handle('CarCare_DB', 'localhost', 27017, 'USERNAME', 'PASSWORD')
collection_handle = get_collection_handle(db_handle, 'REGIONS_COLLECTION')
conn = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
db = conn["CarCare_DB"]

def homepage(request):
	return render(request = request, template_name="./home.html")

def about_us(request):
	return render(request = request, template_name="main/aboutus.html"	)

def contact_us(request):
	context = {}
	if request.method =='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Sumbit successful." )
	form = ContactForm()
	context = {'form':form }
	return render(request = request, template_name="main/contact_us.html")

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	
	return render(request=request, template_name="main/login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")


def upload_file(request):
	context = {}

	if request.method == 'POST':
		form = UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			file = form.cleaned_data['file']

			uploadfile = UploadFile()
			uploadfile.title = title
			uploadfile.file = file
			uploadfile.save()

		messages.info(request, "You have successfully uplaod file.")
		files = UploadFile.objects.values()
		files_pandas = pd.DataFrame(files)

	else:
		form = UploadFileForm()
	context['form'] = form
	
	return render(request,'main/upload.html',context={'form':form})

def data(request):
	files_path = 'C:/Users/USER/Desktop/code/env/mysite/static/files/filesupload'
	read_files = glob.glob(os.path.join(files_path,"*.csv"))

	np_array_values = []
	for files in read_files:
		data = pd.read_csv(files)
		np_array_values.append(data)
		print(files)

	with open("C:/Users/USER/Desktop/code/env/mysite/main/data/info.json","r") as file:
		JsonFile = json.load(file)
		client = pymongo.MongoClient()
		database = client[JsonFile["database"]]
		collection = database[JsonFile["collection"]]
		files = listdir(JsonFile["filePath"])

		for file in range(len(files)):

			fileName = JsonFile["filePath"]+"\\"+files[file]
			csvFile = pd.read_csv(fileName)
    
			[x,y] = csvFile.shape
			columns = list(csvFile.columns)
			data = csvFile.values
    
			for row in range(x):
				dataRow = data[row]
				DataDict = dict(zip(columns, dataRow))
				collection.insert(DataDict)
				
			print("Data has been inserted")

			# delete already read files
			os.remove(os.path.join(files_path, fileName))
		
		col = db["main_file"]
		if request.method == "POST":
			startdate = request.POST.get('startdate')
			enddate = request.POST.get('enddate')
			result = col.find({'date_time':{'$gte' : startdate, '$lte' : enddate}})
			return render(request,'main/data.html',{"data":result})
		else:
			file = File.objects.all()

		return render(request, 'main/data.html',{"data":file})

# reference: https://www.fooish.com/html/hyperlink-a-tag.html
def data_analysis(request):
	form = DatePickerForm(request.POST)
	if form.is_valid():
		date = form.cleaned_data['date']
		datepicker = DatePicker()
		datepicker.date = date
		datepicker.save()

		date = request.POST.get('date')
		if date == '2021-09-30':

			return render(request, "main/data_analysis.html", {'form':form})

	return render(request, "main/data_analysis2.html", {'form':form})


def data_analysis2(request):
	form = DatePickerForm(request.POST)
	if form.is_valid():
		date = form.cleaned_data['date']
		datepicker = DatePicker()
		datepicker.date = date
		datepicker.save()

		date = request.POST.get('date')
		if date == '2021-09-30':
		
			return render(request, "main/data_analysis.html", {'form':form})

	return render(request, "main/data_analysis2.html", {'form':form})

def data_prediction(request):
	
	return render(request=request, template_name="main/data_prediction.html")	

def ubi(request):
	col = db.main_file
	data = col.find()
	list_data = list(data)
	# Converting to the DataFrame
	df = DataFrame(list_data)
	# print(df['Distance_travelled'])
	data = sum(df['Distance_travelled'])
	# print("Total Distance travelled:", sum(df['Distance_travelled']))
	# Insurance calculation
	if data >= 3000:
		fee = '1,170'
	elif data >= 1000:
		fee = 975
	else:
		fee = 780
	
	return render(request, "main/ubi.html", {"data":data, "fee":fee})

# pyecharts integration
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def linechart() -> Line:
	df = pd.read_csv('./main/data/User2_Dataset.csv',  index_col = [1], parse_dates = ['Date'])
	average_speed = df['Average_speed']
	distance_travelled = df['Distance_travelled']
	fuel_used = df['Fuel_used']
	vehicle_speed = df['Vehicle_speed']

	x_date = ['2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', 
			'2021-05', '2021-06','2021-07', '2021-08', '2021-09' ]
	c = (
		Line()
		.add_xaxis(x_date)
		.add_yaxis("Engine RPM", average_speed)
		.add_yaxis("Distance_travelled", distance_travelled)
		.add_yaxis("Fuel Used", fuel_used)
		.add_yaxis("Vehicle Speed", vehicle_speed)

	)
	return c

class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(linechart()))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("main/data_analysis").read())