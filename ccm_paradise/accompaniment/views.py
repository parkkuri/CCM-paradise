from django.shortcuts import render
import os

from django.views.generic import ListView, DetailView
from .models import Music, Chord, Pitch

class accompantiment_list(ListView):
    template_name = os.path.join('list', 'list.html')
    model = Music
    context_object_name = 'object'
    paginate_by = 6



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context["pagelist"] = pagelist
        return context


class accompantiment_detail(DetailView):
    model = Music
    template_name = os.path.join('detail', 'detail.html')

    # def get_queryset(self, *args, **kwargs):
    #     # return self.queryset.filter(book_id=self.kwargs.get('book_id'))
    #     # http://127.0.0.1:8888/musics/1/?pitch_id=1
    #     # self.request.GET['chord']
    #     return super().get_queryset(*args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)


        # context['chord'] = Chord.objects.filter(music_id=self.kwargs['pk']).filter(id=self.request.GET['chord_id']).first()
        all_chord = self.model.objects.filter(id=self.kwargs['pk']).first().chord_music.all()
        context['all_chord'] = all_chord
        woman_chord_pitch = all_chord.filter(woman_chord_whether=True).first()
        if woman_chord_pitch is None:
            woman_chord_pitch_id = None
        else:

            woman_chord_pitch_id = woman_chord_pitch.pitch_id

        man_chord_pitch = all_chord.filter(man_chord_whether=True).first()
        if man_chord_pitch is None:
            man_chord_pitch_id = None
        else:
            man_chord_pitch_id = man_chord_pitch.pitch_id
        context['wonan_chord_pitch_id'] = woman_chord_pitch_id
        context['man_chord_pitch_id'] = man_chord_pitch_id

        # http://127.0.0.1:8888/musics/1/?pitch_id=1
        # '/musics/1/?pitch_id=1'
        chord = all_chord.filter(pitch_id=self.request.GET['pitch_id']).first()
        context['chord'] = chord

        pitch = Pitch.objects.filter(id=self.request.GET['pitch_id']).first()
        context['pitch'] = pitch
        all_pitch_id = self.model.objects.filter(id=self.kwargs['pk']).first().chord_music.all().values('pitch_id')
        all_pitch = Pitch.objects.filter(id__in=all_pitch_id).all()

        context['all_pitch'] = all_pitch

        # context['pitch'] = Pitch.objects.filter(id=self.kwargs['pk']).first().chord_music.all()

        return context

class SearchView(ListView):

    template_name = os.path.join('list', 'list.html')
    model = Music
    context_object_name = 'object'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        object_list = self.model.objects.all()
        if query:
            object_list = object_list.filter(name__icontains=query)
        return object_list