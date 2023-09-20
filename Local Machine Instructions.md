# Intro

This code has been updated to run on a laptop that has Cube Voyager 6.5.0 installed locally. This is primarily the removal and override of anything that appears to be MTC specific (e.g. paths to cube hostnames and a batch file used when calling runtpp).

Questions can be directed to Andrew Rohne at RSG (andrew.rohne (at) rsginc.com). 9/20/2023.

# Setting Up Network Wrangler

1. Created an Anaconda environment
    conda create --name NetworkWrangler python=3.9
2. Switched to it
     conda activate NetworkWrangler
3. Installed packages
    conda install pandas pywin32
    conda install xlrd
    pip install SimpleParse
    pip install partridge
4. Open python, import NetworkWrangler, ensure no errors
5. Get the base network - clone https://github.com/BayAreaMetro/TM1_2015_Base_Network to a local folder (I used C:\Models)
6. Get the projects from Box
    From https://mtcdrive.box.com/s/unic7tf0sokleacg4fgu0dtu8ixkyfg6
    Copied to the files folder as "04_Network_Work\MTC Data\NetworkProjects_20230719.zip
    I unzipped to C:\Models\TM1_NetworkProjects
7. Also download everything on Box since July 19
    Copied to files folder as "04_Network_Work\MTC Data\TM1_NetworkProjects-selected.zip"
8. Create a Cube hostname file called "HostnamesWithCube.txt". For local installations, that file should have the word "localhost" (no quotes) in it. 
9. Set base network env var
    conda env config vars set "TM1_2015_Base_Network=C:\Models\TM1_2015_Base_Network"
    conda env config vars set "TM1_NetworkProjects=C:\Models\TM1_NetworkProjects"
    conda env config vars set "CUBE_HOST_FILE=C:\Models\NetworkWrangler\HostnamesWithCube.txt"
    conda activate NetworkWrangler
    
# Running Network Wrangler for the Base Year

1. Be in the correct Anaconda Environment (if not already)
    conda activate NetworkWrangler
2. Build the test network
    python .\build_network_mtc.py Test .\net_spec_test.py
    
