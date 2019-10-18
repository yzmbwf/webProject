from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.shortcuts import render  #打开文件，读取文件
from django.shortcuts import redirect  #重定向

users = {}
def login(request):
    # request包含用户提交的所有信息，包括请求方式等。。
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("username",None)
        pwd = request.POST.get("passwd",None)
        users["user_name"] = user
        if user=="user02" and pwd == "qwe123":
            return redirect('/home')
        else:
            error_msg = "用户名或密码错误"
    return render(request,'login.html',{"error_msg":error_msg})

USER_LIST = [
    {"username":"xl","age":"19","sex":"boy"},
    {"username":"x2","age":"11","sex":"girl"},
]
def home(request):
    if request.method == "POST": #大写POST
        u = request.POST.get("user")
        a = request.POST.get("age")
        s = request.POST.get("sex")
        data = {"username": u, "age": a, "sex": s}
        USER_LIST.append(data)
    return render(request,'main.html',{"user_list":USER_LIST,"user_name":users["user_name"]})

def register(request):
    return render(request,"register.html")

# Create your views here.
