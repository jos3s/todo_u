def printOptions():
  printTitle('Ações')
  print(f'1. Adicionar tarefa')
  print(f'2. Listar tarefas')
  print(f'3. Remover tarefas')
  print(f'4. Filtrar tarefas')
  print(f'5. Marcar tarefa como concluida')
  print(f'6. Encerrar programa')


def optionFromMenu(msg, lastValue):
  isValidOption = False
  while(not isValidOption):
    option = input(msg)
    if option.isdigit() and int(option) > 0 and int(option) < lastValue:
      isValidOption = True
  return int(option)-1

def menu():
  printOptions()
  option = optionFromMenu('Digite o numero da opção desejada:', 7)
  return option
  
def backToMenu():
  while(True):
    key = input(f'Digite qualquer tecla para voltar para o menu... ')
    if not key :
      break

def printTitle(msg):
  divisor = ''
  for i in range(len(msg)):
    divisor = divisor + "="
  print(f'')
  print(f'{divisor}')
  print(f'{msg}')
