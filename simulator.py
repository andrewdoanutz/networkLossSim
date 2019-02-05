#written by Andrew Doan 2/4/19

import sunau
import random

def randomLoss(notLoss):
    if((random.randint(0,101)>=notLoss)):
        return True
    else:
        return False

def writeZero(writeFile,numFrames):
    writeFile.writeframes(""*numFrames)

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
        if(randomLoss(notLoss)&i!=0):
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
        if(randomLoss(notLoss)&i!=0):
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
        if(randomLoss(notLoss)&i!=0):
            writeLastSample(wFile,numFrames,prevsample)

        else:
            wFile.writeframes(frame)
            wFile.writeframes(sample)
                

simulatorZero(10,"doors.au",50)
simulatorZero(10,"poe.au",50)
#simulatorPacket(2000,"pink_panther.au",100)
#simulatorSample(2000,"simple.au",100)




