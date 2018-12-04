from django.http import JsonResponse, Http404, HttpResponse
import requests
from hs_restclient import HydroShare
from .app import HsModflow as app


def load_resource(request):

    try:

        resourceid = request.POST.get('resourceid')

        hs = HydroShare()

        app_dir = app.get_app_workspace().path
        resourcelist = hs.getResourceFileList(resourceid)

        filelist = []

        for resource in resourcelist:
            url = resource['url'].split("/")
            fname = url[-1]
            hs.getResourceFile('21c38e32c8f34de1a3073e738e7726bc', fname, destination=app_dir)
            filelist.append(fname)

        return_obj = {'success':True, 'filelist':filelist}

    except:

        return_obj = {'success': False}

    # ml = flopy.modflow.Modflow.load(modelname + '.nam', model_ws=app_dir, verbose=False,
    #                                 check=False, exe_name='pymake/examples/temp/mf2005')

    return JsonResponse(return_obj)
