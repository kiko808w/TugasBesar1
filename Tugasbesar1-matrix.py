import re

def decode_matrix():
    # Buka file 'input.txt' untuk dibaca
    with open('input.txt', 'r') as file:
        # Baca baris pertama dan ambil dua angka, n dan m
        dimensions = file.readline().split()
        n, m = map(int, dimensions)
        
        # Baca sisa baris dan susun menjadi matriks berukuran n x m
        matrix = []
        for _ in range(n):
            row = list(file.readline().strip().ljust(m, ' '))
            matrix.append(row)
    
    # Susun ulang matriks dengan cara memutar (transpose) dan gabungkan menjadi satu string
    decoded = ''.join([''.join(chars) for chars in zip(*matrix)])
    
    # Ganti karakter non-alfanumerik yang berdiri sendiri dengan spasi
    decoded_cleaned = re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded)
    
    # Tampilkan hasil dekripsi
    print(decoded_cleaned)

decode_matrix()
