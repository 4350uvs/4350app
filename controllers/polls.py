def index():
	return dict(jsonPolls = api.getJsonDict('polls'))

def new():
	return dict()

def detail():
	if len(request.args) == 1 and request.args[0].isdigit():
		pollJson = None
		try:
			pollJson = api.getJsonDict('polls/' + request.args[0])
		except:
			raise HTTP(404)

		poll = pollJson['poll']
		
		# check if the poll is newly created
		poll["isNewlyCreated"] = False
		if ( request.wsgi.environ.has_key("HTTP_REFERER") ):
			http_refer = request.wsgi.environ['HTTP_REFERER']
			if 'polls/new' in http_refer:
				poll["isNewlyCreated"] = True
		
		# calculate percentage stuff for each poll choice
		poll["totalVotes"] = 0
		 # get total votes
		for choice in poll["choices"]:
			poll["totalVotes"] += choice["chosenTimes"]

		if poll["totalVotes"] is not 0:
			 # calculate percentage
			for choice in poll["choices"]:
				choice["chosenPercentage"] = \
					int(float(choice["chosenTimes"]) / float(poll["totalVotes"]) * 100)

		return dict(poll = poll)
	else:
		raise HTTP(404)