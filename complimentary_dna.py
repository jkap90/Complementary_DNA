def DNA_strand(dna):
    # code here
    a_compliment = 'T'
    t_compliment = 'A'
    c_compliment = 'G'
    g_compliment = 'C'

    compliment = ''
    for letter in dna:
        if letter == 'A':
            compliment = compliment + a_compliment
        elif letter == 'T':
            compliment = compliment + t_compliment
        elif letter == 'G':
            compliment = compliment + g_compliment
        elif letter == 'C':
            compliment = compliment + c_compliment
    print(f'String {dna} is {compliment}')
    
'''
Test cases

DNA_strand('AATGC')

DNA_strand("AAAA")
DNA_strand("ATTGC")
DNA_strand("GTAT")
'''
