from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    context = {
        'photos' : photos
    }
    return render(request, 'photo/list.html', context)


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

