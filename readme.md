# harvest-gplaces
Harvest Google Places to a Worksheet XLSX.

## Dependencies

1. Google Places Python Wrapper
```
# pip install https://github.com/slimkrazy/python-google-places
or
# pip install python-google-places
```

2. XLSX Writer
```
# pip install XlsxWriter
```

## Notes

```
## Check for next page ##
##if query_result.has_next_page_token:
##    query_result_next_page = google_places.text_search(
##            pagetoken=query_result.next_page_token)
##    print('next page')
##    print('---')
##    #_show_results()

   # Getting place photos

##    for photo in place.photos:
##        # 'maxheight' or 'maxwidth' is required
##        photo.get(maxheight=500, maxwidth=500)
##        # MIME-type, e.g. 'image/jpeg'
##        photo.mimetype
##        # Image URL
##        photo.url
##        # Original filename (optional)
##        photo.filename
##        # Raw image data
##        photo.data


# Are there any additional pages of results?



### Adding and deleting a place
##try:
##    added_place = google_places.add_place(name='Mom and Pop local store',
##            lat_lng={'lat': 51.501984, 'lng': -0.141792},
##            accuracy=100,
##            types=types.TYPE_HOME_GOODS_STORE,
##            language=lang.ENGLISH_GREAT_BRITAIN)
##    print(added_place.place_id) # The Google Places identifier - Important!
##    print(added_place.id)
##
##    # Delete the place that you've just added.
##    google_places.delete_place(added_place.place_id)
##except GooglePlacesError as error_detail:
##    # You've passed in parameter values that the Places API doesn't like..
##    print(error_detail)
```

## License

Distributed under MIT License. See `license.md` for more information.
