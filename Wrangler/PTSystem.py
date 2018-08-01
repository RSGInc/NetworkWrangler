import collections

from .NetworkException import NetworkException

__all__ = ['PTSystem']

class PTSystem:
    """
    Public Transport System definition.  Corresponds to the information in Cube's Public Transport system,
    including data for modes, operators, wait curves and crowding curves.
    """

    def __init__(self):
        self.waitCurveDefs  = collections.OrderedDict()
        self.crowdCurveDefs = collections.OrderedDict()
        self.operators      = collections.OrderedDict()  # index is number
        self.modes          = collections.OrderedDict()
        self.vehicleTypes   = collections.OrderedDict()

    def __repr__(self):
        s = ""
        for pt_num, pt_dict in self.modes.items():
            s += "MODE"
            for k,v in pt_dict.items(): s+= " {}={}".format(k,v)
            s+= "\n"
        s += "\n"

        for pt_num, pt_dict in self.operators.items():
            s += "OPERATOR"
            for k,v in pt_dict.items(): s+= " {}={}".format(k,v)
            s+= "\n"
        s += "\n"

        for pt_num, pt_dict in self.vehicleTypes.items():
            s += "VEHICLETYPE"
            for k,v in pt_dict.items(): s+= " {}={}".format(k,v)
            s+= "\n"
        s += "\n"

        for pt_num, pt_dict in self.waitCurveDefs.items():
            s += "WAITCRVDEF"
            for k,v in pt_dict.items(): s+= " {}={}".format(k,v)
            s+= "\n"
        s += "\n"

        for pt_num, pt_dict in self.crowdCurveDefs.items():
            s += "CROWDCRVDEF"
            for k,v in pt_dict.items(): s+= " {}={}".format(k,v)
            s+= "\n"
        s += "\n"

        return s