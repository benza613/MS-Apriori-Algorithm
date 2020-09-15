# keep this here for now
PATH_TRANSACTION_FILE = "input_data/" + "TestTransaction.txt"
PATH_PARAMETER_FILE = "input_data/" + "TestParameter.txt"

import re


def readTransactionFile():

    fileData = open(PATH_TRANSACTION_FILE, "r+").readlines()

    # remove all whitespaces, all newline chars, trailing commas that have no input after it
    arrTransact = [line.replace(" ", "").rstrip("\n").rstrip(",") for line in fileData]
    # print(arrTransact)

    # map to jagged int array
    transact = [list(map(int, line.split(","))) for line in arrTransact]
    print(transact)

    return transact


# pass transactions here to get unique list of items & populate against MIS "rest" values
def readParameterFile(transactions):

    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    flattened_tr = list(set([item for sublist in transactions for item in sublist]))
    print(flattened_tr)

    mis = {}

    fileData = open(PATH_PARAMETER_FILE, "r+").readlines()
    arrParams = [line.replace(" ", "").rstrip("\n") for line in fileData]

    # now we must read exactly-> MIS(n)=<float_value> and MIS(rest)=<float_value> and SDC=<float_value>
    for param in arrParams:

        if param.find("MIS") > -1:
            # get indices
            key_start_idx = param.find("(")
            key_end_idx = param.find(")")
            val_start_idx = param.find("=")
            
            # extract & record dict keys and vals 
            key = param[key_start_idx + 1 : key_end_idx]
            val = float((param[val_start_idx + 1 :]))
            
            if key != 'rest':
                mis[int(key)] = val
            else:
                # if REST -> we have to add this value for keys not in dict already  
                for iter in flattened_tr:
                    if iter not in mis.keys():
                        mis[int(iter)] = val
                        

        if param.find("SDC=") > -1:
            sdc = param[param.find("=") + 1 :]

            # assert if float works
            try:
                sdc = float(sdc)
            except ValueError:
                raise Exception("Error converting SDC value")

    print(sdc)
    print(mis)
    return mis, sdc
