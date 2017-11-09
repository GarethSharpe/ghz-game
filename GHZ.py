'''
Created on Jun 26, 2017
adapted for ibmqx4 by Marcus Edwards on November 9, 2017

@author: Gareth Sharpe
'''

from random import choice
from IBMQuantumExperience import IBMQuantumExperience 

API_TOKEN = 'a0f9090f4b9b0a7f86cb31848730654bb4dbc35aab364a7d728162c96b264752d413b88daea7303c87f12e0a719345119c0f8a880a27d73b998887664a989fce' #'5b31c59ff4a641a3a645cb307580d10d7cebaad6577cccf4f85c882d21343053cff1b6d91a3616a9eb5ed5ffa57b55ad63f6edb278134855180603ee85830b57'
XOR = '⊕'
OR = '∨'

api = IBMQuantumExperience(API_TOKEN)

def test_api_auth_token():
    '''
    Authentication with Quantum Experience Platform
    '''
    api = IBMQuantumExperience(API_TOKEN)
    credential = api.check_credentials()

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
    qasm = """include "qelib1.inc";qreg q[5];creg c[5];h q[2];cx q[2],q[1];cx q[1],q[0];barrier q[2],q[1],q[0];"""

    # If the question is q = 1, then the player performs a Hadamard transform on their qubit
    if r == '1':
        qasm += 'sdg q[2];'
    if s == '1':
        qasm += 'sdg q[1];'
    if t == '1':
        qasm += 'sdg q[0];'
    
    qasm += "h q[2];h q[1];h q[0];measure q[2] -> c[0];measure q[1] -> c[1];measure q[0] -> c[2];"
        
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
    return int(rst == abc)

def xor(a, b, c):
    return int(((a + b + c) % 2) == 1)

def classical_game(rounds, file_name=None):
    
    if file_name:
        file = open(file_name, 'w')
        file.write("round, result, cumulative, average\n")  
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        result = classical_GHZ()
        wins += result
        
        if file_name:
            file.write('{},{},{},{}\n'.format(i, result, wins, str(wins / i)))
    
        i += 1
    
    if file_name:
        print()
        print("File " + file_name + " has been created.")
        file.close()
    
    print()
    print("--------------------")
    print("FINAL RESULTS")
    print("--------------------")
    print("Rounds: " + str(rounds))
    print("Wins: ", str(wins))
    print("Losses: " + str(rounds - wins))
    print("P(win): " + str(wins / rounds))

def quantum_game(rounds, device, file_name=None):
    
    if file_name:
        file = open(file_name, 'w')
        file.write("round, result, cumulative, average\n")  
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        result = quantum_GHZ(device)
        wins += result
        
        if file_name:
            file.write('{},{},{},{}\n'.format(i, result, wins, str(wins / i)))
            
        i += 1
    
    if file_name:
        print()
        print("File " + file_name + " has been created.")
        file.close()
        
    print()
    print("--------------------")
    print("FINAL RESULTS")
    print("--------------------")
    print("Rounds: " + str(rounds))
    print("Wins: ", str(wins))
    print("Losses: " + str(rounds - wins))
    print("P(win): " + str(wins / rounds))

''' Classical Games '''
# classical_game(100)
# classical_game(100, "class_results.txt")

''' Simulated Quantum Games '''
quantum_game(50, 'simulator')
# quantum_game(100, 'simulator', "sim_results.txt")

''' Computed Quantum Games '''
# quantum_game(100, 'real')
# quantum_game(100, 'real', "comp_results.txt")
