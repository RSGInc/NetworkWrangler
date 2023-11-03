Current Branch Changes:
=======================
This branch's purpose is to be used for TM1.5.1.10 model runs.
It was created from the 9 Feb 2023 commit e95e5a3.

please contact david.hensle@rsginc.com with questions


NetworkWrangler
===============

NetworkWrangler is a python library that enables users to define roadway
and transit projects as collection of data files in a local git repository,
and then create networks by starting with a base network and applying a
set of projects to that base network.

The base network and resulting network are in the Citilabs Cube format (http://www.citilabs.com/software/cube/)

See also: [next generation Network Wrangler](https://github.com/wsp-sag/network_wrangler)

Contributors
=======
NetworkWrangler is the brainchild of Billy Charlton, who was the Deputy Director for Technology Services at SFCTA through 2011.
Contributors include:
* Elizabeth Sall, 2010-2014
* Lisa Zorn, 2010-2014, 2018-Present (MTC fork)
* Dan Tischler, 2011-Present
* Drew Cooper, 2013-Present
* Bhargava Sana, 2015-Present

Install
=======
NetworkWrangler recently was updated to Python3. Recommand using conda to install and manage NetworkWrangler environment. For example, run the following commands in Anaconda Prompt:
```
conda env create -f M:\Software\Anaconda\NetworkWrangler_py3.yml
conda activate NetworkWrangler-py3
cd \NetworkWrangler
pip install -e .
```

Usage
=======
If needed, set the PATHs before calling the build_network.py script, for example:
```
set PATH=%PATH%;C:\Users\mtcpb\.conda\envs\NetworkWrangler-py3;C:\Users\mtcpb\.conda\envs\NetworkWrangler-py3\Scripts
set PATH=%PATH%;C:\Program Files\Citilabs\CubeVoyager;
set PYTHONPATH=%PYTHONPATH%;C:\Users\mtcpb\Documents\GitHub\NetworkWrangler
set PYTHONPATH=%PYTHONPATH%;C:\Users\mtcpb\Documents\GitHub\NetworkWrangler\_static
```

With PATHs set, build a network by running the `build_network.py` script  in the `/scripts` folder.
```
python build_network.py [-c configword] [-m test] network_specification.py
```

This will build a network using the specifications in `network_specification.py`, which should define the variables listed below (in this script)
  
If test mode is specified (with -m test), then the following happen:
  * networks are built in OUT_DIR\TEST_hwy and OUT_DIR\TEST_trn
  * RTP projects are not applied
  * TAG is not used for TEST_PROJECTS
    
The [-c configword] is if you want an optional word for your network_specification.py
  (e.g. to have multiple scenarios in one file).  Access it via CONFIG_WORD.
