todo_list=[]
def add_todo(text):
  todo_list.append(text)
def show_todo():
  for index,item in enumerate(todo_list):
    print(f'{index+1}.{item}')
def del_todo(index):
  todo_list.pop(index-1)
if _name_ == '_main_':
  add_todo('完成github作业')
  show_todo
