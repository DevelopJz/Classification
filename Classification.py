import numpy as np
from ast import literal_eval

recvData=None

class Classification:
 def __init__(self,inputData):
  self.inputData=inputData
  print(type(inputData))
  if type(self.inputData)==str:
   print(inputData)
   try:
    self.inputData=int(self.inputData)
    print(type(self.inputData))
   except:
    print("정수가 아닙니다")
    try:
     self.inputData=float(self.inputData)
     print(type(self.inputData))
    except:
     print("실수가 아닙니다")
     try:
      self.inputData=complex(self.inputData)
      print(type(self.inputData))
     except:
      print("복소수가 아닙니다")
      if self.inputData=="True" or self.inputData=="TRUE" or self.inputData=="true":
       self.inputData=True
      elif self.inputData=="False" or self.inputData=="FALSE" or self.inputData=="false":
       self.inputData=False
      else:
       self.inputData=self.inputData
       
 def switching(self):
  return self.inputData

print(type(recvData))

inputData=input("아무 값이나 입력하세요 : ")
a=Classification(inputData)
recvData=a.switching()
print(recvData)
print(type(recvData))
