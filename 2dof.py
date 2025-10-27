import math

# input panjang lengan
L1 = float(input("Masukkan Panjang Femur (L1) : "))
L2 = float(input("Masukkan Panjang Tibia (L2) : "))

# input sudut servo (dalam derajat)
theta1_deg = float(input("Masukkan Sudut Servo 1 (01, derajat) : "))
theta2_deg = float(input("Masukkan Sudut Servo 2 (02,  derajat) : "))

#konfersi ke radian
theta1 = math.radians(theta1_deg)
theta2 = math.radians(theta2_deg)

#rumus forward kinematics
x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

# menampilkan hasil
print("Koordinat ujung kaki robot : ")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")

# menampilkan posisi antar sendi
print("\nPosisi Tiap Sendi : ")
print(f"Sendi 1 (coxa) : (0.00 , 0.00)")
print(f"Sendi 2 (ujung femur) : ({L1 * math.cos(theta1):.2f} , {L1 * math.sin(theta1):.2f})")
print(f"Ujung Kaki (end-effector) : ({x:.2f} , {y:.2f})")