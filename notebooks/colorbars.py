import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

cdict = {'red':   ((0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)),

         'green': ((0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
		   (1.0,  0.0, 0.0)),

         'blue':  ((0.0,  1.0, 1.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  0.0, 0.0))
	}	
blue_red = LinearSegmentedColormap('BlueRed', cdict, 25)
plt.register_cmap(cmap=blue_red)

cdict = {'red':   ((0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)),

         'green': ((0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
		   (1.0,  0.0, 0.0)),

         'blue':  ((0.0,  1.0, 1.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  0.0, 0.0))
	}	
blue_red_more = LinearSegmentedColormap('BlueRedMore', cdict, 50)
plt.register_cmap(cmap=blue_red_more)

cdict = {'red':   ((0.0,  0.29, 0.29),
                   (1.1/6.,  0.0, 0.0),
                   (2.2/6.,  0.0, 0.0),
                   (3./6.,  1.0, 1.0),
                   (3.8/6.,  1.0, 1.0),
                   (4.9/6.,  1.0, 1.0),
                   (1.0,  0.55, 0.55)),

         'green':   ((0.0,  0.0, 0.0),
                   (1.1/6.,  0.0, 0.0),
                   (2.2/6.,  1.0, 1.0),
                   (3./6.,  1.0, 1.0),
                   (3.8/6.,  1.0, 1.0),
                   (4.9/6.,  0.0, 0.0),
                   (1.0,  0.27, 0.27)),

         'blue':   ((0.0,  0.51, 0.51),
                   (1.1/6.,  1.0, 1.0),
                   (2.2/6.,  0.0, 0.0),
                   (3./6.,  1.0, 1.0),
                   (3.8/6.,  0.0, 0.0),
                   (4.9/6.,  0.0, 0.0),
                   (1.0,  0.07, 0.07))
	}	
PurpleBlueGreenWhiteYellowRedBrown = LinearSegmentedColormap('PurpleBlueGreenWhiteYellowRedBrown', cdict, 256)
plt.register_cmap(cmap=PurpleBlueGreenWhiteYellowRedBrown)

cdict = {'red':   ((0.0,  0.0, 0.0),
                   (1./4.,  1.0, 1.0),
                   (1.8/4.,  1.0, 1.0),
                   (2.9/4.,  1.0, 1.0),
                   (1.0,  0.29, 0.29)),

         'green':  ((0.0,  0.0, 0.0),
                   (1./4.,  1.0, 1.0),
                   (1.8/4.,  1.0, 1.0),
                   (2.9/4.,  0.0, 0.0),
                   (1.0,  0.0, 0.0)),

         'blue':   ((0.0,  1.0, 1.0),
                   (1./4.,  1.0, 1.0),
                   (1.8/4.,  0.0, 0.0),
                   (2.9/4.,  0.0, 0.0),
                   (1.0,  0.51, 0.51))
	}	
BlueWhiteYellowRedPurple = LinearSegmentedColormap('BlueWhiteYellowRedPurple', cdict, 256)
plt.register_cmap(cmap=BlueWhiteYellowRedPurple)
BlueWhiteYellowRedPurple13 = LinearSegmentedColormap('BlueWhiteYellowRedPurple13', cdict, 13)
plt.register_cmap(cmap=BlueWhiteYellowRedPurple13)


############################################################################
# define colorbar for biases etc.

hi_color= 'FF3333' # red
mi2_color='FFCCCC' # light red
mi1_color='FFFFFF' # white
mi0_color='CCCCFF' # light blue
lo_color= '3333FF' # blue

# (half) interval
white_mi=0.5
white_sp=0.02
#white_sp=0.1

# ------------------------------------------------------------------------ #

HEX = '0123456789abcdef'
HEX2 = dict((a+b, HEX.index(a)*16 + HEX.index(b)) for a in HEX for b in HEX)
def rgb(triplet):
    triplet = triplet.lower()
    return (HEX2[triplet[0:2]], HEX2[triplet[2:4]], HEX2[triplet[4:6]])

def triplet(rgb):
    return format((rgb[0]<<16)|(rgb[1]<<8)|rgb[2], '06x')

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi=rgb(hi_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo=rgb(lo_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0


#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo[0]/norm),
                   (white_mi-white_sp,  mi0[0]/norm, 	mi0[0]/norm),
	           (white_mi,  		mi1[0]/norm, 	mi1[0]/norm),
		   (white_mi+white_sp,  mi2[0]/norm, 	mi2[0]/norm),
                   (hi_b,  		hi[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo[1]/norm),
		   (white_mi-white_sp,  mi0[1]/norm, 	mi0[1]/norm),
                   (white_mi,  		mi1[1]/norm, 	mi1[1]/norm),
		   (white_mi+white_sp,  mi2[1]/norm, 	mi2[1]/norm),
            	   (hi_b,  		hi[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo[2]/norm),
		   (white_mi-white_sp,  mi0[2]/norm, 	mi0[2]/norm),
                   (white_mi,  		mi1[2]/norm, 	mi1[2]/norm),
		   (white_mi+white_sp,  mi2[2]/norm, 	mi2[2]/norm),
                   (hi_b,  		hi[2]/norm, 	dummy))
     	}

light_blue_red = LinearSegmentedColormap('LightBlueRed', cdict, 20)
plt.register_cmap(cmap=light_blue_red)




############################################################################
# colorbar for barotropic streamfunction

# define colorbar (baro. streamfunc.)
hi_color= 'FFFF00' # yellow
mi2_color='FF9900' # orange
mi1_color='FF0000' # red
mi0_color='00FFFF' # white
lo_color= '0000FF' # blue
# position of middle color (mi1)
pos_mid=0.62
# place mi2 & mi0 relative to mi1
dx_up=0.19
dx_do=-0.31

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi=rgb(hi_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo=rgb(lo_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
                   (hi_b,  		hi[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
            	   (hi_b,  		hi[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
                   (hi_b,  		hi[2]/norm, 	dummy))
     	}

blue_red_yellow = LinearSegmentedColormap('BlueRedYellow', cdict)
plt.register_cmap(cmap=blue_red_yellow)

############################################################################
# colorbar for APPOSITE sea ice concentration

# define colorbar (baro. streamfunc.)
hi_color= 'FFFFFF' # white
mi2_color='66CCFF' # 
mi1_color='66CCFF' # light blue
mi0_color='66CCFF' # 
lo_color= '000066' # dark blue
# position of middle color (mi1)
pos_mid=0.5
# place mi2 & mi0 relative to mi1
dx_up=0.0
dx_do=-0.0

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi=rgb(hi_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo=rgb(lo_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
                   (hi_b,  		hi[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
            	   (hi_b,  		hi[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
                   (hi_b,  		hi[2]/norm, 	dummy))
     	}

sea_ice_concentration = LinearSegmentedColormap('SeaIceConcentration', cdict, 10)
plt.register_cmap(cmap=sea_ice_concentration)


############################################################################
# colorbar for APPOSITE sea ice thickness

# define colorbar (baro. streamfunc.)
hi_color= 'FF0B0B' # dark red
#hi_color= 'FF0000' # red
mi2_color='FFFF33' # yellow
mi1_color='339900' # green
mi0_color='66CCFF' # light blue
lo_color= 'FFFFFF' # white
# position of middle color (mi1)
pos_mid=0.45
# place mi2 & mi0 relative to mi1
dx_up=0.10
dx_do=-0.25

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi=rgb(hi_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo=rgb(lo_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
                   (hi_b,  		hi[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
            	   (hi_b,  		hi[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
                   (hi_b,  		hi[2]/norm, 	dummy))
     	}

sea_ice_thickness = LinearSegmentedColormap('SeaIceThickness', cdict, 17)
plt.register_cmap(cmap=sea_ice_thickness)

############################################################################
# colorbar for SSTs

# define colorbar
hi_color= 'E60000' # dark red
mi2_color='FFFF00' # yellow
mi1_color='FFFFFF' # white
mi0_color='0066FF' #'66CCFF' # light blue
lo_color= 'CC0099' # violet
# position of middle color (mi1)
pos_mid=0.7
# place mi2 & mi0 relative to mi1
dx_up=0.05
dx_do=-0.3 #-0.3

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi=rgb(hi_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo=rgb(lo_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
                   (hi_b,  		hi[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
            	   (hi_b,  		hi[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
                   (hi_b,  		hi[2]/norm, 	dummy))
     	}

sea_surface_temperatures = LinearSegmentedColormap('SeaSurfaceTemperature', cdict, 17)
plt.register_cmap(cmap=sea_surface_temperatures)

############################################################################
# colorbar for SST standard deviations

# define colorbar
hi1_color= 'FF0000' # red
hi0_color= 'FF0000' # red
mi2_color='FFFF00' # yellow
mi1_color='33CC33' # green
mi0_color='478947' # darkgreen
lo1_color= 'ACC2D6' #'89A8C5' # gray-blue, darker: '7C9EBF'
lo0_color= 'FFFFFF' # white
# position of middle color (mi1)
pos_mid=0.6
# place mi2 & mi0 relative to mi1
dx_up=0.1
dx_do=-0.1
# place hi0 and lo1 relative to hi1 and lo0
lo_up=0.3
hi_do=-0.1

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi1=rgb(hi1_color)
hi0=rgb(hi0_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo1=rgb(lo1_color)
lo0=rgb(lo0_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo0[0]/norm),
		   (low_b+lo_up,  	lo1[0]/norm, 	lo1[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
		   (hi_b+hi_do,  	hi0[0]/norm, 	hi0[0]/norm),
                   (hi_b,  		hi1[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo0[1]/norm),
		   (low_b+lo_up,  	lo1[1]/norm, 	lo1[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
		   (hi_b+hi_do,  	hi0[1]/norm, 	hi0[1]/norm),
            	   (hi_b,  		hi1[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo0[2]/norm),
		   (low_b+lo_up,  	lo1[2]/norm, 	lo1[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
		   (hi_b+hi_do,  	hi0[2]/norm, 	hi0[2]/norm),
                   (hi_b,  		hi1[2]/norm, 	dummy))
     	}

sst_standard_deviations = LinearSegmentedColormap('SSTStandardDeviations', cdict, 256)
plt.register_cmap(cmap=sst_standard_deviations)

############################################################################
# colorbar for DPP (modified from SST-sd)

# define colorbar
hi1_color= 'FF0000' # red
hi0_color= 'FF7700' # orange
mi2_color='FFFF00' # yellow
mi1_color='33CC33' # green
mi0_color='478947' # darkgreen
lo1_color= 'ACC2D6' #'89A8C5' # gray-blue, darker: '7C9EBF'
lo0_color= 'FFFFFF' # white
# position of middle color (mi1)
pos_mid=0.5
# place mi2 & mi0 relative to mi1
dx_up=1./6.
dx_do=-1./6.
# place hi0 and lo1 relative to hi1 and lo0
lo_up=1./6.
hi_do=-1./6.

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi1=rgb(hi1_color)
hi0=rgb(hi0_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo1=rgb(lo1_color)
lo0=rgb(lo0_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo0[0]/norm),
		   (low_b+lo_up,  	lo1[0]/norm, 	lo1[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
		   (hi_b+hi_do,  	hi0[0]/norm, 	hi0[0]/norm),
                   (hi_b,  		hi1[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo0[1]/norm),
		   (low_b+lo_up,  	lo1[1]/norm, 	lo1[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
		   (hi_b+hi_do,  	hi0[1]/norm, 	hi0[1]/norm),
            	   (hi_b,  		hi1[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo0[2]/norm),
		   (low_b+lo_up,  	lo1[2]/norm, 	lo1[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
		   (hi_b+hi_do,  	hi0[2]/norm, 	hi0[2]/norm),
                   (hi_b,  		hi1[2]/norm, 	dummy))
     	}

cmap_dpp = LinearSegmentedColormap('DPP_colormap', cdict, 256)
plt.register_cmap(cmap=cmap_dpp)
iceberg_input_cmap = LinearSegmentedColormap('IcebergInput', cdict, 8)
plt.register_cmap(cmap=iceberg_input_cmap)
iceberg_input_cmap256 = LinearSegmentedColormap('IcebergInput256', cdict, 256)
plt.register_cmap(cmap=iceberg_input_cmap256)

############################################################################
# colorbar for correlations

# define colorbar
hi1_color= '990000' # red
hi0_color= 'FF3300' # orange
mi2_color='FFFF75' # light yellow
mi1_color='FFFFFF' # white
mi0_color='99EBFF' # light blue
lo1_color= '333399' # lila
lo0_color= 'CC0099' # violet
# position of middle color (mi1)
pos_mid=0.5
# place mi2 & mi0 relative to mi1
dx_up=0.1
dx_do=-0.1
# place hi0 and lo1 relative to hi1 and lo0
lo_up=0.2
hi_do=-0.25

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi1=rgb(hi1_color)
hi0=rgb(hi0_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo1=rgb(lo1_color)
lo0=rgb(lo0_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo0[0]/norm),
		   (low_b+lo_up,  	lo1[0]/norm, 	lo1[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
		   (hi_b+hi_do,  	hi0[0]/norm, 	hi0[0]/norm),
                   (hi_b,  		hi1[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo0[1]/norm),
		   (low_b+lo_up,  	lo1[1]/norm, 	lo1[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
		   (hi_b+hi_do,  	hi0[1]/norm, 	hi0[1]/norm),
            	   (hi_b,  		hi1[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo0[2]/norm),
		   (low_b+lo_up,  	lo1[2]/norm, 	lo1[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
		   (hi_b+hi_do,  	hi0[2]/norm, 	hi0[2]/norm),
                   (hi_b,  		hi1[2]/norm, 	dummy))
     	}

cmap_correlations = LinearSegmentedColormap('Correlations', cdict, 21) #256
plt.register_cmap(cmap=cmap_correlations)

############################################################################
# colorbar for correlations (256)

# define colorbar
hi1_color= '990000' # red
hi0_color= 'FF3300' # orange
mi2_color='FFFF75' # light yellow
mi1_color='FFFFFF' # white
mi0_color='99EBFF' # light blue
lo1_color= '333399' # lila
lo0_color= 'CC0099' # violet
# position of middle color (mi1)
pos_mid=0.5
# place mi2 & mi0 relative to mi1
dx_up=0.1
dx_do=-0.1
# place hi0 and lo1 relative to hi1 and lo0
lo_up=0.2
hi_do=-0.25

# ------------------------------------------------------------------------ #

# convert hex to RGB
hi1=rgb(hi1_color)
hi0=rgb(hi0_color)
mi2=rgb(mi2_color)
mi1=rgb(mi1_color)
mi0=rgb(mi0_color)
lo1=rgb(lo1_color)
lo0=rgb(lo0_color)

# do not change
norm=255.0
dummy=0.0
low_b=0.0
hi_b=1.0

#	           	level		value<level	value>level

cdict = {'red':   ((low_b,  		dummy, 		lo0[0]/norm),
		   (low_b+lo_up,  	lo1[0]/norm, 	lo1[0]/norm),
                   (pos_mid+dx_do,  	mi0[0]/norm, 	mi0[0]/norm),
	           (pos_mid,  		mi1[0]/norm, 	mi1[0]/norm),
		   (pos_mid+dx_up,  	mi2[0]/norm, 	mi2[0]/norm),
		   (hi_b+hi_do,  	hi0[0]/norm, 	hi0[0]/norm),
                   (hi_b,  		hi1[0]/norm, 	dummy)),

         'green': ((low_b,  		dummy, 		lo0[1]/norm),
		   (low_b+lo_up,  	lo1[1]/norm, 	lo1[1]/norm),
		   (pos_mid+dx_do,  	mi0[1]/norm, 	mi0[1]/norm),
                   (pos_mid,  		mi1[1]/norm, 	mi1[1]/norm),
		   (pos_mid+dx_up,  	mi2[1]/norm, 	mi2[1]/norm),
		   (hi_b+hi_do,  	hi0[1]/norm, 	hi0[1]/norm),
            	   (hi_b,  		hi1[1]/norm, 	dummy)),

         'blue':  ((low_b,  		dummy, 		lo0[2]/norm),
		   (low_b+lo_up,  	lo1[2]/norm, 	lo1[2]/norm),
		   (pos_mid+dx_do,  	mi0[2]/norm, 	mi0[2]/norm),
                   (pos_mid,  		mi1[2]/norm, 	mi1[2]/norm),
		   (pos_mid+dx_up,  	mi2[2]/norm, 	mi2[2]/norm),
		   (hi_b+hi_do,  	hi0[2]/norm, 	hi0[2]/norm),
                   (hi_b,  		hi1[2]/norm, 	dummy))
     	}

cmap_correlations256 = LinearSegmentedColormap('Correlations', cdict, 256) #256
plt.register_cmap(cmap=cmap_correlations256)

# Rusul's adjusted colormap with more white space:
cdict ={'blue':((0.0, 100.0/255.0, 100.0/255.0 ),
       (0.2, 1.0, 1.0  ),
       (0.4, 1.0, 1.0),
       (0.5, 1.0, 1.0),
       (0.6, 1.0, 0.4588235294117647),
       (0.75,0.0, 0.0),
       (1.0, 0.0, 0.0)),

   'green':((0.0,2.0/255.0,2.0/255.0),
       (0.2, 0.0, 0.0),
       (0.4, 1.0, 1.0),
       (0.5, 1.0, 1.0),
       (0.6, 1.0, 1.0),
       (0.75,0.2, 0.2),
       (1.0, 0.0, 0.0)),

   'red' :((0.0, 78.0/255.0, 78.0/255.0),
       (0.2, 0.0, 0.0),#here
       (0.4, 1.0, 1.0),
       (0.5, 1.0, 1.0),
       (0.6, 1.0, 1.0),
       (0.75,1.0, 1.0),
       (1.0, 0.6, 0.0))}


cmap_correlations_white = LinearSegmentedColormap('CustomMap', cdict)
plt.register_cmap(cmap=cmap_correlations_white)