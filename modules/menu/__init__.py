def menu():
  isValidOption = False
  while(not isValidOption):
    printOptions()
    option = input(f'Digite o numero da opção desejada: ')
    if option.isdigit() and int(option) > 0 and int(option) < 7:
      isValidOption = True
  return int(option)


def printOptions():
  print(f'Ações')
  print(f'1. Adicionar tarefa')
  print(f'2. Listar tarefas')
  print(f'3. Remover tarefas')
  print(f'4. Filtrar tarefas')
  print(f'5. Marcar tarefa como concluida')
  print(f'6. Encerrar programa')

