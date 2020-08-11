from django.shortcuts import render
from .models import Company, Trading, Share
from users.models import User
from .forms import BidForm


def home(request):
	context = {
		'Companys': Company.objects.all()
	}
	return render(request, 'home/index.html', context)


def trading(request):
	context = {
		'Tradings': Trading.objects.all(),
	}
	tradingform(my_var)
	return render(request, 'home/trading.html', context)
	# if request.method == 'POST':
	# 	form = BidForm(request.POST)
	# 	form = 
			# Trading = form.save()

			# messages.success(request, f'Your account has been created! You can login now.')
	# 		return redirect('trading')

	# else:
	# form = BidForm()

	# print(context[trading])
	
def tradingform(my_var):
	if request.method == 'POST':
		form = BidForm(request.POST, instance=my_var)

		if form.is_valid():
			form.save()

def bidding(request):
	return render(request, 'home/letsbid.html')

def mycompanies(request):
	context = {
		'Shares': Share.objects.all(),
	}
	return render(request, 'home/mycompanies.html', context)

