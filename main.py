import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
        
    if (S[0] == T[0]):
        return(MED(S[1:], T[1:]))

    #account for insertions, deletions, and substitutions
    insert = MED(S, T[1:])
    delete = MED(S[1:], T)
    substitute = MED(S[1:], T[1:])
    return (1 + min(insert, delete, substitute))
      

def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization

    #check if the strings are already stored in the moization dictionary
    if ((S, T) in MED):
        return(MED[(S, T)])

    #If the string is empty, return the length of the other string
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
        
    #If the first character of the strings are the same - just do rest of string
    if (S[0] == T[0]):
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
        return(MED[(S, T)])

    #Otherwise, calculate the minimum of insertion, deletion, and substitution
    insert = fast_MED(S, T[1:], MED)
    delete = fast_MED(S[1:], T, MED)
    substitute = fast_MED(S[1:], T[1:], MED)

    #find the minimum of the three and add 1
    MED[(S, T)] = 1 + min(insert, delete, substitute)
    return(MED[(S, T)])


def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment

     #check if the strings are already stored in the moization dictionary
    if (S, T) in MED:
        return MED[(S, T)]

    #If the string is empty, return the length of the other string
    if S == "":
        MED[(S, T)] = (len(T), '-' * len(T), T)
    elif T == "":
        MED[(S, T)] = (len(S), S, '-' * len(S))
        
    #If the first character of the strings are the same - just do rest of string
    elif S[0] == T[0]:
        dist, align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (dist, S[0] + align_S, T[0] + align_T)

    #Otherwise, calculate the minimum of insertion, deletion, and substitution
    else:
        # Insertion
        insert_dist, insert_S, insert_T = fast_align_MED(S, T[1:], MED)
        insert = (1 + insert_dist, '-' + insert_S, T[0] + insert_T)

        # Deletion
        delete_dist, delete_S, delete_T = fast_align_MED(S[1:], T, MED)
        delete = (1 + delete_dist, S[0] + delete_S, '-' + delete_T)

        # Substitution
        subs_dist, subs_S, subs_T = fast_align_MED(S[1:], T[1:], MED)
        substitute = (1 + subs_dist, S[0] + subs_S, T[0] + subs_T)

        # Choose the best one 
        best = min([insert, delete, substitute], key=lambda x: x[0])
        MED[(S, T)] = best

    return MED[(S, T)]


    
    
   

