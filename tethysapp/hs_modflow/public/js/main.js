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
    var wait_text = "<strong>Loading...</strong><br>" +
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/static/hs_modflow/images/loading.gif'>";
    document.getElementById('loading').innerHTML = wait_text;
}

function run_model (){
    alert("run model")
}

function load_page() {
     document.getElementById("content").innerHTML='<object type="text/html" data="etsdrt.html" ></object>';
}

function load_model (){
    var resourceid = $("#model_select option:selected").attr("value")
    $("#resourceid").text(resourceid)
    waiting_output()

    $.ajax({
        url: '/apps/hs-modflow/load-resource/',
        type: 'POST',
        data: {'resourceid' : resourceid},
        success: function (response) {
            $("#prodTabs").empty()
            $("#tabcontents").empty()
            for (var i = 0; i < response['filelist'].length; i++) {
                filename = response['filelist'][i]
                // create the tab
                $('<li><a href="#tab'+filename+'" id="'+filename+' data-url="">'+filename+'</a></li>').appendTo('#prodTabs');

                // create the tab content
                $('<div class="tab-pane" id="tab'+filename+'"><h1>'+filename+'</h1></div>').appendTo('.tab-content');

            document.getElementById("loading").innerHTML = '';
            }
        }
    })
}
