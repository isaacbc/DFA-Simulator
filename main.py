class DFA:

  def __init__(self, states, input_symbols, transitions, initial_state,
               final_states):
    self.states = states
    self.input_symbols = input_symbols
    self.transitions = transitions
    self.initial_state = initial_state
    self.final_states = final_states

  def printDfa(self):
    print("States: ", self.states)
    print("Input Symbols: ", self.input_symbols)
    print("Transitions: ", self.transitions)
    print("Initial State: ", self.initial_state)
    print("Final States: ", self.final_states)

  ## EXEMPLO:
  #   dfa = DFA(
  #       states={'q0', 'q1', 'q2'},
  #       input_symbols={'a', 'b'},
  #       transitions={
  #           'q0': {'a': 'q0', 'b': 'q1'},
  #           'q1': {'a': 'q0', 'b': 'q2'},
  #           'q2': {'a': 'q2', 'b': 'q1'}
  #       },
  #       initial_state='q0',
  #       final_states={'q1'}
  # )


def createTransitionsDic(lista):
  transitions = {}
  for transicao in lista:
    #destruct da lista ["q0", "a", "q1] = origem, simbolo, destino
    origem, simbolo, destino = transicao
    if origem not in transitions:
      transitions[origem] = {}

    # q0['a'] = q1
    transitions[origem][simbolo] = destino
  return transitions
  

def readFile(nome_arquivo):
  with open(nome_arquivo, 'r') as file:
    content = file.read()  #retorna uma string
    print(content)
    return content


def instantiateDfaFromString(dfaString):
  #Remove espaços em branco e quebras de linha
  content = dfaString.replace('\n', '')

  #Divide o conteúdo em partes relevantes
  try:
    automata = content.split('={')[1].split("}p:")
    infos = automata[0]
    transitionsString = automata[1]

    transitionsList = transitionsString.split(")(")
    processedStatesList = [(x.replace("(", "").replace(")", "").split(","))
                           for x in transitionsList]

    separetedInfo = infos.split(",{")
    alfabeto = separetedInfo[0].replace("{", "").replace("}", "").split(",")
    separetedStates = separetedInfo[1].split("},")
    states = separetedStates[0].split(",")
    initial_state = separetedStates[1]
    final_states = separetedInfo[2].replace("}", "").split(",")

    transitions = createTransitionsDic(processedStatesList)

    dfa = DFA(
        states=states,
        input_symbols=alfabeto,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states,
    )
    return dfa
  except Exception as e:
    print("Formatação incorreta do arquivo", e)


def main():
  fileName = 'automato_test.txt'
  dfaString = readFile(fileName)
  dfa = instantiateDfaFromString(dfaString)
  if (dfa):
    dfa.printDfa()
