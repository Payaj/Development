from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import Property_Info

# Create your views here.


# def List(request):
#     listings = Property_Info.objects.all()
#     return render(request,"BLOG_POSTS/Post_List.html", {'listings':listings})

# def PostForm(request):
#     form = forms.Listings
#     if request.method == 'POST':
#         form = forms.Listings(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('PostList')
#             # print ("Validation Worked")
#     return render(request, "BLOG_POSTS/Post_Form.html",{'form': form})

def List(request):
    form = forms.Listings
    listings = Property_Info.objects.all()
    if request.method == 'POST':
        form = forms.Listings(request.POST)
        if form.is_valid():
            form.save()
            # print ("Validation Worked")
    return render(request, "BLOG_POSTS/Post_List.html",{'form': form, 'listings':listings})

def DeleteRecord(request, id):
    record = Property_Info.objects.get(id = id)
    return render(request, "BLOG_POSTS/Post_Delete.html", {'record': record})


def DeleteRecord_final(request, id):
    record = Property_Info.objects.get(id = id)
    record.delete()
    return redirect('PostList')

def edit(request,id):
    record = Property_Info.objects.get(id = id)
    return render(request, "BLOG_POSTS/Post_Form.html", {'record': record})

def update(request,id):
    record = Property_Info.objects.get(id = id)
    form = forms.Listings(request.POST, instance=record)
    if form.is_valid():
        form.save()
    return redirect('PostList')