# Python3 연습 과제
## 1-Python3 Variable Classification

### 라이브러리
ast  
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

### 코드 설명
try / except 문을 이용해 변수 구분하는 간단한 함수 구현  
None 타입의 변수에 입력 변수를 넣어 변수 자동 형변환 후 저장

### 동작 결과
**입력값이 정수일 때**  
![image](https://user-images.githubusercontent.com/96412126/157577151-713c3b5e-8d35-4790-8c22-086fdd33de03.png)

**입력값이 실수일 때**  
![image](https://user-images.githubusercontent.com/96412126/157577243-b74ec489-9256-4777-add7-b091b8bf5ca7.png)

**입력값이 문자열일 때**  
![image](https://user-images.githubusercontent.com/96412126/157577389-7b30302e-f210-4549-b5e3-cf32c4e19c32.png)

**입력값이 복소수일 때**  
![image](https://user-images.githubusercontent.com/96412126/157577499-950fdbea-db3c-41ba-8f56-ad89cf678f94.png)

**입력값이 True / False 일 때**  
![image](https://user-images.githubusercontent.com/96412126/157577623-e7e7e1ce-0f84-4801-8f98-11ba21657f73.png)

![image](https://user-images.githubusercontent.com/96412126/157577582-c17a3b27-ae43-42bd-a90e-b7a9ce5dea4e.png)

![image](https://user-images.githubusercontent.com/96412126/157586378-c0964981-81d7-4450-adbe-992c15a6e219.png)

![image](https://user-images.githubusercontent.com/96412126/157586432-57f1afcb-99d1-4b24-b5f4-fe6cf56e58eb.png)

