from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers


from .models import Tags,Work

def test1(request):
    tags = list(Tags.objects)[:10]
    return render(request,'index.html',{'title':'首页','tags':tags})

def test2(request):
    if request.method == "POST":
        tags = list(Tags.objects)[:10]
        return render(request,"index.html",{'title':'点击后首页','tags':tags})
    else:
        tag_name = request.GET.get("username")
        password = request.GET.get("password")
        print(tag_name)

        # res 是py的字典，不能直接传， 必须json传过去
        # res = {'user': tag_name, 'msg': password}  # 自定义一个字典存储登录账户，和登录错误信息
        # works = Work.objects()

        workl = Work.objects(tags = tag_name)
        print(workl)
        # data = serializers.serialize("json",workl)
        # print(data)
        #
        # return HttpResponse(json.dumps(data))

        return render(request,"test.html",{"works":workl,'title':'链接','tagname':tag_name})


def test3(request):

    return render(request,"test.html",{'title':'链接'})


def ajax_index(request):
    return render(request,'ajax_request.html')

def ajax_get(request):
    return HttpResponse('')

def ajax_post(request):
    return HttpResponse('')

def ajax_json(request):
    return HttpResponse('')