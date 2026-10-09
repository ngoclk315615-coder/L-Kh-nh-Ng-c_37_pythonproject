#1. Tạo DataFrame
import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Họ và tên': [
        'Nguyễn Minh Anh','Trần Bảo Bình','Lê Quốc Cường','Phạm Thùy Dương',
        'Hoàng Hải Đăng','Vũ Khánh Phương','Đoàn Gia Huy','Bùi Thu Hà',
        'Ngô Tuấn Kiệt','Đặng Bích Khuê',],
    'Điểm chuyên cần': [9.0, 8.0, 7.5, 6.0, 9.5, 5.0, 8.5, 10.0, 4.0, 7.0],
    'Điểm giữa kỳ': [8.5, 7.0, 6.0, 5.5, 9.0, 4.5, 7.5, 8.5, 5.0, 6.5],
    'Điểm cuối kỳ': [8.0, 8.5, 5.5, 4.0, 8.5, 6.0, 7.0, 9.0, 3.5, 6.0]}
df = pd.DataFrame(data)

#2.Tính điểm tổng kết.
df['Tổng kết'] = (
    0.20 * df['Điểm chuyên cần'] + 
    0.30 * df['Điểm giữa kỳ'] + 
    0.50 * df['Điểm cuối kỳ']).round(2)

#3.Xếp loại sinh viên.
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'
df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)
print("=== BẢNG DỮ LIỆU SAU KHI XẾP LOẠI ===")
print(df.to_string(index=False))

#4.Thống kê.
dtk_tb = df["Tổng kết"].mean()
sv_max = df.loc[df["Tổng kết"].idxmax()]
sv_min = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = (df["Tổng kết"] >= 5.0).sum()
print("=== KẾT QUẢ THỐNG KÊ ===")
print(f"1. Điểm tổng kết trung bình của lớp: {dtk_tb:.2f}")
print(f"2. Sinh viên điểm cao nhất: {sv_max['Họ và tên']} ({sv_max['Tổng kết']} điểm)")
print(f"3. Sinh viên điểm thấp nhất: {sv_min['Họ và tên']} ({sv_min['Tổng kết']} điểm)")
print(f"4. Số sinh viên đạt (Điểm tổng kết >= 5.0): {so_sv_dat}/{len(df)} sinh viên\n")

#5.Trực quan hóa.
plt.figure(figsize=(9, 5.5))
plt.barh(
    df['Họ và tên'],
    df['Tổng kết'],
    color='#5b9bd5',
    height=0.55,)
plt.gca().invert_yaxis()
plt.title('Điểm tổng kết của 10 sinh viên', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Điểm tổng kết', fontsize=11)
plt.ylabel('Họ và tên sinh viên', fontsize=11)
plt.xlim(0, 10)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_color('#cccccc')
plt.tight_layout()
plt.show()
