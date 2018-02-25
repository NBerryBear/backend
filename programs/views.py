# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Program
from commands import robot_comands

def names(request):
    programs = Program.objects.all()

    response = []
    for p in programs:
        response.append({
                    "id": p.id,
                    "name" : p.name
                })
    return JsonResponse(response, safe = False)


def add(request):
    body = request.body.decode('utf-8') 
    data = json.loads(body)
    new = Program(name = data["name"], commands = data["commands"])
    print (data)
    new.save()
    response = {
        "name" : new.name,
        "commands" : new.commands
    }
    print (new.commands)
    return JsonResponse(response, safe = False)


@csrf_exempt
def programs (request):
    print (request.method)
    if request.method == "GET":
        return names(request)
    elif request.method == "POST":
        return add(request)

    return HttpResponse(501)




def program_info(program_id):
    info = Program.objects.get(id = program_id)

    response = {
        "id" : info.id,
        "name" : info.name,
        "commands" : info.commands
    }

    return JsonResponse(response)

def run(program_id):
    commands = json.loads(Program.objects.get(id = program_id).commands)
    for i in range(len(commands)):
        print(commands[i]['name'])
        method_to_call = getattr(robot_comands, commands[i]['name'])
        method_to_call(commands[i]['settings'])

    return JsonResponse(len(commands), safe = False)



def update(request, program_id):
    body = request.body.decode('utf-8')
    new_info = json.loads(body)

    Program.objects.filter(id = program_id).update(name = new_info["name"])
    Program.objects.filter(id = program_id).update(commands = new_info["commands"])    

    return HttpResponse("update")

def delete(program_id):
    Program.objects.get(id = program_id).delete();
    return JsonResponse({})


@csrf_exempt
def info(request, program_id):
    if request.method == "GET":
        return program_info(program_id)
    elif request.method == "POST":
        return run(program_id)
    elif request.method == "PUT":
        return update(request, program_id)
    elif request.method == "DELETE":
        return delete(program_id)

    return HttpResponse("Work")
