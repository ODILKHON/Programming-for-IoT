import cherrypy
#Defines a Python class named HelloWorld which will act as your web service.
class HelloWorld(object):
    #Tells CherryPy that this class and its methods are allowed to be accessed by web requests from users.
    exposed = True
    #Defines a function that automatically handles incoming HTTP GET requests. It accepts extra URL path values (*uri) and any query parameters (**params).
    def GET(self,*uri, **params):
        #Standard output
        output = "Hello World!" 
        #Check the uri in the requests
        #<br> is just used to append the content in a new line
        #(<br> is the \n for HTML)
        if len(uri)!=0:
            #This line adds an HTML line break (<br>) and appends the URI parts to your output message.
            output += '<br>uri: '+','.join(uri)
        #Check the parameters in the request
        if params!={}:
            #Checks if any parameters (like query strings) were sent along with the request.
            output += '<br>params: '+ str(params)
        return output
if __name__ == "__main__":
    #Standard configuration to serve the url "localhost: 8080"
    #Starts a configuration dictionary that tells CherryPy how to handle routing and features for specific URL paths.
    conf = {
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    webService = HelloWorld()
    cherrypy.tree.mount(webService,'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()

