function callAPI(method) {
    $.ajax({
        url: method,
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert(XMLHttpRequest.responseText)
        }
    });
}