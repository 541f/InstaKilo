from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import signup

def home(request):
	if request.method== 'POST':
		data1=request.POST.get('email')
		data2=request.POST.get('fnm')
		data3=request.POST.get('unm')
		data4=request.POST.get('ps')
		a=signup(email= data1, fullname= data2, username= data3, password=data4)
		a.save()
		return render(request,'login.html')
	else:
		return render(request, 'home.html')

	return render(request,'home.html')
def login(request):
	if request.method == "POST":
		uss=request.POST['unm']
		pss=request.POST['ps']
		try:
			d1=signup.objects.get(username=uss)
			d2=signup.objects.get(password=pss)
		except signup.DoesNotExist:
			d1= None
			d2= None
			if(uss==d1 and pss==d2):
				return redirect('n4')
			else:
				return render(request,'login.html')
		else:
			if(uss==d1.username and pss==d2.password):
				request.session['username'] = uss
				return redirect('n4')
			else:
				return render(request,'login.html')
	return render(request,'login.html')
def common(request):
	return render(request,'common.html')
def main(request):
	a=signup.objects.all()
	return render(request,'main.html',{"c":a})
def profile(request):
	return render(request,'profile.html')

def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
		return render(request,'login.html')
	return redirect('n4')


# Create your views here.
