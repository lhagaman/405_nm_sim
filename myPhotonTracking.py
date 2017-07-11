import rat
import ROOT
import sys
import runCheckTools as RCT
import json

# Get command line arguments
cmdArgs = sys.argv

file_name = '~/Desktop/RAT_files/405_nm_sim/output.root'

fileIterator = rat.dsreader(file_name)

for iEntry, anEntry in enumerate(fileIterator):
    print("########################## NEW MC ######################")
    MC = anEntry.GetMC()
    num_tracks = MC.GetMCTrackCount()
    print('num_tracks: ', num_tracks)
    track = MC.GetMCTrack(0)
    for i in range(track.GetMCTrackStepCount()):
        print("######### NEW STEP #########")
        step = track.GetMCTrackStep(i)
        endpoint = step.GetEndpoint()
        volume = step.GetVolume()
        momentum = step.GetMomentum()
        process = step.GetProcess()
        print('endpoint: ', endpoint[0], endpoint[1], endpoint[2])
        print('momentum: ', momentum[0], momentum[1], momentum[2])
        print('volume: ', volume)
        print('process: ', process)

