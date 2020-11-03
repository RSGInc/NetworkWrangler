import os
# MANDATORY. Set this to be the Project Name.
# e.g. "RTP2021", "TIP2021", etc
PROJECT  = "Blueprint"

# MANDATORY. Set this to be the git tag for checking out network projects.
TAG = "HEAD"

# A project can either be a simple string, or it can be
# a dictionary with with keys 'name', 'tag' (optional), and 'kwargs' (optional)
# to specify a special tag or special keyword args for the projects apply() call.
# For example:
#     {'name':"Muni_TEP", 'kwargs':{'servicePlan':"'2012oct'"}}
###########################################################
COMMITTED_PROJECTS = collections.OrderedDict([
    (2015, {
        'hwy':['PROJ_attributes',  # adds PROJ attributes to NODE and LINK
               {'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2015'}}],
        'trn':[]
    }),
    (2020, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2020'}},
               {'name':'EXP_237B',                   'kwargs':{'FUTURE':"PBA50"}}, # todo: update this to support PBA50
               'EXP_580C',
               'EXP_680D',
               'EXP_680F',
               'SCL130001_237_101_MAT_Int_Mod',
               'REG090003_SCLARA_FIP',
               'ALA130005_Dougherty_road_widening',
               'ALA130006_Dublin_Blvd_widening',
               'ALA130014_7th_St_road_diet',
               'ALA130026_Shattuck_Complete_Streets',
               'ALA170049_Central_AVE_Safety_Improvements',
               'ALA150004_EastBay_BRT',
               'CC_130001_BaileyRd_SR4',
               'CC_130046_I680_SR4_Int_Rec',
               'CC_070035_I80_SPDamRd_Int_Phase1',
               'CC_070011_Brentwood_Blvd_Widening',
               'CC_070075_Kirker_Pass_Truck_Lane',
               'CC_090019_Bollinger_Canyon_Widening',
               'CC_130006_Concord_BART_road_diets',
               'CC_170001_SanRamonValleyBlvd_Lane_Addition',
               'CC_170061_Bus_On_Shoulder_680BRT',
               'MRN150009_San_Rafael_Bridge_Improvements',
               'SF_070027_Yerba_Buena_Ramp_Imp',
               'SF_070005_VanNess_BRT',
               'SF_130011_2ndSt_Road_Diet',
               'SF_Market_Street_Closure',
               'SM_110047_SR92_ElCam_Ramp_Mod',
               'SOL110005_Jepson_Van_to_Com',
               'SON070004_101_MarinSonNarrows_Phase1',
               'ALA050014_SR84_Widening',
               'ALA170011_BayBridge_HOV_Connectors',
               'ALA150047_TelegraphAve_Complete_Streets',
               'SM_110047_SR92_ElCam_Ramp_Mod',
               'SCL190002_280_Foothill_improvement',
               'SCL190006_101SB_offramp_improvement',
               'I80_AdaptiveRampMetering',
               'VAR170021_Freeway_Performance_I880',
               'SonomaCounty_Transit_NoBuild2050',
               'SF_MuniForward_Committed',
               'FBP_MU_029_Broadway_Transit_Only_Lanes',
               'EXP_Blueprint_NoProject'],
        'trn':['ALA050015_BART_to_WarmSprings',
               'ACGo',
               'CC_050025_EBart_to_Antioch',
               'GGTransit_Committed',
               'SCL110005_BART_to_Berryessa',
               'SF_010015_Transbay_Terminal',
               'SF_010037_Muni_Central_Subway',
               'SF_070027_Yerba_Buena_Ramp_Imp',
               'SOL030002_FairfieldVacaville_Stn',
               'SON090002_SMART',
               'SON090002_SMART_to_Larkspur',
               'CC_070062_Richmond_Ferry',
               'SF_MuniForward_Committed',
               'VTA_Next',
               'SCL130001_237_101_MAT_Int_Mod',
               'SonomaCounty_Transit_NoBuild2050',
               'SMART_Novato',
               'Xfare_update_2020',
               'ACTransit_Committed',
               'ferry_update_2019',
               'Napa_Solano_Updates_2020',
               'FBP_Beale_Transit_Only_Lane',
               'SamTrans_ECR_Rapid'],
    }),
    (2025, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2025'}},
               'EXP_CC_050028_I680_SB_HOV_Completion',
               'EXP_101B1',
               'EXP_101B2',
               'EXP_680C1',
               'EXP_85D',
               'EXP_101C',
               'ALA150001_I680_SR84_Int_Wid',
               'ALA150043_Claremont_road_diet',
               'CC_070009_Slatten_Ranch_Rd_Extension',
               'SF_070004_Geary_BRT_Phase1',
               'SON070004_101_MarinSonNarrows_Phase2',
               'SOL110006_Jepson_1B_1C',
               'SCL190008_US101_DLC_Int_Imp',
               'I880_US101_AdaptiveRampMetering',
               'MAJ_SCL050009_VTA_Eastridge_Extension',
               'SOL070020_I80_I680_SR12_Int_1_2A',
               'ALA170052_Fruitvale_Ave_ped_improvements',
               'EXP_Blueprint_NoProject'],
        'trn':['SF_010028_Caltrain_Modernization',
               'SON090002_SMART_to_Windsor',
               'MAJ_SCL050009_VTA_Eastridge_Extension',
               'REG090037_New_BART_Trains',
               'SOL070020_I80_I680_SR12_Int_1_2A']
    }),
    (2030, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2030'}},
               'EXP_880A',
               'EXP_Blueprint_NoProject'],
        'trn':['BART_NoProject']
    }),
    (2035, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2035'}},
               'EXP_Blueprint_NoProject'],
        'trn':[]
    }),
    (2040, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2040'}},
               'EXP_Blueprint_NoProject'],
        'trn':[]
    }),
    (2045, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2045'}},
               'EXP_Blueprint_NoProject'],
        'trn':[]
    }),
    (2050, {
        'hwy':[{'name':'Bridge_Toll_Updates_2_2pct', 'kwargs':{'MODELYEAR':'2050'}},
               'EXP_Blueprint_NoProject'],
        'trn':[]
    })
])

###########################################################
# Blueprint projects
BLUEPRINT_PROJECTS = collections.OrderedDict([
        (2015, {'hwy':[],
                'trn':[]
        }),
        (2020, {'hwy':['RRSP_Alameda_Point_Transit_Improvements',
                       'MAJ_MTC050027_Berkeley_Ferry',
                       'MAJ_WETA_Service_Frequency_Increase',
                       'ALA150004_EastBay_BRT',
                       'EXP_Blueprint',
                       {'name':'EXP_uncommitted_all', 'kwargs':{'MODELYEAR':'2020'}}],
                'trn':['MAJ_MTC050027_Berkeley_Ferry',
                       'MAJ_WETA_Service_Frequency_Increase',
                       'ALA150004_EastBay_BRT',
                       'RRSP_Alameda_Point_Transit_Improvements']
        }),
        (2025, {'hwy':['RRSP_E14_Mission_Corridor',
                       'Transform_SR37_Widening_Interim',
                       'MAJ_SF_Congestion_Pricing',
                       'MAJ_Geary_BRT_Phase2',
                       'FBP_MU_041_Hovercraft_Pilot',
                       'BP_Vision_Zero',
                       'EXP_Blueprint',
                       'MAJ_AC_Frequency_Improvement',
                       'FBP_MU_044_SouthSF_Ferry_Serv_Incr',
                       'FBP_MU_029_ACRapid_2025',
                       'FBP_MR_026_NovatoWide',
                       'FBP_CC_054_CrowCanyonWide',
                       'FBP_NP_038_TSP_On_SR29',
                       'FBP_CC_050_SR4_Operation_Improvements_EB',
                       'FBP_NP_044_Soscol_Junction',
                       'FBP_SL_033_FairgroundsWide',
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'2B'"}},
                       {'name':'FBP_CC_040_041_042_I680_SR4_Int_Phases_1_2_4_5','kwargs':{'PHASE':"'1'"}},
                       {'name':'FBP_CC_040_041_042_I680_SR4_Int_Phases_1_2_4_5','kwargs':{'PHASE':"'2'"}},
                       {'name':'EXP_uncommitted_all', 'kwargs':{'MODELYEAR':'2025'}}],
                'trn':[{'name':'FBP_MU_046_ACE_Freq_Inc', 'kwargs':{'MODELYEAR':'2025'}},
                       'RRSP_E14_Mission_Corridor',
                       'Transform_SR37_Widening_Interim',
                       'MAJ_SF_Congestion_Pricing',
                       'MAJ_Geary_BRT_Phase2',
                       'FBP_MU_041_Hovercraft_Pilot',
                       'FBP_MU_049_Caltrain_6TPHPD',
                       'FBP_MU_059_ACTransbay_Freq_Incr',
                       'FBP_MU_060_ReX_Blue',
                       'MAJ_AC_Frequency_Improvement',
                       'FBP_MU_044_SouthSF_Ferry_Serv_Incr',
                       'GGT_Service_Imp',
                       'FBP_MU_029_ACRapid_2025',
                       'FBP_NP_044_Soscol_Junction',
                       'FBP_AL_001_NewarkFremPDA',
                       'MAJ_RedwoodCity_SF_Ferry',
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'2B'"}}]
        }),
        (2030, {'hwy':['MAJ_SanPablo_BRT',
                       'BP_Tolls_On_Congested_Freeways_2030',
                       'BP_Vision_Zero',
                       'FBP_AL_021_South_Bay_Connect',
                       'FBP_MU_056_Dumbarton_GRT',
                       'FBP_MU_044_Richmond_Ferry_Serv_Incr',
                       'MAJ_REG090037_BART_Core_Cap',
                       'Transform_Valley_Link',
                       'FBP_NP_040_VINE_Exp_Bus_Enhancements',
                       'FBP_MR_021_101_580_Direct_Connector',
                     #  'FBP_MR_018_US101_BOS',
                       'FBP_CC_036_I80_ExpBus_Impr',
                       'EXP_Blueprint',
                       {'name':'FBP_CC_040_041_042_I680_SR4_Int_Phases_1_2_4_5','kwargs':{'PHASE':"'4'"}},
                       'FBP_CC_021_Ant_Mart_Herc_Ferry',
                       {'name':'EXP_uncommitted_all', 'kwargs':{'MODELYEAR':'2030'}}],
                'trn':[{'name':'FBP_MU_046_ACE_Freq_Inc', 'kwargs':{'MODELYEAR':'2030'}},
                       'MAJ_BRT030001_BART_to_SanJose',
                       'BART_Irvington_Infill',
                       'MAJ_REG090037_BART_Core_Cap',
                       'FBP_AL_021_South_Bay_Connect',
                       'FBP_MU_056_Dumbarton_GRT',
                       'FBP_MU_049_Caltrain_8TPHPD',
                       'FBP_MU_061_ReX_Green',
                       'MAJ_SanPablo_BRT',
                       'FBP_MU_044_Richmond_Ferry_Serv_Incr',
                       'Transform_Valley_Link',
                       'FBP_SF_028_SF_Express_Bus_On_Exp_Lanes',
                       'MAJ_SF_050002_Caltrain_Ext_TransbayTerminal',
                       'FBP_SF_024_Historic_Streetcar_Ext',
                       'FBP_MuniForward_Uncommitted_Rail',
                       'FBP_CC_036_I80_ExpBus_Impr',
                       'BP_PDA_Transit_Enhancements',
                       'FBP_CC_021_Ant_Mart_Herc_Ferry']
        }),
        (2035, {'hwy':['MAJ_MuniForward_Uncommitted',
                       'MAJ_Treasure_Island_Congestion_Pricing',
                       'BP_Tolls_On_Congested_Freeways_2035',
                       'BP_Vision_Zero',
                       'RRSP_East_West_Connector',
                       'EXP_Blueprint',
                       'Transform_I680_Multimodal_Imp',
                       'FBP_SM_022_I380_Widening',
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'3'"}},
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'4'"}},
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'5'"}},
                       {'name':'EXP_uncommitted_all', 'kwargs':{'MODELYEAR':'2035'}}],
                'trn':['MAJ_MuniForward_Uncommitted',
                       'RRSP_South_East_Waterfront_Transit_Imp',
                       'FBP_MU_062_ReX_Red',
                       'Transform_I680_Multimodal_Imp',
                       'Transform_SeamlessTransit',
                       'MAJ_Treasure_Island_Congestion_Pricing',
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'3'"}},
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'4'"}},
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'5'"}}]
        }),
        (2040, {'hwy':['BP_Vision_Zero',
                       'FBP_SC_050_I680_Montague_Int_Imp', 
                       'EXP_Blueprint',
                       'FBP_MU_029_ACRapid_2040',
                       'FBP_NP_074_SoscolWide',
                       'FBP_CC_059_PittAntiochWide',
                       'FBP_CC_051_SR4_Operation_Improvements_WB',
                       'FBP_CC_037_680_AuxLanes',
                       'RRSP_EC_Cap_Imp_ECR_Bus',
                       'MAJ_SR_239',
                       'FBP_NP_033_Napa_PNR_Lots',
                       'FBP_CC_018_BRT_Brentwood',
                       'MAJ_ElCaminoReal_BRT',
                       {'name':'FBP_CC_040_041_042_I680_SR4_Int_Phases_1_2_4_5','kwargs':{'PHASE':"'5'"}},
                       {'name':'EXP_uncommitted_all', 'kwargs':{'MODELYEAR':'2040'}}],
                'trn':[{'name':'FBP_MU_046_ACE_Freq_Inc', 'kwargs':{'MODELYEAR':'2040'}},
                       'MAJ_Vasona_LRT_Extension',
                       'FBP_MU_029_ACRapid_2040',
                       'RRSP_EC_Cap_Imp_ECR_Bus',
                       'MAJ_SJC_People_Mover',
                       'FBP_NP_028_NapaVineRegRoutesFrequency',
                       'FBP_NP_034_NapaVineRegExpServiceHrs',
                       'FBP_NP_029_NapaVineLocExpServiceHrs',
                       'FBP_NP_033_Napa_PNR_Lots',
                       'FBP_CC_018_BRT_Brentwood',
                       'MAJ_ElCaminoReal_BRT']
        }),
        (2045, {'hwy':['BP_Vision_Zero',
                       'EXP_Blueprint',
                       {'name':'EXP_uncommitted_all', 'kwargs':{'MODELYEAR':'2045'}}],
                'trn':[{'name':'FBP_MU_046_ACE_Freq_Inc', 'kwargs':{'MODELYEAR':'2045'}},
                       'FBP_SC_106_VTA_LRT_Modernization']
        }),
        (2050, {'hwy':['BP_Vision_Zero',
                       'EXP_Blueprint',
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'6'"}},
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'7'"}},
                       'FBP_SC_028_Stevens_Creek_LRT'],
                'trn':[{'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'6'"}},
                       {'name':'MAJ_SOL070020_I80_I680_SR12_Int_2B_7','kwargs':{'PHASE':"'7'"}},
                       'FBP_SC_028_Stevens_Creek_LRT']
        })
    ])


# Put them together for NETWORK_PROJECTS
NETWORK_PROJECTS   = collections.OrderedDict()

for YEAR in COMMITTED_PROJECTS.keys():
    if BP_VARIANT == "Baseline":
        # baseline: just committed
        NETWORK_PROJECTS[YEAR] = {
            'hwy':COMMITTED_PROJECTS[YEAR]['hwy'],
            'trn':COMMITTED_PROJECTS[YEAR]['trn']
        }
        # todo: add sea level rise since it's unprotected

    elif BP_VARIANT == "Blueprint":
        # blueprint basic: baseline plus blueprint projects, some seal level rise effects
        NETWORK_PROJECTS[YEAR] = {
            'hwy':COMMITTED_PROJECTS[YEAR]['hwy'] + BLUEPRINT_PROJECTS[YEAR]['hwy'],
            'trn':COMMITTED_PROJECTS[YEAR]['trn'] + BLUEPRINT_PROJECTS[YEAR]['trn']
        }

    # NOTE: SLR and crossings are handled in build_network_mtc_blueprint.py

#
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
