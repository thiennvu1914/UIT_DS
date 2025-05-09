# 🇻🇳 ViLegalNLI: Vietnamese Legal Natural Language Inference Dataset

**ViLegalNLI** là tập dữ liệu NLI (Natural Language Inference) đầu tiên được xây dựng dành riêng cho lĩnh vực pháp luật bằng tiếng Việt. Dự án này nhằm phục vụ việc huấn luyện và đánh giá các mô hình học sâu trong bài toán suy diễn ngôn ngữ tự nhiên trên văn bản pháp lý.

## 👨‍🔬 Nhóm thực hiện

| Tên                   | MSSV      | Email                    |
|------------------------|-----------|---------------------------|
| Nguyễn Phi Long        | 22520818  | 22520818@gm.uit.edu.vn    |
| Hồ Nguyễn Thiên Vũ     | 22521689  | 22521689@gm.uit.edu.vn    |
| Dương Thị Hồng Nhung   | 22521056  | 22521056@gm.uit.edu.vn    |

**Đơn vị:** Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM  
**Giảng viên hướng dẫn:** M.A. Huỳnh Văn Tín

## 📚 Giới thiệu

Mặc dù tiếng Việt là ngôn ngữ có hơn 90 triệu người dùng, nhưng vẫn được xem là ngôn ngữ ít tài nguyên trong NLP. Đặc biệt, dữ liệu NLI chuyên biệt cho lĩnh vực pháp lý còn rất khan hiếm. ViLegalNLI được xây dựng để lấp đầy khoảng trống này, với mục tiêu:

- Tạo ra bộ dữ liệu chất lượng cao, đa dạng chủ đề pháp luật
- Phục vụ nghiên cứu và huấn luyện mô hình NLI tiếng Việt
- Thúc đẩy phát triển NLP cho các ngôn ngữ ít tài nguyên

## 🏗️ Chi tiết tập dữ liệu

- **Số lượng mẫu:** 9,667 cặp premise-hypothesis
- **Nguồn:** 3,232 văn bản pháp luật Việt Nam thuộc 23 lĩnh vực
- **Gán nhãn:** 
  - `0` (Entailment – Hỗ trợ)
  - `1` (Neutral – Trung lập)
  - `2` (Contradiction – Phản bác)
- **Phân loại chủ đề:** 26 chủ đề như "tài chính", "giáo dục", "bất động sản", "dân sự", v.v.

## 📄 Tài liệu tham khảo

- SNLI, XNLI, ViNLI, ViHealthNLI, ViFactCheck
- PhoBERT, XLM-R, CafeBERT, mBERT
- [Django Official](https://www.djangoproject.com/)
- [PhoBERT Paper](https://arxiv.org/abs/2003.00744)

**Thời gian hoàn thành:** 05/2024
