from modules.menu import *
from classes.todos import *

todos = Todos()

def createTodo():
  printTitle("Adicione uma nova tarefa")
  description = input(f'Descrição: ')
  todos.createTodo(description)
  print(f'Tarefa adicionada')

def listTodos():
  printTitle("Listagem das tarefas")
  if(len(todos) == 0):
    print(f'Não há tarefas')
    return
  print(todos)
  backToMenu()

def removeTodo():
  printTitle("Remover uma tarefa")
  if len(todos) == 0:
    print(f'Não há tarefas')  
    return

  print(todos)
  index = optionFromMenu('Digite o número da tarefa a ser removida: ', len(todos) +1)
  todos.removeTodo(index)
  print(f'Tarefa Removida')

def doneTodo():
  printTitle("Definir tarefa como concluída ")
  if len(todos) == 0:
    print(f'Não há tarefas')  
    return

  print(todos)
  index = optionFromMenu('Digite o número da tarefa a ser concluída: ', len(todos) +1)
  todos.doneTodo(index)
  print(f'Tarefa concluída')
 

def searchTodoByStatus():
  isDone = True
  print(f'Deseja buscar tarefas por:')
  print(f'1. Concluídas')
  print(f'2. Não Concluidas')
  index = optionFromMenu('Digite o número escolhido: ', 3)
  if index == 2:
    isDone = False
  filterTodos = todos.searchTodoByStatus(isDone)
  if(len(filterTodos) == 0):
    print(f'Não há tarefas')
  else: 
    print(filterTodos)

if __name__ == "__main__":
  print(f'Bem vindo')
  
  while(True):
    option = menu()
    if option == 0:
      createTodo()
    elif option == 1:
      listTodos()
    elif option == 2:
      removeTodo()
    elif option == 3:
      searchTodoByStatus()
    elif option == 4:
      doneTodo()
    else:
      print(f'Fim do Programa')
      break


