# Yuchen Shi
# ITP115, Spring 2018
# Lab L13
# yuchensh@usc.edu

from earsketch import *

init()
setTempo(120)

fitMedia(HIPHOP_DUSTYGROOVE_001, 1, 1, 9)
fitMedia(Y07_HI_HAT, 2, 3, 18)
fitMedia(Y05_PIANO_1, 3, 6, 18)
fitMedia(YG_ALT_POP_GUITAR_1, 4, 3, 15)

for i in range (1, 15):
  fitMedia(RD_TRAP_BELLLEAD_1, 5, i, i+0.5)
  fitMedia(RD_ELECTRO_DRUM_PART_5, 6, i+0.5, i+1)
  fitMedia(RD_RNB_KEYSRHODES_1, 7, i, i+0.8)
  fitMedia(EIGHT_BIT_ANALOG_DRUM_LOOP_013, 8, i+0.3, i+1)

setEffect(1, VOLUME, GAIN, 5)
setEffect(1, VOLUME, GAIN, 8)

beatString1 = "0-00-00-0++0+0"
beatString2 = "000-0-0+0++0-0"
for i in range(2, 10):
  makeBeat(YG_RNB_FUNK_PIANO_2, 9, i, beatString1)
  makeBeat(RD_ROCK_POPELECTRICBASS_1, 10, i, beatString2)


finish()
