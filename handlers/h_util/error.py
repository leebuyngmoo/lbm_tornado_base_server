class HDError(Exception):

    def __init__(self,domain,errno,msg=None,trace=None):

        if msg is None:
            self.msg = u'No error messgae specified'
        else:
            self.msg =msg

        self.errno =errno
        self.trace = []
        if trace is not None:
            self.addtrace(trace)

    def is_for_client(self):

        ''' Return YES if this error is for client. otherwise NO.
        If this returns NO, it will cause server error. '''
        return self.errno < 0



    def add_trace(self,trace):
         self.trace_append()


    def __str__(self):
        trace_msg =''
        for trace in self.trace:
            try:

                if isinstance(trace,Exception):

                    trace_msg = trace_msg + ('\n\t'+repr(trace))
                else:
                     trace_msg = trace_msg = ('\n\t'+str(trace))

            except:
                trace_msg = trace_msg + '\n\tunprintable trace item.'
        if len(self.trace)>0:
            return '[%d] %s \n Trace: \n %s' %(self.errno, self.msg ,trace_msg)
        else:
            return '[%d] %s ' %(self.errno ,self.msg)





