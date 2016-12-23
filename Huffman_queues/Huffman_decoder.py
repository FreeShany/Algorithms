def read_data():
    line = input().split()
    letters_n = line[0]
    code_len = line[1]
    alphabet = {}
    for i in range(int(letters_n)):
        s = input().split(': ')
        alphabet[s[1]] = s[0]
    code = input()
    return alphabet, code

def Huffman_decoder(alphabet, code):
    substring = ''
    decoded_line = ''
    for symbol in code:
        substring += symbol
        if substring in alphabet:
            decoded_line += alphabet[substring]
            substring = ''
    return decoded_line


alphabet, code = read_data()
print(Huffman_decoder(alphabet, code))
