from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Publisher
from .forms import UploadFileForm, NameForm
from django.views.generic.edit import FormView
from django.views.generic import ListView


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


def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            if request.session['password'] == 'abc':
                request.session.delete_test_cookie()
                return HttpResponse('login success')
            else:
                return HttpResponse('wrong username or password')
        else:
            return HttpResponse('please enable your cookie')
    request.session.set_test_cookie()
    return render(request, 'login.html')


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('get name' + form.your_name)
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


class PublisherList(ListView):
    model = Publisher
