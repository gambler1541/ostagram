from django.shortcuts import render
from django.views.generic import CreateView

from .models import Photo

def photo_list(request):
    photo = Photo.objects.all()
    context = {
        'photo' : photo
    }
    return render(request, 'photo/list.html', context)


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        pass