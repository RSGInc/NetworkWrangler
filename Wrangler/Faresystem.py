import collections

class Faresystem(collections.OrderedDict):
    """
    Faresystem definition.  A faresystem is a Cube Public Transport construct.
    """

    def __init__(self):
        collections.OrderedDict.__init__(self)

    def __repr__(self):
        s = "FARESYSTEM "

        fields = ['%s=%s' % (k,v) for k,v in self.items()]
        s += " ".join(fields)

        return s
