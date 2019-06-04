from hGplacesVars import *

## Harvest Gplaces file includes
##
## hSuppressor 	- Error suppressor for functions
## hPrintf 		- Print function for result outputs
## hParseint	- Integer parser
## hGplace		- GPlace structure
## hGplacePhoto	- GPlace photo structure

##__all__ = ['hSuppressor', 'hPrintf', 'hParseint', 'hGplace', 'hGplacePhoto']
## Error suppressor ##
## Handles specified error in execution and suppresses it
class hSuppressor:
    def __init__(self, exception_type):
        self._exception_type = exception_type

    def __call__(self, expression):
        try:
            exec(expression)
        except self._exception_type as e:
            print('Suppressor: suppressed exception %s with content "%s"' % (type(self._exception_type), e))
			
## hGplace - Structure for a Place object ##
## name			- Place name
## location.lat	- Latitude
## location.lng - Longitude
## address		- Formatted address
## phonenumber 	- International phone number
## json.address - JSON address components
## json.openinghours - JSON opening hours decimal
## json.openinghours.text - JSON openinghours in text
## gplaceid		- Google place id
## rating		- Google rating in decimal
## json.types	- JSON establishment types
## utcoffset	- UTC offset
## website		- Website
class hGplace:
	def __init__(self):
		self.name = None
		self.location.lat = None
		self.location.lng = None
		self.address = None
		self.phonenumber = None
		self.json.address = None
		self.json.openinghours = None
		self.json.openinghours.text = None
		self.gplaceid = None
		self.rating = None
		self.json.types = None
		self.utcoffset = None
		self.website = None

## hGplacePhoto - Structure for Place Photo object ##
## filename 	- Photo filename
## url 			- URL to place photo
## mime			- Photo mimetype
## data 		- Raw encoded photo data		
class hGplacePhoto:
	def __init__(self):
		self.filename = None
		self.url = None
		self.mime = None
		self.data = None			

## Integer parser ##
## Tries to parse an Integer from a var that has a string of chars
def hParseInt(string):
    return int(''.join([x for x in string if x.isdigit()]))
	
## Print function ##
## Prints the result of function in a str to be used elsewhere
def hPrintf(*args):
    together = ''.join(map(str, args))    # avoid the arg is not str
    print(together)
    return together
	
