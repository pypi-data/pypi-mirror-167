from person_generator import PersonGenerator
HEADERS = ("id", "first_name", "last_name", "title", "gender", "email", "ip_address", "is_active", "avatar", "language", "job_title")
def main():
  import tablib
  pg = PersonGenerator()
  #pg.print_persons(20)
  table = tablib.Dataset(pg.get_persons(), header=HEADERS)
  # TODO: print complete table (or at least more than 2, not complete, entries)
  print(table.export('df'))

if __name__ == '__main__':
  main()