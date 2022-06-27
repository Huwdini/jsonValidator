# jsonValidator
## Simple RESTful json validator api 

Tested using: Python 3.9.4

## Quick Start Guide:

pip INSTALL flask, pip INSTALL jsonschema

## Start api which will listed out of http requests
python a_main.py

## Test api, utilise this module to test GET and PUT requests
python d_test.py

### High level architecture ###

a_main.py has been created to listen for http request, currently GET and PUT requests are handled.

GET request - the directory titled /storage will be searched to locate the schemaId provided.
if a json file name matches the shemaId provided by the client, the data included will be cleaned are returned to the client.

PUT request - json data provided in the HTTP request will be cleaned, validated and saved to directory /storage.
a response will be provided to the client to determin upload status.

b_clean.py is utilised to clean json data by looping through the nested key values, and removing none/nulls

c_validate.py is utlised to validate client json data with json schema.

d_test.py has been created to send http requests, currently testing GET and PUT requests.

TODO: 
Change PUT to POST requests to satisfy requirements brief accurately.

#Create /validate/SCHEMAID endpoint

Error handling



