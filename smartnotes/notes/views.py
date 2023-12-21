from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from . models import Notes
from django.http import Http404
from django.views.generic import DetailView,ListView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesListView(LoginRequiredMixin,ListView):
    # use cheyyunna model
    model = Notes

    # pass cheyyunna key name
    context_object_name = "notes"

    # use cheyyunna template
    template_name = 'notes/notes_list.html'

    #login url
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    #same as the create view - same class variables used

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

