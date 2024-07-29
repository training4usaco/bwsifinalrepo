import csv
import numpy as np
from math import ceil, log2, pi
from pathlib import Path
from qiskit import QuantumCircuit
from qiskit.circuit import ControlledGate
from qiskit.circuit.library import RYGate

def DecimalToBinary(n):
    ret = ""
    while(n):
        ret += str(n % 2)
        n //= 2
    return ret

def FRQI(data_set, num_categories) -> QuantumCircuit:
    # for normalizing
    N = len(data_set[0])   # number of datapoints
    n = ceil(log2(N))   # need extra qubit as target qubit to hold the encryption

    qc = QuantumCircuit(n + num_categories)
    qc.h(range(n))

    ctrl_bits = list(range(n))

    for i in range(num_categories):
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

            qc.append(mcry, ctrl_bits + [n + i])

    # print(qc.draw())

    return qc

def EncodeData(num_categories, relative_path = "../data/card_transdata.csv") -> QuantumCircuit:
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
    return FRQI(data_set, num_categories)