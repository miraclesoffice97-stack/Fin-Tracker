#the main deal 🤝 

import json
import os    
import sys
from datetime import datetime

class Main:
  def __init__(self, username):
    self.username = username
    self.total_income = 0
    self.total_expenses = 0
    self.aincome = 0
    self.history = []
    self.j_file = "FintrackerMain.json"
    
    if os.path.exists(self.j_file):
      pass
    else:
      self.init_json()
      
    self.load_data()
    
  def init_json(self):
    with open (self.j_file, "w") as file:
      json.dump([], file)
      
  def home(self):
    while True:
      print(f'''{"-"*40} \n      Home 🏡 Menu 
      \n{"-"*40}
      1. Dashboard 
      
      2. Record income 
      
      3. Record Expenses 
      
      4. Activity History 
      
      5. log_out
      
      6. exit''')
      
      entry = input ("Entry ⌨️: ")
      
      if entry == "1":
        self.dashboard()
        
      elif entry == "2":
        self.income()
        
      elif entry == "3":
        self.expenses()
        
      elif entry == "4":
        self.activity_history()
        
      elif entry == "5":
        break
       
      elif entry == "6":
        sys.exit()
        
  def income(self):
    while True:
      try:
        income_entry = float(input("Enter/Register income or 0 to exit: $"))
        now = datetime.now().strftime("%d-%m-%y, %H:%M")
        print (f"\n Income ${income_entry:.2f} recorded..")
        
        if income_entry == 0:
          break
         
        else:
          self.recent_income = f"income ${income_entry:.2f} recorded {now}\n"
          self.history.append(self.recent_income)
          self.total_income += income_entry
          self.data_savi()
          
      except ValueError:
        print("invalid entry!")
        
  def expenses(self):
    while True:
      try:
        expense_entry = float(input("Enter/Register expenses or 0 to exit: $"))
        now = datetime.now().strftime("%d-%m-%y, %H:%M")
        print (f"\n Income ${expense_entry:.2f} recorded..")
        
        if expense_entry == 0:
          print()
          break
         
        else:
          self.recent_expense = f"expence ${expense_entry:.2f} recorded {now}\n"
          self.history.append(self.recent_expense)
          self.total_expenses += expense_entry
          self.data_savi()
          
      except ValueError:
        print("Invalid entry ")
        
  def activity_history(self):
    
    print ("--------- Activity ----------\n")
    self.ACTIVITY_HISTORY = "\n".join(self.history)
    print (f"\n{self.ACTIVITY_HISTORY}")
    
    print ()
    exit = input("Enter 0 to exit: ")
    print()
    
    if exit == "0":
      return
      
    else:
      print("Invalid! entry 🚫")
    
  def dashboard(self):
    self.aincome = self.total_income - self.total_expenses
    self.data_savi()
    print(f'''Dashboard 🧾____________|
    \nWelcome {self.username} 👤_____|
    
         Total_income                Total_expences
         ${self.total_income:.2f}                  ${self.total_expenses:.2f}
         
         Available Income
         ${self.aincome:.2f}
         
    ____________________________________________________
    |                                                   |
    |                    😎😎😎                         |
    |             Hey Fintracker!...........            |
    |___________________________________________________|\n''')
    
    exit = input("Enter 0 to exit: ")
    
    if exit == "0":
      return
      
    else:
      print ("invalid input")
      
  def data_savi(self):
    
    self.data = {
      self.username: {
        "total_income": 0,
        "total_expenses": 0,
        "available":0,
        "history": []
      }
    }
    
    
    with open(self.j_file, "r") as file:
      self.data_save = json.load(file)
      
    check = False
    for data in self.data_save:
      if self.username in data:
        data[self.username]["total_income"] = self.total_income
        data[self.username]["total_expenses"] = self.total_expenses
        data[self.username]["history"] = self.history
        data[self.username]["available"] = self.aincome
        check = True
        
    if not check:
      self.data_save.append(self.data)
      
    with open (self.j_file, "w") as file:
      json.dump(self.data_save, file, indent=4) 
      
  def load_data(self):
    
    try:
      
      with open(self.j_file, "r") as file:
        self.data_l = json.load(file)
      
      check = False
      
      for data in self.data_l:
        if self.username in data:
          self.total_income = data[self.username]["total_income"]
          self.total_expenses = data[self.username]["total_expenses"]
          self.history = data[self.username]["history"]
          self.aincome = data[self.username]["available"]
          check = True
          
      if not check:
        pass
          
    except FileNotFoundError:
      print("Error! file not found")