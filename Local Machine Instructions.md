# Intro

This code has been updated to run on a laptop that has Cube Voyager 6.5.0 installed locally. This is primarily the removal and override of anything that appears to be MTC specific (e.g. paths to cube hostnames and a batch file used when calling runtpp).

Questions can be directed to Andrew Rohne at RSG (andrew.rohne (at) rsginc.com). 9/20/2023.

# Setting Up Cube

The computer's path needs to include the path to Cube Voyager to use an executable there. Follow [these instructions](https://www.computerhope.com/issues/ch000549.htm) for your OS version, add C:\Program Files\Citilabs\CubeVoyager to the path.

To test this, open any command prompt () and type `runtpp`. There should be an error that says "Error in Arg 1: (null)".

# Setting Up Network Wrangler
1. Download the [Anaconda environment](https://github.com/RSGInc/travel-model-one/blob/transit_2050/tm15-python310.yml) to a location on your hard drive.
1. Created the local Anaconda environment. Open Anaconda Prompt or Anaconda Powershell (either will work, hereinafter referred to as Anaconda Prompt) and type:
    `cd path\you\downloaded\the\above\file\to`
    `conda create -f tm15-python310.yml`
2. Switched to it. Use the following command in the Anaconda prompt
    `conda activate tm15-python310`
3. Change directories to an appropriate location on your hard drive.
4. Clone the network Wrangler Repo
    `git clone https://github.com/RSGInc/NetworkWrangler.git`
5. Go into that folder and checkout the transit_2050 branch
    `git checkout transit_2050`
6. Install NetworkWrangler. 
    `cd NetworkWrangler`
    `pip install -e .`
7. Open python, import NetworkWrangler, ensure no errors
8. Get the base network - clone https://github.com/BayAreaMetro/TM1_2015_Base_Network to a local folder (I used C:\Models). This probably should not be done inside the network wrangler folder.
9. Get the projects from Box
    Not-RSG: From https://mtcdrive.box.com/s/unic7tf0sokleacg4fgu0dtu8ixkyfg6
    RSG: I Copied to the files folder to Sharepoint as "04_Network_Work\MTC Data\NetworkProjects_20230719.zip
    I unzipped to C:\Models\TM1_NetworkProjects
10. Also download everything on Box since July 19
    Not-RSG: use box, sort by date, select all necessary
    RSG: Copied to files folder as "04_Network_Work\MTC Data\TM1_NetworkProjects-selected.zip"
11. Set base network env var. Use these commands in an Anaconda prompt:
    `conda env config vars set "TM1_2015_Base_Network=C:\Models\TM1_2015_Base_Network"`
    `conda env config vars set "TM1_NetworkProjects=C:\Models\TM1_NetworkProjects"`
    `conda env config vars set "CUBE_HOST_FILE=C:\Models\NetworkWrangler\HostnamesWithCube.txt"`
    `conda activate NetworkWrangler`
    Note: you can test these using `conda env config vars list`

# Running Network Wrangler for the Base Year
1. Be in the correct Anaconda Environment (if not already)
    conda activate tm15-python310
2. Build the test network
    python .\build_network_mtc.py Test .\net_spec_test.py
    
# Adding Project Cards

---
Note: This is still being written! 
---

This largely follows [the Network Wrangler Documentation](https://github.com/BayAreaMetro/modeling-website/wiki/Network-Building-with-NetworkWrangler#step-4-build-a-network-with-your-project) but is distilled down to something a little more concise.

The basic version is to add the cards to the TM1_NetworkProjects folder, and then copy the net_spec_test.py script to something a little more descriptive (for the BART San Jose example, I used `net_spec_MAJ_BRT030001_BART_to_SanJose.py`). The script needs to have a project code, scenario (for the purposes of this project, I use `build`)

Run with `python build_network_mtc.py build net_spec_MAJ_BRT030001_BART_to_SanJose.py`

## Determine Pre-requisite Projects



# Notes and Errors

## Pre-requisite Projects

If you see this: `WranglerLogger: DEBUG    !!!WARNING!!! Some PRE-REQUISITES were not found or ordered correctly.  Continue anyway? (y/n)`, that means you're missing one or more projects and these projects are required for the project you're using to work. Listed above this, you'll see the pre-requisite projects:

```
WranglerLogger: INFO     Requirement verification - Pre-requisite
WranglerLogger: INFO         Year    Project                                                Pre-requisite Project                              Year
WranglerLogger: INFO     trn 2020.trn.01 MAJ_BRT030001_BART_to_SanJose                      trn ALA050015_BART_to_WarmSprings                      -1
WranglerLogger: INFO     trn 2020.trn.01 MAJ_BRT030001_BART_to_SanJose                      trn SCL110005_BART_to_Berryessa                        -1
```

In this case, it can be fixed by including the prerequisite projects in the appropriate network.