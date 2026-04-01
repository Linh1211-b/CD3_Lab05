import pandas as pd
import numpy as np

# ========================== TẠO DỮ LIỆU GỐC ==========================
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 20, 2, 5, None],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None]
}

df = pd.DataFrame(data)

print("========== DỮ LIỆU GỐC ==========")
print(df)
print("\nKích thước dữ liệu:", df.shape)
print("\nSố lượng giá trị thiếu theo từng cột:")
print(df.isnull().sum())

# ========================== LÀM SẠCH DỮ LIỆU ==========================

# 1. Xóa bản ghi trùng lặp theo MaSV
df = df.drop_duplicates(subset="MaSV").reset_index(drop=True)

# 2. Chuẩn hóa cột GioiTinh
df["GioiTinh"] = df["GioiTinh"].astype(str).str.strip().str.capitalize()
df["GioiTinh"] = df["GioiTinh"].replace({"Nu": "Nữ", "Nan": "Không rõ"})
df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# 3. Điền giá trị thiếu bằng trung bình cho các cột số
numeric_cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# 4. Xử lý giá trị bất thường (Outlier)
df.loc[df["Tuoi"] > 30, "Tuoi"] = df["Tuoi"].mean()                    # Tuổi > 30
df.loc[df["GioTuHoc"] < 0, "GioTuHoc"] = df["GioTuHoc"].mean()         # Giờ tự học âm
df.loc[df["GioMangXaHoi"] > 12, "GioMangXaHoi"] = df["GioMangXaHoi"].mean()  # Mạng xã hội > 12h
df.loc[df["DiemTB"] > 4.0, "DiemTB"] = df["DiemTB"].mean()             # Điểm TB > 4.0

# ========================== HIỂN THỊ KẾT QUẢ ==========================
print("\n" + "="*60)
print("DỮ LIỆU SAU KHI LÀM SẠCH")
print("="*60)
print(df.round(2))

print("\nKiểm tra lại dữ liệu thiếu sau khi xử lý:")
print(df.isnull().sum())

# Thống kê mô tả sau khi làm sạch
print("\nThống kê mô tả dữ liệu sau khi làm sạch:")
print(df.describe().round(2))

# ========================== LƯU FILE (tùy chọn) ==========================
# df.to_excel("SinhVien_Sach.xlsx", index=False)
# df.to_csv("SinhVien_Sach.csv", index=False, encoding='utf-8-sig')

print("\nHoàn tất làm sạch dữ liệu!")