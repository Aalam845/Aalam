from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth import authenticate,login,logout

from .models import car,house

# Create your views here.

def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			return redirect('index')
		else:
			return HttpResponse('Credentials does not match!')	
	return render(request,'buying/login.html')


def logout_user(request):
	logout(request)
	return redirect('login_user')

def index(request):
	return render(request,'index.html')


def car_form(request):
	if request.method=="POST":
		name_car = request.POST['name_car']
		date_car = request.POST['date_car']
		car.objects.create(name_car=name_car,date_car=date_car)
		return redirect('cardb')
	return render(request,'car_form.html')

def cardb(request):
	data = car.objects.all()
	return render(request,'cardb.html',{'details':data})


def house_form(request):
	if request.method=='POST':
		name_house = request.POST['name_house']
		date_house = request.POST['date_house']
		house.objects.create(name_house=name_house,date_house=date_house)
		return redirect('house_db')
	return render(request,'house_form.html')

def house_db(request):
	data=house.objects.all()
	return render(request,'house_db.html',{'details':data})

def wishlist(request,id):
	data2 = house.objects.get(id=id)
	return render(request,'wishlist.html',{'details':data2})
	# else:
	# 	data1 = car.objects.get(id=id)	
		# return render(request,'wishlist.html',{'details':data1})
	# return render(request,'wishlist.html')

# def add(request):

# 	return redirect('wishlist')

def wishlist1(request,id):
	data1=car.objects.get(id=id)
	return render(request,'wishlist.html',{'details':data1})

def destroy(request,id):
	data =  house.objects.get(id=id)
	data.delete()
	return redirect('house_form')


