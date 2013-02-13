def index():
    return dict(jsonPolls = api.getJsonDict('/polls'))

def new():
    import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Title:', INPUT(_type='text', _name='title', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a title for your poll'),
						IS_LENGTH(maxsize=100, error_message='Please keep the title under 100 characters')])),
						
        TR('Description:', TEXTAREA(_type='text', _name='description', 
			requires=	IS_EMPTY_OR(IS_LENGTH(maxsize=250, error_message='Please keep the description under 250 characters')))),
			
		TR('Group:', SELECT('All','Studets','Teachers', _name="group",
			requires=	IS_IN_SET(['All','Studets','Teachers']))),
			
		TR('Poll Question:', TEXTAREA(_name='question', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a question for your poll'),
						IS_LENGTH(maxsize=250, error_message='Please keep the question under 100 characters')])),
						
		TR('Answer #1:', INPUT(_type='text', _name='answer1', 
			requires=	[IS_NOT_EMPTY(error_message='Enter an answer for your poll'),
						IS_LENGTH(maxsize=100, error_message='Please keep the answer under 100 characters')])),
						
		TR('Answer #2:', INPUT(_type='text', _name='answer2', 
			requires=	[IS_NOT_EMPTY(error_message='Enter another answer for your poll'),
						IS_LENGTH(maxsize=100, error_message='Please keep the answer under 100 characters')])),
						
		TR('Answer #3:', INPUT(_type='text', _name='answer3', 
			requires=	IS_EMPTY_OR(IS_LENGTH(maxsize=100, error_message='Please keep the answer under 100 characters')))),
			
		TR('Answer #4:', INPUT(_type='text', _name='answer4', 
			requires=	IS_EMPTY_OR(IS_LENGTH(maxsize=100, error_message='Please keep the answer under 100 characters')))),
			
		TR('Answer #5:', INPUT(_type='text', _name='answer5', 
			requires=	IS_EMPTY_OR(IS_LENGTH(maxsize=100, error_message='Please keep the answer under 100 characters')))),
			
        TR('', INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'Your poll has been accepted'
    elif form.errors:
        response.flash = 'Please fill out the highlighted fields'
    else:
        response.flash = 'Please enter your poll information'
    return dict(form=form, vars=sj.dumps(form.vars))
