from django.shortcuts import render
from django.template import RequestContext
from django.template import context
from models import Add_Device
from django.shortcuts import render_to_response
#from userauth.forms import UserForm, UploadForm ,Login_Adver
from userauth.forms import UserForm, UserProfileForm, UploadForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ssad15.views import check_availability
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from userauth.models import UserProfile,UploadAdvetisement
def register(request):

	registered = False

    	if request.method == 'POST':
        	user_form = UserForm(data=request.POST)
        	profile_form = UserProfileForm(data=request.POST)

        	if user_form.is_valid() and profile_form.is_valid():
                #if user_form.is_valid():
            		user = user_form.save()

            		user.set_password(user.password)
            		user.save()

            		profile = profile_form.save(commit=False)
            		profile.user = user


            		profile.save()

            		registered = True


        	else:
            		print user_form.errors , profile_form.errors

    	else:
        	user_form = UserForm()
        	profile_form = UserProfileForm()

    	return render(request,'userauth/register_login.html',
                {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/userauth/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(email_id, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request,'userauth/login.html', {})

@login_required
def restricted(request):
	 return HttpResponse("Since you're logged in, you can see this text!")
def user_logout(request):
    	logout(request)
	return HttpResponseRedirect('/userauth/')
	#return render(request,'userauth/base.html', {})

def upload(request):
	print  "inside upload"
	uploaded = False
	time_error = False
	msg = "sendig nothing "
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		print "the requeat is post"
		# print form
		if form.is_valid():
			post = form.save(commit=False)
			post.uploader = request.user
			uploaded = True
			print "form has been validated"
			if post.time_of_advertisement <= post.no_of_slots*30:
				time_error = True
				print "post is ", post.start_week
				if not check_availability(post) :
					print "THe demanded resources are not avaialable"
				else :
					post.save()
		else :
			print form.errors
	else :
		form = UploadForm()
	if time_error == True :
		return home(request)
	return render(request,'userauth/upload.html', {'form': form , 'uploaded':uploaded , 'time_error':time_error,'msg':msg})

def home(request):
	return render(request,'userauth/index.html')
def device_login(request):
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                #if Add_Device.objects.filter(Username=request.POST['username'], password=request.POST['password']).exists():
                if Add_Device.objects.filter(Username=request.POST['username'],password=request.POST['password']).count()==1:
                        #return render(request,'/userauth/')
                        return HttpResponseRedirect('/ssad15/start_advertisement')
                else:
                        return HttpResponse("Invalid Login")
        else:
                return render(request,'userauth/logdiv.html', {})
def user_edit(request,pk):

        if UserProfile.objects.filter(user = request.user).count()==1:
                Edit = 0
                user = get_object_or_404(User, pk=pk)
                userprofile = get_object_or_404(UserProfile , user=user)
                if request.method == "POST":
                        user_form = UserForm(data=request.POST , instance=user)
                        profile_form = UserProfileForm(data=request.POST , instance = userprofile)
                        if user_form.is_valid() and profile_form.is_valid():
                                Edit = 1
                                user_form.save()
                                profile_form.save()
                                return HttpResponseRedirect('/userauth/')
                        else:
                                print user_form.errors , profile_form.errors
                else:
                        user_form = UserForm(instance=user)
                        profile_form = UserProfileForm(instance=userprofile)
                return render(request, 'userauth/register_edit.html', {'user_form': user_form, 'profile_form': profile_form, 'Edit':Edit})
        else:
                Edit = 2
                user = get_object_or_404(User, pk=pk)
                if request.method == "POST":
                        user_form = UserForm(data=request.POST , instance=user)
                        if user_form.is_valid():
                                Edit = 3
                                user_form.save()
                                return HttpResponseRedirect('/userauth/')
                        else:
                                print user_form.errors
                else:
                        user_form = UserForm(instance=user)
                return render(request, 'userauth/register_edit.html', {'user_form': user_form, 'Edit':Edit})
def user_history(request):
        #advertisment = UploadAdvetisement.objects.all().order_by('-date')
        advertisment = UploadAdvetisement.objects.filter(uploader = request.user).order_by('-date')
        return render(request, 'userauth/user_history.html', {'advertisment':advertisment})
