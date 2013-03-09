def index():
	return dict(message="Surveys");
  
def new():
import gluon.contrib.simplejson as sj

    form = FORM(TABLE(
        TR('Survey name:', INPUT(_type='text', _name='name',requires=	[IS_NOT_EMPTY(error_message='Enter a title for your survey data'),
		IS_LENGTH(maxsize=100, error_message='Please keep the heading under 100 characters')])),
        
        TR('Heading:', INPUT(_type='text', _name='heading',requires=	[IS_NOT_EMPTY(error_message='Enter a heading for your survey data'),
		IS_LENGTH(maxsize=100, error_message='Please keep the heading under 100 characters')])),
		
		TR('Introduction:',TEXTAREA(_type='text', _name='intro', 
			requires=	IS_EMPTY_OR(IS_LENGTH(maxsize=300, error_message='Please keep the introduction under 300 characters')))),

		TR('Group:', SELECT('All','Studets','Teachers', _name="group",
			requires=	IS_IN_SET(['All','Studets','Teachers']))),
			
		TR('Background Theme:', SELECT('Default','Red','Green', _name="backkground",
			requires=	IS_IN_SET(['Default','Red','Green']))),
			
		TR('Question text:', TEXTAREA(_name='question', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a question for your SURVEY'),
						IS_LENGTH(maxsize=250, error_message='Please keep the question under 100 characters')])),

        TR('choice A:',INPUT(_type='text', _name='choiceA', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a choice for your survey'),
						IS_LENGTH(maxsize=100, error_message='Please keep the choice under 100 characters')])),
        
        TR('choice B:',INPUT(_type='text',  _name='choiceB', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a choice for your survey'),
						IS_LENGTH(maxsize=100, error_message='Please keep the choice under 100 characters')])),
        
        TR('choice C:',INPUT(_type='text',  _name='choiceC', 
			requires=	[IS_NOT_EMPTY(error_message='Enter a choice for your survey'),
						IS_LENGTH(maxsize=100, error_message='Please keep the choice under 100 characters')])),
        TR('choice D:',INPUT(_type='text',  _name='choiceD', 
        
			requires=	[IS_NOT_EMPTY(error_message='Enter a choice for your survey'),
						IS_LENGTH(maxsize=100, error_message='Please keep the choice under 100 characters')])),
        
        
        TR('',INPUT(_type='submit', _value='Submit'))
       
    ))
    if form.process().accepted:
        response.flash = 'Form accepted'
    elif form.errors:
        response.flash = 'Missing required information '
    else:
        response.flash = 'Enter survey data'
    return dict(form=form, vars=sj.dumps(form.vars))
