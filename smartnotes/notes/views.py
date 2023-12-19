from django.shortcuts import render
from . models import Notes
from django.http import Http404
from django.views.generic import ListView

class NotesListVieew(ListView):
    model = Notes
    context_object_name = "notes"

def list(request):
    all_notes = Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes': all_notes})

def detail(request, pk):
    try:
        notes = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return render(request,'notes/error.html',{})
        #raise Http404("Note does not exist")
    return render(request, 'notes/notes_details.html', {'note':notes})