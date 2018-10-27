import json
import traceback

from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from loginapp.models import UserData

#open login page as landing page
def load_landing_page(request):
    print '----request in | login view.py | load_landing_page----'
    return render(request, 'login.html')


# check username and password from database
@csrf_exempt
def sign_in(request):
    try:
        print '----request in | login view.py | sign_in----'
        message = ''
        url = ''
        #save username and password from database in
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        #check if username and password in dabase is same as the entered in textbox
        user = authenticate(username=username, password=password)
        #if password and username is same
        if user:
            #if user is active load dashboard page
            if user.is_active:
                url = '/dashboard/'
            else:
                message = 'User is not active'
        else:
            message = 'Enter valid username and password'

        #send success, message and url
        data = {'success': 'true', 'message': message, 'url':url}
        print "----------data--------",data
    except Exception as exe:
        # traceback to know the error on specific line
        print 'exception', str(traceback.print_exc())
        print 'exception in | loginapp views.py | sign_in', exe
        data = {'error': 'true'}
    print '----request out | login view.py | sing_in----'
    return HttpResponse(json.dumps(data), content_type='application/json')


# Store data into table
@csrf_exempt
@transaction.atomic
def sign_up(request):
    #variable for performing transaction
    sid = transaction.savepoint()
    try:
        print '----request in | loginapp views.py | sign_up----'
        #save data from form to database in variable user_data
        user_data = UserData(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            username=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            country=request.POST.get('country'),
        )
        #save data
        user_data.save()
        #to save passowrd (encrypted)
        user_data.set_password(request.POST.get('password'))
        user_data.save()
        #transaction commit
        transaction.savepoint_commit(sid)
        data = {'success': 'true'}
        print '----end | loginapp views.py | sign_up----'
    except Exception as exe:
        print 'exception', str(traceback.print_exc())
        print 'exception in | loginapp views.py | sign_up', exe
        #if exception occur rollback transaction
        transaction.rollback(sid)
        data = {'error': 'true'}
    print '----request out | login view.py | sign_up----'
    return HttpResponse(json.dumps(data), content_type='application/json')

#open dashboard page
def open_dashboard(request):
    return render(request, 'dashboard.html')
