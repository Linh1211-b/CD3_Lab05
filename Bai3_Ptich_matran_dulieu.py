import numpy as np

quantity = np.array([
    [10, 12, 9, 14],
    [5, 7, 8, 6],
    [20, 18, 25, 22]
])
price = np.array([15000, 25000, 10000])

revenue = quantity * price.reshape(3, 1)

print("=== DOANH THU CỬA HÀNG ===\n")
print("1. Doanh thu từng sản phẩm theo ngày:\n", revenue)
print("\n2. Tổng doanh thu từng sản phẩm:", sum_product := np.sum(revenue, axis=1))
print("3. Tổng doanh thu từng ngày    :", sum_day := np.sum(revenue, axis=0))
print(f"\n4. Ngày có doanh thu cao nhất: Ngày {np.argmax(sum_day)+1} ({sum_day.max():,} VNĐ)")

ratio = sum_product / np.sum(sum_product)
print("\n5. Tỷ trọng đóng góp của từng sản phẩm:")
print(np.round(ratio * 100, 2), "%")
print(f"Tổng doanh thu 4 ngày: {np.sum(revenue):,} VNĐ")