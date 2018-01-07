# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from commands import robot_comands

@csrf_exempt
def direction(request, robot_id):
    robot_comands.init_pins()
    body = request.body.decode('utf-8')
    data = json.loads(body)
    print(data)
    method_to_call = getattr(robot_comands, data["name"])
    method_to_call(data['settings'])
    return HttpResponse(data["settings"])

