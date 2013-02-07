def form():
    import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Name:', INPUT(_type='text', _name='name', requires=IS_NOT_EMPTY())),
        TR('Email:', INPUT(_type='text', _name='email', requires=IS_EMAIL())),
		TR('Poll Question:', TEXTAREA(_name='question', requires=IS_NOT_EMPTY())),
		TR('Answer #1:', INPUT(_type='text', _name='answer1', requires=IS_NOT_EMPTY())),
		TR('Answer #2:', INPUT(_type='text', _name='answer2', requires=IS_NOT_EMPTY())),
		TR('Answer #3:', INPUT(_type='text', _name='answer3')),
		TR('Answer #4:', INPUT(_type='text', _name='answer4')),
		TR('Answer #5:', INPUT(_type='text', _name='answer5')),
        TR('', INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'Your poll has been accepted'
    elif form.errors:
        response.flash = 'Please fill out the highlighted fields'
    else:
        response.flash = 'Please enter your poll information'
    return dict(form=form, vars=sj.dumps(form.vars))
