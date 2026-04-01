import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ==================== Phần 1: Một random walk ====================
steps = np.random.choice([-1, 1], size=100)
walk = np.cumsum(steps)

print("10 vị trí đầu tiên:", walk[:10])
print("Vị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

# Vẽ đồ thị
plt.figure(figsize=(10, 6))
plt.plot(walk)
plt.title("Random Walk 1 chiều - 100 bước")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.axhline(0, color='red', linestyle='--')
plt.show()

# ==================== Phần nâng cao: 100 random walk ====================
steps_many = np.random.choice([-1, 1], size=(100, 100))
walks_many = np.cumsum(steps_many, axis=1)

print("\nSố walk kết thúc dương:", np.sum(walks_many[:, -1] > 0))
print("Số walk chạm ngưỡng |10|:", np.sum(np.any(np.abs(walks_many) >= 10, axis=1)))