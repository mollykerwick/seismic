# Variables for collect_events

arrtfile  detect.list.sort 	! Name of sorted pick file
evntfile  event.file	! Name of (output) event file
tstep	10.d0		! Maximum amount of time between detections to permit association
minsav   4		! Minimum number of detections required to constitue an event
snrmin   1000.		! Minimum SNR level to be considered a 'superior' detection
minsnrth 1		! Minimum number of 'superior' detections required to constitue an event
dupopt   1

