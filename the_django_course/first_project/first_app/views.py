from django.shortcuts import render
from django.http import HttpResponse
#connecting with db or importing models from db
from first_app.models import AccessRecord,Webpage,Topic,User
from . import forms

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_rec':webpages_list}
    my_dict = { 'insert_me':"yayy its working" }
    return render(request,'index.html',context=date_dic)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'user.html',context=user_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("NAME-->"+form.cleaned_data['name'])
            print("EMAIL-->"+form.cleaned_data['email'])
            print("TEXT-->"+form.cleaned_data['text'])
    return render(request,'form_page.html',{'form':form})

def base(request):
    date = "date"
    return render(request,'base.html')

def other(request):
    return render(request,'other.html')
