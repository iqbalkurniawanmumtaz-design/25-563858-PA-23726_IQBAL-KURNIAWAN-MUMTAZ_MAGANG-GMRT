import math

def F(jadi_derajat):
    return jadi_derajat * math.pi / 180.0

def main():
    n = int(input("Masukkan jumlah link (lengan robot): "))

    panjang = []
    sudut_mentah = []
    sudut_derajat = []

    print("Panjang Tiap Lengan")
    for i in range(n):
        nilai = float(input(f"Panjang lengan ke-{i + 1}: "))
        panjang.append(nilai)

    print("Masukkan sudut pergerakkan:")
    for i in range(n):
        nilai = float(input(f"Sudut lengan ke-{i + 1} (°): "))
        sudut_mentah.append(nilai)
        sudut_derajat.append(F(nilai))

    x, y = 0.0, 0.0
    total_sudut = 0.0

    for i in range(n):
        total_sudut += sudut_derajat[i]
        x += panjang[i] * math.cos(total_sudut)
        y += panjang[i] * math.sin(total_sudut)

    print("\nHasil Forward Kinematics:")
    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")

if __name__ == "__main__":
    main()
