from hs_restclient import HydroShare
import flopy


def run_modflow():

    hs = HydroShare()

    app_dir = '/home/ckrewson/tethysdev/hs_modflow/tethysapp/hs_modflow/workspaces/app_workspace'
    modelname = 'etsdrt'

    resourcelist = hs.getResourceFileList('21c38e32c8f34de1a3073e738e7726bc')
    for resource in resourcelist:
        url = resource['url'].split("/")
        fname = url[-1]
        hs.getResourceFile('21c38e32c8f34de1a3073e738e7726bc', fname, destination=app_dir)

    ml = flopy.modflow.Modflow.load(modelname + '.nam', model_ws=app_dir, verbose=False,
                                    check=False, exe_name='pymake/examples/temp/mf2005')

    return
