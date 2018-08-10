import collections, re

from .Logger import WranglerLogger

class Faresystem(collections.OrderedDict):
    """
    Faresystem definition.  A faresystem is a Cube Public Transport construct representing a single faresystem.

    It's a subclass of an Ordered Dictionary.
    """

    def __init__(self):
        collections.OrderedDict.__init__(self)

        self.fare_zone_mat = {} # origin fare zone (int) => dest fare zone (int) => fare (float)

    def __repr__(self):
        s = "FARESYSTEM "

        fields = ['%s=%s' % (k,v) for k,v in self.items()]
        s += ", ".join(fields)

        return s

    def getId(self):
        """
        Retrieve the ID number.
        """
        return int(self["NUMBER"])

    def setFarezoneODPair(self, farezone_i, farezone_j, fare_val):
        """
        Sets the fare for the given farezone pair
        """
        if farezone_i not in self.fare_zone_mat:
            self.fare_zone_mat[farezone_i] = {}
        self.fare_zone_mat[farezone_i][farezone_j] = fare_val

    def getFareZoneMatrixLines(self):
        """
        Returns farezone to farezone string for writing.
        """
        s = ""
        if len(self.fare_zone_mat) == 0: return s

        for farezone_i in sorted(self.fare_zone_mat.keys()):
            for farezone_j in sorted(self.fare_zone_mat[farezone_i].keys()):
                s += "{} {} {} {:.4f}\n".format(self.getId(), farezone_i, farezone_j, self.fare_zone_mat[farezone_i][farezone_j])
        return s

    @staticmethod
    def readFareZoneMatrixFile(farezonematrix_file, faresystems_dict):
        """
        Reads the a farezone matrix file (see FAREMATI documentation in Public Transport)
        and updates the given dictionary of faresystems.
        """
        WranglerLogger.debug("Reading {}".format(farezonematrix_file))
        f = open(farezonematrix_file, 'r')
        while True:
            line = f.readline().strip()
            if not line: break

            row  = re.split("[\s+\,]", line) # split on whitespace or comma

            faresystem    = int(row[0])
            farezone_i    = int(row[1])
            farezone_j    = int(row[2])
            for fare_str in row[3:]:
                fare_val = float(fare_str)
                # print("faresystem {}  i={}  j={}  fare={}".format(faresystem, farezone_i, farezone_j, fare_val))
                faresystems_dict[faresystem].setFarezoneODPair(farezone_i, farezone_j, fare_val)
                farezone_j += 1
        f.close()