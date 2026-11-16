import cherrypy
import json
class exercise2(object):
    exposed = True
    def PUT(self, *uri, **params):
        #1. Read the raw data sent in the body of the PUT request
        body_data = cherrypy.request.body.read()
        #2. Convert the raw JSON body into a Python dictionary
        data_dict = json.loads(body_data)
        #3. Create a new dictionary to hold the reversed string values
        reversed_dict = {}
        for key, value in data_dict.items():
            reversed_dict[key] = value[::-1]
        #4. Tell the browser/client that the response is JSON data
        cherrypy.response.headers['Content-Type'] = 'application/json'
        #5. Convert the dictionary back to a JSON string and return it 
        return json.dumps(reversed_dict).encode('utf-8')
if __name__ == "__main__":
        conf = {
            '/':{
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.sessions.on':True
            }
        }
        webService = exercise2()
        cherrypy.tree.mount(webService,'/', conf)
        cherrypy.engine.start()
        cherrypy.engine.block()
    