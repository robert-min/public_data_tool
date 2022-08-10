import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .elasticsearch import push_elasticsearch


# Create your views here.

def tool_in_category(request):
    return render(request, 'category/category.html')

def upload_csv(request):
    return render(request, 'category/upload.html')

# ajax로 받아온 json 데이터 처리
@csrf_exempt
def ajax_method(request):
    print("test")
    if request.method == "POST":
        uploaded = request.POST.get('upload_data', None)
        uploaded_list = json.loads(uploaded)
        push_elasticsearch(uploaded_list)
        message = "통신 성공"
        context = {"message": message}
        return HttpResponse(json.dumps(context), content_type="application/json")

def upload_loading(request):
    return render(request, 'category/loading.html')