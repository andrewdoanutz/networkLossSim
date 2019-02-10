#written by Andrew Doan 2/4/19

import sunau
import random

def randomLoss(notLoss):
    if((random.randint(0,101)>=notLoss)):
        return True
    else:
        return False

def writeZero(writeFile,numFrames):
    writeFile.writeframes(bytes("00"*numFrames,'utf-8'))

def writeLastPacket(writeFile,packet):
    writeFile.writeframes(packet)

def writeLastSample(writeFile,numFrames,sample):
    writeFile.writeframes(sample*(numFrames/2))

def simulatorZero(numFrames,filename,notLoss):
    wFile=sunau.open("(copy)"+filename,"w")
    rFile=sunau.open(filename, 'r')
    i=0
    frames=rFile.getnframes()
    wFile.setparams(rFile.getparams())
    while i<frames:
        i+=1
        frame=rFile.readframes(numFrames)
        if(randomLoss(notLoss)):
            writeZero(wFile,numFrames)
        else:
            wFile.writeframes(frame)
        
           
def simulatorPacket(numFrames,filename,notLoss):
    wFile=sunau.open("(copy)"+filename,"w")
    rFile=sunau.open(filename, 'r')
    i=0
    frames=rFile.getnframes()
    wFile.setparams(rFile.getparams())
    frame=""
    while i<frames:
        i+=1
        prevframe=frame
        frame=rFile.readframes(numFrames)
        if(randomLoss(notLoss)):
            writeLastPacket(wFile,prevframe)
        else:
            wFile.writeframes(frame)

def simulatorSample(numFrames,filename,notLoss):
    wFile=sunau.open("(copy)"+filename,"w")
    rFile=sunau.open(filename, 'r')
    i=0
    frames=rFile.getnframes()
    wFile.setparams(rFile.getparams())
    sample=""
    while i<frames:
        i+=1
        frame=rFile.readframes(numFrames-2)
        prevsample=sample
        sample=rFile.readframes(2)
        if(randomLoss(notLoss)):
            writeLastSample(wFile,numFrames,prevsample)

        else:
            wFile.writeframes(frame)
            wFile.writeframes(sample)
                

simulatorZero(2000,"doors.au",70)
simulatorZero(2000,"poe.au",70)
#simulatorPacket(2000,"pink_panther.au",100)
#simulatorSample(2000,"simple.au",100)




