# Spec file for rcor.f
#
#  File connections
#
# Filelist has names of traces to analyize
# Reflist  has names of reference traces
# Pickfile is the output pick file
#
filelist	trace.list
datalist	bogus.file
pickfile	rest4.pickfile

#   default sample rate
dtn   1.0d-2

# byte swap flag
iswap   0

# ---filtering
#       iirf   1        to apply a butterworth filter.   We go both directions to preserve phase
#       npolelo         number of low pass poles.  If   0, then low pass not applied
#       passlo          low pass frequency
#       npolehi         number of high pass poles.  If   0, then high pass not applied
#       passhi          high pass frequency
# --P wave default for passlo is 3 Hz; S wave may be better at 2 hz

iirf   2
npolelo   6
npolehi   6
passhi   1.0
passlo   -0.5

#  thresholds for phase detection (R score)
prthres   1.0
srthres   1.0

# percent thresholds for classes.  

pc0   20.00
pc1   10.00
pc2   5.00
sc0   20.00
sc1   10.00
sc2   5.0

#  mavh is the half length of the moving window used to average spectra in specsm and specform
#  note that setting mavh to 0 is the same as no smoothing
mavh   2

#  iwhite 1 applies a whitening step the target trace prior to the ref. fun. filter
#  This is yet to be tested so I would avoid it for now - in any event you could be amping the noise
iwhite  0

# use pick file for making windows
usepks	T
# half with of the window about the P pick
pkwin   4.0
# half with of the window about the S pick
skwin   10.0
arrtfile  syn.picks

noisein  2
nsmooth  128

tstpmax 0.5

isuffs 2

estout F
whitout F
