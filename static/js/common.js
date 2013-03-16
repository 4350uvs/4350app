var API = {
    ROOT_URL: 'http://' + document.domain + ':8274'
};

var ApiUrlBuilder = {
    fromFormAction: function(form) {
        return API.ROOT_URL + form.attr('action');
    }
};