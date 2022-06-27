from flask import Flask, request, Response
from flask_restful import Api, Resource, reqparse
import json

## module created to clean data
from b_clean import cleanJson

## module created to validate data
from c_validate import validateJson

## utilised to check of file exists
from os.path import exists

## setup api
app = Flask(__name__)
api = Api(app)

## setup json data capture
data_put_args = reqparse.RequestParser()
data = {}

class transferJson(Resource):

    ## load file using schemaId provided by user, clean and return back to client
    def get(self, schemaId):
        try:
            path = (f'storage/{schemaId}')
            fileExists = exists(path)
            if fileExists:
                print(fileExists)
                f = open(path)
                storedData = cleanJson(json.load(f))         
                return storedData
            else:
                return "File does not exist"
        except:
            responseMessage = {
            "message": "Other error occured"
            }

        return responseMessage

    ## clean, validate, store json provided by user and return response message
    def put(self, schemaId):
        try:
            uploadData = request.form
            print(uploadData)
    
            path = (f'storage/{schemaId}.json')
            with open(path, 'w') as f:
                json.dump(uploadData, f)

            responseMessage = {
            "action": "uploadSchema",
            "id": schemaId,
            "status": "success"
            }

            statusCode = 201
        
        except:
            responseMessage = {
            "action": "uploadSchema",
            "id": schemaId,
            "status": "error",
            "message": "Invalid JSON"
            }
        
        return responseMessage, statusCode

api.add_resource(transferJson, "/schema/<string:schemaId>")

if __name__ == '__main__':
    app.run(debug=True)
