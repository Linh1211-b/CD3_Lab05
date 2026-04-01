import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("1. Ma trận điểm:")
print(scores)

print("\n2. Điểm TB toàn bộ:", np.mean(scores))
print("3. Điểm TB từng SV:", np.mean(scores, axis=1))
print("4. Điểm TB từng môn:", np.mean(scores, axis=0))
print("5. Điểm cao nhất:", np.max(scores), "- Thấp nhất:", np.min(scores))
print("6. Độ lệch chuẩn từng môn:", np.std(scores, axis=0))

avg_students = np.mean(scores, axis=1)
best = np.argmax(avg_students)
print(f"\n7. Sinh viên có điểm TB cao nhất: index {best} (SV thứ {best+1}), điểm TB = {avg_students[best]:.2f}")