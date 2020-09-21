import utils, itertools
from operator import itemgetter

M = []
L = []
sup_count = {}

transactions = utils.readTransactionFile()
MIS, SDC = utils.readParameterFile(transactions)
print("MIS", MIS)
##### Calculate M <- sort(I, MS) where I == items in transactions
M = sorted(MIS.items(), key=itemgetter(1))

n = len(transactions)
##### L <- init-pass(M,T)
for t in transactions:
    for i in t:
        sup_count[i] = sup_count.get(i, 0) + 1

min_sup = None

print("M", M)
print("sup_count", sup_count)
for m in M:
    m_key = m[0]
    ms_val = [item for item in M if item[0] == m_key][0][1]

    # if m_key in sup_count:
    #     print(m_key, sup_count[m_key], sup_count[m_key] / n,  [item for item in M if item[0] == m_key][0])

    if min_sup:
        if m_key in sup_count and sup_count[m_key] / n >= min_sup:
            L.append(m)
    elif m_key in sup_count and sup_count[m_key] / n >= ms_val:
        L.append(m)
        min_sup = ms_val

print("min_sup", min_sup)
print("L", L)

F = {}

if len(L) == 0:
    print(" NO FREQ ITEMS ")

##### F1 <- {{i} | i in L, i.count/ n >= MS(i)}
F[1] = [[L[0]]]
for i in L[1:]:
    if sup_count[i[0]] / n >= MIS[i[0]]:
        F[1].append([i])

print("F", F)


def level2_candidate_gen(L_copy):
    c = []
    for i, l in enumerate(L_copy):
        lkey = l[0]
        if sup_count[lkey] / n >= MIS[lkey]:
            for j in range(i + 1, len(L_copy)):
                if (
                    sup_count[L_copy[j]] / n > MIS[lkey]
                    and abs(sup_count[L_copy[j]] / n - sup_count[lkey] / n) <= SDC
                ):
                    c.append({"c": [lkey, L_copy[j]], "count": 0})
    return c

def MScandidate_gen(F_copy, k):
    c = []
    for i, f1 in enumerate(F_copy):
        for j, f2 in enumerate(F_copy[i+1:]):
            if set(f1[:-1]) == set(f2[:-1]) and abs(sup_count[f2[k-2]]/n - sup_count[f1[k-2]]/n) <= SDC: 
                candidate = list(f1)
                candidate.append(f2[k-2])
                delete = False
                for s in list(itertools.combinations(candidate, k-1)):
                    if candidate[0] in s or MIS[candidate[0]] == MIS[candidate[1]]:
                        if list(s) not in F:
                            delete = True
                if not delete:
                    c.append({'c':candidate,'count':0})
    return c


C = {}
for k in range(2, 10):
    if k == 2:
        ##### C2 <- level2-candidate-gen(L, SDC)
        C[k] = level2_candidate_gen(L)
    else:
        ##### Cl <- MScandidate-gen(Fk-1, SDC)
        C[k] = MScandidate_gen(F[k - 1], k)
        
