from modules.menu import *
from .todo import *

class Todos():
  def __init__(self):
    self._todos = []

  def createTodo(self, description):
    todo = Todo(description)
    self._todos.append(todo)

  def __str__(self):
    string =''
    for i, todo in enumerate(self._todos):
      string = string + f'#{i+1}: {todo}\n'
    return string

  def removeTodo(self, index):
    del self._todos[index]

  def doneTodo(self, index):
    self._todos[index].setdone()
  
  def __len__(self):
    return len(self._todos)

  def searchTodoByStatus(self, done):
    filterTodos = Todos()
    for todo in self._todos:
      if todo.done == done:
        filterTodos.createTodo(todo.description)
    return filterTodos
