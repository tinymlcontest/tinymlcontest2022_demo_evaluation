import argparse
import serial
from datetime import datetime
import time
import numpy as np
from sklearn.metrics import confusion_matrix
from tqdm import tqdm
import os

def txt_to_numpy(filename, row):
    file = open(filename)
    lines = file.readlines()
    datamat = np.arange(row, dtype=np.float64)
    row_count = 0
    for line in lines:
        line = line.strip().split(' ')
        datamat[row_count] = line[0]
        row_count += 1

    return datamat

def main():
    t = time.strftime('%Y-%m-%d_%H-%M-%S')
    if not os.path.exists('./log/'):
        os.makedirs('./log/')
    List = []
    resultList = []
    labelList = []
    timeList = []
    port = args.com # set port number
    ser = serial.Serial(port=port, baudrate=115200) # open the serial
    print(ser)
    f = open('./test_indice.txt', 'r')
    for line in f:
        List.append(line)
    ofp = open(file='log/res_{}.txt'.format(t), mode='w') # make a new log file

    for idx in tqdm(range(0,len(List))):
        labelList.append(List[idx].split(',')[0])
        # load data from txt files and reshape to (1, 1, 1250, 1)
        testX = txt_to_numpy(args.path_data + List[idx].split(',')[1].strip(), 1250).reshape(1,1,1250,1)
        # receive messages from serial port, the length is the number of bytes remaining in the input buffer
        for i in range(0, testX.shape[0]):
            # don't continue running the code until a "begin" is received, otherwise receive iteratively
            while ser.in_waiting <5:
                pass
                time.sleep(0.01)

            # when receiving the code "begin", send the test data cyclically
            recv = ser.read(size=ser.in_waiting).decode(encoding='utf8')
            # clear the input buffer
            ser.reset_input_buffer()
            if recv.strip() == 'begin':
                for j in range(0, testX.shape[1]):
                    for k in range(0, testX.shape[2]):
                        for l in range(0, testX.shape[3]):
                            send_str = str(testX[i][j][k][l])+' '
                            ser.write(send_str.encode(encoding='utf8'))

                # Set a time point to represent that all data are sent and the development board starts to perform model inference.
                start_time = datetime.now()
                # don't continue running the code until a "ok" is received
                while ser.in_waiting < 2:
                    pass
                time.sleep(0.01)
                recv = ser.read(size=ser.in_waiting).decode(encoding='utf8')
                ser.reset_input_buffer()
                if recv.strip() == 'ok':
                    time.sleep(0.02)
                    # send status 200 to the board
                    send_str = '200 '
                    ser.write(send_str.encode(encoding='utf8'))
                    time.sleep(0.01)
                # receive results from the board, which is a string separated by commas
                while ser.in_waiting < 1:
                    pass
                recv = ser.read(size=1).decode(encoding='utf8')
                ser.reset_input_buffer()
                end_time = datetime.now()
                results = recv.strip()
                if results == '0':
                    resultList.append('0')
                else:
                    resultList.append('1')
                timeList.append(((end_time-start_time).seconds*1000)+((end_time-start_time).microseconds/1000)-44)
                ofp.write(str(results)+'\r')
    ofp.close()

    C = confusion_matrix(labelList, resultList)
    print(C)

    total_time = sum(timeList)
    avg_time = np.mean(timeList)
    acc = (C[0][0] + C[1][1]) / (C[0][0] + C[0][1] + C[1][0] + C[1][1])
    precision = C[1][1] / (C[1][1] + C[0][1])
    sensitivity = C[1][1] / (C[1][1] + C[1][0])
    FP_rate = C[0][1] / (C[0][1] + C[0][0])
    PPV = C[1][1] / (C[1][1] + C[1][0])
    NPV = C[0][0] / (C[0][0] + C[0][1])
    F1_score = (2 * precision * sensitivity) / (precision + sensitivity)
    F_beta_score = (1+2**2) * (precision * sensitivity) / ((2**2)*precision + sensitivity)

    print("\nacc: {},\nprecision: {},\nsensitivity: {},\nFP_rate: {},\nPPV: {},\nNPV: {},\nF1_score: {}, "
          "\ntotal_time: {},\n average_time: {}".format(acc, precision, sensitivity, FP_rate, PPV, NPV, F1_score,
                                                        total_time, avg_time))

    f = open('./log/log_{}.txt'.format(t), 'a')
    f.write("Accuracy: {}\n".format(acc))
    f.write("Precision: {}\n".format(precision))
    f.write("Sensitivity: {}\n".format(sensitivity))
    f.write("FP_rate: {}\n".format(FP_rate))
    f.write("PPV: {}\n".format(PPV))
    f.write("NPV: {}\n".format(NPV))
    f.write("F1_Score: {}\n".format(F1_score))
    f.write("F_beta_Score: {}\n".format(F_beta_score))
    f.write("Total_Time: {}\n".format(total_time))
    f.write("Average_Time: {}\n\n".format(avg_time))
    f.write(str(C)+"\n\n")
    f.close()

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--com', type=str, default='com5')
    argparser.add_argument('--path_data', type=str, default='path/to/dataset')
    args = argparser.parse_args()
    main()

