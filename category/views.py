from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def tool_in_category(request):
    return render(request, 'category/category.html')

def upload_csv(request):
    return render(request, 'category/upload.html')

# ajax로 받아온 json 데이터 처리
def ajax_method(request):
    if request.method == "POST":
        uploaded = request.POST.get('uploaded_data', None)
        print(uploaded)