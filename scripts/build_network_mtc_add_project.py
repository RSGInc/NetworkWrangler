import argparse,collections,copy,datetime,os,pandas,re,shutil,sys,time
import Wrangler

USAGE = """

  Builds a network plus project, given a base network and a project and project_short_id.

  Creates PPA_DIR\project_short_id
    with subdirs BASE_DIR_project_short_id

"""
PPA_DIR = "M:\Application\Model One\RTP2021\ProjectPerformanceAssessment\Projects"

def findBaseDirectory(future):
    """
    Returns the highest version base directory for the given future.
    Right now, that just means sorting alphabetically and returning the last one.

    Returns just the dirname (not full path)
    """
    dir_list = sorted(os.listdir(PPA_DIR))

    model_id_re = re.compile("^2050_TM151_PPA_(BF|CG|RT)_(.*)")
    return_dir  = None

    for dirname in dir_list:
        match = model_id_re.match(dirname)
        if match == None: continue
        future_code = match.group(1)
        run_version = match.group(2)

        if future=="CleanAndGreen" and future_code=="CG":
            return_dir = dirname
        elif future=="RisingTides" and future_code=="RT":
            return_dir = dirname
        elif future=="BackToTheFuture" and future_code=="BF":
            return_dir = dirname

    return return_dir

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=USAGE, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("future", choices=["CleanAndGreen", "RisingTides", "BackToTheFuture"], help="Specify which Future Scenario for which to create networks")
    parser.add_argument("--hwy", dest='hwy', action='store_true', help="Pass if project is a roadway project")
    parser.add_argument("--trn", dest='trn', action='store_true', help="Pass if project is a transit project")
    parser.add_argument("project_short_id", help="Short ID of project, to be used for directory")
    parser.add_argument("project", help="Project to add", nargs="+")
    args = parser.parse_args()

    if not args.hwy and not args.trn:
        print("Project must be roadway, transit or both.  Please specify --hwy and/or --trn")
        sys.exit(2)

    NOW              = time.strftime("%Y%b%d.%H%M%S")
    PROJECT          = "PPA"
    SCENARIO         = args.future
    NETWORK_BASE_DIR = r"M:\\Application\\Model One\\NetworkProjects"
    HWY_NET_NAME     = "freeflow.net"
    TRN_NET_NAME     = "transitLines"
    BASE_DIR         = findBaseDirectory(args.future)   # e.g. 2050_TM150_PPA_BF_00
    PIVOT_DIR        = os.path.join(PPA_DIR, BASE_DIR, "INPUT")  # full path of input network
    SUFFIX_NUM       = 0  # suffix for this network
    TRANSIT_CAPACITY_DIR = os.path.join(PIVOT_DIR, "trn")

    OUTPUT_DIR       = os.path.join(PPA_DIR, args.project_short_id)
    # make OUTPUT_DIR
    if not os.path.exists(OUTPUT_DIR): os.mkdir(OUTPUT_DIR)

    # move into it so the log is here
    os.chdir(OUTPUT_DIR)

    LOG_FILENAME     = "addproject_{}_{}_{}_{}.info.LOG".format(PROJECT, SCENARIO, args.project_short_id, NOW)
    Wrangler.setupLogging(LOG_FILENAME, LOG_FILENAME.replace("info", "debug"))


    Wrangler.WranglerLogger.info("Using base directory {}".format(PIVOT_DIR))

    # Create a scratch directory to check out project repos into
    SCRATCH_SUBDIR   = "scratch"
    TEMP_SUBDIR      = "Wrangler_tmp_" + NOW    
    if not os.path.exists(SCRATCH_SUBDIR): os.mkdir(SCRATCH_SUBDIR)
    os.chdir(SCRATCH_SUBDIR)

    networks = {
        'hwy' :Wrangler.HighwayNetwork(modelType=Wrangler.Network.MODEL_TYPE_TM1, modelVersion=1.0,
                                       basenetworkpath=os.path.join(PIVOT_DIR,"hwy"),
                                       networkBaseDir=NETWORK_BASE_DIR,
                                       networkProjectSubdir=None,
                                       networkSeedSubdir=None,
                                       networkPlanSubdir=None,
                                       isTiered=True,
                                       tag=None,
                                       tempdir=TEMP_SUBDIR,
                                       networkName="hwy",
                                       tierNetworkName=HWY_NET_NAME),
        'trn':Wrangler.TransitNetwork( modelType=Wrangler.Network.MODEL_TYPE_TM1, modelVersion=1.0,
                                       basenetworkpath=os.path.join(PIVOT_DIR,"trn"),
                                       networkBaseDir=NETWORK_BASE_DIR,
                                       networkProjectSubdir=None,
                                       networkSeedSubdir=None,
                                       networkPlanSubdir=None,
                                       isTiered=True,
                                       networkName=TRN_NET_NAME)
    }
    if TRANSIT_CAPACITY_DIR:
        Wrangler.TransitNetwork.capacity = Wrangler.TransitCapacity(directory=TRANSIT_CAPACITY_DIR)

    # figure out the directory for writing networks
    while True:
      OUTPUT_FUTURE_DIR = os.path.join(OUTPUT_DIR, "{}_{}_{:02d}".format(BASE_DIR, args.project_short_id, SUFFIX_NUM))
      if os.path.exists(OUTPUT_FUTURE_DIR):
        Wrangler.WranglerLogger.info("OUTPUT_FUTURE_DIR {} exists -- iterating".format(OUTPUT_FUTURE_DIR))
        SUFFIX_NUM += 1
      else:
        Wrangler.WranglerLogger.info("OUTPUT_FUTURE_DIR is {}".format(OUTPUT_FUTURE_DIR))
        os.mkdir(OUTPUT_FUTURE_DIR)
        break

    for netmode in ["hwy","trn"]:
        # if applying project
        if (netmode == "hwy" and args.hwy) or (netmode == "trn" and args.trn):

            # iterate through projects specified, since args.project is a list
            for my_project in args.project:

                Wrangler.WranglerLogger.info("Applying project [%s] of type [%s]" % (my_project, netmode))
                cloned_SHA1 = networks[netmode].cloneProject(networkdir=my_project, tag=None,
                                                             projtype="project", tempdir=TEMP_SUBDIR)
                (parentdir, networkdir, gitdir, projectsubdir) = networks[netmode].getClonedProjectArgs(my_project, None, "project", TEMP_SUBDIR)

                applied_SHA1 = networks[netmode].applyProject(parentdir, networkdir, gitdir, projectsubdir)

        # write networks
        final_path = os.path.join(OUTPUT_FUTURE_DIR,netmode)
        if not os.path.exists(final_path): os.makedirs(final_path)

        if netmode=="hwy":
            networks['hwy'].write(path=final_path,name=HWY_NET_NAME,suppressQuery=True,
                                  suppressValidation=True) # MTC doesn't have turn penalties
        else:
            networks['trn'].write(path=final_path,
                                  name=TRN_NET_NAME,
                                  writeEmptyFiles = False,
                                  suppressQuery = False,
                                  suppressValidation = False,
                                  cubeNetFileForValidation = os.path.join(os.path.abspath(OUTPUT_FUTURE_DIR), "hwy", HWY_NET_NAME))
            # Write the transit capacity configuration
            Wrangler.TransitNetwork.capacity.writeTransitVehicleToCapacity(directory = final_path)
            Wrangler.TransitNetwork.capacity.writeTransitLineToVehicle(directory = final_path)
            Wrangler.TransitNetwork.capacity.writeTransitPrefixToVehicle(directory = final_path)

    Wrangler.WranglerLogger.debug("Successfully completed running %s" % os.path.abspath(__file__))

