# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def direction(request, robot_id):
    data = json.loads(request.body)
    #	move(data["direction"])
    return HttpResponse(data["direction"])

