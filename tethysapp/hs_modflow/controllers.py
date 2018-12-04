from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, SelectInput, TextInput
from .model import save_hs_to_favorites, get_all_models

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='Save to Hydroshare',
        name='save-button',
        attributes={
            'data-toggle':'modal',
            'data-target':'#upload-modal',
            'data-placement':'top',
            'title':'Save',
        }
    )

    upload_button = Button(
        display_text='Upload from Hydroshare',
        name='edit-button',
        attributes={
            'data-toggle':'modal',
            'data-target':'#upload-modal',
            'data-placement': 'top',
            'title':'Upload'
        }
    )

    run_button = Button(
        display_text='Run Model',
        name='run-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Run Model',
            'onclick':'run_model ()'
        }
    )

    load_button = Button(
        display_text='Load Model',
        name='load-button',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'title': 'Load Model',
            'onclick': 'load_model ()'
        }
    )

    modellist = get_all_models()

    model_select = SelectInput(display_text='Select Favorite Models',
                                name='model_select',
                                multiple=False,
                                options=modellist,
                                select2_options={'placeholder': 'Select a number',
                                                 'allowClear': False})

    modeltype_select = SelectInput(display_text='Select Model Type',
                               name='modeltype_select',
                               multiple=False,
                               options=[('Modflow 2005', 'mf2005'), ('Modflow-NWT', 'mfnwt')],
                               select2_options={'placeholder': 'Select a Model Type',
                                                'allowClear': False})

    resourceid_input = TextInput(display_text='Resource ID',
                           name='resourceid_input',
                           placeholder='')

    resourcedisplay_input = TextInput(display_text='Resource Display Name for Favorite Select',
                                 name='resourcedisplay_input',
                                 placeholder='')

    # Default Values
    resourceid = ''
    displayname = ''
    modeltype = ''

    # Errors
    resourceid_error = ''
    displayname_error = ''
    modeltype_error = ''

    # Handle form submission
    if request.POST and 'upload-button' in request.POST:
        # Get values
        has_errors = False
        resourceid = request.POST.get('resourceid_input', None)
        displayname = request.POST.get('resourcedisplay_input', None)
        modeltype = request.POST.get('modeltype_select', None)

        # Validate
        if not resourceid:
            has_errors = True
            resourceid_error = 'Name is required.'

        if not displayname:
            has_errors = True
            displayname_error = 'Owner is required.'

        if not modeltype:
            has_errors = True
            modeltype_error = 'River is required.'

        if not has_errors:
            save_hs_to_favorites(resourceid,displayname,modeltype)
            return redirect(reverse('hs_modflow:home'))

        messages.error(request, "Please fix errors.")

    context = {
        'save_button': save_button,
        'upload_button': upload_button,
        'load_button': load_button,
        'run_button': run_button,
        'model_select': model_select,
        'modeltype_select':modeltype_select,
        'resourceid_input':resourceid_input,
        'resourcedisplay_input':resourcedisplay_input
    }

    return render(request, 'hs_modflow/home.html', context)