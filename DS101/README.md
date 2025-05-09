# ❤️ Phân Loại Bệnh Nhân Suy Tim Bằng Naïve Bayes

**📚 Đồ án môn học:** Thống kê và xác suất chuyên sâu
**🏫 Trường:** Đại học Công nghệ Thông tin – ĐHQG TP.HCM

**👨‍💻 Nhóm sinh viên thực hiện:**

| STT | Họ tên                | MSSV      | Lớp      |
|-----|-----------------------|-----------|----------|
| 1   | Hồ Nguyễn Thiên Vũ    | 22521689  | KHDL2022 |
| 2   | Châu Nguyễn Tri Vũ    | 22521687  | KHDL2022 |

---

## 1. 🧾 Giới thiệu đề tài

Suy tim là một trong những căn bệnh tim mạch nguy hiểm, ảnh hưởng đến hàng triệu người trên toàn cầu. Đồ án này nghiên cứu và ứng dụng **thuật toán Naïve Bayes** – một phương pháp học máy dựa trên định lý Bayes – để phân loại bệnh nhân suy tim thành hai nhóm: **tử vong** và **sống sót** trong quá trình theo dõi lâm sàng.

Dữ liệu sử dụng bao gồm **299 bệnh nhân** với 13 thuộc tính y tế đặc trưng, được lấy từ UCI Machine Learning Repository. Mục tiêu là đánh giá hiệu suất mô hình trong các tỷ lệ chia train/test khác nhau và phân tích chi tiết qua các chỉ số như accuracy, recall, precision, F1-score, confusion matrix.

---

## 2. 📊 Tập dữ liệu

- **Nguồn:** [UCI Heart Failure Clinical Records Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records)
- **Số mẫu:** 299 bệnh nhân
- **Số đặc trưng:** 12 thuộc tính đầu vào + 1 thuộc tính mục tiêu (death event)
- **Các đặc trưng gồm:** tuổi, giới tính, thiếu máu, tiểu đường, cao huyết áp, hút thuốc, creatinine, sodium, tiểu cầu, ejection fraction, thời gian theo dõi, v.v.
- **Đặc trưng mục tiêu:** `DEATH_EVENT` (0: sống, 1: tử vong)

---

## 3. ⚙️ Phương pháp

### ✅ Mô hình sử dụng:
- **Naïve Bayes** – Dựa trên định lý Bayes với giả định độc lập giữa các đặc trưng
- Tiền xử lý bằng công cụ **Weka**

### ⚗️ Tỷ lệ chia dữ liệu:
- 60% train / 40% test
- 70% train / 30% test
- 80% train / 20% test (cho kết quả tốt nhất)

### 🧮 Đánh giá mô hình:
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix
- ROC, PRC Area

---

## 4. 💡 Kết luận

- **Naïve Bayes** là một phương pháp đơn giản nhưng hiệu quả trong việc phân loại bệnh nhân suy tim.
- Với bộ dữ liệu y tế thực tế, mô hình đạt độ chính xác đến **80%** cùng với các chỉ số đánh giá khả quan.
- Đây là công cụ hỗ trợ tiềm năng cho bác sĩ trong phân tầng nguy cơ bệnh nhân, tuy nhiên cần kết hợp thêm với chuyên môn y khoa và các mô hình phức tạp hơn trong thực tế.

---

## 5. 📚 Tài liệu tham khảo

- Anitha & Vanitha (2022), *Classification of VASA Dataset Using Naïve Bayes*  
- Brown et al. (2020), *Application of Naïve Bayes in heart failure classification*  
- Domingos & Pazzani (1997), *On the optimality of Naive Bayes*  
- Russell & Norvig (2016), *Artificial Intelligence – A Modern Approach*  
- UCI Machine Learning Repository

---

**📅 Thời gian hoàn thành:** 12/2023  
**👨‍🏫 Giảng viên hướng dẫn:** *Thầy Dương Ngọc Hảo*
