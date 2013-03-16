$(document).ready(function() {
    initAddForm();
});

function getFormAjax(form) {
    return jQuery.ajax({
        type: form.attr('method'),
        url: ApiUrlBuilder.fromFormAction(form),
        data: form.serialize(),
    });
}

function initAddForm() {
    var form = $('form.new-poll');

    // choices
    var choicesClass = form.find('.choices');
    choicesClass.find('select').change(function() {
        var choiceInputs= function() { return choicesClass.find('input'); };

        var countDiff = choiceInputs().size() - $(this).val();
        var iterator;
        if (countDiff > 0) {
            iterator = function() { choiceInputs().last().remove(); };
        }
        else if (countDiff < 0) {
            iterator = function() { choicesClass.append(choiceInputs().last()[0].outerHTML); };
        }
        _(Math.abs(countDiff)).times(iterator);
    });

    // form submit
    var submitButton = $('form.new-poll button[type=submit]');
    submitButton.click(function(event) {
        event.preventDefault();

        // feedback before perform ajax request
        submitButton.button('loading');

        // ajax
        getFormAjax(form)
            .done(function(pollId) {
                window.location.href = "/polls/detail/" + pollId;
            })
            .error(function(data) {
                submitButton.button('reset');

                submitButton.tooltip({
                    placement: 'bottom',
                    title: 'Failed to post it...'
                });
                submitButton.tooltip('show');
                
            });
    });
}

