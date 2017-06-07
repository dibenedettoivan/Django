# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import time
from datetime import datetime

# Create your views here.

def home(request):
	home = "Sistema di gestione Istituto C.Zuccante "
	ora = str(datetime.now())
	return HttpResponse (home + ora)


def benvenuto(request):
	tmp = {'Saluto': "Benvenuto!", 'Cognome': "Di Benedetto", 'Nome': "Ivan", 'Ora': datetime.today()}
        return render(request, 'benvenuto.html', {'cntx': tmp})
