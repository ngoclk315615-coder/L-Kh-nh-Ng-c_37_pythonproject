Python
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Cấu hình trang web
st.set_page_config(page_title="QUẢN LÝ ĐIỂM SINH VIÊN", layout="wide")

# Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")

# Dữ liệu 10 sinh viên
data = {
    'Họ và tên': [
        'Nguyễn Văn A',
        'Trần Thị B',
        'Lê Văn C',
        'Phạm Thị D',
        'Hoàng Văn E',
        'Vũ Thị F',
        'Đoàn Văn G',
        'Bùi Thị H',
        'Ngô Văn I',
        'Đặng Thị K',
    ],
    'Điểm chuyên cần': [9.0, 8.0, 7.5, 6.0, 9.5, 5.0, 8.5, 10.0, 4.0, 7.0],
    'Điểm giữa kỳ': [8.5, 7.0, 6.0, 5.5, 9.0, 4.5, 7.5, 8.5, 5.0, 6.5],
    'Điểm cuối kỳ': [8.0, 8.5, 5.5, 4.0, 8.5, 6.0, 7.0, 9.0, 3.5, 6.0],
}

df = pd.DataFrame(data)

# Tính điểm Tổng kết
df['Tổng kết'] = (
    0.20 * df['Điểm chuyên cần']
    + 0.30 * df['Điểm giữa kỳ']
    + 0.50 * df['Điểm cuối kỳ']
).round(2)


# Hàm xếp loại
def xep_loai(score):
    if score >= 8.5:
        return 'Giỏi'
    elif score >= 7.0:
        return 'Khá'
    elif score >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'


df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 1. Hiển thị bảng điểm sinh viên
st.subheader("📋 Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# 2. Hiển thị thông tin thống kê
st.subheader("📊 Thống kê lớp học")
dtk_tb = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình lớp", f"{dtk_tb:.2f}")
col2.metric(
    "Điểm cao nhất", f"{sv_max['Tổng kết']}", f"SV: {sv_max['Họ và tên']}"
)
col3.metric(
    "Điểm thấp nhất", f"{sv_min['Tổng kết']}", f"SV: {sv_min['Họ và tên']}"
)
col4.metric("Số sinh viên đạt (≥ 5.0)", f"{so_sv_dat}/{len(df)}")

st.divider()

# 3. Tra cứu thông tin bằng Selectbox[cite: 3]
st.subheader("🔍 Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn một sinh viên:", df['Họ và tên'])

if selected_student:
    sv_info = df[df['Họ và tên'] == selected_student].iloc[0]
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.write(f"**Chuyên cần:** {sv_info['Điểm chuyên cần']}")
    c2.write(f"**Giữa kỳ:** {sv_info['Điểm giữa kỳ']}")
    c3.write(f"**Cuối kỳ:** {sv_info['Điểm cuối kỳ']}")
    c4.write(f"**Tổng kết:** {sv_info['Tổng kết']}")
    c5.write(f"**Xếp loại:** {sv_info['Xếp loại']}")

st.divider()

# 4. Hiển thị biểu đồ cột điểm tổng kết[cite: 3]
st.subheader("📈 Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(df['Họ và tên'], df['Tổng kết'], color='#5b9bd5', height=0.55)
ax.invert_yaxis()

ax.set_title('Điểm tổng kết của 10 sinh viên', fontsize=13, fontweight='bold')
ax.set_xlabel('Điểm tổng kết', fontsize=11)
ax.set_ylabel('Họ và tên sinh viên', fontsize=11)
ax.set_xlim(0, 10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#cccccc')

st.pyplot(fig)

# 5. Thông tin sinh viên tạo app ở cuối trang (chữ nhỏ)[cite: 3]
st.markdown("---")
st.caption("Người thực hiện: **Nguyễn Văn A** | MSSV: **12345678**")
