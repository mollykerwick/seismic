#---This is an example of a specification file for running sphfdloc and 
#	associated programs
#
#	Variables are specified by inputing the variable name followed by the
#	value of that variable.
#
#	Blank lines and lines beginning with # are not read in and so may
#	be used for comments
#
#	Blanks and tabs are ignored
#
#	This file is read in and interpreted by the subroutine "parseparms"
#

	verbose  T	! Flag for verbose output to the screen (sphfdloc)
	maxretry 2	! The number of times sphfdloc will try to recover outliers after a relocation

#---In sphfdsyn.f:  if allsta = 0, just do the stations in the data file.  If =1, do P only for
#	all stations in the station list.  If = 2, do P and S for all stations in
#	the station list.
	allsta 2
#
#------Origin of the model.  This lat (y0), lon (x0), depth (z0) specifies the location of the upper
#	NW corner of the grid.
        x0   -151.384
        y0   62.7433
        z0   -30.0

#------Fine grid spacing (dq, df, h).  h is the depth spacing in km, dq and df the latitude and longitude
#	spacing in degrees.  Note that if dq and df are not specified they will be computed
#      in the software to match h for the origin chosen.
#
        h  3.0
	df 0.200
	dq 0.090


#------Coarse grid specifications
#  nxc, nyc, and nzc are the number of nodes in the x, y, and z directions
        nxc 65
        nyc 111
	nzc 74

#  These are the number of fine grid spaces between the coarse grid points.  There
#  should be at least (nxc-1) of these specified for igridx, and similar for igridy and igridz

        igridx  1 +

        igridy  1 +

        igridz  1 +

#------Lat/Lon Center of Coordinates geographic location of Cartesian (0,0) (NOT USED IN THESE ROUTINES).
        clat  -29.3
        clon  -73.0

#  sph = 1 if we are using a spherical system, 0 for cartesian
        sph     1
#  flat = 1 to work with flattened earth (transform spherical <-> cartesian)
        flat    0

#  FDLOC VARIABLES
     nthres 	 4	#  Minimum number of phases allowed 
# first run
     resthres  2.0	#  Residual threshold (absolute time)
     resthrep  20.00	#  Residual threshold (percentage time)
     stdmax    10.00     #  Standard Deviation threshold
# second run
#     resthres   1.0	#  Residual threshold (absolute time)
#     resthrep   5.00	#  Residual threshold (percentage time)
#     stdmax     1.50     #  Standard Deviation threshold
# third run
#     resthres   1.2     #  Residual threshold (absolute time)
#     resthrep   5.00    #  Residual threshold (percentage time)
#     stdmax     1.50     #  Standard Deviation threshold

#  Add an error due to model uncertainty
        pmod_err 0.20
        smod_err 0.50

# Additional used by SPHFDLOC for defining bounds
     flagout   T        #  If flagout is true, then sphfdloc will flag out of bounds events
#     depmin   -20.0     #  Minimum allowed depth
#     depmax   295.0     #  Maximum allowed depth
#     delymax  -29.5     #  Minimum Latitude
#     delymin  -32.5     #  Maximum Latitude
#     delxmax  -68.0     #  Maximum Longitude
#     delxmin  -72.8     #  Minimum Longitude

#  GENERAL VARIABLES
      doshot    0	# if = 1, process shot data
      dotel     0	# if = 1, process teleseismic data
      ittnum	1	# iteration number

# SPHFDSYN parameters
      allsta	  2	#  = 2 P&S waves at all stations in the station list.
      			#  = 1 P waves only at all stations in the station list.
			#  = 0 to reproduce the stations in the input data file

##################################################################################
#
#                          ****FILE CONNECTIONS****
#
# Table for building the 1D model (make1d).  Output from make1d goes to oldvfil.
onedfil		mod.1d
vs1d		1

# Starting Coarse model file name (P and S)
oldvfil		illap.mod1d

# Travel time directory
timedir	../../ttimes0		# 1D background model
#
# FDLOC Input
#
leqsfil		fdloc.data	# Local Earthquake data - header input for sphfdsyn
kmin		2			#Beginning Depth grid, Earthquakes happens below surface
#
# FDLOC Output
#
fsumfil		fdloc.sumout		#  Location Summary File
outlfil 	fdloc.outliers		#  Outliers
fhedfil		fdloc.nheads		#  New Headers
fdatfil 	fdloc.ndat		#  New Data - output from sphfdsyn also
#
stafile		../../all.stns		# Station List
#
# Fine model file name (P and S): Output from c2f
#
# Note: these names must be used for runinvg to work correctly (they
#	are hardwired in that script).
#
finevel		tempvela
finpvel		tempvela.pvel
finsvel		tempvela.svel

# c2f test grid output
tgrdfil		c2f.gridout

pbasfil		./Ptimes.prism
