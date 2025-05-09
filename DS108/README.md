# 🌸 Xây Dựng Bộ Dữ Liệu Gợi Ý Hoa – Tiền Xử Lý & Phân Loại Hình Ảnh

**📚 Đồ án môn học:** Tiền xử lý và Xây dựng bộ dữ liệu  
**🏫 Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM**

**👨‍💻 Thành viên nhóm:**
| STT | Họ và tên              | MSSV      | Email                  |
|-----|------------------------|-----------|------------------------|
| 1   | Hồ Nguyễn Thiên Vũ     | 22521689  | 22521689@gm.uit.edu.vn |
| 2   | Lê Vy                  | 22521703  | 22521703@mail.edu.vn   |
| 3   | Lưu Bảo Uyên           | 22521640  | 22521640@mail.edu.vn   |
| 4   | Trần Lương Vân Nhi     | 22521044  | 22521044@gm.edu.vn     |
---

## 1. 📌 Mô tả dự án

Đồ án tập trung xây dựng bộ dữ liệu hình ảnh các loài hoa nhằm phục vụ ứng dụng **gợi ý hoa trang trí**. Quy trình bao gồm: thu thập ảnh, tiền xử lý, phân đoạn, trích xuất đặc trưng và huấn luyện mô hình phân loại bằng các thuật toán học máy (Random Forest và SVM). Đồng thời, nhóm thử nghiệm các bộ lọc cạnh như Sobel, Prewitt và Scharr để cải thiện đặc trưng ảnh.

---

## 2. 📁 Tóm tắt bộ dữ liệu

- **Tổng số ảnh thu thập:** 17.808 ảnh (từ Wikimedia, Pixabay, Pexels, Unsplash, Oxford 102flowers)  
- **Sau lọc nhiễu:** 1.674 ảnh thuộc 14 loài hoa  
- **Nhãn:** Tên khoa học và màu sắc chủ đạo  
- **Yêu cầu ảnh:** Rõ nét, chính diện, độ phân giải >6MP, chuẩn kích thước 180x200 mm  

---

## 3. 🛠️ Tiền xử lý dữ liệu

- **Khử nhiễu:** Bộ lọc Median  
- **Chuyển đổi không gian màu:** RGB → Grayscale, Lab, HSV  
- **Phân đoạn ảnh:** K-means + Ngưỡng Otsu  
- **Trích xuất đặc trưng:**  
  - **Đặc trưng màu:** HSV, Lab  
  - **Đặc trưng cạnh:** Sobel, Prewitt, Scharr

---

## 4. 🤖 Mô hình học máy & đánh giá

- **Mô hình sử dụng:**  
  - Random Forest  
  - Support Vector Machine (SVM)  
- **Đánh giá bằng các chỉ số:** Accuracy, Precision, Recall, F1-score  
- **Kỹ thuật cải thiện dữ liệu:** Oversampling để xử lý mất cân bằng lớp

---

## 5. 🎯 Kết quả

Đồ án đã hoàn thiện bộ dữ liệu ảnh hoa được tiền xử lý và đánh giá với các mô hình học máy cơ bản.  

## 📚 Tài liệu tham khảo

1. Patel & Isha (2019) – *Flower Classification with ML & CV*  
2. Zawbaa et al. (2014) – *Automatic Flower Classification*  
3. Bộ dữ liệu Oxford 102 Category Flowers  
4. Sunil Bangare et al. – *Otsu Thresholding*

---

📅 *Thời gian hoàn thành: 06/2024*  
📝 *Dự án phục vụ mục đích học thuật.*
