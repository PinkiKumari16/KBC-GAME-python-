
   ###################### KBC   ###########################
   ###########  with 50-50 life line  #############
q_l=["tomato is a vegatable or fruit?",
     "what is a capital of india?",
     "NG me kon sa course karaya jata hai?",
     "when came covid in india?"
     ]
o_l=[["red color","fruit","vegatable","flower"],
     ["patna","bhopal","delhi","itanagar"],
      ["software engineering","counseling","tourism","agriculture"],
     [2021,2018,2020,2019]]
s_l=[2,3,1,4]
o_50_50=[["fruit","vegatable"],
         ["patna","delhi"],
         ["software engineering","agriculture"],
         [2020,2019]]
s_50_50_l=[1,2,1,2]
print("WELCOME TO THE KBC CONTEST")
c=0
i=0
while i<len(q_l):
  print("Aapka Sawal Hai :")
  print(q_l[i])
  print("Aapke Options Hai :")
  j=0
  while j<=3:
    print(str(j+1)+".",o_l[i][j])
    j+=1
  a=input("do you want to use 50-50 life line(yes or no):")
  if a=="yes":
    c+=1
    if c==1:
      k=0
      while k<2:
        print(str(k+1)+".",o_50_50[i][k])
        k+=1
      answer=int(input("Enter your anwer: "))
      if q_l[i] and answer==s_50_50_l[i]:
        print("Congrates! Aapka Answer Sahi Hai")
        i+=1
      else:
        print("Aapka Answer Galat Hai")
        break
    elif c!=1:
      print("Aap 50-50 life line ka use kr chuke ho")
      answer=int(input("Enter your anwer like 1,2: "))
      if q_l[i] and answer==s_l[i]:
       print("Congrates! Aapka Answer Sahi Hai")
       i+=1
      else:
       print("Aapka Answer Galat Hai")
       break
  else:
   answer=int(input("Enter your anwer like 1,2: "))
   if q_l[i] and answer==s_l[i]:
       print("Congrates! Aapka Answer Sahi Hai")
       i+=1
   else:
       print("Aapka Answer Galat Hai")
       break
