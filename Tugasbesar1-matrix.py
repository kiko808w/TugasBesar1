import re

def decode_matrix():
    with open('input.txt', 'r') as file:
        dimensions = file.readline().split()
        n, m = map(int, dimensions)
        
        matrix = []
        for _ in range(n):
            row = list(file.readline().strip().ljust(m, ' '))
            matrix.append(row)
    
    decoded = ''.join([''.join(chars) for chars in zip(*matrix)])
    
    decoded_cleaned = re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded)
    
    print(decoded_cleaned)

decode_matrix()
