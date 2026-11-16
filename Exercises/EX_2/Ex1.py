import cherrypy
class exercise1(object):
    exposed = True
    def GET(self,*uri,**params):
        output = ""
        if len(uri)!=0:
            reversedURL = uri[0][::-1]
            output += reversedURL
        return output
if __name__ == "__main__":
    conf = {
        '/':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    webService = exercise1()
    cherrypy.tree.mount(webService,'/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
"""
Why we need [0] to get the stringBecause uri is a tuple, you 
cannot apply string operations (like character reversing [::-1])
directly to the tuple itself. You have to extract the actual text 
string out of the tuple first.uri[0] grabs the first element 
inside that tuple, which is the string "friday".Once you have 
the string "friday", you can apply the reversal slice to it: 
uri[0][::-1] turns "friday" into "yadirf".What if there are 
multiple path parts?If someone visits a longer URL like 
http://localhost:8080/friday/hello, the tuple becomes:
$$\text{uri} = (\text{'friday'}, \text{'hello'})$$uri[0] would be 
"friday"uri[1] would be "hello"Since Exercise 1 only asks you to 
take the URI and return it reversed, targeting uri[0] grabs that 
first word so you can reverse its characters.
"""
