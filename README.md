# Ứng dụng Note-Taking

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Giới thiệu

**Note-Taking** là một ứng dụng ghi chú đơn giản, hiệu quả được phát triển bằng Python. Ứng dụng cho phép người dùng tạo, quản lý và tổ chức ghi chú một cách dễ dàng, hỗ trợ nhiều tính năng hữu ích cho công việc và học tập hàng ngày.

## Tính năng chính

### 1. Quản lý ghi chú
- **Tạo ghi chú mới**: Dễ dàng tạo ghi chú mới với tiêu đề và nội dung
- **Chỉnh sửa ghi chú**: Cập nhật nội dung ghi chú đã tạo
- **Xóa ghi chú**: Loại bỏ các ghi chú không cần thiết
- **Xem danh sách ghi chú**: Hiển thị tất cả ghi chú trong hệ thống

### 2. Tổ chức và phân loại
- **Gắn thẻ (tag)**: Phân loại ghi chú bằng các thẻ tùy chỉnh
- **Sắp xếp ghi chú**: Sắp xếp theo ngày tạo, tiêu đề hoặc thẻ
- **Tạo danh mục**: Nhóm các ghi chú theo danh mục

### 3. Tìm kiếm và lọc
- **Tìm kiếm nhanh**: Tìm ghi chú theo từ khóa
- **Bộ lọc nâng cao**: Lọc ghi chú theo thẻ, danh mục hoặc ngày tạo

### 4. Lưu trữ và bảo mật
- **Lưu trữ tự động**: Tự động lưu ghi chú khi có thay đổi
- **Sao lưu dữ liệu**: Tùy chọn sao lưu và khôi phục dữ liệu ghi chú
- **Bảo vệ ghi chú**: Tùy chọn đặt mật khẩu cho ghi chú quan trọng

## Cài đặt

### Yêu cầu hệ thống
- Python 3.8 trở lên
- Các thư viện phụ thuộc (được liệt kê trong `requirements.txt`)

### Bước cài đặt

1. Clone repository về máy:
```bash
git clone https://github.com/TienPMT/Note-Taking.git
cd Note-Taking
```

2. Tạo và kích hoạt môi trường ảo (khuyến nghị):
```bash
python -m venv venv
# Trên Windows
venv\Scripts\activate
# Trên macOS/Linux
source venv/bin/activate
```

3. Cài đặt các thư viện phụ thuộc:
```bash
pip install -r requirements.txt
```

4. Chạy ứng dụng:
```bash
python main.py
```

## Hướng dẫn sử dụng

### Khởi động ứng dụng
Sau khi cài đặt, khởi động ứng dụng bằng lệnh:
```bash
python main.py
```

### Tạo ghi chú mới
1. Chọn tùy chọn "Tạo ghi chú mới"
2. Nhập tiêu đề cho ghi chú
3. Nhập nội dung ghi chú
4. Tùy chọn gắn thẻ hoặc chọn danh mục
5. Lưu ghi chú

### Quản lý ghi chú
- Để xem danh sách ghi chú: Chọn "Xem tất cả ghi chú"
- Để chỉnh sửa: Chọn ghi chú và nhấp vào "Chỉnh sửa"
- Để xóa: Chọn ghi chú và nhấp vào "Xóa"
- Để tìm kiếm: Nhập từ khóa vào ô tìm kiếm

### Tổ chức ghi chú
- Tạo thẻ mới: Vào phần "Quản lý thẻ" và chọn "Tạo thẻ mới"
- Tạo danh mục: Vào phần "Quản lý danh mục" và chọn "Tạo danh mục mới"
- Gắn thẻ cho ghi chú: Mở ghi chú và chọn "Thêm thẻ"

## Cấu trúc dự án

```
Note-Taking/
│
├── main.py                  # File chạy chính của ứng dụng
├── requirements.txt         # Các thư viện phụ thuộc
├── README.md                # Tài liệu hướng dẫn
│
├── src/                     # Mã nguồn chính
│   ├── __init__.py
│   ├── models/              # Các lớp dữ liệu
│   │   ├── __init__.py
│   │   ├── note.py          # Lớp Note
│   │   ├── tag.py           # Lớp Tag
│   │   └── category.py      # Lớp Category
│   │
│   ├── services/            # Logic xử lý
│   │   ├── __init__.py
│   │   ├── note_service.py  # Dịch vụ quản lý ghi chú
│   │   ├── storage.py       # Dịch vụ lưu trữ
│   │   └── search.py        # Dịch vụ tìm kiếm
│   │
│   └── ui/                  # Giao diện người dùng
│       ├── __init__.py
│       ├── main_window.py   # Cửa sổ chính
│       └── dialogs.py       # Hộp thoại
│
└── tests/                   # Kiểm thử
    ├── __init__.py
    ├── test_note.py
    └── test_storage.py
```

## Công nghệ sử dụng

- **Python**: Ngôn ngữ lập trình chính
- **SQLite**: Cơ sở dữ liệu nhẹ để lưu trữ ghi chú
- **Tkinter/PyQt** (tùy phiên bản): Thư viện giao diện người dùng
- **Pytest**: Framework kiểm thử

## Đóng góp

Mọi đóng góp cho dự án đều được hoan nghênh! Nếu bạn muốn đóng góp, vui lòng:

1. Fork dự án
2. Tạo nhánh tính năng (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi của bạn (`git commit -m 'Add some amazing feature'`)
4. Push lên nhánh (`git push origin feature/amazing-feature`)
5. Mở Pull Request

## Liên hệ và hỗ trợ

Nếu bạn có bất kỳ câu hỏi hoặc gặp vấn đề với ứng dụng, vui lòng tạo issue trên GitHub hoặc liên hệ trực tiếp qua:

- GitHub: [TienPMT](https://github.com/TienPMT)

## Giấy phép

Dự án này được phân phối dưới giấy phép MIT. Xem tệp `LICENSE` để biết thêm thông tin.

---

© 2025 TienPMT. All Rights Reserved.
