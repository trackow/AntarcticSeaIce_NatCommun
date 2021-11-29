# AntarcticSeaIce_NatCommun
Jupyter notebooks to reproduce the main figures of the paper by Rackow et al. (2021)

# Directory structure
```
└─ notebooks/:
|   └─ Figure1.ipynb: Read data and reproduce Figure 1 (R script)
|   └─ Figure2.ipynb: Read data and reproduce figure
|   └─ Figure3a.ipynb: Read data and reproduce panel a) in Figure 3
|   └─ colorbars.py: continues some colorbars
└─ data/:
|   └─ Figure1.csv: data for Figure 1
|   └─ data_Fig2.pickle: data for Figure 2
|   └─ data_Fig3a.pickle: data for Figure 3, panel a
|   └─ ...: more data for Figure 2
```

# Jupyter notebooks
Interactive jupyter notebook are provided to reproduce the figures of this paper. You can install [Jupyter](https://jupyter.org/) and then launch the notebooks [here](https://github.com/trackow/AntarcticSeaIce_NatCommun/blob/main/notebooks/).

# Packages to install
conda create -n natcommun netCDF4 numpy matplotlib xarray scipy \
conda install -c anaconda basemap \
conda install jupyter python=3.8
