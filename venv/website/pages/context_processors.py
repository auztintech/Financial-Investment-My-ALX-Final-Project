from website import settings

'''
let the following informations in settings to be accessible in all pages 
'''
def all_pages(request):
	return {
	'site_name':settings.SITE_NAME,
	'meta_keywords':settings.META_KEYWORDS,
	'meta_description':settings.META_DESCRIPTION,
	'tagline':settings.SITE_TAGLINE,
	'request':request,

	}
