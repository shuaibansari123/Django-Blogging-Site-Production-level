#from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import uuid
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import RequestAborted
from django.shortcuts import render, redirect
from .models import User, Comment, Blog  # , Likes
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, logout

from .models import Contact


def home(request):

    all_obj = Blog.objects.all()
    #url = 'http://ipinfo.io/json'
    #response = requests.get(url=url)
    #response = eval(response.text)
    #ip = requests.get('https://api.ipify.org').content.decode('utf8')
    #print('My public IP address is: {}'.format(ip))
    for i in all_obj:
        print(i.video_blog)

    # change theme
    return render(request, '2125_artxibition/2125_artxibition/index.html', {'all_obj': all_obj})

    # return render(request, 'home.html' , {'all_obj':all_obj})


def blogView(request, pk):
    obj = Blog.objects.get(id=pk)
    import uuid
    print(request.user)
    like_obj = Blog.objects.get(id=pk)
    like_count = like_obj.like_blog.all().count()
    print(uuid.uuid4)

    if str(request.user) == 'AnonymousUser':
        not_right_like = True
        print('likeeeeeeeeeeeekkkkkkkkkkkkk')
        return render(request, 'blogView.html', {'obj': obj, 'like_count': like_count, "not_right_like": not_right_like})

    return render(request, 'blogView.html', {'obj': obj, 'like_count': like_count})


def add_bio(request):
    if request.method == "POST":
        name_get = request.POST.get('name_name', 'notfoundName')
        story_get = request.POST.get('story_name', 'notfoundStory')
        image_get = request.FILES['image_name']
        print(story_get)

        try:
            if User.objects.get(username=request.user) != 'None':
                obj = Blog.objects.create(
                    create_by=request.user,  main_image=f'images/shop/{image_get}',  main_title=story_get)

                fs = FileSystemStorage()
                filename = fs.save(image_get.name, image_get)
                uploaded_file_url = fs.url(filename)
                from django.http import httpResponse
                return redirect('/')

                # return httpResponse(f'<p>{{uploaded_file_url}}</p>')
        except:
            custom = User.objects.get(email='Anonymous@gmail.com')
            obj = Blog.objects.create(
                create_by=custom, main_title=story_get, main_image=image_get)
            return redirect('/')
    return render(request, 'add_bio.html')


# likes

'''
def comment_ajax2(request):
    if request.method == 'POST':
        input1_val = request.POST.get('input1' , 'NotFound')
        input2_val = request.POST.get('input2' , 'NotFound')
        print(input1_val ,input2_val)
        
        like_obj = Likes.objects.get(like_for= Blog.objects.get(id=input2_val) )
        number_like = len(like_obj.like_person.all())
        if request.user == 'AnonymousUser':
            print('anon------------------')
            print(request.user)
            custom= User.objects.get(email='Anonymous@gmail.com')
            
            like_obj.like_person.add(custom )
        else:
            print(request.user)
            
            print('+++++++++++++++++++++++++++++')
            custom= User.objects.get(username=request.user)
            like_obj.like_person.add(custom )
        print(number_like , input2_val , input1_val)
        

        # ANON USER CAN NOT MODIFY  COMMENT

        #DELETE THIS MIGRATIONS THIS WILL CREATE AN ERROR nODE NAME FOTFOUND
        
        return render(request , 'like-ajax.html' , {'number_like':number_like} )

'''


def comment_ajax1(request):
    if request.method == 'POST':
        input1_val = request.POST.get('input1', 'NotFound')

        obj_val = request.POST.get('obj', 'NotFound-objects')
        blog_obj = Blog.objects.get(id=obj_val)
        custom = User.objects.get(email='Anonymous@gmail.com')
        try:
            if User.objects.get(username=request.user) != 'None':
                obj_quary = Comment.objects.create(
                    comment_for=blog_obj, comment_text=input1_val, comment_created_by=request.user)
        except:
            obj_quary = Comment.objects.create(
                comment_for=blog_obj, comment_text=input1_val, comment_created_by=custom)
        all_comment_ob = Comment.objects.filter(
            comment_for=blog_obj).exclude(comment_text="")
        all_comment_obj = all_comment_ob[len(all_comment_ob)::-1]
        param = {'input1_val': input1_val, 'all_comment_obj': all_comment_obj}
        # ANON USER CAN NOT MODIFY  COMMENT
        return render(request, 'ajax1.html', param)


def edit_comment_ajax(request):
    if request.method == "POST":
        comment_create = request.POST.get('comment_create', 'notfoundNameUser')
        new_comment = request.POST.get('new_comment', 'notfoundCOMMENT_id')
        comment_id = request.POST.get('comment_id', 'NOTFOUND COMMENT ID ')
        print(comment_create, new_comment)
        try:
            if User.objects.get(username=request.user) != 'None':
                obj = Comment.objects.get(id=comment_id)
                obj.comment_text = new_comment
                obj.save()
        except:
            print('no modify right---------------')
    return render(request, 'edit_comment_ajax.html')


def test(request):
    return render(request, 'test.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def like_view(request):
    if request.method == 'POST':
        likes = request.POST.get('likes', 'not found likes count')
        blog_number = request.POST.get('blog_number', 'not fount blog number')
        obj = Blog.objects.get(id=blog_number)
        t_like = Blog.like_blog.through.objects.count()

        print(t_like)
        try:
            if User.objects.get(username=request.user).username != 'None':
                print('my user not anon --------')
                if request.user in obj.like_blog.all():
                    obj.like_blog.remove(
                        User.objects.get(username=request.user))
                    t_like = obj.like_blog.all().count()
                    print('remove------------------')
                    return render(request, 'like-ajax.html', {'number_like': t_like})

                else:
                    obj.like_blog.add(User.objects.get(username=request.user))
                    t_like = obj.like_blog.all().count()

                    return render(request, 'like-ajax.html', {'number_like': t_like})
        except Exception as e:
            go_signup = True
            print('GGGGGGGGGGOOOOOOOOOOOOO', e)
            return render(request, 'like-ajax.html', {'number_like': t_like, 'go_signup': go_signup})

        return render(request, 'like-ajax.html', {'number_like': t_like})


def test01(request):
    form1 = UserCreationForm()
    form2 = AuthenticationForm()
    return render(request, 'test01.html', {'form1': form1, 'form2': form2})


# copy the code


#################### index#######################################
def index(request):
    return render(request, 'user/index.html', {'title': 'index'})

########### register here #####################################


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = {'username': username}
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################
            messages.success(
                request, f'Your account has been created ! You are now able to log in')
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'reqister here'})

################ login forms###################################################


def MyLogin(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'account done not exist plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/register2.html', {'form': form, 'title': 'log in'})


def mysignup(request):

    form = UserCreationForm()
    if request.method == 'POST':

        first_name = request.POST.get('myfirst_name', 'NOT FOUND')

        last_name = request.POST.get('mylast_name', 'NOT FOUND')

        email = request.POST.get('myemail', 'NOT FOUND')

        password1 = request.POST.get('pass1', 'NOT FOUND')
        password2 = request.POST.get('pass2', 'NOT FOUND')

        if password1 != password2:

            return render(request, 'user/signup.html', {'form': form, "error": "Password Does Not Match"})

        import random
        obj = User(email=email, first_name=first_name, last_name=last_name,
                   username=first_name+last_name+str(random.randint(1, 10000)))

        obj.set_password(password2)
        obj.save()
        print('save-----------')

        return render(request, "2125_artxibition/2125_artxibition/index.html")

    return render(request, 'user/signup.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def index_view(request):

    return render(request, "2125_artxibition/2125_artxibition/index.html")


def about_view(request):
    all_obj = Blog.objects.all()
    return render(request, "2125_artxibition/2125_artxibition/about.html", {'all_obj': all_obj})


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')

        msg = request.POST.get('msg')
        obj = Contact.objects.create(name=name, message=msg)

        return render(request, '2125_artxibition/2125_artxibition/index.html', {'contact': True})

    return render(request, 'user/contact2.html')
