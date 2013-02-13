def index():
    return dict(jsonPolls = api.getJsonDict('/polls'))

def new():
    import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Title:', INPUT(_type='text', _name='title', requires=IS_LENGTH(100, 1))),
        TR('Description:', TEXTAREA(_type='text', _name='description', requires=IS_EMPTY_OR(IS_LENGTH(250, 1)))),
		TR('Password:', INPUT(_type='text', _name='password', requires=IS_EMPTY_OR(IS_LENGTH(12, 6)))),
		TR('Group', SELECT('All','Studets','Teachers', _name="group",requires=IS_IN_SET(['All','Studets','Teachers']))),
		TR('Start Date:', INPUT(_type='date', _name='start_date')),
		TR('Start Time:', INPUT(_type='time', _name='start_time')),
		TR('End Date:', INPUT(_type='date', _name='end_date')),
		TR('End Time:', INPUT(_type='time', _name='end_time')),
        TR('', INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'Your lecture has been accepted'
    elif form.errors:
        response.flash = 'Please fill out the highlighted fields'
    else:
        response.flash = 'Please enter your lecture information'
    return dict(form=form, vars=sj.dumps(form.vars))
