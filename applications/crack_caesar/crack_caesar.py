# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# get filestring split into letters
# create a histogram for letters
# normalize the counts to show percentage '0.00'

# create a dictionary with frequency data

# with a sorted dictionaries get the most highest used letter
# create a dictionary with a mapping to use switch

# using split letters switch using ciphertext

# create alphabet dictionary
def decode(filename):
    frequency_data = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
    'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    # Frequency Analysis
    letter_count = { chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

    with open(filename) as f:
        filestring = f.read()
        
    result = ''
    for l in filestring:
        if l in letter_count:
            letter_count[l] += 1
        
    ordered_letters = [k for k, v in sorted(letter_count.items(), key=lambda items: -items[1])]
    decode_table = dict(zip(ordered_letters,frequency_data))
    for i in filestring:
        if i in decode_table:
            result += decode_table[i]
        else:
            result += i

    return result

if __name__ == "__main__":
    result = decode('ciphertext.txt')
    print(result)