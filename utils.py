# keep this here for now
PATH_TRANSACTION_FILE = "input_data/" + "TestTransaction.txt"
PATH_PARAMETER_FILE = "input_data/" + "TestParameter.txt"

import re


def readTransactionFile():
    
    fileData = open(PATH_TRANSACTION_FILE, "r+").readlines()

    # remove all whitespaces, all newline chars, trailing commas that have no input after it
    arrTransact = [line.replace(" ", "").rstrip("\n").rstrip(",") for line in fileData]
    print(arrTransact)

    # map to jagged int array
    transact = [list(map(int, line.split(","))) for line in arrTransact]

    return transact

# pass transactions here to get unique list of items & populate against MIS "rest" values
def readParameterFile(transactions):
    
    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    flattened_tr = list(set([item for sublist in transactions for item in sublist]))
    # print(flatted_tr)
    
    fileData = open(PATH_PARAMETER_FILE, "r+").readlines()
    arrParams = [line.replace(" ", "").rstrip("\n") for line in fileData]

    # now we must read exactly-> MIS(n)=<float_value> and MIS(rest)=<float_value> and SDC=<float_value>
    for param in arrParams:

        if param.find("SDC=") > -1:
            sdc = param[param.find("=") + 1 :]

            # assert if float works
            try:
                sdc = float(sdc)
            except ValueError:
                raise Exception("Error converting SDC value")
            
            
    return mis, sdc

