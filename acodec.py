# acodec.py
import encodings, codecs

# Our StreamReader
class aStreamReader(codecs.StreamReader):
    def outputFromInput(self, input):
        output = input
        return output

    def readline(self, size = None, keepends = True):
        if getattr(self, "pysrc", None) == None:          
            input = self.stream.read().decode("utf8")
            output = self.outputFromInput(input)
            self.pysrc = output.splitlines()
        return u'%s\n' % self.pysrc.pop(0) if self.pysrc else u''
        
def search_function(s):
    if s != "acodec": 
        return None
    u8 = encodings.search_function("utf8")
    return codecs.CodecInfo( name = 'acodec', 
                             encode = u8.encode,
                             decode = u8.decode,
                             incrementalencoder = u8.incrementalencoder,
                             incrementaldecoder = u8.incrementaldecoder,
                             streamreader = aStreamReader,        # acodec StreamReader
                             streamwriter = u8.streamwriter)

codecs.register(search_function)  # register our new codec search function

