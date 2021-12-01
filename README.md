# AntarcticSeaIce_NatCommun
Jupyter notebooks to reproduce the main figures of the paper by Rackow et al. (2021)

# Directory structure
```
└─ notebooks/:
|   └─ Figure1.ipynb: Read data and reproduce Figure 1 (R script)
|   └─ Figure2.ipynb: Read data and reproduce Figure 2
|   └─ Figure3a.ipynb: Read data and reproduce panel a) in Figure 3
|   └─ Figure3b.ipynb: Read data and reproduce panel b) in Figure 3
|   └─ Figure3c.ipynb: Read data and reproduce panel c) in Figure 3
|   └─ Figure4.ipynb: Read data and reproduce all panels of Figure 4 (except sea ice in panel a))
|   └─ Figure4_NSIDCice.ipynb: Read data and reproduce sea ice in panel a) of Figure 4
|   └─ Figure5ad.ipynb: Read data and reproduce panels a) and d) of Figure 5
|   └─ Figure5bcef.ipynb: Read data and reproduce panels b), c) and e),f) of Figure 5
|   └─ colorbars.py: contains some colorbars
└─ data/:
|   └─ Figure1.csv: data for Figure 1
|   └─ data_Fig2.pickle: data for Figure 2
|   └─ data_Fig3a.pickle: data for Figure 3, panel a)
|   └─ data_Fig3b.pickle: data for Figure 3, panel b)
|   └─ data_Fig3c_HR.pickle: HR data for Figure 3, panel c) (use git lfs)
|   └─ data_Fig3c_LR.pickle: LR data for Figure 3, panel c)
|   └─ data_Fig4.pickle: data for Figure 4 (except ice), all panels (use git lfs)
|   └─ data_Fig4_ice.pickle: HR and LR sea ice data for Figure 4, panels b) and c)
|   └─ mean.sep.1979-2020.s.bil: OBS sea ice data for Figure 4, panel a)
|   └─ data_Fig5a.pickle: model data for Figure 5, panel a)
|   └─ data_Fig5d.pickle: model data for Figure 5, panel d)
|   └─ CMIP5_OHF_ensmeans_allmodels_1990-2019.csv: CMIP5 meridional heat flux, 1990-2019 for Fig. 5d
|   └─ CMIP5_OHF_ensmeans_allmodels_2070-2099.csv: CMIP5 meridional heat flux, 2070-2099 for Fig. 5d
|   └─ data_Fig5bcef.pickle: model data for Figure 5, panels b),c) and e),f)
|   └─ CMIP5_iceedge_latitudes_1990-2019.csv: CMIP5 location of sea ice edge, 1990-2019 for Fig. 5e
|   └─ CMIP5_iceedge_latitudes_2070-2099.csv: CMIP5 location of sea ice edge, 2070-2099 for Fig. 5e
|   └─ ...: some more data
```
# Jupyter notebooks
Interactive jupyter notebook are provided to reproduce the figures of this paper. You can install [Jupyter](https://jupyter.org/) and then launch the notebooks [here](https://github.com/trackow/AntarcticSeaIce_NatCommun/blob/main/notebooks/).

# Packages to install

Download e.g. a miniconda installer from [here](https://docs.conda.io/en/latest/miniconda.html#macos-installers) and then type
```
conda create -n natcommun netCDF4 numpy matplotlib xarray scipy
conda install -c anaconda basemap
conda install jupyter python=3.8
conda install seawater joblib
conda install cmocean
```
to create a "natcommun" environment with necessary dependencies. 

# Further information
In order to plot Figure 4, the [pyfesom](https://pyfesom.readthedocs.io/en/latest/installation.html) package needs to be installed and the path to your local installation
included:
```
import sys
sys.path.append("/path/to/pyfesom/")
import pyfesom as pf
```
To install an R kernel for Figure 1, you can follow the instructions [here](https://richpauloo.github.io/2018-05-16-Installing-the-R-kernel-in-Jupyter-Lab/).
In order to run Figure4_NSIDCice.ipynb, you need to have 'gdal' installed. This can sometimes be [problematic](https://stackoverflow.com/questions/33574902/install-gdal-using-conda) on some operating systems like macOS, but you can try the following recipe:
```
conda create -n gdal python=3.8
conda activate gdal
conda install -c conda-forge gdal
conda install numpy matplotlib 
conda install jupyter
```
