#finance tracker..
import json
import os
import FintrackerMain

class Account:
  def __init__(self):
    
    self.json_acc = "Fintracker_acc.json"
    
    if os.path.exists(self.json_acc):
      pass
     
    else:
      self.json_init()
      
    self.home()
  def json_init(self):
    
    with open (self.json_acc, "w") as json_init:
      json.dump([], json_init)
      
  def home(self):
    while True:
      print('''---------- FinTracker -----------\n
      1. New? Select to Sign-up\n
      2. Login to existing account\n
      3. Exit app\n
      ''')
      select_opt = input("Entry ⌨️: ")
      
      if select_opt == "1":
        self.sign_up()
        
      elif select_opt == "2":
        self.login()
        
      elif select_opt == "3":
        break
      
      else:
        print("Invalid entry! 🐍")
        
  def sign_up(self):
    
    print("----------- Sign up ------------\n")
    
    password_req = '''    Password requirements:    
      1. Must have upper case
      2. Must include at least one special characters
      3. Must include digit
      4. at least 8 characters or more'''
      
    username_req = '''    User name requirements:       
    1. Must have upper case
    2. Must not include any special characters
    3. at least 8 characters or more'''
    
    while True:
      print(f"{username_req}\n")
      
      self.user_name = input("Enter a username: ")
      
      req = [any(char.isdigit() or char.isalnum() for char in self.user_name),
      any(char.isupper() for char in self.user_name),
      len(self.user_name) >= 8,
        ]
        
      if all(req):
        print("username successful ✅") 
        print()
        break
        
      else:
        print("please check user-name requirements and try again")
        print()
        continue
      
    while True:
      print(f"{password_req}\n")
      self.password = input(f"Setup a password {self.user_name}: ")
      req_pas = [any(char.isdigit() for char in self.password),
      any(char.isupper() for char in self.password),
      len(self.password) >= 8,
      any(not char.isalnum() for char in self.password)
        ]
        
      if all(req_pas):
        print("account creation successful 👤")
        print ()
        self.writejs()
        break
      
      else:
        print("please check password requirements and try again")
        print()
        continue
      
  def writejs(self):
    
    self.data = {
      "username": self.user_name,
      "password": self.password
    }
    
    try:
      with open (self.json_acc, "r") as f:
        self.real_data = json.load(f)

        self.real_data.append(self.data)
        
    except FileNotFoundError:
      print("Dc24 file dir not found")
    
    with open (self.json_acc, "w") as file:
      json.dump(self.real_data, file, indent=4)
      
      
  def login(self):
    print("       Login - page   \n")
    
    username_log = input("Enter username: ")
    password_log = input("Enter Password 🔑: ")
    
    
    with open (self.json_acc, "r") as file:
      self.log_data = json.load(file)
     
    found = False
    
    for item in self.log_data:
      
      if item["username"] == username_log and item["password"] == password_log:
        self.Finmain = FintrackerMain.Main(username_log)
        self.Finmain.home()
        found = True
        break
        
    if found:
      pass
      
    else:
      print()
      print("Invalid username or password 🔑..TRY AGAIN")
    
test = Account()