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

def EncodeDataUtility(data_set) -> QuantumCircuit:
    # for normalizing
    mx = np.max(data_set)
    mn = np.min(data_set)

    # sizes
    N = len(data_set)   # number of datapoints
    n = ceil(log2(N))   # need extra qubit as target qubit to hold the encryption

    qc = QuantumCircuit(n + 1)
    qc.h(range(n))

    for i in range(N):
        datapoint = data_set[i]
        datapoint = (datapoint - mn) / (mx - mn) * pi    # scale properly. NOTE: SCALED FROM 0 TO PI!

        binrep = DecimalToBinary(i)
        binrep = (binrep + (n - len(binrep)) * '0')[::-1]   # fill with 0's to match ctrl_state length
                                                            # reverse because ctrl_state is in little endian

        # https://quantumcomputing.stackexchange.com/questions/27077/qiskit-custom-multi-controlled-gate <- example (the documentations bad)

        rry = RYGate(datapoint) # custom gate
        mcry = ControlledGate(name="mcry", num_qubits=n+1, params=rry.params, num_ctrl_qubits=n, definition=rry.definition, ctrl_state=binrep, base_gate=rry)   # custom control gate
        qc.append(mcry, (range(n + 1)))

    return qc

def EncodeData(relative_path = "../data/card_transdata.csv"):
    # init
    distance_from_home = []
    distance_from_last_purchase = []
    ratio_to_median = []
    repeat_retailer = []
    used_chip = []
    used_pin_number = []
    online_order = []
    fraud = []

    # reads in the data
    absolute_path = Path(__file__).parent / relative_path
    with open(absolute_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader) # skip first line because it's just header stuff that we dont need to read

        for row in spamreader:  # pls help idk how to pythong
            distance_from_home.append(float(row[0]))
            distance_from_last_purchase.append(float(row[1]))
            ratio_to_median.append(float(row[2]))
            repeat_retailer.append(float(row[3]))
            used_chip.append(float(row[4]))
            used_pin_number.append(float(row[5]))
            online_order.append(float(row[6]))
            fraud.append(float(row[7]))
    
    # encode all the data
    distance_from_home_qc = EncodeDataUtility(distance_from_home)
    distance_from_last_purchase_qc = EncodeDataUtility(distance_from_last_purchase)
    ratio_to_median_qc = EncodeDataUtility(ratio_to_median)
    repeat_retailer_qc = EncodeDataUtility(repeat_retailer)
    used_chip_qc = EncodeDataUtility(used_chip)
    used_pin_number_qc = EncodeDataUtility(used_pin_number)
    online_order_qc = EncodeDataUtility(online_order)
    fraud_qc = EncodeDataUtility(fraud)