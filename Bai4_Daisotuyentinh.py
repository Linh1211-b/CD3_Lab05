import numpy as np

A = np.array([[2, 1], [1, 3]])
B = np.array([[4, 2], [1, 5]])
b = np.array([5, 7])

print("A + B =\n", A + B)
print("\nA - B =\n", A - B)
print("\nA @ B =\n", A @ B)
print("\ndet(A) =", np.linalg.det(A))
print("\nA^-1 =\n", np.linalg.inv(A))
print("\nNghiệm hệ phương trình:", np.linalg.solve(A, b))

# Kiểm tra nghiệm
print("\nKiểm tra nghiệm:", A @ np.linalg.solve(A, b))