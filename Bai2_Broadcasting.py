import numpy as np
np.set_printoptions(precision=2, suppress=True, linewidth=100)

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

# ===================== Z-score =====================
mean_col = np.mean(scores, axis=0)
std_col  = np.std(scores, axis=0)
z_scores = (scores - mean_col) / std_col

print("=== Z-score Normalization ===")
print(np.round(z_scores, 2))

print("\nTrung bình các cột sau khi chuẩn hóa Z-score:")
print(np.round(np.mean(z_scores, axis=0), decimals=10))

# ===================== Min-Max [0,1] =====================
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)
min_max_scaled = (scores - min_col) / (max_col - min_col)

print("\n=== Min-Max Normalization [0,1] ===")
print(np.round(min_max_scaled, 2))