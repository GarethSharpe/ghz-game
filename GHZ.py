'''
Created on Jun 26, 2017

@author: Gareth Sharpe
'''

from random import choice
from IBMQuantumExperience import IBMQuantumExperience 

API_TOKEN = 'ae62fe37579104f45f6d8f3b02a86b7f3de4a3ec864980c041268859060d90c30e3e30ff695536567f6a52c991d553dc04e5625cf4529bead5946a059525efa7'
XOR = '⊕'
OR = '∨'

api = IBMQuantumExperience.IBMQuantumExperience(API_TOKEN)

def test_api_auth_token():
    '''
    Authentication with Quantum Experience Platform
    '''
    api = IBMQuantumExperience.IBMQuantumExperience(API_TOKEN)
    credential = api._check_credentials()

    return credential

def connect():
    '''
    Attempt to connect to the Quantum Experience Platform
    ''' 
    connection_success = test_api_auth_token()

    if(connection_success == True):
        print("API authentication success.")
    else:
        print("API authentication failure.")
        exit()

def print_results(exp):
    '''
    Print the distribution of measured results from the given experiment
    Returns the measured state
    '''
    print("---------------------")
    print("RESULTS: ")
    print("---------------------")
    states = "State       | "
    probabilities = "Probability | "
    for i in range(len(exp['result']['measure']['labels'])):
        state = exp['result']['measure']['labels'][i]
        probability = exp['result']['measure']['values'][i]

        states += str(state) + " | " 
        probabilities += "{:.3f}".format(probability) + " | "
        
    print(states)
    print(probabilities)
    print()
    return state

def classical_GHZ():
    
    # The referee chooses a three bit string r s t uniformly from the set {000, 011, 101, 110}
    set = ['000', '011', '101', '110']
    referee = choice(set)
    r = referee[0]
    s = referee[1]
    t = referee[2]
    
    print("Referee: " + referee)
    print("r: " + r + ", s: " + s + ", t: " + t)
    print()
    
    # The referee sends r to Alice, s to Bob, and t to Charlie.
    # To maximize their chance of success, each player returns a '1', regardless of r s t
    alice = '1'
    bob = '1'
    charlie = '1'
    
    print("Alice: " + alice)
    print("Bob: " + bob)
    print("Charlie: " + charlie)
    
    win = get_result(alice, bob, charlie, r, s, t)
    
    if win:
        print("Round win.")
    else:
        print("Round lose.")
    
    return win

def quantum_GHZ(device):
    
    connect()
    
    # The referee chooses a three bit string r s t uniformly from the set {000, 011, 101, 110}
    set = ['000', '110', '101', '011']
    referee = choice(set)
    r = referee[0]
    s = referee[1]
    t = referee[2]
    # The referee sends r to Alice, s to Bob, and t to Charlie
    
    print("Referee: " + referee)
    print("r: " + r + ", s: " + s + ", t: " + t)
    
    # Create GHZ state
    qasm = """include "qelib1.inc";qreg q[5];creg c[5];h q[0];cx q[0],q[1];cx q[1],q[2];barrier q[0],q[1],q[2];"""

    # If the question is q = 1, then the player performs a Hadamard transform on their qubit
    if r == '1':
        qasm += 'sdg q[0];'
    if s == '1':
        qasm += 'sdg q[1];'
    if t == '1':
        qasm += 'sdg q[2];'
    
    qasm += "h q[0];h q[1];h q[2];measure q[0] -> c[0];measure q[1] -> c[1];measure q[2] -> c[2];"
        
    # The players measures their qubits in the standard basis and returns the answer to the referee.
    exp = api.run_experiment(qasm, device, 1)

    state = print_results(exp)
    state = state[2::]
    
    alice = state[2]
    bob = state[1]
    charlie = state[0]
    
    print("Alice: " + alice)
    print("Bob: " + bob)
    print("Charlie: " + charlie)
    
    win = get_result(alice, bob, charlie, r, s, t)
    
    if win:
        print("Round win.")
    else:
        print("Round lose.")
    print()
    
    return win
    
def get_result(a, b, c, r, s, t):
    rst = int(r) or int(s) or int(t)
    abc = xor(int(a), int(b), int(c))
    print("r∨s∨t = " + r + OR + s + OR + t + ' = ' + str(rst))
    print("a⊕b⊕c = " + a + XOR + b + XOR + c + ' = ' + str(abc))
    return rst == abc

def xor(a, b, c):
    return int(((a + b + c) % 2) == 1)

def classical_game(rounds):
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        wins += classical_GHZ()
        i += 1
    
    print()
    print("--------------------")
    print("FINAL RESULTS")
    print("--------------------")
    print("Rounds: " + str(rounds))
    print("Wins: ", str(wins))
    print("Losses: " + str(rounds - wins))
    print("P(win): " + str(wins / rounds))

def quantum_game(rounds, device):
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        wins += quantum_GHZ(device)
        i += 1
    
    print()
    print("--------------------")
    print("FINAL RESULTS")
    print("--------------------")
    print("Rounds: " + str(rounds))
    print("Wins: ", str(wins))
    print("Losses: " + str(rounds - wins))
    print("P(win): " + str(wins / rounds))
    
classical_game(50)
# quantum_game(50, 'simulator')