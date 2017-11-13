from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.views.generic.edit import FormView


# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle upload file code
            handle_upload_file(request.FILES['filename'])
            return HttpResponseRedirect('/success/url/')
    else:
        forml = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def handle_upload_file(f):
    with open('fileurl', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class FormFieldView(FormView):
    form_class = UploadFileForm
    template_name = 'upload.html'
    success_url = 'success'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pass
            # deal with files
            return self.form_valid(form)
        else:
            self.form_invalid(form)
