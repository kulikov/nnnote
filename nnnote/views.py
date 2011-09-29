# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from nnnote.models import NoteItem


def index(request):
    notes = NoteItem.objects.all()
    return render_to_response('nnnote/index.html', { 'notes': notes })

def save(request):
    for (id, text) in request.POST.items():
        note = NoteItem(pk=id, text=text)
        note.save()

    return HttpResponse("ok!")