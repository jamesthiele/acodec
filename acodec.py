# acodec.py
import encodings, codecs, re, sys
# a mini tokenizer
_qs=r"'(?:[^'\\\n]|\\.|\\\n)*?'(?!')|'''(?:[^\\]|\\.)*?'''"
String = r"[uU]?[rR]?(?:%s|%s)"%(_qs, _qs.replace("'",'"'))
Comment=r'\#.*'
Name= r"[^#\"'\s\n;]+"
tok_re=re.compile(r"%s|%s|%s|(?P<e>[;\.])"%(Name, String , Comment))

# Our StreamReader
class aStreamReader(codecs.StreamReader):
    def readline(self, size=None, keepends=True):
        def repl(m):
            r=m.group()
            return "end," if m.group("e") else r+","
        if getattr(self, "pysrc", None)==None:          
            r=self.stream.read().decode("utf8")
            r="from amachine import *;run([%s])" % tok_re.sub(repl,r)
            self.pysrc=r.splitlines()
        return  u'%s\n'%self.pysrc.pop(0) if self.pysrc else u''
        
def search_function(s):
    if s!="acodec": 
        return None
    u8=encodings.search_function("utf8")
    return codecs.CodecInfo( name='acodec', 
        encode=u8.encode, decode=u8.decode,
        incrementalencoder=u8.incrementalencoder,
        incrementaldecoder=u8.incrementaldecoder,
        streamreader=aStreamReader,        # acodec StreamReader
        streamwriter=u8.streamwriter)

codecs.register(search_function)  # register our new codec search function
# End of acodec.py

