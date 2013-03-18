function vote() {
    var choicesSelectorCriteria = ":radio[name=choices]";
    var choices = $(choicesSelectorCriteria);

	// ajax request

	var choiceId = $(choicesSelectorCriteria + ":checked").val();
	var pollId = $(choices[0]).data("pid");

	var request = jQuery.ajax({
		type: 'PUT',
		url: ApiUrlBuilder.chooseChoice(pollId),
		data: 'cid=' + choiceId,
	});

	// feedback

	var currFeedback = $($(this).parent().find('.vote')[0]);

	var setFeedback = function(type, content) {
		var feedbacks = $('.vote');
		feedbacks.attr('class', 'vote btn ' + type);
		feedbacks.html('');
		feedbacks.html(content);
	};

	request.done(function() {
		setFeedback('btn-success', 'Success');
		$('#voteBtn').attr('onclick','noVote();');
	});

	request.error(function(xhr, textStatus, errorThrown) {
		setFeedback('btn-warning', 'Error')
		
		var voteBtn = $('#voteBtn');
		voteBtn.attr('data-content', "Please try voting again.");
		$('#voteBtn').popover('toggle');
	});
	
}

function noVote(){

	var voteBtn = $('#voteBtn');
	voteBtn.attr('data-content', "You've already voted.");
	$('#voteBtn').popover('toggle');
}