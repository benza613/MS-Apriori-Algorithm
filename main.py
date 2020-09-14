import utils

M = []

transactions = utils.readTransactionFile()
MIS, sdc = utils.readParameterFile(transactions)

# Calculate M <- sort(I, MS)