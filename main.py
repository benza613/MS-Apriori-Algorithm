import utils
from operator import itemgetter

M = []

transactions = utils.readTransactionFile()
MIS, sdc = utils.readParameterFile(transactions)

# Calculate M <- sort(Items, MS)
M = sorted(MIS.items(), key=itemgetter(1))
print(M)