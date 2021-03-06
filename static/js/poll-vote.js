$(document).ready(function() {
    initVoteChoices();
});

function initVoteChoices() {
    var choicesSelectorCriteria = ":radio[name=choices]";
    var choices = $(choicesSelectorCriteria);
    
    choices.change(function(event) {
        event.preventDefault();

        // ajax request

        var choiceId = $(choicesSelectorCriteria + ":checked").val();
        var pollId = $(choices[0]).data("pid");

        var request = jQuery.ajax({
            type: 'PUT',
            url: ApiUrlBuilder.chooseChoice(pollId),
            data: 'cid=' + choiceId,
        });

        // feedback

        var currFeedback = $($(this).parent().find('.vote-feedback')[0]);

        var setFeedback = function(type, content) {
            var feedbacks = $('.vote-feedback');
            feedbacks.attr('class', 'vote-feedback label');
            feedbacks.html('');

            currFeedback.addClass('label-' + type);
            currFeedback.html(content);
            
            if (type == 'success') {
            	choices.attr('disabled', 'disabled');
            }
        };

        request.done(function() {
            setFeedback('success', 'Success');
        });

        request.error(function(xhr, textStatus, errorThrown) {
            setFeedback('warning', 'Error')
        });
    });
}