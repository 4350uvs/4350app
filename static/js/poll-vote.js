$(document).ready(function() {
    initVoteChoices();
});

function initVoteChoices() {
    var choicesSelectorCriteria = ":radio[name=choices]";
    var choices = $(choicesSelectorCriteria);
    
    choices.change(function(event) {
    	event.preventDefault();
    	
        var choiceId = $(choicesSelectorCriteria + ":checked").val();
        var pollId = $(choices[0]).data("pid");

        jQuery.ajax({
            type: 'PUT',
			url: ApiUrlBuilder.chooseChoice(pollId),
			data: 'cid=' + choiceId,
		})
		.done(function() {
			alert("done");
		})
		.error(function(xhr, textStatus, errorThrown) {
			alert("error: " + textStatus + " " + errorThrown)
		});
    });
}