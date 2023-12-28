import os
import collections
# MANDATORY. Set this to be the Project Name.
# e.g. "RTP2021", "TIP2021", etc
PROJECT  = "NGF"

# MANDATORY. Set this to be the git tag for checking out network projects.
#TAG = "HEAD"               # Use this tag if you want NetworkWrangler to use the latest version in the local repo to build the network
#TAG = "PBA50_Blueprint"    # Use this tag if you want to replicate the network built for PBA50
TAG = "HEAD"

# A project can either be a simple string, or it can be
# a dictionary with with keys 'name', 'tag' (optional), and 'kwargs' (optional)
# to specify a special tag or special keyword args for the projects apply() call.
# For example:
#     {'name':"Muni_TEP", 'kwargs':{'servicePlan':"'2012oct'"}}

###########################################################
# NextGenFwy projects


# Pathways - note these are 2035 projects
NGF_PROJECTS = {
    'BlueprintSegmented':{
        'hwy':[
            'NGF_BlueprintSegmented',      # All lane tolling on freeways
        ],   
        'trn':[]
    },
    # NGF Round 2 pathway definitions: https://mtcdrive.app.box.com/file/1381469356636?s=8mpbmehocafa83lckc6bsatrhow87cne

    # Pathway 4: Pathway 4 2035 Express Lanes (would be most similar to Round 1 No New Pricing)
    # https://app.asana.com/0/1203644633064654/1206115787970079/f
    'R2P4_2035_Express_Lanes':{
        'hwy':[
            'NGF_BlueprintSegmented',         # All lane tolling on freeways
            {'name':'EXP_uncommitted_noAllLaneTolling',     'kwargs':{'MODELYEAR':'2035','PATHWAY':"'P4'"},     'branch':'NGF'},
            #'Futures_C4_ReX_Express',         # New Transit Service Near Tolling: ReX Express
            #'ReX_link',                       # New Transit Service Near Tolling: ReX Link
            #'NGF_CarpoolLanes',               # Carpool Lanes
            #'NGF_TransitPriorityOnArterials', # Transit Priority - All Lane Tolling
            #'Transform_I680_Multimodal_Imp',
            #'FBP_CC_036_I80_ExpBus_Impr',
            #'FBP_NP_040_VINE_Exp_Bus_Enhancements',
            #'FBP_MR_018_US101_BOS',
            #'MAJ_MuniForward_Uncommitted',
            #'MAJ_AC_Frequency_Improvement',
            #'BP_Vision_Zero',               # Local Street Safety Improvements and Speed Reductions
         ],
        'trn':[
            #'NGF_NoProject_farefiles',      # ensures these files get included; note this is not a real project
            #'Futures_C4_ReX_Express',       # New Transit Service Near Tolling: ReX Express
            #'ReX_link',                     # New Transit Service Near Tolling: Rex Link
            #'Transform_I680_Multimodal_Imp',
            #'FBP_CC_036_I80_ExpBus_Impr',
            #'FBP_SL_026_SolExpressBus',
            #'MAJ_MuniForward_Uncommitted',
            #'VTA_Next',
            #'MAJ_AC_Frequency_Improvement',
            #'FBP_MuniForward_Uncommitted_Rail',
            # Local Transit Frequency Boosts 2
            # Parameters defined here: https://app.asana.com/0/0/1203931443540514/f
            #{'name':'NGF_IncreaseTrnFreqXferRoutes2BartCaltrainFerry',  'kwargs':{
            #    'top_n_local':'2', 
            #    # configure by mode: https://github.com/BayAreaMetro/modeling-website/wiki/TransitModes
            #    'min_headway':'{"local_default":15, 21:10, 24:10, 27:10, 28:10, 30:10, 111:10}', 
            #    'include_connections_to_express_bus':'True',
            #    # this directory is used to determine which routes have frequency increases.  So to include ReX Express bus routes,
            #    # use a directory that includes ReX Express routes (e.g. an earlier iteration of this scenario)
            #    'transit_assignment_dir':'r"L:\\Application\\Model_One\\NextGenFwys\\Scenarios\\2035_TM152_NGF_ReXExpress_ReXLink_trnassignment\\OUTPUT\\trn"'
            #}},
            # Trunkline Transit Frequency Boosts 2
            #{'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
            #    'min_headway':'10',
            #    'include_rail':'False'
            #}},
            # Extended Transit Service Hours
            #{'name':'NGF_TrnExtendedServiceHours',  'kwargs':{'EV_headway':'15'}},
        ]
    },
    # Pathway 1b: All-lane tolling + Focus on Affordability (new numbering in AG10: P1b_AllLaneTolling_Affordable --> 3B)
    # https://app.asana.com/0/1203644633064654/1203644636776965/f
    'P1b_AllLaneTolling_Affordable':{
        'hwy':[
            'NGF_BlueprintSegmented',       # All lane tolling on freeways
            'NGF_CarpoolLanes',             # Carpool Lanes
            'BP_Vision_Zero',               # Local Street Safety Improvements and Speed Reductions
        ],
        'trn':[
            'NGF_NoProject_farefiles',      # ensures these files get included; note this is not a real project
            # Trunkline Transit Frequency Bosts 2
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'10',
                'include_rail':'False'
            }}
        ]
    },
    # new numbering in AG10: P2a_AllLaneTollingPlusArterials_ImproveTransit --> 4A)
    'P2a_AllLaneTollingPlusArterials_ImproveTransit':{
        'hwy':[
            'NGF_BlueprintSegmented',         # All lane tolling on freeways
            'Futures_C4_ReX_Express',         # New Transit Service Near Tolling: ReX Express
            'ReX_link',                       # New Transit Service Near Tolling: ReX Link
            'NGF_CarpoolLanes',               # Carpool Lanes
            'NGF_TransitPriorityOnArterials', # Transit Priority - All Lane Tolling
            'Transform_I680_Multimodal_Imp',
            'FBP_CC_036_I80_ExpBus_Impr',
            'FBP_NP_040_VINE_Exp_Bus_Enhancements',
            'FBP_MR_018_US101_BOS',
            'MAJ_MuniForward_Uncommitted',
            'MAJ_AC_Frequency_Improvement',
            'NGF_Arterials',                 # Code arterials for tolling in Pathway 2
            'BP_Vision_Zero',                # Local Street Safety Improvements and Speed Reductions
         ],
        'trn':[
            'NGF_NoProject_farefiles',      # ensures these files get included; note this is not a real project
            'Futures_C4_ReX_Express',       # New Transit Service Near Tolling: ReX Express
            'ReX_link',                     # New Transit Service Near Tolling: Rex Link
            'Transform_I680_Multimodal_Imp',
            'FBP_CC_036_I80_ExpBus_Impr',
            'FBP_SL_026_SolExpressBus',
            'MAJ_MuniForward_Uncommitted',
            'VTA_Next',
            'MAJ_AC_Frequency_Improvement',
            'FBP_MuniForward_Uncommitted_Rail',
            # Local Transit Frequency Boosts 2
            # Parameters defined here: https://app.asana.com/0/0/1203931443540514/f
            {'name':'NGF_IncreaseTrnFreqXferRoutes2BartCaltrainFerry',  'kwargs':{
                'top_n_local':'2', 
                # configure by mode: https://github.com/BayAreaMetro/modeling-website/wiki/TransitModes
                'min_headway':'{"local_default":15, 21:10, 24:10, 27:10, 28:10, 30:10, 111:10}', 
                'include_connections_to_express_bus':'True',
                # this directory is used to determine which routes have frequency increases.  So to include ReX Express bus routes,
                # use a directory that includes ReX Express routes (e.g. an earlier iteration of this scenario)
                'transit_assignment_dir':'r"L:\\Application\\Model_One\\NextGenFwys\\Scenarios\\2035_TM152_NGF_ReXExpress_ReXLink_trnassignment\\OUTPUT\\trn"'
            }},
            # Trunkline Transit Frequency Boosts 2
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'10',
                'include_rail':'False'
            }},
            # Extended Transit Service Hours
            {'name':'NGF_TrnExtendedServiceHours',  'kwargs':{'EV_headway':'15'}},
        ]
    },
    # new numbering in AG10: P2b_AllLaneTollingPlusArterials_Affordable --> 4B)
    'P2b_AllLaneTollingPlusArterials_Affordable':{
        'hwy':[
            'NGF_BlueprintSegmented',       # All lane tolling on freeways
            'NGF_CarpoolLanes',             # Carpool Lanes
            'NGF_Arterials',                # Code arterials for tolling in Pathway 2
            'BP_Vision_Zero',               # Local Street Safety Improvements and Speed Reductions
        ],
        'trn':[
            'NGF_NoProject_farefiles',      # ensures these files get included; note this is not a real project
            # Trunkline Transit Frequency Bosts 2
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'10',
                'include_rail':'False'
            }}
        ]
    },
    # new numbering in AG10: P3a_3Cordons_ImproveTransit --> 2A
    'P3a_3Cordons_ImproveTransit':{
        'hwy':[
            'MAJ_SF_Congestion_Pricing',     # San Francisco Cordon Pricing
            'NGF_AL_Cordon',                 # Oakland Cordon Pricing
            'NGF_SC_Cordon',                 # San Jose Cordon Pricing
            'MAJ_MuniForward_Uncommitted',
            'MAJ_AC_Frequency_Improvement',
            'Futures_C4_ReX_Express',         # New Transit Service Near Tolling: ReX Express
            'ReX_link',                       # New Transit Service Near Tolling: ReX Link
            'BP_Vision_Zero',                 # Local Street Safety Improvements and Speed Reductions
            'NGF_TransitPriorityCordons'      # Transit Priority - Cordons
       ],
        'trn':[
            'NGF_NoProject_farefiles',       # ensures these files get included; note this is not a real project
            'MAJ_SF_Congestion_Pricing',
            'MAJ_MuniForward_Uncommitted',
            'VTA_Next',
            'MAJ_AC_Frequency_Improvement',
            'FBP_MuniForward_Uncommitted_Rail',
            'Futures_C4_ReX_Express',         # New Transit Service Near Tolling: ReX Express
            'ReX_link',                       # New Transit Service Near Tolling: ReX Link
            # Trunkline Transit Frequency Bosts 1
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'15',
                'include_rail':'False'
            }},
            # Local Transit Frequency Boosts Cordons
            {'name':'NGF_TrnFreqBoostsCordons', 'kwargs':{
                'top_n_local':'15',
                'min_headway':'7',
                'min_headway_LRT':'10',
                'transit_assignment_dir':'r"L:\\Application\\Model_One\\NextGenFwys\\Scenarios\\2035_TM152_NGF_ReXExpress_ReXLink_trnassignment\\OUTPUT\\trn"'
            }},
            # Extended Transit Service Hours - Cordons          
            {'name':'NGF_TrnExtendedServiceHours_Cordons', 'kwargs':{
                'top_n_local':'15',
                'EV_headway':'10',
                'transit_assignment_dir':'r"L:\\Application\\Model_One\\NextGenFwys\\Scenarios\\2035_TM152_NGF_ReXExpress_ReXLink_trnassignment\\OUTPUT\\trn"'
            }},
        ]
    },
    # new numbering in AG10: P3b_3Cordons_Affordable --> 2B
    'P3b_3Cordons_Affordable':{
        'hwy':[
            'MAJ_SF_Congestion_Pricing',     # San Francisco Cordon Pricing
            'NGF_AL_Cordon',                 # Oakland Cordon Pricing
            'NGF_SC_Cordon',                 # San Jose Cordon Pricing
            'MAJ_MuniForward_Uncommitted',
            'MAJ_AC_Frequency_Improvement',
            'BP_Vision_Zero',                # Local Street Safety Improvements and Speed Reductions
        ],
        'trn':[
            'NGF_NoProject_farefiles',       # ensures these files get included; note this is not a real project
            'MAJ_SF_Congestion_Pricing',
            'MAJ_MuniForward_Uncommitted',
            'VTA_Next',
            'MAJ_AC_Frequency_Improvement',
            'FBP_MuniForward_Uncommitted_Rail',
            # Trunkline Transit Frequency Bosts 1
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'15',
                'include_rail':'False'
            }},
            # Local Transit Frequency Boosts Cordons
            {'name':'NGF_TrnFreqBoostsCordons', 'kwargs':{
                'top_n_local':'15',
                'min_headway':'7',
                'min_headway_LRT':'10',
                'transit_assignment_dir':'r"L:\\Application\\Model_One\\NextGenFwys\\Scenarios\\2035_TM152_NGF_ReXExpress_ReXLink_trnassignment\\OUTPUT\\trn"'
            }}
        ]
    },
    # new numbering in AG10: P4_NoNewPricing --> P1
    'P4_NoNewPricing':{
        'hwy':[
            'BP_Vision_Zero',                # Local Street Safety Improvements and Speed Reductions
        ],
        'trn':[
            'NGF_NoProject_farefiles',       # ensures these files get included; note this is not a real project
            # Trunkline Transit Frequency Bosts 2
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'10',
                'include_rail':'False'
            }}
        ]
    },

    # All-lane tolling pricing strategy only: https://app.asana.com/0/1201809392759895/1205309291141002/f
    'P1x_AllLaneTolling_PricingOnly':{
        'hwy':[
            'NGF_BlueprintSegmented',        # All lane tolling on freeways
            'BP_Vision_Zero',                # Local Street Safety Improvements and Speed Reductions
        ],
        'trn':[
            'NGF_NoProject_farefiles',       # ensures these files get included; note this is not a real project
            # Trunkline Transit Frequency Bosts 2
            {'name':'NGF_TrunklineTrnFreqBoosts', 'kwargs':{
                'min_headway':'10',
                'include_rail':'False'
            }}
        ]
    }
}

# Put them together for NETWORK_PROJECTS
NETWORK_PROJECTS   = collections.OrderedDict()

# we're only building 2035
for YEAR in [2035]:

    NETWORK_PROJECTS[YEAR] = {
        'hwy':NGF_PROJECTS[SCENARIO]['hwy'],
        'trn':NGF_PROJECTS[SCENARIO]['trn']
    }
    # handle net_remove, nets keywords
    for netmode in ['hwy','trn']:

        # iterate backwards via index to delete cleanly
        for project_idx in range(len(NETWORK_PROJECTS[YEAR][netmode])-1,-1,-1):
            project = NETWORK_PROJECTS[YEAR][netmode][project_idx]
            # special handling requires project to be specified as dictionary
            if not isinstance(project, dict): continue

            # variants_exclude: specifies list of network variants for which this project should be *excluded*
            if 'variants_exclude' in project.keys() and NET_VARIANT in project['variants_exclude']:
                Wrangler.WranglerLogger.info("Removing {} {} {}".format(YEAR, netmode, project))
                del NETWORK_PROJECTS[YEAR][netmode][project_idx]
                continue

            # variants_include: specifies list of network variants for which this project should be *included*
            # if this keyword is present, then this project is included *only* for variants in this list
            if 'variants_include' in project.keys() and NET_VARIANT not in project['variants_include']:
                Wrangler.WranglerLogger.info("Removing {} {} {}".format(YEAR, netmode, project))
                del NETWORK_PROJECTS[YEAR][netmode][project_idx]
                continue

# For every year where a project is applied do the following:
# Convert all zero-length links to 0.01
# Move buses to HOV/Express lanes at the end
#
for YEAR in NETWORK_PROJECTS.keys():
    # if anything is applied
    if ((len(NETWORK_PROJECTS[YEAR]['hwy']) > 0) or (len(NETWORK_PROJECTS[YEAR]['trn']) > 0)):
        NETWORK_PROJECTS[YEAR]['hwy'].append('No_zero_length_links')

    if ((len(NETWORK_PROJECTS[YEAR]['hwy']) > 0) or (len(NETWORK_PROJECTS[YEAR]['trn']) > 0)):
        NETWORK_PROJECTS[YEAR]['trn'].append('Move_buses_to_HOV_EXP_lanes')


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
