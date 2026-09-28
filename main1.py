todo_list=[]
def add_todo(text):
  todo_list.append(text)
def show_todo():
  for index,item in enumerate(todo_list):
    print(f'{index+1}.{item}')
if _name_ == '_main_':
  print('待办系统启动')
