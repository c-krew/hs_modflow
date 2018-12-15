function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function waiting_output() {
    $('#loading').html('').removeClass('alert')
    .removeClass('alert-success');

    var wait_text = "<strong>Loading...</strong><br>" +
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/static/hs_modflow/images/loading.gif'>";
    document.getElementById('loading').innerHTML = wait_text;
}

function run_model (){
    alert("run model")
}

function load_model (){
    var displayname = $("#model_select option:selected").attr("value")
    $("#displayname").text(displayname)
    waiting_output()

    $.ajax({
        url: '/apps/hs-modflow/load-resource/',
        type: 'POST',
        data: {'displayname' : displayname},
        success: function (response) {
            $("#prodTabs").empty()
            $("#tabcontents").empty()
            for (var i = 0; i < response['filelist'].length; i++) {
                filename = response['filelist'][i]
                // create the tab
                $('<li><a href="#tab'+filename+'" id="'+filename+' data-url="">'+filename+'</a></li>').appendTo('#prodTabs');

                // create the tab content
                $('<div class="tab-pane" id="tab'+filename+'"><h1>'+filename+'</h1></div>').appendTo('.tab-content');

            $('.nav-tabs a:first').tab('show');

            document.getElementById("inputTextToSave").style.display = "block";

            document.getElementById("loading").innerHTML = '';
            }
        }
    })
}

function enable_text_edit (){
   document.getElementById("inputTextToSave").readOnly=false;
}

function load_text_files (){
    var url = window.location.href;
    var filename = url.slice(42);
    $.ajax({
        url: '/apps/hs-modflow/load-text-file/',
        type: 'POST',
        data: {'filename' : filename},
        success: function (response) {

            document.getElementById("inputTextToSave").value = response['filetext'];

            document.getElementById("loading").innerHTML = '';

        }
    })
}

function save_text_files (){
    var displayname = $("#model_select option:selected").attr("value");
    var url = window.location.href;
    var filename = url.slice(42);
    var editedfiletext = document.getElementById("inputTextToSave").value

    $.ajax({
        url: '/apps/hs-modflow/save-text-file/',
        type: 'POST',
        data: {'filename' : filename, 'editedfiletext' : editedfiletext, 'displayname':displayname},
        success: function (response) {

            addSuccessMessage('File Saved Successfully', 'loading');

            hideOverwriteModal();

            document.getElementById("inputTextToSave").readOnly=true;
        }
    })
}

function save_new_entry (){
    var displayname = $("#model_select option:selected").attr("value");
    $("#displayname").text(displayname);
    var url = window.location.href;
    var filename = url.slice(42);
    var editedfiletext = document.getElementById("inputTextToSave").value;
//    var display_name = document.getElementById("new_display_name_input").value;
    var new_display_name = $("#new_display_name_input").val();

    $.ajax({
        url: '/apps/hs-modflow/save-new-entry/',
        type: 'POST',
        data: {'filename' : filename, 'editedfiletext' : editedfiletext, 'displayname':displayname, 'new_display_name':new_display_name},
        success: function (response) {

            addSuccessMessage('File Saved Successfully', 'loading');

            hideNewEntryModal();

            window.location.href = 'http://127.0.0.1:8000/apps/hs-modflow/';

            document.getElementById("inputTextToSave").readOnly=true;
        }
    })
}

function hideOverwriteModal () {
    $('#save-modal').modal('hide');
}

function hideNewEntryModal () {
    $('#new-entry-modal').modal('hide');
}


function addSuccessMessage(message, div_id) {
    var div_id_string = '#message';
    if (typeof div_id != 'undefined') {
        div_id_string = '#'+div_id;
    }
    $(div_id_string).html(
      '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span>' +
      '<span class="sr-only">Sucess:</span> ' + message
    ).removeClass('hidden')
    .removeClass('alert-danger')
    .removeClass('alert-info')
    .removeClass('alert-warning')
    .addClass('alert')
    .addClass('alert-success');
}

function show_save_modal (){
    $("#save-modal").modal('show');

}


$('input[type=radio][name=uploadtype]').change(function() {
    if (this.value == 'new') {
        $("#new-resource").removeClass("hidden");
    }
    else {
        $("#new-resource").addClass("hidden");
    }
});

$('input[type=radio][name=searchtype]').change(function() {
    if (this.value == 'creator') {
        $("#search_input").attr("placeholder", "email or username");
    } else if (this.value == 'user') {
        $("#search_input").attr("placeholder", "email or username");
    } else if (this.value == 'owner') {
        $("#search_input").attr("placeholder", "email or username");
    } else if (this.value == 'author') {
        $("#search_input").attr("placeholder", "email or username");
    } else if (this.value == 'group') {
        $("#search_input").attr("placeholder", "id or name");
    } else if (this.value == 'subject') {
        $("#search_input").attr("placeholder", "comma,separated,list,of,subjects");
    } else if (this.value == 'type') {
        $("#search_input").attr("placeholder", "resource type");
    } else if (this.value == 'full_text') {
        $("#search_input").attr("placeholder", "any text here");
    }
});

function search (){
    $('#search-results').modal('show');
    var searchtype = $('input[name=searchtype]:checked').val();
    var searchinput = $('#search_input').val();

    $.ajax({
        url: '/apps/hs-modflow/search/',
        type: 'POST',
        data: {'searchtype' : searchtype, 'searchinput': searchinput},
        success: function (response) {
            var resources = response['resources']

            var i;
            for (i = 0; i < resources.length; i++) {
              var markup = "<tr id='" + resources[i][4] + "'><td>" + resources[i][0] +
              "</td><td>" + resources[i][1] +
              "</td><td>" + resources[i][2] +
              "</td><td>" + resources[i][3] +
              "</td><td>" + resources[i][4] +
              "</td></tr>";
              $("#search-table tbody").append(markup);
            }

        }
    })
}

$("#search-button").on('click',search)

$(document).on("dblclick", "#search-table tr", function(e) {
    $("#resourceid_input").val(this.id);
    $('#search-results').modal('hide');
});

$(function(){

//    load_text_files();

    document.getElementById("inputTextToSave").style.display = "none";

    $('.nav-tabs').bind('click', function (e){
            $(this).tab('show');
            load_text_files();

    });

});
