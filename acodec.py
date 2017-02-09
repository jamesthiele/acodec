import codecs, cStringIO, encodings

class NullCodec(codecs.StreamReader):
    def translate(self, input):
        output = input
        return output

    def readline(self, size = None, keepends = True):
        if getattr(self, "pysrc", None) == None:          
            input = self.stream.read().decode("utf8")
            output = self.translate(input)
            self.pysrc = output.splitlines()
        return u'%s\n' % self.pysrc.pop(0) if self.pysrc else u''
        
def search_function(s):
    if s != "acodec": 
        return None
    utf8 = encodings.search_function("utf8")
    return codecs.CodecInfo( name = 'acodec', 
                             encode = utf8.encode,
                             decode = utf8.decode,
                             incrementalencoder = utf8.incrementalencoder,
                             incrementaldecoder = utf8.incrementaldecoder,
                             streamreader = NullCodec,
                             streamwriter = utf8.streamwriter)

codecs.register(search_function)

