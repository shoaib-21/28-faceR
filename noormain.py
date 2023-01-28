import noorcode
import RRead
print("reading rfid")
rfidUserName = RRead.readRfid()
print("rfid read complete, initiating face recognition")
authorizedUser=noorcode.faceR(rfidUserName)
print("authorized.....door opens")