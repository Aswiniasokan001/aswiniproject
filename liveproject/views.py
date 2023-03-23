from django.shortcuts import render
from liveproject.models import *
from django.http import HttpResponseRedirect
import datetime
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
import random
from django.http import JsonResponse
# Create your views here.


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

# def services(request):
# 	return render(request,'services.html')
def single(request):
		pid=request.GET['pid']
		sngl =prodcuct_tb.objects.filter(id=pid)
		return render(request,'single.html',{'sngl' : sngl})
		
def services(request):
	srv =prodcuct_tb.objects.all()
	return render(request,'services.html',{'srv' : srv})

# def single(request):
# 	return render(request,'single.html')

def team_single(request):
	return render(request,'team-single.html')

def login(request):
	return render(request,'login.html')

# def timeline(request):
# 	return render(request,'timeline.html')
# def faq(request):
# 	return render(request,'faq.html')

def contact(request):
	category=condact_tb.objects.raw('SELECT * FROM fourthapp  GROUP BY category')
	if request.method == "POST":
		Name=request.POST['Name']
		email=request.POST['email']
		Number=request.POST['Number']
		Message=request.POST['Message']
		check=condact_tb.objects.filter(Name=Name,email=email,Number=Number,Message=Message)
		if check:
			return render(request,'contact.html',{"error":"already registered phno"})
		else:
			add=condact_tb(Name=Name,email=email,Number=Number,Message=Message)
			add.save()
			x = ''.join(random.choices(Name + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'Contact form'
			message = f'Hi a message from {Name} {email}, phone is {Number}, message is {Message} thank you .'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['aswiniasokan098@gmail.com',]
			send_mail( subject,message, email_from, recipient_list )
			return render(request,'index.html',{"success":"email saved"})
	else:
		return render(request,'contact.html',{"category":category})
	# 	user=condact_tb(Name=Name,Number=Number,Message=Message)
	# 	user.save()
	# 	return render(request,'index.html')
	# else:
	# 	return render(request,'contact.html',{"error":"message is not sent"})

# def pricing(request):
# 	return render(request,'pricing.html')

def condact_display(request):
	data=condact_tb.objects.all()
	return render(request,"admin/condact_display.html",{'data':data})

# def condact_delete(request):
# 	uid=request.GET['uid']
# 	data=condact_tb.objects.filter(id=uid).delete()
# 	return HttpResponseRedirect('admin/condact_delete/')

def portfolio(request):
	port =image_enter_tb.objects.all()
	return render(request,'portfolio.html',{'port':port})


##########################ADMIN#######################################################

def admin_index(request):
	return render(request,'admin/index.html')

def admin_forms(request):
	return render(request,'admin/forms.html')

def admin_cards(request):
	return render(request,'admin/forms.html')

def admin_pricing(request):
	return render(request,'admin/pricing.html')

def admin_login(request):
	return render(request,'admin/login.html')

def admin_register(request):
	if request.method == 'POST':
		UserName= request.POST['UserName']
		email=request.POST['email']
		password = request.POST['password']
		val = register_tb.objects.filter(email=email)
		if val:
			return render(request,"admin/register.html",{"error":"email already taken"})
		else:
			user= register_tb(UserName=UserName,email=email,password=password)
			user.save()
			return render(request,"admin/index.html")
	else:
		return render(request,"admin/register.html")


def admin_login(request):
	if request.method == 'POST':
		UserName= request.POST['UserName']
		password = request.POST['password']
		check = register_tb.objects.filter(UserName=UserName,password=password)
		if check:
			for a in check:
				request.session['myid']=a.id 
				request.session['myname']=a.UserName
				return render(request,'admin/index.html',{"success" : "Logged in"})

		else:

			return render(request,'admin/login.html')

	else:
		return render(request,'admin/login.html')


def admin_logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return HttpResponseRedirect('/admin_index/')
	else:
		return HttpResponseRedirect('/admin_index/') 
#####################################################################
def admin_product(request):
	if request.method=='POST':
		product_name = request.POST['product_name']
		category = request.POST['category']
		image = request.FILES['image']
		discription = request.POST['discription']
		user = prodcuct_tb(product_name=product_name,category=category,image=image,discription=discription)
		user.save()
		return render(request,"admin/forms.html")
	else:
		return render(request,"admin/forms.html")


def product_display(request):
	data=prodcuct_tb.objects.all()
	return render(request,"admin/product_display.html",{'data':data})

def product_delete(request):
	uid=request.GET['uid']
	data=prodcuct_tb.objects.filter(id=uid).delete()
	return HttpResponseRedirect('/product_display/')


def update_product(request):
	if request.method=='POST':
		product_name = request.POST['product_name']
		category = request.POST['category']
		uid=request.GET['uid']
		image = request.POST['image']
		discription = request.POST['discription']
		if image == "yes":
			image=request.FILES['image']
			oldrec=prodcuct_tb.objects.filter(id=uid)
			updrec=prodcuct_tb.objects.get(id=uid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image=image
			updrec.save()
		user = prodcuct_tb.objects.filter(id=uid).update(product_name=product_name,category=category,discription=discription)
		return HttpResponseRedirect('/product_display/')
	else:
		uid=request.GET['uid']
		mno = prodcuct_tb.objects.filter(id=uid)
		return render(request,"admin/update_product.html",{'data':mno})


	##############################################################################################################

	

	


def image_enter(request):
	if request.method=='POST':
		images = request.FILES['images']
		user = image_enter_tb(images=images)
		user.save()
		return render(request,"admin/image_enter.html")
	else:
		return render(request,"admin/image_enter.html")


def image_display(request):
	port=image_enter_tb.objects.all()
	return render(request,"admin/image_display.html",{'port':port})