# 16
N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))
apples_per_student = K // N
apples_remaining = K % N
print(f"Each student gets {apples_per_student} apples.")
print(f"{apples_remaining} apples remain in the basket.")
