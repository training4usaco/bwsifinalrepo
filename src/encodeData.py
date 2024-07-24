import csv
import sys
import numpy as np
from math import ceil, log2, pi
from pathlib import Path
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import ControlledGate, RYGate

def DecimalToBinary(n): 
    return bin(n).replace("0b", "") 

def EncodeDataUtility(data_set) -> QuantumCircuit:
    # TODO: encode each dataset with entanglement
    # for normalizing
    tot = np.sum(data_set)
    mn = np.min(data_set)

    # sizes
    N = len(data_set)   # number of datapoints
    n = ceil(log2(N))  # need extra qubit as target qubit to hold the encryption

    qc = QuantumCircuit(n + 1)
    qc.h(range(n))

    for i in range(N):
        datapoint = data_set[i]
        datapoint -= mn
        datapoint = datapoint / tot * pi    # scale properly. NOTE: SCALED FROM 0 TO PI!

        binrep = str(DecimalToBinary(i))[::-1]  # reverse because ctrl_state is in little endian

        # https://quantumcomputing.stackexchange.com/questions/27077/qiskit-custom-multi-controlled-gate <- example (the documentations bad)

        rry = RYGate(datapoint) # custom gate
        mcry = ControlledGate(name="mcry", num_qubits=n+1, params=rry.params, num_ctrl_qubits=n, definition=rry.definition, ctrl_state=binrep, base_gate=rry)
        qc.append(mcry(range(n)))
        # ccry = ControlledGate(name="cry", num_qubits=3, params=rry.params, num_ctrl_qubits=2, definition=rry.definition,ctrl_state='01', base_gate=rry)

    return qc

def EncodeData(relative_path = "../data/card_transdata.csv"):
    # reads in the data

    distance_from_home = []
    distance_from_last_purchase = []
    ratio_to_median = []
    repeat_retailer = []
    used_chip = []
    used_pin_number = []
    online_order = []
    fraud = []

    absolute_path = Path(__file__).parent / relative_path
    with open(absolute_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:  # pls help idk how to pythong
            distance_from_home.append(row[0])
            distance_from_last_purchase.append(row[1])
            ratio_to_median.append(row[2])
            repeat_retailer.append(row[3])
            used_chip.append(row[4])
            used_pin_number.append(row[5])
            online_order.append(row[6])
            fraud.append(row[7])
    
    # encode all the data
    distance_from_home_qc = EncodeDataUtility(distance_from_home)
    distance_from_last_purchase_qc = EncodeDataUtility(distance_from_last_purchase)
    ratio_to_median_qc = EncodeDataUtility(ratio_to_median)
    repeat_retailer_qc = EncodeDataUtility(repeat_retailer_qc)
    used_chip_qc = EncodeDataUtility(used_chip)
    used_pin_number_qc = EncodeDataUtility(used_pin_number)
    online_order_qc = EncodeDataUtility(online_order)
    fraud_qc = EncodeDataUtility(fraud)

    