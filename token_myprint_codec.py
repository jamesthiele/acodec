import codecs, cStringIO, encodings
from encodings import utf_8
import tokenize

class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        data = tokenize.untokenize(self.translate(self.stream.readline))
        self.stream = cStringIO.StringIO(data)

    def translate(self, readline):
        for type, name,_,_,_ in tokenize.generate_tokens(readline):
            if type == tokenize.NAME and name == 'myprint':
                yield tokenize.NAME, 'print'
            else:
                yield type,name

def search_function(s):
    if s != 'token_myprint':
        return None
    utf8 = encodings.search_function("utf8")
    return codecs.CodecInfo(name='mylang',
        encode = utf8.encode,
        decode = utf8.decode,
        incrementalencoder = utf8.incrementalencoder,
        incrementaldecoder = utf8.incrementaldecoder,
        streamreader = StreamReader,
        streamwriter = utf8.streamwriter)

codecs.register(search_function)
