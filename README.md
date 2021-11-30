# AntarcticSeaIce_NatCommun
Jupyter notebooks to reproduce the main figures of the paper by Rackow et al. (2021)

# Directory structure
```
└─ notebooks/:
|   └─ Figure1.ipynb: Read data and reproduce Figure 1 (R script)
|   └─ Figure2.ipynb: Read data and reproduce figure
|   └─ Figure3a.ipynb: Read data and reproduce panel a) in Figure 3
|   └─ Figure3b.ipynb: Read data and reproduce panel b) in Figure 3
|   └─ Figure4.ipynb: Read data and reproduce all panels of Figure 4 (except sea ice in panel a))
|   └─ Figure4_NSIDCice.ipynb: Read data and reproduce sea ice in panel a) of Figure 4
|   └─ colorbars.py: continues some colorbars
└─ data/:
|   └─ Figure1.csv: data for Figure 1
|   └─ data_Fig2.pickle: data for Figure 2
|   └─ data_Fig3a.pickle: data for Figure 3, panel a
|   └─ data_Fig3b.pickle: data for Figure 3, panel b
|   └─ data_Fig4.pickle: data for Figure 4 (except ice), all panels
|   └─ data_Fig4_ice.pickle: HR and LR sea ice data for Figure 4, panels b and c
|   └─ mean.sep.1979-2020.s.bil: OBS sea ice data for Figure 4, panel a
|   └─ ...: more data
```
https://github.com/trackow/AntarcticSeaIce_NatCommun/blob/main/data/
# Jupyter notebooks
Interactive jupyter notebook are provided to reproduce the figures of this paper. You can install [Jupyter](https://jupyter.org/) and then launch the notebooks [here](https://github.com/trackow/AntarcticSeaIce_NatCommun/blob/main/notebooks/).

# Packages to install

Download e.g. a miniconda installer from [here](https://docs.conda.io/en/latest/miniconda.html#macos-installers) and then type
```
conda create -n natcommun netCDF4 numpy matplotlib xarray scipy
conda install -c anaconda basemap
conda install jupyter python=3.8
```
to create a "natcommun" environment with necessary dependencies.

To install an R kernel for Figure 1, you can follow the instructions [here](https://richpauloo.github.io/2018-05-16-Installing-the-R-kernel-in-Jupyter-Lab/).
