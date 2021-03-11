import requests
import json
import os
import dotenv

'''
A Simple handler to make connections to the Connectwise REST API. User must provide a valid client ID,
endpoint URL and a valid API key. all can be obtained via your Connectwise account.

Object includes handles for GET, POST, PUT, PATCH and DELETE requests. Data handed to functions is in
JSON format which is a series of key, value pairs. the same as a python dictionary.

results are handed back in a similar way. single results can be broken down in a single for loop,
multiple results can be broken down in a nested for loop.

Credentials should be stored in a file called .env which is stored in the project folder. 

.env format:

CLIENT_ID = <Your Connectwise client ID>
API_KEY = <Your Connectwise API key>
URL = <Your Connectwise API endpoint>

For further information on endpoints and how to get your credentials via your connectwise account
please view developer.connectwise.com
'''


# Load environment variables
dotenv.load_dotenv()

# Get enviroment variables
cwUrl = os.getenv('URL')
client_id = os.getenv('CLIENT_ID')
api_key = api = os.getenv('API_KEY')


class ConnectWizer():
    '''
    API caller, makes basic GET, POST, PATCH, PUT and DELETE requests.
    Messages that require a context should be handed JSON objects

    Author: Patrick Ward.
    Company: Equate Group ltd

    Version 2.1

    Additions to this code are very much welcome.
    '''

    # Constructor for Connectwizer Object
    def __init__(self, url, client_id, api_key):
        # Constructs your callers authentication and URL attributes
        self.url = url
        self.client_id = client_id
        self.api_key = api_key

        # Builds your call headers
        self.cWHeaders = {"Authorization": "Basic " + self.api_key,
                          'clientId': self.client_id,
                          "Content-Type": "application/json"}
    # Getter Methods.
    def get_url(self):
        return self.url

    def get_client(self):
        return self.client_id

    def get_api(self):
        return self.api_key

    def get_headers(self):
        return self.cWHeaders

    def make_request(self, r):
        try:
            # request has been made
            r.raise_for_status()
        except:
            print(r.text)
            raise
        returned_data = r.json()
        return returned_data

    # Make get request message
    def make_get_request(self, slug):
        '''
        Makes a GET request to the endpoint provided in the slug param.
        :param slug: A string which will be added to the end of your URL to provide your endpoint
        eg/ http://yourconnectwiseapiurl/<slug>
        :return: A Json object ( nested for multiple results )
        '''
        cwHeaders = self.get_headers()
        r = requests.get(cwUrl + slug, headers=cwHeaders)
        return self.make_request(r)


    def make_post_request(self, slug, context):
        '''
        Makes a POST request to the endpoint provided in the slug param
        Context must be provided in the standard JSON object format.

        :param slug: slug: A string which will be added to the end of your URL to provide your endpoint
        eg/ http://yourconnectwiseapiurl/<slug>

        :param context: Json object giving Key Value pairs, for information on what values are required
        for which endpoint go to developer.connectwise.com

        :return: A Json object ( nested for multiple results )
        '''
        context = json.dumps(context)
        cwHeaders = self.get_headers()
        r = requests.post(cwUrl + slug, headers=cwHeaders, data=context)
        return self.make_request(r)


    def make_put_request(self, slug, context):
        '''
        Makes a PUT request to the endpoint provided in the slug param
        Context must be provided in a JSON Array object format.

        :param slug: slug: A string which will be added to the end of your URL to provide your endpoint
        eg/ http://yourconnectwiseapiurl/<slug>

        :param context: context: Json Array object consisting on an Array of Key Value pairs,
        for information on what values are required for which endpoint go to developer.connectwise.com

        :return: A Json object ( nested for multiple results )

        '''
        context = json.dumps(context)
        cwHeaders = self.get_headers()
        r = requests.put(cwUrl + slug, headers=cwHeaders, data=context)
        return self.make_request(r)


    def make_patch_request(self, slug, context):
        '''
        Makes a PATCH request to the endpoint provided in the slug param
        Context must be provided in a JSON Array object format.

        :param slug: slug: A string which will be added to the end of your URL to provide your endpoint
        eg/ http://yourconnectwiseapiurl/<slug>

        :param context: context: Json Array object consisting on an Array of Key Value pairs,
        for information on what values are required for which endpoint go to developer.connectwise.com

        :return: A Json object ( nested for multiple results )

        '''
        context = json.dumps(context)
        cwHeaders = self.get_headers()
        r = requests.patch(cwUrl + slug, headers=cwHeaders, data=context)
        return self.make_request(r)

    def make_delete_request(self, slug):
        '''
        Makes a DELETE request to the endpoint provided in the slug param

        :param slug: slug: A string which will be added to the end of your URL to provide your endpoint
        eg/ http://yourconnectwiseapiurl/<slug>

        for information on what values are required for which endpoint go to developer.connectwise.com

        :return: NONE
        '''
        cwHeaders = self.get_headers()
        # slug = self.get_slug(slug)
        r = requests.delete(cwUrl + slug, headers=cwHeaders)
        try:
            # request has been made
            r.raise_for_status()
        except:
            print(r.text)
            raise
