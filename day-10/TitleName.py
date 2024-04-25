def format_name(f_name, l_name):
  return f_name.title() + " "+  l_name.title()
  
first_name = input("what's your first name?\n")
last_name = input("what's your last name?\n")
name = format_name(f_name = first_name, l_name = last_name)
print(name)
