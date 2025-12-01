# make a dictionary

contacte = {}

#take permision from user

print("enter 1 for start")
print("enter 10 for close")
n = int(input("//"))

# running loop

while n == 1 :

  print("enter 1 for add contacte")
  print("enter 2 for find contacte")
  print("enter 3 for update contacte")
  print("enter 4 for delete contacte")
  print("enter 0 for print contacte")
  print("enter 10 for close")
  a = int(input("//"))
# take a input for do opration

# add contect

  if a == 1 :
    name = input("enter name:-- ")
    number = int(input("enrer number:-- "))
    contacte[name] = number
    
    # find contect

  elif a == 2 :
    name = input("enter name to you find:-- ")
    if name in contacte :
      print("number is : ",contacte[name])
    else:
      print("contect not found!")
      # update contect
      
  elif a == 3:
    name = input("enter name do you update:-- ")
    if name in contacte:
      contacte.pop(name)
      new_name =  input("enter name new name:-- ")
      new_number = int(input("enter new number:-- "))
      contacte[new_name] = new_number
      print("contecte updated!")
    else:
      print("contecte not found!")
      
      # delete contect

  elif a == 4 :
    name = input("enter name do you delete :-- ")
    if name in contacte:
      contacte.pop(name)
      print("contacte deleted!")
    else:
      print("contecte not found!")
      
      # print contect

  elif a == 0:
      print(contacte)
      
      # close programe

  elif a == 10:
     print("closed!")
  break
      
      # for unknown input

else:
  print("unknown input!")

    


