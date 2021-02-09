from django.shortcuts import render,HttpResponse,redirect
from app01.models import User
# Create your views here.


def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if request.session.has_key('islogin'):
            # 用户已登录,调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录,跳转到登录页
            # return redirect('/index')
            return HttpResponse("请登录")
    return wrapper

#index 主页
def index(request):
    return render(request,'my_index_app01/index.html')

def login_check(request):
    requsername = request.POST.get('username')
    reqpassword = request.POST.get('password')
    reqremember = request.POST.get('remember')
    dbobjlist = User.objects.filter(username=requsername)
    try:
        if(reqpassword==dbobjlist[0].password):
            response = render(request,'my_index_app01/login_success.html',{'username':requsername})
            if reqremember == 'on':
                    # 设置cookie username，过期时间1周
                response.set_cookie('username', requsername, max_age=7*24*3600)

            request.session['islogin'] = True
            request.session['username'] = requsername
            request.session['password'] = reqpassword

            return response
        else:
            return HttpResponse("密码错了")

    except:
        return HttpResponse("没注册ma?")

    



@login_required
def userpage(request):
    print(request.COOKIES)
    print(request.session['islogin'])
    print(request.session['username'])
    print(request.session['password'])
    #用起来很像
    # return render(request,'my_index_app01/user_page.html',{'username':request.session['username']})
    return render(request,'my_index_app01/user_page.html',{'username':request.COOKIES['username']})

def sign_up(request):
    return render(request,'my_index_app01/sign_up.html')

def sign_up_check(request):
    a = User()
    a.username = request.POST.get('username')
    a.password = request.POST.get('password')
    a.save()
    return render(request,'my_index_app01/sign_up_jump.html') 


def default_index(request):
    return render(request,'my_index_app01/index.html')


