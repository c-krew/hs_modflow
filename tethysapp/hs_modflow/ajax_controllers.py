from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect, reverse
import os
from shutil import copyfile
from hs_restclient import HydroShare
from .app import HsModflow as app
import flopy
from model import *

def search(request):

    return_obj = {'success':False}

    hs=HydroShare()

    searchtype = request.POST.get('searchtype')
    searchinput = request.POST.get('searchinput')

    if searchtype == 'creator':
        resources = hs.resources(creator=searchinput)
    elif searchtype == 'user':
        resources = hs.resources(user=searchinput)
    elif searchtype == 'owner':
        resources = hs.resources(owner=searchinput)
    elif searchtype == 'author':
        resources = hs.resources(author=searchinput)
    elif searchtype == 'group':
        resources = hs.resources(group=searchinput)
    elif searchtype == 'subject':
        resources = hs.resources(subject=searchinput)
    elif searchtype == 'type':
        resources = hs.resources(type=searchinput)
    elif searchtype == 'full_text':
        resources = hs.resources(full_text_search=searchinput)

    resourcelist = []

    for resource in resources:
        resourcelist.append([resource['resource_title'],
                    resource['creator'],
                    resource['abstract'],
                    resource['resource_type'],
                    resource['resource_id']
                    ])

    return_obj['success'] = False
    return_obj['resources'] = resourcelist

    return JsonResponse(return_obj)

def load_text_file(request):
    try:

        filename = request.POST.get('filename')
        app_dir = app.get_app_workspace().path
        # app_dir = '/Users/travismcstraw/tethysdev/hs_modflow/tethysapp/hs_modflow/workspaces/app_workspace/'

        filepath = os.path.join(app_dir, filename)

        with open(
                filepath,
                'r'
        ) as myfile:
            filetext = myfile.read()

        return_obj = {'success':True, 'filetext':filetext}


    except:

        return_obj = {'success':False}

    return JsonResponse(return_obj)

def save_text_file(request):

    filename = request.POST.get('filename')
    editedfiletext = request.POST.get('editedfiletext')
    displayname = request.POST.get('displayname')

    app_dir = app.get_app_workspace().path
    # app_dir = '/Users/travismcstraw/tethysdev/hs_modflow/tethysapp/hs_modflow/workspaces/app_workspace/'

    filepath = os.path.join(app_dir, filename)

    with open(filepath,'w') as myfile:
        myfile.write(editedfiletext)

    Session = app.get_persistent_store_database('primary_db', as_sessionmaker=True)
    session = Session()
    model = session.query(Model).filter(Model.displayname==displayname).first()
    model_type = model.modeltype
    resourceid = model.resourceid

    session.close()

    save_to_db(resourceid, displayname, model_type)

    return_obj = {'success':True}

    return JsonResponse(return_obj)

def save_new_entry(request):

    filename = request.POST.get('filename')
    editedfiletext = request.POST.get('editedfiletext')
    displayname = request.POST.get('displayname')
    new_display_name = request.POST.get('new_display_name')

    app_dir = app.get_app_workspace().path
    # app_dir = '/Users/travismcstraw/tethysdev/hs_modflow/tethysapp/hs_modflow/workspaces/app_workspace/'

    filepath = os.path.join(app_dir, filename)

    file = open(filepath, 'w')
    file.write(editedfiletext)
    file.close()

    Session = app.get_persistent_store_database('primary_db', as_sessionmaker=True)
    session = Session()
    model = session.query(Model).filter(Model.displayname==displayname).first()
    model_type = model.modeltype
    resourceid = model.resourceid

    session.close()

    save_to_db_newentry(resourceid, displayname, new_display_name, model_type)


    return_obj = {'success':True}
    return JsonResponse(return_obj)
