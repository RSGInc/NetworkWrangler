print("Network Specification: {}".format(__file__))
import os

# MANDATORY. Set this to be the Project Name.
# e.g. "RTP2021", "TIP2021", etc
PROJECT = "FU1" # Futures Round 1

# MANDATORY. Set this to be the git tag for checking out network projects.
TAG = "HEAD"

# OPTIONAL. If you are building on top of a previously built network, this
# should be set to the location of those networks.  This should be a directory
# which has "hwy" and "trn" subdirectories.
PIVOT_DIR = os.path.join(os.environ["USERPROFILE"], "Box","Modeling and Surveys","Development","Travel Model Two Development","Model Inputs","2015_revised_mazs")

# OPTIONAL. If PIVOT_DIR is specified, MANDATORY.  Specifies year for PIVOT_DIR.
PIVOT_YEAR = 2015

# MANDATORY. Set this to the directory in which to write your outputs.
# "hwy" and "trn" subdirectories will be created here.
OUT_DIR = "network_{}"  # YEAR

# MANDATORY.  Should be a dictionary with keys "hwy", "muni", "rail", "bus"
# to a list of projects.  A project can either be a simple string, or it can be
# a dictionary with with keys 'name', 'tag' (optional), and 'kwargs' (optional)
# to specify a special tag or special keyword args for the projects apply() call.
# For example:
#     {'name':"Muni_TEP", 'kwargs':{'servicePlan':"'2012oct'"}}
NETWORK_PROJECTS = collections.OrderedDict([
    (2015, {
        'hwy':[], 'trn':[]
    }),
    (2020, {
        'hwy':['SMART'],
        'trn':['SMART']
    }),
    (2025, {
        'hwy':[], 'trn':[]
    }),
    (2030, {
        'hwy':[], 'trn':[]
    }),
    (2035, {
        'hwy':[], 'trn':[]
    }),
    (2040, {
        'hwy':[], 'trn':[]
    }),
    (2045, {
        'hwy':[], 'trn':[]
    }),
    (2050, {
        'hwy':[], 'trn':[]
    })
])

# done at the end in case they need to remove transit project links
if SCENARIO=="CleanAndGreen":
    # Sea Level Rise in 2045
    NETWORK_PROJECTS[2045]['hwy'].append("SeaLevelRise_1foot")
    NETWORK_PROJECTS[2045]['trn'].append("SeaLevelRise_1foot")
elif SCENARIO=="RisingTides":
    # Sea Level Rise in 2030
    NETWORK_PROJECTS[2030]['hwy'].append("SeaLevelRise_1foot")
    NETWORK_PROJECTS[2030]['trn'].append("SeaLevelRise_1foot")
    # Sea Level Rise in 2040
    NETWORK_PROJECTS[2040]['hwy'].append("SeaLevelRise_2feet")
    NETWORK_PROJECTS[2040]['trn'].append("SeaLevelRise_2feet")
    # Sea Level Rise in 2050
    NETWORK_PROJECTS[2050]['hwy'].append("SeaLevelRise_3feet")
    NETWORK_PROJECTS[2050]['trn'].append("SeaLevelRise_3feet")

# OPTIONAL. The default route network project directory is Y:\networks.  If
# projects are stored in another directory, then use this variable to specify it.
# For example: Y:\networks\projects
# NETWORK_BASE_DIR = None
# NETWORK_PROJECT_SUBDIR = None
# NETWORK_SEED_SUBDIR = None
# NETWORK_PLAN_SUBDIR = None

# OPTIONAL. A list of project names which have been previously applied in the
# PIVOT_DIR network that projects in this project might rely on.  For example
# if DoyleDrive exists, then Muni_TEP gets applied differently so transit lines
# run on the new Doyle Drive alignment
APPLIED_PROJECTS = None

# OPTIONAL.  A list of project names.  For test mode, these projects won't use
# the TAG.  This is meant for developing a network project.
TEST_PROJECTS = []
