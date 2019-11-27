import os

# MANDATORY. Set this to be the Project Name.
# e.g. "RTP2021", "TIP2021", etc
PROJECT = "Test_Project"

# MANDATORY. Set this to be the Scenario Name
# e.g. "Base", "Baseline"
SCENARIO = "Test_Scenario"

# MANDATORY. Set this to be the git tag for checking out network projects.
TAG = "HEAD"

# MANDATORY. Set this to the directory in which to write your outputs.
# "hwy" and "trn" subdirectories will be created here.
OUT_DIR = SCENARIO + "_network_{}"  # YEAR

# MANDATORY.  Should be a dictionary with keys "hwy", "muni", "rail", "bus"
# to a list of projects.  A project can either be a simple string, or it can be
# a dictionary with with keys 'name', 'tag' (optional), and 'kwargs' (optional)
# to specify a special tag or special keyword args for the projects apply() call.
# For example:
#     {'name':"Muni_TEP", 'kwargs':{'servicePlan':"'2012oct'"}}
NETWORK_PROJECTS = collections.OrderedDict([
    (2015, 
        {'hwy':[
            'PROJ_attributes', # adds PROJ attributes to NODE and LINK
            {'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2015'}}
        ], 'trn':[]}),  
    (2020, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2020'}},
              ],
        'trn':[{'name':'demo_project', 'kwargs':{'FUTURE':'"BackToTheFuture"'}}]
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
