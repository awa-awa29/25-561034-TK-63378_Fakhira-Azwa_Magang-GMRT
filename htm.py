import numpy as np
import math

# input data panjang lengan
L1 = float(input("Masukkan Panjang Femur (L1) : "))
L2 = float(input("Masukkan Panjang Tibia (L2) : "))

# input sudut servo (dalam derajat)
theta1_deg = float(input("Masukkan Sudut Servo 1 (01, derajat) : "))
theta2_deg = float(input("Masukkan Sudut Servo 2 (02,  derajat) : "))

# konversi ke radian
theta1 = math.radians(theta1_deg)
theta2 = math.radians(theta2_deg)

# Matrix transformasi homogen
T1 = np.array([
    [math.cos(theta1), -math.sin(theta1), L1 * math.cos(theta1)],
    [math.sin(theta1), math.cos(theta1), L1 * math.sin(theta1)],
    [ 0, 0, 1]
])

T2 = np.array([
    [math.cos(theta2), -math.sin(theta2), L2 * math.cos(theta2)],
    [math.sin(theta2), math.cos(theta2), L2 * math.sin(theta2)],
    [ 0, 0, 1]
])

# kalikan T1 dan T2
T_total = np.dot(T1, T2)

# ambil posisi end-effector
x = T_total[0, 2]
y = T_total[1, 2]

# menampilkan hasil
print("\nMatrix Transformasi Total (T_total) : ")
print(np.round(T_total, 3))

print("\nKoordinat Ujung Kaki Robot (end-effector) : ")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")