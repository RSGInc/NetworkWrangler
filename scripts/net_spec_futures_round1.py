import os

# MANDATORY. Set this to be the Project Name.
# e.g. "RTP2021", "TIP2021", etc
# PROJECT = "FU1" or "PPA", set by build_network_mtc_futures.py based on argument

# MANDATORY. Set this to be the git tag for checking out network projects.
TAG = "HEAD"

# MANDATORY. Set this to the directory in which to write your outputs.
# "hwy" and "trn" subdirectories will be created here.
OUT_DIR = "network_{}"  # YEAR

# MANDATORY.  Should be a dictionary with keys "hwy", "trn"
# to a list of projects.  A project can either be a simple string, or it can be
# a dictionary with with keys 'name', 'tag' (optional), and 'kwargs' (optional)
# to specify a special tag or special keyword args for the projects apply() call.
# For example:
#     {'name':"Muni_TEP", 'kwargs':{'servicePlan':"'2012oct'"}}
NETWORK_PROJECTS = collections.OrderedDict([
    (2015, {'hwy':['PROJ_attributes'], 'trn':[]}),  # adds PROJ attributes to NODE and LINK
    (2020, {
        'hwy':['EXP_SOL110001_SOL110002_I80_HOT_Lanes',
               'EXP_ALA170006_I880_HOTLanes_Dixon_Hegenberger',
               'EXP_ALA130034_I680_NB_HOTLane',
               'EXP_CC_050028_I680_SB_HOV_Completion',
               'EXP_SM150017_US101_HOTLanes',
               'CC_130001_BaileyRd_SR4',
               'CC_130046_I680_SR4_Int_Rec',
               'SCL130001_237_101_MAT_Int_Mod',
               'REG090003_SCLARA_FIP',
               'ALA130005_Dougherty_road_widening',
               'ALA130006_Dublin_Blvd_widening',
               'ALA130014_7th_St_road_diet',
               'ALA130026_Shattuck_Complete_Streets',
               'ALA170049_Central_AVE_Safety_Improvements',
               'ALA170052_Fruitvale_Ave_ped_improvements',
               'CC_070011_Brentwood_Blvd_Widening',
               'CC_070075_Kirker_Pass_Truck_Lane',
               'CC_090019_Bollinger_Canyon_Widening',
               'CC_130006_Concord_BART_road_diets',
               'CC_170001_SanRamonValleyBlvd_Lane_Addition',
               'MRN150009_San_Rafael_Bridge_Improvements',
               'SF_130011_2ndSt_Road_Diet'],
        'trn':['ALA050015_BART_to_WarmSprings',
               'SCL110005_BART_to_Berryessa'],
    }),
    (2025, {
        'hwy':['ALA150001_I680_SR84_Int_Wid',
               'EXP_CC_170002_I680_NorthernSegment_SB_HOTLane',
               'ALA150043_Claremont_road_diet'],
        'trn':['BRT030001_BART_to_SanJose']
    }),
    (2030, {
        'hwy':['EXP_ALA170009_I680_HOT_Alcosta_SR84'], 'trn':[]
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
# remove "False and" clauses when these are coded
if SCENARIO=="CleanAndGreen":
    # NOTE: Earthquake is assumed in Round1 2035 but since the effect doesn't stay; this is handled in build_network_mtc_futures.py
    if PROJECT == "FU1":
        # Haywired Earthquake in 2035
        NETWORK_PROJECTS[2035]['hwy'].append("Earthquake")
        NETWORK_PROJECTS[2035]['trn'].append("Earthquake")
    # Sea Level Rise in 2045
    # NETWORK_PROJECTS[2045]['hwy'].append("SeaLevelRise_1foot")
    # NETWORK_PROJECTS[2045]['trn'].append("SeaLevelRise_1foot")
    pass
elif SCENARIO=="RisingTides":
    # Sea Level Rise in 2030
    # NETWORK_PROJECTS[2030]['hwy'].append("SeaLevelRise_1foot")
    # NETWORK_PROJECTS[2030]['trn'].append("SeaLevelRise_1foot")
    if PROJECT == "FU1":
        # Haywired Earthquake in 2035
        NETWORK_PROJECTS[2035]['hwy'].append("Earthquake")
        NETWORK_PROJECTS[2035]['trn'].append("Earthquake")
    # Sea Level Rise in 2040
    # NETWORK_PROJECTS[2040]['hwy'].append("SeaLevelRise_2feet")
    # NETWORK_PROJECTS[2040]['trn'].append("SeaLevelRise_2feet")
    # Sea Level Rise in 2050
    # NETWORK_PROJECTS[2050]['hwy'].append("SeaLevelRise_3feet")
    # NETWORK_PROJECTS[2050]['trn'].append("SeaLevelRise_3feet")
elif SCENARIO=="BackToTheFuture":
    # NETWORK_PROJECTS[2035]['hwy'].append("SeaLevelRise_1foot")
    # NETWORK_PROJECTS[2035]['trn'].append("SeaLevelRise_1foot")
    # NOTE: Earthquake is assumed in Round1 2035 but since the effect doesn't stay; this is handled in build_network_mtc_futures.py
    if PROJECT == "FU1":
        # Haywired Earthquake in 2035
        NETWORK_PROJECTS[2035]['hwy'].append("Earthquake")
        NETWORK_PROJECTS[2035]['trn'].append("Earthquake")

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
