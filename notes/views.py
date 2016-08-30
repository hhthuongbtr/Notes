from django.shortcuts import render, get_object_or_404, Http404

# Create your views here.
from django.http import HttpResponse
from .models import Subject, Note
from django.template import loader


def index(request):
    subject_list = Subject.objects.all()
    template = loader.get_template('notes/index.html')
    context = {
        'subject_list1': subject_list,
    }
    return HttpResponse(template.render(context, request))

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'notes/subject_detail.html', {'subject': subject})

def results(request, subject_id):
    response = "You're looking at the results of subject %s."
    return HttpResponse(response % subject_id)

def vote(request, subject_id):
    return HttpResponse("You're voting on subject %s." % subject_id)

def note_detail(request, subject_id, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})
