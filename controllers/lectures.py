def index():
    return dict(jsonPolls = api.getJsonDict('/polls'))

def new():
    import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Title:', INPUT(_type='text', _name='title', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a title for your lecture'),
						IS_LENGTH(maxsize=100, error_message='Please keep the title under 100 characters')])),
						
        TR('Description:', TEXTAREA(_type='text', _name='description', 
			requires=	IS_EMPTY_OR(IS_LENGTH(maxsize=250, error_message='Please keep the description under 250 characters')))),
			
		TR('Password:', INPUT(_type='text', _name='password', 
			requires=	IS_EMPTY_OR(IS_LENGTH(12, 6, error_message='Password must be 6 to 12 characters')))),
			
		TR('Group:', SELECT('All','Studets','Teachers', _name="group",
			requires=	IS_IN_SET(['All','Studets','Teachers']))),
			
		TR('Start Date:', INPUT(_type='date', _name='start_date', 
			requires=	IS_NOT_EMPTY(error_message='Enter a start date for your lecture'))),
			
		TR('Start Time:', INPUT(_type='time', _name='start_time', 
			requires=	IS_NOT_EMPTY(error_message='Enter a start time for your lecture'))),
			
		TR('End Date:', INPUT(_type='date', _name='end_date', 
			requires=	IS_NOT_EMPTY(error_message='Enter an end date for your lecture'))),
			
		TR('End Time:', INPUT(_type='time', _name='end_time', 
			requires=	IS_NOT_EMPTY(error_message='Enter an end time for your lecture'))),
			
        TR('', INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'Your lecture has been accepted'
    elif form.errors:
        response.flash = 'Please fill out the highlighted fields'
    else:
        response.flash = 'Please enter your lecture information'
    return dict(form=form, vars=sj.dumps(form.vars))
