from django.shortcuts import render, get_object_or_404

# Create your views here.

def tool_in_category(request):
    return render(request, 'category/category.html')