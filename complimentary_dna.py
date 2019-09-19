def DNA_strand(dna):
    # Dictionary with key : values
    # Print(key) returns value
    complement = { "A":"T",
                   "T":"A",
                   "C":"G",
                   "G":"C"
                 }
    # .join() joins to given string
    # write what you want to iterate as a for loop(with [] since you're calling a dictionary) : the letters in the given dna sequequence
    # in this case letter = key in 'complement'
    # precede it with the desire result
    print("".join([complement[letter] for letter in dna]))
