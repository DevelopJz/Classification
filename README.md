# Python3 연습 과제
## 1-Python3 Variable Classification

### 라이브러리
Python.ast  
Numpy

### 코드
```Python3

import numpy as np  
from ast import literal_eval

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
```

