from googleplaces import GooglePlaces, types, lang
from hGplacesBase import *
from hGplacesVars import *
import json
from datetime import datetime
import xlsxwriter
from shutil import copyfile

## hMigrationPrep
## Prepare a new template copy for migration
## Returns migration filename
def hMigrationPrep():
    global HG_TEMPLATENAME, HG_MIGNAME_PREFIX, HG_MIGNAME_SUFFIX, HG_MIGNAME_EXT
    timedate = str(kv_ParseInt(str(datetime.now())))
    HG_MIGRATIONFILENAME = HG_MIGNAME_PREFIX + timedate + HG_MIGNAME_SUFFIX + HG_MIGNAME_EXT
    copyfile(HG_TEMPLATENAME, HG_MIGRATIONFILENAME)
    return HG_MIGRATIONFILENAME

#def hPlaceExport(Place):
#    if Place is object:
#        workbook = xlsxwriter.Workbook(

def _show_results(query_result):
    global HG_SRCH_RESULTS, HG_SRCH_TOTAL, HG_SRCH_PAGE, SPRS
    if query_result.has_attributions:
        print(query_result.html_attributions)
    for place in query_result.places:
        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        #print(place.details)# A dict matching the JSON response from Google.

        placedata = place.details
        if 'name' in placedata:
           print(placedata['name'])
        if 'geometry' in placedata:
            if 'location' in placedata['geometry']:
                if 'lat' in placedata['geometry']['location']:
                    print(placedata['geometry']['location']['lat'])
                if 'lng' in placedata['geometry']['location']:
                    print(placedata['geometry']['location']['lng'])
        if 'formatted_address' in placedata:
            print(placedata['formatted_address'])
        if 'international_phone_number' in placedata:
            print(placedata['international_phone_number'])
        if 'address_components' in placedata:
            print(placedata['address_components'])
        if 'opening_hours' in placedata:
            if 'periods' in placedata['opening_hours']:
                print(placedata['opening_hours']['periods'])
            if 'weekday_text' in placedata['opening_hours']:            
                print(placedata['opening_hours']['weekday_text'])
        if 'place_id' in placedata:
            print(placedata['place_id'])
        if 'rating' in placedata:
            print(placedata['rating'])
        if 'types' in placedata:
            print(placedata['types'])
        if 'utc_offset' in placedata:
            print(placedata['utc_offset'])
        if 'website' in placedata:
            print(placedata['website'])
        print('---')
##        except KeyError as e:
##            pass
##            print('Error(s) occurred during data parsing "%s"' % str(e))

        ## Check if theres a next page ##
    if query_result.has_next_page_token:
        query_result_next_page = google_places.text_search(
            pagetoken=query_result.next_page_token)
        HG_SRCH_TOTAL += kv_Parseint(printf(query_result))
        HG_SRCH_PAGE +=1
        print('next page, ' + str(HG_SRCH_PAGE) + '. processing ' + str(HG_SRCH_RESULTS))
        print('---')
        _show_results(query_result_next_page)
                      
## Show search results ##
def _show_results(query_result):
    global HG_SRCH_RESULTS, HG_SRCH_TOTAL, HG_SRCH_PAGE, SPRS
    if query_result.has_attributions:
        print(query_result.html_attributions)
    for place in query_result.places:
        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        #print(place.details)# A dict matching the JSON response from Google.

        placedata = place.details
        if 'name' in placedata:
           print(placedata['name'])
        if 'geometry' in placedata:
            if 'location' in placedata['geometry']:
                if 'lat' in placedata['geometry']['location']:
                    print(placedata['geometry']['location']['lat'])
                if 'lng' in placedata['geometry']['location']:
                    print(placedata['geometry']['location']['lng'])
        if 'formatted_address' in placedata:
            print(placedata['formatted_address'])
        if 'international_phone_number' in placedata:
            print(placedata['international_phone_number'])
        if 'address_components' in placedata:
            print(placedata['address_components'])
        if 'opening_hours' in placedata:
            if 'periods' in placedata['opening_hours']:
                print(placedata['opening_hours']['periods'])
            if 'weekday_text' in placedata['opening_hours']:            
                print(placedata['opening_hours']['weekday_text'])
        if 'place_id' in placedata:
            print(placedata['place_id'])
        if 'rating' in placedata:
            print(placedata['rating'])
        if 'types' in placedata:
            print(placedata['types'])
        if 'utc_offset' in placedata:
            print(placedata['utc_offset'])
        if 'website' in placedata:
            print(placedata['website'])
        print('---')
##        except KeyError as e:
##            pass
##            print('Error(s) occurred during data parsing "%s"' % str(e))

        ## Check if theres a next page ##
    if query_result.has_next_page_token:
        query_result_next_page = google_places.text_search(
            pagetoken=query_result.next_page_token)
        HG_SRCH_TOTAL += kv_Parseint(printf(query_result))
        HG_SRCH_PAGE +=1
        print('next page, ' + str(HG_SRCH_PAGE) + '. processing ' + str(HG_SRCH_RESULTS))
        print('---')
        _show_results(query_result_next_page)

## Google Places API Query builder ##
def _gapi_query_builder(query, location, radius, type):
    query_result = google_places.text_search(
        location=location, query=query,
        radius=radius, type=type)
    return query_result
                      
## Assign GAPI KEY
google_places = GooglePlaces(HG_GAPI_PLACES_KEY)

## Do search
SPRS = hSuppressor(KeyError)
search_results = _gapi_query_builder('', 'Paris, France', 50000, 'pharmacy')
_show_results(search_results)

## end statistics
print('Processed ' + str(HG_SRCH_TOTAL) + ' results through ' + str(HG_SRCH_PAGE) + ' pages')

print('Processed results: ' + str(HG_SRCH_TOTAL))
