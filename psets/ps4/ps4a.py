# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # pass #delete this line and replace with your code here
    import math
    l = list(sequence)
    perm_list = []
    
    if len(sequence) == 1:
        return(l)
    
    else:
        iter_list = get_permutations(sequence[1:len(sequence)])
        for list_comb in range(math.factorial(len(l)-1)):
            for i in range(len(l)):
                perm_list.append(mutate_get_permutations(iter_list, list_comb, i, l))
        return(perm_list)
    
def mutate_get_permutations(m, comb, i, l):
    import copy
    if len(m) == 1:
        m_m = copy.deepcopy(m)
        m_m.insert(i, l[0])
    else:
        m_m = copy.deepcopy(m[comb])
        m_m.insert(i, l[0])
    # if len(m_m) == x:
    #     m_m = ''.join(m_m)
    return(m_m)

def el_to_str(perms):
    l = perms[:]
    for i in range(len(l)):
        l[i] = ''.join(l[i])
    # for el in l:
    #     print(''.join(s for s in el), end=' ')
    print(l)




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here
    
    el_to_str(get_permutations('abc'))
    # print(get_permutations('abc'))
