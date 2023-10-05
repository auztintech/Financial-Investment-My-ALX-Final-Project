from django.shortcuts import render,redirect, get_object_or_404
from user.models import User
from .models import Plan, Earned, Deposit, Withdraw, MakeDeposit,Company_Account
from .forms import DepositForm,WithdrawForm,MakeDepositForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




#user's deposit history function
@login_required
def deposit_history(request):
	context = {}
	page_title = "Deposit History "
	all_deposit = MakeDeposit.objects.filter(user=request.user)
	context['all_deposit'] = all_deposit
	context['page_title'] = page_title
	if request.method == 'POST':
		amount_entered = request.POST.get('amount')
		request.session['amount_entered'] = amount_entered
		return redirect("wallet:payment_proof")
	return render(request, 'wallet/deposit_history.html',context)


#user's uploading payment proof if investment was done without any plan
@login_required
def payment_proof(request):
	context = {}
	page_title = "Upload Proof"
	context['page_title'] = page_title
	amount_entered = request.session.get('amount_entered',None)
	context['amount_entered'] = amount_entered
	context['form'] = MakeDepositForm()
	if request.method == 'POST':
		form_data = MakeDepositForm(data=request.POST,files=request.FILES)
		if form_data.is_valid():
			updated_data_form = form_data.save(commit=False)
			updated_data_form.amount = amount_entered
			updated_data_form.user = request.user
			updated_data_form.save()
			messages.success(request, "Payment details send successfully ")
			messages.info(request,"We will contact you once your payment has been confirmed")
			return redirect("wallet:deposit_history")
	return render(request, 'wallet/payment_proof.html',context)


#function for investment 
@login_required
def make_deposit(request):
	page_title = "Make Deposit"
	plans = Plan.objects.all()
	# if user.
	if request.method == 'POST':
		amount_entered = request.POST.get('amount')
		request.session['amount_entered'] = amount_entered
		return redirect("wallet:payment_proof")
	context = {'page_title':page_title,'plans':plans,}
	return render(request, 'wallet/make_deposit.html',context)




#this handles more details as the investor proceeds with investment. it checks if the amout
#he is investing is in range with the plan chosen else, it raises error
@login_required
def make_deposit_detail(request,plan_name):
	page_title = "Make Deposit Details"
	plan_selected = get_object_or_404(Plan,plan_name=plan_name)
	deposit_form = DepositForm()
	if request.method == "POST":
		deposit_form_data = DepositForm(data=request.POST)
		if deposit_form_data.is_valid():
			amount_entered = deposit_form_data.cleaned_data.get('amount')#Give us the exact data type
			if amount_entered < plan_selected.min_deposit:
				messages.error(request, "You can't enter amount less than the selected plan . ")
				return redirect("wallet:make_deposit_detail", plan_selected.plan_name)

			elif amount_entered > plan_selected.max_deposit:
				messages.error(request, "The amount entered exceed the maximum allowable")
				messages.info(request,"Please select greater plan ")
				return redirect("wallet:make_deposit_detail", plan_selected.plan_name )

			else:
				deposit_form_data = deposit_form_data.save(commit=False)
				deposit_form_data.user = request.user
				deposit_form_data.plan = plan_selected
				deposit_form_data.save()
				request.session['deposit_id'] = deposit_form_data.id
				# request.session['deposit_id'] = str(deposit_form_data.id)
				return redirect("wallet:deposit_authorization")

	context = {'page_title':page_title,'plan_selected':plan_selected,'deposit_form':deposit_form,}
	return render(request, 'wallet/make_deposit_detail.html',context)





#this requests for transaction_ID if the user followed a plan whlie investing
@login_required
def deposit_authorization(request):
	context = {}
	page_title = "Make Your Payment "
	deposit_id = request.session.get('deposit_id',None)
	context['page_title'] = page_title
	if deposit_id:
		deposit_selected = get_object_or_404(Deposit, id=deposit_id)
		company_account = Company_Account.objects.last()
		context['deposit_selected'] = deposit_selected
		context['company_account'] = company_account
		if request.method == 'POST':
			transaction_id = request.POST.get("transaction_id")
			deposit_selected.transaction_ID = transaction_id
			deposit_selected.payment_status = "Paid"
			deposit_selected.save()
			messages.success(request, "Transaction ID submitted successfully")
			messages.info(request, "Amount will be added to your active balance on confirmation")
			return redirect("wallet:deposit_authorization")
		return render(request, "wallet/payment_auth.html", context)
	else:
		return render(request, "404.html",context)
	return render(request, 'wallet/your_deposit.html',context)



@login_required
def your_deposit(request):
	page_title = "Your Deposit"
	context = {'page_title':page_title}
	return render(request, 'wallet/your_deposit.html',context)


@login_required
def ask_for_withdraw(request):
	context = {}
	user = request.user
	page_title = "Ask For Withdraw "
	form = WithdrawForm()
	context['page_title']=page_title
	context['form']=form
	if request.method == 'POST':
		form_data = WithdrawForm(request.POST)
		if form_data.is_valid():
			amount_entered = form_data.cleaned_data.get('amount')
			if amount_entered > user.balance:
				messages.error(request, "You can't withdraw more than your balance")
			else:
				form_data = form_data.save(commit=False)
				form_data.user = request.user
				form_data.save()
				messages.success(request, "The money has been deducted from you account. ")
				messages.info(request, "You will be credited within 24 Hours ")
				return redirect("wallet:ask_for_withdraw")

	return render(request, 'wallet/ask_for_withdraw.html',context)


#############################################################
@login_required
def about_to_withdraw(request):
	context = {}
	user = request.user
	page_title = "About To Withdraw "
	return render(request, 'wallet/about_to_withdraw.html',context)
#############################################################################################

@login_required
def earning_history(request):
	context = {}
	page_title = "Earning History"
	all_earning = Earned.objects.filter(user=request.user)
	context['page_title'] = page_title
	context['all_earning'] = all_earning
	return render(request, 'wallet/earning_history.html',context)


@login_required
def withdraw_history(request):
	context = {}
	page_title = "Withdraw History"
	all_withdraw = Withdraw.objects.filter(user=request.user)
	context['page_title'] = page_title
	context['all_withdraw'] = all_withdraw
	return render(request, 'wallet/withdraw_history.html',context)