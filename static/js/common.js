var API = {
    ROOT_URL: 'http://' + document.domain + ':8274'
};

var ApiUrlBuilder = {
    fromFormAction: function(form) {
        return API.ROOT_URL + form.attr('action');
    },
    chooseChoice: function(pollId) {
    	return _.string.sprintf("%s/polls/%s/choices", API.ROOT_URL, pollId);
    }
};