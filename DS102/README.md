# 🧬 Chẩn đoán Tế Bào Khối U Lành Tính / Ác Tính Trong Ung Thư Vú

**📚 Đồ án môn học:** Nhập môn Khoa học Dữ liệu  
**🏫 Trường:** Đại học Công nghệ Thông tin – ĐHQG TP.HCM  

**👨‍💻 Nhóm sinh viên thực hiện:**

| STT | Họ tên               | MSSV      | Ngành                     |
|-----|----------------------|-----------|---------------------------|
| 1   | Lê Tiến Quyết        | 21520428  | Khoa học máy tính         |
| 2   | Hồ Nguyễn Thiên Vũ   | 22521689  | Khoa học dữ liệu          |
| 3   | Nguyễn Phi Long      | 22520818  | Khoa học dữ liệu          |

---

## 1. 🧾 Giới thiệu

Ung thư vú là một trong những căn bệnh phổ biến và nguy hiểm ở nữ giới. Việc chẩn đoán sớm tính chất của khối u (lành tính hoặc ác tính) có vai trò quan trọng trong điều trị.

Trong đồ án này, nhóm áp dụng các thuật toán học máy kết hợp với xử lý dữ liệu, lựa chọn đặc trưng và tinh chỉnh tham số nhằm xây dựng mô hình hỗ trợ chẩn đoán bệnh từ dữ liệu tế bào khối u vú.

---

## 2. 📊 Dữ liệu sử dụng

- **Nguồn:** [Kaggle - Breast Cancer Wisconsin Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)  
- **Số lượng mẫu:** 569  
- **Số thuộc tính:** 30 đặc trưng + 1 nhãn (`diagnosis`)  
- **Tỉ lệ phân chia:** 80% train – 20% test  
- **Nhãn:** `0` – Lành tính | `1` – Ác tính

---

## 3. 🛠️ Phương pháp thực hiện

### ⚙️ Mô hình sử dụng
- 💡 **SVM (Support Vector Machine)**
- 🌲 **Random Forest**
- 📈 **Logistic Regression**

### 🔁 Quy trình thực hiện
- Xử lý dữ liệu với MinMaxScaler, PCA
- Tinh chỉnh siêu tham số bằng GridSearchCV
- Đánh giá mô hình bằng Accuracy và F1-score

---

## 4. ✅ Kết luận

Nhóm đã xây dựng thành công hệ thống chẩn đoán khối u vú dựa trên dữ liệu tế bào học, với hiệu suất trên 95% cho tất cả các mô hình. Các kết quả đạt được khẳng định tiềm năng ứng dụng Machine Learning trong hỗ trợ y tế, đặc biệt là trong việc chẩn đoán sớm ung thư vú.

> ⚠️ Mô hình không thay thế bác sĩ nhưng có thể giảm tải khối lượng công việc, hỗ trợ hiệu quả trong thực hành lâm sàng.

---
  
**🗓️ Thời gian hoàn thành:** 06/2024
