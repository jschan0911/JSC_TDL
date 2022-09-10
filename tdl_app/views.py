from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def index(request):
    ing_tdls = tdl.objects.filter(is_end = False).order_by('-writtendate')
    end_tdls = tdl.objects.filter(is_end = True).order_by('-writtendate')
    return render(request, 'index.html', {'ing_tdls':ing_tdls, 'end_tdls':end_tdls})

def detail(request, tdl_id):
    tdl_detail = get_object_or_404(tdl, pk = tdl_id)
    return render(request, 'detail.html', {'tdl_detail':tdl_detail})

def create(request):
    if (request.method == 'POST'):
        form = tdlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = tdlForm()
    return render(request, 'create.html', {'form':form})

def tdlend(request, tdl_id):
    now_tdl = get_object_or_404(tdl, pk = tdl_id)
    if (now_tdl.is_end == False):
        now_tdl.is_end = True
    else:
        now_tdl.is_end = False
    now_tdl.save()
    return redirect('index')

def tdldelete(request, tdl_id):
    now_tdl = get_object_or_404(tdl, pk = tdl_id)
    now_tdl.delete()
    return redirect('index')
# Create your views here.
