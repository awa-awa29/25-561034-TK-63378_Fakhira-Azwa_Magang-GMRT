import math

# input panjang lengan
L1 = float(input("Masukkan Panjang Femur (L1) : "))
L2 = float(input("Masukkan Panjang Tibia (L2) : "))

# input posisi ujung kaki
x = float(input("Masukkan Koordinat x : "))
y = float(input("Masukkan Koordinat y : "))

# hitung nilai cos(theta2)
cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)

# cek apakah posisi bisa dijangkau
if abs(cos_theta2) > 1:
    print("\nPosisi tidak dapat dijangkau oleh robot (diluar jangkauan)")
else:
    # Hitung dua kemungkinan sudut (siku ke atas dan ke bawah)
    theta2a = math.acos(cos_theta2)
    theta2b = -math.acos(cos_theta2)

    # hitung theta1 untuk masing-masing kemungkinan
    theta1a = math.atan2(y, x) - math.atan2(L2 * math.sin(theta2a), L1 + L2 * math.cos(theta2a))
    theta1b = math.atan2(y, x) - math.atan2(L2 * math.sin(theta2b), L1 + L2 * math.cos(theta2b))

    # konversi ke derajat
    theta1a_deg = math.degrees(theta1a)
    theta2a_deg = math.degrees(theta2a)
    theta1b_deg = math.degrees(theta1b)
    theta2b_deg = math.degrees(theta2b)

    # Tampilkan hasil
    print("\nSolusi 1 (siku ke bawah) : ")
    print(f"01 = {theta1a_deg:.2f}")
    print(f"02 = {theta2a_deg:.2f}")

    print("\nSolusi 2 (siku ke atas) : ")
    print(f"01 = {theta1b_deg:.2f}")
    print(f"02 = {theta2b_deg:.2f}")
    