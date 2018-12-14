from django.http import JsonResponse, Http404, HttpResponse
from hs_restclient import HydroShare

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