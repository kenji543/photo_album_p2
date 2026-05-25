from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.shortcuts import get_object_or_404

from .forms import AlbumForm, ContactForm, PhotoForm, SignUpForm
from .models import Album, Photo


class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'
    paginate_by = 12


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'


class AlbumPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        album = self.get_object()
        return self.request.user.is_staff or album.owner == self.request.user


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, AlbumPermissionMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_form.html'


class AlbumDeleteView(LoginRequiredMixin, AlbumPermissionMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')


class PhotoPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        photo = self.get_object()
        return self.request.user.is_staff or photo.uploaded_by == self.request.user or photo.album.owner == self.request.user


class PhotoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'albums/photo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff or self.album.owner == self.request.user

    def form_valid(self, form):
        form.instance.album = self.album
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.album
        return context

    def get_success_url(self):
        return self.album.get_absolute_url()


class PhotoDeleteView(LoginRequiredMixin, PhotoPermissionMixin, DeleteView):
    model = Photo
    template_name = 'albums/photo_confirm_delete.html'

    def get_success_url(self):
        return self.object.album.get_absolute_url()


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ContactCreateView(FormView):
    template_name = 'albums/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_thanks')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactThanksView(TemplateView):
    template_name = 'albums/contact_thanks.html'
