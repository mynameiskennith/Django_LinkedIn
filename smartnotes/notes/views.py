from django.shortcuts import render
from . models import Notes
from django.http import Http404
from django.views.generic import DetailView,ListView,CreateView,UpdateView
from .forms import NotesForm

class NotesListView(ListView):
    # use cheyyunna model
    model = Notes

    # pass cheyyunna key name
    context_object_name = "notes"

    # use cheyyunna template
    template_name = 'notes/notes_list.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_details.html'


# def detail(request, pk):
#     try:
#         notes = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         return render(request,'notes/error.html',{})
#         #raise Http404("Note does not exist")
#     return render(request, 'notes/notes_details.html', {'note':notes})
    
class NotesCreateView(CreateView):
    model = Notes
    #fields = ['title','text']
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    #fields = ['title','text']
    success_url = '/smart/notes'
    form_class = NotesForm