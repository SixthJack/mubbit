class HTTPHeaders( dict ):
    @classmethod
    def parse( cls, hdrdata ):
        """Returns HTTPHeaders object."""
        def consume( obj, line ):
            name, value = line.split( b":", 1 )
            name = name.strip()
            name = name.replace(b'-',b'_').lower()
            pvalue = obj.get( name, None)
            obj[ name.decode() ] = (value if pvalue == None else (pvalue+b', '+value)).decode().strip()

        obj, prev_line = cls(), b''
        for line in hdrdata.splitlines() :
            if not line : continue

            if line[:1].isspace() : # continuation of a multi-line header
                prev_line += ' ' + line.lstrip(' \t')
            else :
                consume( obj, prev_line ) if prev_line else None
                prev_line = line
        consume( obj, prev_line ) if prev_line else None    # Corner case
        return obj
