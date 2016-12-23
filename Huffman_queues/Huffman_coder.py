def read_data():
    line = input()
    alphabet = {}
    for symbol in line:
        if symbol not in alphabet:
            alphabet[symbol] = line.count(symbol)
    return(line, alphabet)

def extract_min(alphabet):
    minf = 10000
    for symbol in alphabet:
        if alphabet[symbol] < minf:
            minf = alphabet[symbol]
            letter = symbol
    return(letter, minf)

def huffman_coder(alphabet):
    new_alphabet = {}
    if len(alphabet) == 1:
        for symbol in alphabet:
            new_alphabet[symbol] = '0'
    while len(alphabet) > 1:
        letter_i, f_i = extract_min(alphabet)
        del alphabet[letter_i]
        letter_j, f_j = extract_min(alphabet)
        del alphabet[letter_j]
        alphabet[letter_i + letter_j] = f_i + f_j
        for symbol in letter_i:
            if symbol in new_alphabet:
                new_alphabet[symbol] = '0' + new_alphabet[symbol]
            else:
                new_alphabet[symbol] = '0'
        for symbol in letter_j:
            if symbol in new_alphabet:
                new_alphabet[symbol] = '1' + new_alphabet[symbol]
            else:
                new_alphabet[symbol] = '1'
    return(new_alphabet)

def huffman_line_coder(line, alphabet):
    code = ''
    for symbol in line:
        code += alphabet[symbol]
    return(code)



line, alphabet = read_data()
new_alphabet = huffman_coder(alphabet)
code = huffman_line_coder(line, new_alphabet)
print(str(len(new_alphabet)) + ' ' + str(len(code)))
for symbol in new_alphabet:
    print(symbol + ': ' + str(new_alphabet[symbol]))
print(code)
