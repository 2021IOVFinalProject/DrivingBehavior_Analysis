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

def userpage(request):

	return render(request=request, template_name="main/user.html")

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
		result = col.find({'Date':{'$gte' : startdate, '$lte' : enddate}})
		return render(request,'main/data.html',{"data":result})
	else:
		file = File.objects.all()
	return render(request, 'main/data.html',{"data":file})

def data_analysis(request):
	form = DatePickerForm

	return render(request, "main/data_analysis.html", {'form':form})

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
		fee = 1170
	elif data >=1000:
		fee = 975
	else:
		fee = 780
	
	return render(request, "main/ubi.html", {"data":data, "fee":fee})	