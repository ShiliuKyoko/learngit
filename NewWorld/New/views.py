from django.shortcuts import render
from New.models import Blong
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    limit = 5
    blong_info = Blong.objects
    paginator = Paginator(blong_info,limit)
    page = request.GET.get('page',1)
    loaded = paginator.page(page)
    context = {
            'info':loaded
    }
    return render(request,'index.html',context)


'''
        'des':blong_info[0].adress,
        'title':blong_info[0].title,
        'author':blong_info[0].name
'''
