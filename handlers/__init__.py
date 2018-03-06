# -*- coding: utf-8 -*-
'''
Created on 2016. 5. 25.

@author: Sunhong Kim
'''

import tornado.web
import functools, json

from tornado_cors import CorsMixin # cors
from handlers.h_util.error import HDError
# from models.session import HDSession
# from models.user import HDUser

def authenticated_api(method):
    ''' Decorate methods with this to require that the user be logged in.
    Not like tornado.web.authenticated, this method decorated API methods.
    This will not redirect user to login url when not authenticated.

    NOTE: If you use authenticated_api decorator with asynchronous and gen.coroutine,
        should follow writing sequence like below.

        @tornado.web.asynchronous
        @authenticated_api
        @tornado.gen.coroutine

        If you did not follow like this, server will not response and block ioLoop. '''

    @functools.wraps(method)
    @tornado.gen.coroutine
    def wrapper(self, *args, **kargs):
        yield self.get_current_user()
        if self.current_user is None:
            raise tornado.web.HTTPError(403)
        yield method(self, *args, **kargs)
    return wrapper

class CommonHandler(CorsMixin, tornado.web.RequestHandler):
    ''' Base requestHandler on our service '''

    ERR_MISSING_PARAM			= -300
    ERR_INVALID_PARAM			= -301

    # Value for the Access-Control-Allow-Origin header.
    # Default: None (no header).
    CORS_ORIGIN = '*'

    # Value for the Access-Control-Allow-Headers header.
    # Default: None (no header).
    CORS_HEADERS = 'Content-Type'

    # Value for the Access-Control-Allow-Methods header.
    # Default: Methods defined in handler class.
    # None means no header.
    CORS_METHODS = '*'

    # Value for the Access-Control-Allow-Credentials header.
    # Default: None (no header).
    # None means no header.
    CORS_CREDENTIALS = True

    # Value for the Access-Control-Max-Age header.
    # Default: 86400.
    # None means no header.
    CORS_MAX_AGE = 21600

    # Value for the Access-Control-Expose-Headers header.
    # Default: None
    CORS_EXPOSE_HEADERS = 'Location, X-WP-TotalPages'

    def __init__(self, application, request):
        super(CommonHandler, self).__init__(application, request)
        self.current_user = None
        self.current_session = None


    ''' Helper functions '''
    def finish_and_return(self, rc=0, result=None):
        ''' Write a structured response to the client.

        @param rc:		Return code. 0 means success.
        @param result:	Any object that can be converted to JSON.
                    This object will be returned to the client as a result. '''
        # print "result == " ,result;

        res = {'rc':rc}
        if result is not None:
            res['result'] = result

        self.write(json.dumps(res))
        self.finish()

    def get_params(self, plist):
        ''' Try to get a list of params in plist. Each list consists of tuple like the following.

        (param_name, required, default_value)

        If any of the required parameter is missing, this will raise Exception.
        If successful, this will return a dict containing each value for requested parameters. '''

        res = {}
        for tple in plist:
            if len(tple) == 3:
                print ("3")

                (pn, req, dv) = tple
                fn = None
            else:
                (pn, req, dv, fn) = tple

            if pn in self.request.arguments:
                res[pn] = int(self.request.arguments[pn][0]);
            elif req:

                raise HDError(domain="Handler", errno = CommonHandler.ERR_MISSING_PARAM,
                              msg = "%s parameter is required." % pn)
            else:
                res[pn] = dv
            if fn is not None and res[pn] is not None:
                try:
                    res[pn] = fn(res[pn])
                except:
                    raise HDError(domain="Handler", errno=CommonHandler.ERR_INVALID_PARAM,
                                  msg="%s parameter is invalid." % pn)
        return res

    ''' Handle exceptions '''
    def _handle_request_exception(self, exception):
        ''' Handle exceptions and return according to the exception. (or raise exception) '''
        if isinstance(exception, HDError) and exception.is_for_client():
            return self.finish_and_return(rc=exception.errno, result=exception.msg)

        super(CommonHandler, self)._handle_request_exception(exception)
