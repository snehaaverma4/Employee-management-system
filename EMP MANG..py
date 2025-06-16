#EMPLOYEE MANAGEMENT SYSTEM                                                               


#REGISTRATION OF EMPLOYEES:-
def saveinfo():  
 import pickle
 emp={}
 empfile=open('EMP.dat','ab')
 ans='y'
 while ans=='y':
    empid=int(input("Enter id : "))
    name=input("Enter Name : ")
    gender=input("Enter gender :")
    designation=(input("Enter designation : "))
    salary=int(input("Enter salary : "))
    emp['EMPID']=empid
    emp['NAME']=name
    emp['GENDER']=gender
    emp['DESIGNATION']=designation
    emp['SALARY']=salary
    pickle.dump(emp, empfile)
    ans=input("WANNA ENTER MORE RECORDS? (y/n):  ")
 empfile.close()




#SEARCHING THE RECORD OF EMPLOYEE:-
def searchinfo():
 print("ENTER 1 TO SEARCH RECORD BY ID:")
 print("ENTER 2 TO SEARCH RECORD BY NAME:")
 a=int(input("ENTER YOUR CHOICE:"))

 
 if a==1:
  import pickle
  emp={}
  empfile=open('EMP.dat','rb')
  flag=0
  key=int(input("ENTER ID TO SEARCH THE RECORD :"))
  try:
   print("SEARCHING RECORD PLEASE WAIT......")  
   while True:
    emp=pickle.load(empfile)
    if emp['EMPID']==key:
        print(emp)
        flag=1      
  except EOFError:
   if flag==0:
     print("RECORD NOT FOUND ")
   empfile.close()

   
 elif a==2:
  import pickle
  emp={}
  empfile=open('EMP.dat','rb')
  flag=0
  key=input("ENTER NAME TO SEARCH THE RECORD :")
  try:
   print("SEARCHING RECORD PLEASE WAIT......")  
   while True:
    emp=pickle.load(empfile)
    if emp['NAME']==key:
        print(emp)
        flag=1      
  except EOFError:
   if flag==0:
     print("RECORD NOT FOUND ")
   empfile.close()

 else:
     print("SORRY! INVALID CHOICE")


   

#UPDATING THE RECORD OF EMPLOYEE:-
def updateinfo():
  import pickle
  emp={}
  empfile=open('EMP.dat','rb+')
  flag=0
  try:
   while True:
    fpos=empfile.tell() 
    emp=pickle.load(empfile)
    if emp['SALARY']>30000:
       emp['SALARY']+=1000
       empfile.seek(fpos)
       pickle.dump(emp, empfile)
       flag=1
       print("UPDATED SUCCESSFULLY. ")
  except EOFError:
      if flag==0:
        print("RECORD NOT FOUND ")
      empfile.close()


    
            
#PRINTING THE RECORD OF EMPLOYEE:-   
def printinfo():
 import pickle
 emp={}
 empfile=open('EMP.dat','rb')
 try:
  while True:
    emp=pickle.load(empfile)
    print(emp)
 except EOFError:    
  empfile.close()

  


while True:
 print("                                                                -------------------------------------------"                                                                )
 print("                                                                ==========================================="                                                                )
 print("                                                                >>>>>>>>EMPLOYEE MANAGEMENT SYSTEM<<<<<<<<<"                                                                )
 print("                                                                ==========================================="                                                                )
 print("                                                                -------------------------------------------"                                                                )
 print("                                     ")
 print("                                     ")
 print("===========================================================================================================================================================================")
 print("-------------------------------------")
 print("  FOLLOWING OPTIONS ARE AVAILABLE:- ")
 print("   ~SELECT AS PER YOUR CHOICE~")
 print("-------------------------------------")
 print("=====================================")
 print("                                     ")
 print("                                     ")
 print("*ENTER 1 :  TO REGISTOR THE RECORDS OF EMPLOYEES.")
 print("                                     ")
 print("*ENTER 2 : TO SEARCH THE RECORDS OF EMPLOYEES.")
 print("                                     ")
 print("*ENTER 3 : TO UPDATE THE RECORDS OF EMPLOYEES.")
 print("                                     ")
 print("*ENTER 4 : TO PRINT THE RECORDS OF EMPLOYEES.")
 print("                                     ")
 print("*ENTER 5: TO EXIT.")
 print("                                     ")
 print("                                     ")
 
 ch=int(input("ENTER YOUR CHOICE:"))
 if ch==1:
    a=saveinfo()
 elif ch==2:
    a=searchinfo()
 elif ch==3:
    a=updateinfo()
 elif ch==4:
    a=printinfo()
 elif ch==5:
    print("THANK YOU")
    break
 else:
    print("SORRY! INVALID CHOICE")

