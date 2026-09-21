# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
       name = request.GET.get("name") or "world" #add this line
       return render(request,"bookmodule/index.html",{"name":name}) #Changes HttpsResponse to render function
def index2(request, val1 = 0 ): # add the view function (index2)
       return HttpResponse("value1 = "+str(val1))
def viewbook(request, bookId):
       #assume that we have the follwing books somewhere (e.g. database)
       book1 = {'id':123,'title':'Continous Delivery','author':'J. Humble and D. Farly'}
       book2 = {'id':456,'title':'Secrets of Reverse Engineering','author':'E. Eilam'}
       targetBook = None
       if book1['id'] == bookId: targetBook = book1
       if book2['id'] == bookId: targetBook = book2
       context = {'book':targetBook}#book is the variable name accessiable by the template
       return render(request,'bookmodule/show.html',context)