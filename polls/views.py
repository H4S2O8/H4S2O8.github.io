from django.shortcuts import render
from django.http import HttpResponse

ls = []

def index(request):
    return render(request, 'index.html')

def getData(request):
    # 获取请求参数
    num1 = request.GET.get('num1',0)
    num2 = request.GET.get('num2',0)
    # 处理业务逻辑
    ans = int(num1) + int(num2)
    # 返回响应
    return HttpResponse(f"the answer is {ans}")


def getRESTfulData(request, num1, num2):
    # 获取请求参数
    # 处理业务逻辑
    ans = num1 + num2
    # 返回响应
    return HttpResponse(f"the answer is {ans}")


def postData(request):
    # 获取请求参数
    num1 = request.POST.get('num1',0)
    num2 = request.POST.get('num2',0)
    # 处理业务逻辑
    ans = int(num1) + int(num2)
    # 返回响应
    ls.append(ans)
    print(ls)

    return render(request, 'index.html', {'ans': ans})


from .AzureVoice.test import text_to_mp3
import time

def speech_synthesis(request):
    text = request.POST.get('speech', '未获取到文本')
    text_to_mp3(text)

    print(request.COOKIES.get('time_stamp', 'cookie未获取到时间戳'))

    print(request.session.get('time_stamp', 'session未获取到时间戳'))
    request.session['time_stamp'] = time.time()

    resp = render(request, 'synthesis_result.html', {'text': text})
    resp.set_cookie('time_stamp', time.time())
    return resp
    # return HttpResponse(request, data, content_type='audio/mpeg')



