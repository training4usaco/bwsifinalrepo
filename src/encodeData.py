import csv
import sys
import numpy as np
from math import ceil, log2, pi
from pathlib import Path
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import ControlledGate
from qiskit.circuit.library import RYGate

def DecimalToBinary(n):
    ret = ""
    while(n):
        ret += str(n % 2)
        n //= 2
    return ret

def FRQI(data_set) -> QuantumCircuit:
    # for normalizing
    N = len(data_set[0])   # number of datapoints
    n = ceil(log2(N))   # need extra qubit as target qubit to hold the encryption

    qc = QuantumCircuit(n + len(data_set))
    qc.h(range(n))

    for i in range(len(data_set)):
        for j in range(len(data_set[i])):
            mx = np.max(data_set[i])
            mn = np.min(data_set[i])

            if(mx == mn):   # can't even happen but just in case
                data_set[i] = 0
            else:
                data_set[i][j] = (data_set[i][j] - mn) / (mx - mn) * pi   # scale properly. NOTE: SCALED FROM 0 TO PI!

            binrep = DecimalToBinary(j)
            binrep = (binrep + (n - len(binrep)) * '0')[::-1]   # fill with 0's to match ctrl_state length
                                                                # reverse because ctrl_state is in little endian

            # https://quantumcomputing.stackexchange.com/questions/27077/qiskit-custom-multi-controlled-gate <- example (the documentations bad)

            rry = RYGate(data_set[i][j]) # custom gate
            mcry = ControlledGate(name="mcry", num_qubits=n+1, params=rry.params, num_ctrl_qubits=n, definition=rry.definition, ctrl_state=binrep, base_gate=rry)   # custom control gate

            qc.append(mcry, list(range(n)) + [n + i])

    print(qc.draw())

    return qc

def EncodeData(relative_path = "../data/card_transdata.csv"):
    # init
    data_set = [[] for i in range(8)]

    # reads in the data
    absolute_path = Path(__file__).parent / relative_path
    with open(absolute_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader) # skip first line because it's just header stuff that we dont need to read

        for row in spamreader:  # pls help idk how to pythong
            for i in range(len(row)):
                data_set[i].append(float(row[i]))
    
    # encode all the data and converts things to theta list
    FRQI(data_set)