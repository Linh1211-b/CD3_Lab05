import pandas as pd
import numpy as np

# ==================== DỮ LIỆU SAU KHI LÀM SẠCH (từ bài trước) ====================
data_clean = {
    "MaSV": ["SV01", "SV02", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20.0, 21.0, 19.0, 22.83, 22.0, 22.83, 20.0],
    "GioiTinh": ["Nam", "Nữ", "Nữ", "Nam", "Nữ", "Nam", "Không rõ"],
    "GioTuHoc": [2.5, 3.0, 3.33, 2.0, 10.0, 3.33, 3.5],
    "GioMangXaHoi": [4.0, 5.0, 3.5, 6.58, 2.0, 5.0, 6.58],
    "DiemTB": [3.1, 2.8, 3.5, 2.0, 3.8, 3.28, 3.28]
}

df = pd.DataFrame(data_clean)

# ==================== CHUẨN HÓA DỮ LIỆU ====================

cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]

# 1. Chuẩn hóa Min-Max về khoảng [0, 1]
df_minmax = df.copy()
for col in cols:
    min_val = df[col].min()
    max_val = df[col].max()
    df_minmax[col] = (df[col] - min_val) / (max_val - min_val)

# 2. Chuẩn hóa Z-score
df_zscore = df.copy()
for col in cols:
    mean_val = df[col].mean()
    std_val = df[col].std()
    df_zscore[col] = (df[col] - mean_val) / std_val

# ==================== HIỂN THỊ KẾT QUẢ ====================

print("="*70)
print("DỮ LIỆU SAU KHI CHUẨN HÓA MIN-MAX [0, 1]")
print("="*70)
print(df_minmax.round(4))

print("\n"*2 + "="*70)
print("DỮ LIỆU SAU KHI CHUẨN HÓA Z-SCORE")
print("="*70)
print(df_zscore.round(4))

# ==================== KIỂM TRA KẾT QUẢ CHUẨN HÓA ====================

print("\n" + "="*70)
print("KIỂM TRA SAU CHUẨN HÓA")
print("="*70)

print("1. Min-Max Normalization:")
print("   Giá trị nhỏ nhất:", df_minmax[cols].min().values)
print("   Giá trị lớn nhất :", df_minmax[cols].max().values)

print("\n2. Z-score Normalization:")
print("   Trung bình từng cột:", df_zscore[cols].mean().round(4).values)
print("   Độ lệch chuẩn từng cột:", df_zscore[cols].std().round(4).values)