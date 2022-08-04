import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def tool_in_category(request):
    return render(request, 'category/category.html')

def upload_csv(request):
    return render(request, 'category/upload.html')

# ajax로 받아온 json 데이터 처리
@csrf_exempt
def ajax_method(request):
    if request.method == "POST":
        uploaded = request.POST.get('upload_data', None)
        uploaded_list = json.loads(uploaded)
        print(uploaded_list)
    return render(request, 'category/loading.html')
