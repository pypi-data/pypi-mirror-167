from json import load, dumps
from os import path
class PersonGenerator:
  def __init__(self) -> None:
    this_dir, this_filename = path.split(__file__)
    DATA_PATH = path.join(this_dir, "data", "MOCK_DATA.json")
    self.test = "test"
    try:
      mock_data = open(DATA_PATH)
      self.person_list = load(mock_data)
      mock_data.close()
    except:
      print("Error while loading MOCK_DATA.json.")
  
  def get_persons(self, ammount:int = 20):
    if ammount > 0 and ammount < 1000:
      return self.person_list[0:ammount]
    else: return self.person_list[0]
  
  def get_all(self):
    return self.person_list
  
  def print_persons(self, ammount:int = 20, indent:int = 2):
    print(dumps(self.get_persons(ammount), indent=indent))