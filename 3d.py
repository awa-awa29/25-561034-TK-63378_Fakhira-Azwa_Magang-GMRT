import numpy as np
import math
import matplotlib.pyplot as plt

# input panjang
L1 = float(input("Masukkan panjang link 1 (L1): "))
L2 = float(input("Masukkan panjang link 2 (L2): "))
L3 = float(input("Masukkan panjang link 3 (L3): "))

# input sudut (dalam derajat)
theta1 = math.radians(float(input("Masukkan sudut θ1 (rotasi horizontal): ")))
theta2 = math.radians(float(input("Masukkan sudut θ2 (rotasi vertikal 1): ")))
theta3 = math.radians(float(input("Masukkan sudut θ3 (rotasi vertikal 2): ")))

# Matriks rotasi & translasi
def Tz(theta):
    return np.array([
        [math.cos(theta), -math.sin(theta), 0, 0],
        [math.sin(theta),  math.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def Ty(theta, L):
    return np.array([
        [math.cos(theta), 0, math.sin(theta), L * math.cos(theta)],
        [0, 1, 0, 0],
        [-math.sin(theta), 0, math.cos(theta), -L * math.sin(theta)],
        [0, 0, 0, 1]
    ])

# Hitung transformasi total
T1 = Tz(theta1)
T2 = Ty(theta2, L1)
T3 = Ty(theta3, L2)

T_total = T1 @ T2 @ T3

# Ambil posisi end-effector
x = T_total[0, 3] + L3 * math.cos(theta2 + theta3) * math.cos(theta1)
y = T_total[1, 3] + L3 * math.cos(theta2 + theta3) * math.sin(theta1)
z = T_total[2, 3] + L3 * math.sin(theta2 + theta3)

print("\nKoordinat Ujung Kaki (End-Effector):")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")

# Visualisasi 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Titik-titik sendi
x_points = [0,
            L1 * math.cos(theta2) * math.cos(theta1),
            x]
y_points = [0,
            L1 * math.cos(theta2) * math.sin(theta1),
            y]
z_points = [0,
            L1 * math.sin(theta2),
            z]

# Gambar lengan
ax.plot(x_points, y_points, z_points, '-o', linewidth=3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualisasi Robot 3 DOF')
ax.set_box_aspect([1, 1, 1])
plt.show()
