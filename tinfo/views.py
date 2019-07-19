from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Tripinfo
# Create your views here.
def index(request):
    latest_trip_info = Tripinfo.objects.all
    context = {'latest_trip_info': latest_trip_info}
    return render(request, 'tinfo/index.html', context)

def delete(request, question_id):
    item = Tripinfo.objects.get(pk=question_id)
    item.delete()
    return redirect('tinfo:index')

def detail(request, question_id):
    question = get_object_or_404(Tripinfo, pk=question_id)
    return render(request, 'tinfo/detail.html', {'question': question})

def vote(request, question_id):
    question = Tripinfo.objects.get(pk=question_id)
    question="{{ question.name }}"
    return redirect('tinfo:index')