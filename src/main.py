import encodeData
from autoEncoder import AutoEncoder

CATEGORIES = 7

def main():
    (normal_data, fraud_data)  = encodeData.EncodeData(CATEGORIES, "../data/test_data.csv")
    theta_list = [0] * normal_data.num_qubits    # NOTE: temporary
    # AutoEncoder(normal_data, CATEGORIES, theta_list)

if __name__ == "__main__":
    main()

