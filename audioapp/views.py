from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from audioapp.models import program , subprogram, audio , coupon ,OrderDetail
import datetime
import re
import stripe
from audiomusic.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY
# Create your views here.
def home(request):
    schedule(request);
    Program = program.objects.all()
    Subprogram = subprogram.objects.all()
    Audio = audio.objects.all()
    for subprograms in Subprogram:
        sid = subprograms.id
        sp = subprogram.objects.get(id = sid)
        if audio.objects.filter(subprogram = subprograms).count() > 0:
           
            sp.p_status = True
            sp.save()
        else:
            sp.p_status = False
            sp.save()
    context = {'program': Program , 'subprogram': Subprogram, 'audio': Audio}
    return render(request, "homepage.html" , context)
def Userlogin(request):
    Program = program.objects.all()
    Subprogram = subprogram.objects.all()
    Audio = audio.objects.all()
    context = {'program': Program , 'subprogram': Subprogram, 'audio': Audio}
    if request.method == "POST":
        # Get the post parameters
      
        username = request.POST['uname']
        password = request.POST['upassword']
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            messages.success(request, "You have succesfully login.")
            return render(request, 'login.html', context)

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "login.html")
    return render(request, 'login.html' ,context)
  
def signup(request):
    Program = program.objects.all()
    Subprogram = subprogram.objects.all()
    Audio = audio.objects.all()
    context = {'program': Program , 'subprogram': Subprogram, 'audio': Audio}
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'signup.html')
        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'signup.html')

        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'signup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'signup.html')
        
        if(re.search(regex,email)):   
           print("Valid Email")   
        else:   
           messages.error(request, " invalid email")
           return render(request, 'signup.html') 
         
        # Create the user
        user = User.objects.create_user(username, email, password)
        user.save()
        
        messages.success(request, "You have succesfully Registerd.")
        return render(request, 'signup.html')
    return render(request, 'signup.html' , context)
def ulogout(request):
    logout(request)
    return redirect('/')
def list(request, id):
        Program = program.objects.all()
        Subprogram = subprogram.objects.all()
        Audio = audio.objects.all()
        Subprogram1 = subprogram.objects.get(id=id)
        purchased = None

        if request.user.is_authenticated:
             user1 = User.objects.get(username=request.user.username)
             if OrderDetail.objects.filter(ProgramID = id, user = user1 ):
                    purchased = 'purchased'
                    
        
        Audio1 = audio.objects.filter(subprogram=Subprogram1)
        context = {'purchased':purchased,'subprogram': Subprogram, 'audio': Audio, 'program':Program, 'subprogram1': Subprogram1, 'audio1': Audio1, }

      
        return render(request, 'list.html' ,context )
def schedule(request):
    Program = program.objects.all()
    for x in Program:
        ptime =  x.Duration
        ID = x.id
        current_date = datetime.datetime.now()
        a = (current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000 + current_date.hour*10000 + current_date.minute*100 +current_date.second)
        b = (ptime.year*10000000000 + ptime.month * 100000000 + ptime.day * 1000000 + ptime.hour*10000 + ptime.minute*100 +ptime.second)
        diff = b - a
        if(diff > 0):
              Program1 = program.objects.get(id=ID)
              Sub = subprogram.objects.filter(program = Program1)
              for n in Sub:
                     ID1 = n.id
                     Sub1 = subprogram.objects.get(id=ID1)
                     audio1 = audio.objects.filter(subprogram = Sub1)
                     for a in audio1:
                           a.audio = True
                           a.save()
                     n.subprogram_status = True
                     n.save()
              Program1.interview_status = True
              Program1.save()
        else:
              Program1 = program.objects.get(id=ID)
              Sub = subprogram.objects.filter(program = Program1)
              for n in Sub:
                     ID1 = n.id
                     Sub1 = subprogram.objects.get(id=ID1)
                     audio1 = audio.objects.filter(subprogram = Sub1)
                     for a in audio1:
                           a.audio = False
                           a.save()
                           ab = a.subprogram  
                     n.subprogram_status = False
                     n.save()
              Program1.interview_status = False
              Program1.save()
def proceedcheckout(request):
    couponexpire(request)
    schedule(request);
    amount = 0
    Couponcode = None
    message = None
    Program = program.objects.all()
    Subprogram = subprogram.objects.all()
    Audio = audio.objects.all()
    if request.method == "POST" and 'apply' in request.POST:
        price = 0  
        totalprice = request.POST['totalPrice']
        code1 = request.POST['Coupon']
        print(totalprice)
        if coupon:
            try:
                 Couponcode = coupon.objects.get(code = code1)
                 price = Couponcode.price
            except:
                message = 'invalid coupon'
        totalprice1 = int(totalprice)
        price1 = int(price)
        amount1 =  (totalprice1 - ( totalprice1 * price1 * 0.01 )) 
        amount = int(amount1)
    if request.method == "POST" and 'proceedcheckout' in request.POST:
        totalprice = request.POST['totalPrice']
        context1 = {'totalprice': totalprice}
        return render(request , 'checkout.html',context1 )
    context = {'program': Program , 'subprogram': Subprogram, 'audio': Audio , 'amount' : amount, 'message':message , 'Couponcode':Couponcode} 
    return render(request, "proceedcheckout.html", context )
def charge(request):
    schedule(request);
    user = User.objects.get(username=request.user.username)
    Program = program.objects.all()
    Subprogram = subprogram.objects.all()
    Audio = audio.objects.all()
    if request.method == "POST" :
        ID = request.POST.getlist('id')
        ID1 = [int(x) for x in ID]
        amount = int(request.POST['amount'])
        currency = request.POST['currency']
        customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)
        charge =  stripe.Charge.create(
			customer=customer,
			amount = amount * 100,
			currency=currency,
			description="audioMusic"
			)
     
        thank = True
        for x  in ID1 :
            z = OrderDetail(user=user, ProgramID = x , price = amount)
            z.save()
        context = {'program': Program , 'subprogram': Subprogram, 'audio': Audio , 'thank':thank}
        return render(request , 'successpage.html' , context)
  
    return render(request, "homepage.html")
def couponexpire(request):
    Coupon = coupon.objects.all()
    for c in Coupon:
        Coupontime = c.timeDuration
        couponid = c.id
        current_date = datetime.datetime.now()
        a = (current_date.year*10000000000 + current_date.month * 100000000 + current_date.day * 1000000 + current_date.hour*10000 + current_date.minute*100 +current_date.second)
        b = ( Coupontime.year*10000000000 +  Coupontime.month * 100000000 +  Coupontime.day * 1000000 +  Coupontime.hour*10000 +  Coupontime.minute*100 + Coupontime.second)
        diff = b - a
        if(diff < 0):
            Coupontable =  coupon.objects.get(id = couponid) 
            Coupontable.delete()
 
        


			








