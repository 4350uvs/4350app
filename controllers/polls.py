def index():
    return dict(jsonPolls = api.getJsonDict('/polls'))

def new():
    import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Title:', INPUT(_type='text', _name='title', requires=IS_LENGTH(100, 1))),
        TR('Description:', TEXTAREA(_type='text', _name='description', requires=IS_EMPTY_OR(IS_LENGTH(250, 1)))),
		TR('Group:', SELECT('All','Studets','Teachers', _name="group",requires=IS_IN_SET(['All','Studets','Teachers']))),
		TR('Poll Question:', TEXTAREA(_name='question', requires=IS_LENGTH(250, 1))),
		TR('Answer #1:', INPUT(_type='text', _name='answer1', requires=IS_LENGTH(100, 1))),
		TR('Answer #2:', INPUT(_type='text', _name='answer2', requires=IS_LENGTH(100, 1))),
		TR('Answer #3:', INPUT(_type='text', _name='answer3', requires=IS_EMPTY_OR(IS_LENGTH(100, 1)))),
		TR('Answer #4:', INPUT(_type='text', _name='answer4', requires=IS_EMPTY_OR(IS_LENGTH(100, 1)))),
		TR('Answer #5:', INPUT(_type='text', _name='answer5', requires=IS_EMPTY_OR(IS_LENGTH(100, 1)))),
        TR('', INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'Your poll has been accepted'
    elif form.errors:
        response.flash = 'Please fill out the highlighted fields'
    else:
        response.flash = 'Please enter your poll information'
    return dict(form=form, vars=sj.dumps(form.vars))
