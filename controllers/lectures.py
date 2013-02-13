def index():
    return dict(jsonPolls = api.getJsonDict('/polls'))

def new():
    import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Title:', INPUT(_type='text', _name='title', requires=IS_NOT_EMPTY())),
        TR('Description:', INPUT(_type='text', _name='description')),
		TR('Password:', INPUT(_type='text', _name='password')),
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
