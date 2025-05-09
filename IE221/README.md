# 🧑‍🍳 Website Quản Lý Nhà Hàng - Django Project

**📚 Đồ án môn học:** Kỹ thuật lập trình Python

## 👨‍💻 Thành viên nhóm

| STT | Họ tên               | MSSV      | Ngành              |
|-----|----------------------|-----------|--------------------|
| 1   | Dương Anh Vũ         | 22521688  | CNTT Việt - Nhật   |
| 2   | Hồ Nguyễn Thiên Vũ   | 22521689  | Khoa học dữ liệu   |

## 🛠️ Công nghệ sử dụng

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL
- **Khác:** Django ORM, Form Validation, Messages Framework, QR Code

## 🎯 Mục tiêu dự án

Tạo ra một website quản lý nhà hàng chuyên nghiệp, giúp:
- Quản lý thực đơn, bàn, nhân viên, doanh thu và lịch làm việc
- Tối ưu quy trình phục vụ khách hàng
- Cải thiện trải nghiệm khách hàng với tính năng đặt món qua QR Code

## 🗂️ Kiến trúc hệ thống

Dự án sử dụng kiến trúc **MVT (Model - View - Template)**:

- `Model`: Thiết kế qua Django ORM với các ràng buộc (constraint), kiểm tra dữ liệu
- `View`: Xử lý request/response, phân quyền, redirect, validate
- `Template`: Hiển thị dữ liệu người dùng từ view gửi về

## 🧾 Các chức năng chính

| Chức năng                      | Mô tả |
|-------------------------------|-------|
| Đăng nhập / Đăng xuất         | Xác thực người dùng và phân quyền |
| Quản lý menu                  | Thêm, sửa, xóa, tìm kiếm món ăn, đề xuất combo lợi nhuận |
| Quản lý bàn                   | Mở bàn, đặt món, xác nhận lên món, thanh toán |
| Quản lý nhân viên             | Thêm, sửa, xóa, xem lịch làm việc |
| Quản lý doanh thu             | Thống kê hóa đơn, tìm kiếm doanh thu |
| Quản lý khuyến mãi            | Áp dụng mã giảm giá vào đơn hàng |
| Quản lý lịch làm việc         | Check-in/out ca làm, điều phối nhân viên |

Phân quyền người dùng được triển khai theo các vai trò: **admin**, **quản lý**, **phục vụ**, **bếp**.

## 🧩 Cơ sở dữ liệu

Hệ thống sử dụng sơ đồ ERD với các bảng chính:
- `CustomUser`: Thông tin nhân viên
- `Menu`, `Order`, `ChiTietOrder`: Món ăn và đơn hàng
- `Ban`: Thông tin bàn ăn
- `KhuyenMai`: Mã giảm giá
- `LichLamViec`: Ca làm của nhân viên

## 📌 Điểm nổi bật

Chức năng đặt món bằng QR Code là điểm sáng của hệ thống:
- Cho phép khách tự đặt món, xem hóa đơn tạm
- Giảm thời gian chờ phục vụ
- Tránh sai sót trong phục vụ và thanh toán

## 📸 Demo & Hình ảnh

- Màn hình đăng nhập
  ![image](https://github.com/user-attachments/assets/3c2bdbf1-3b82-4d82-8494-07ef009c8a44)

- Màn hình chính khi đăng nhập (admin)
  ![image](https://github.com/user-attachments/assets/e6863e48-5649-4978-826c-7e939024f7d4)


> Demo video: https://youtu.be/h8uHfngvhec

## 📚 Tài liệu tham khảo

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [W3Schools JavaScript](https://www.w3schools.com/js/)
- [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

---

> 📝 *Dự án thực hiện tại Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM*  
> Thời gian hoàn thành: **12/2024**

