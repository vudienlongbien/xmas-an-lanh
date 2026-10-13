# 🎄 Giáng Sinh An Lành CLI (`xmas-an-lanh`)

> **Một công cụ đếm ngược & thông báo Giáng Sinh siêu nhẹ, dành riêng cho dân nghiện Linux Terminal & Termux trên Android.**

---

## 🌟 Tính năng nổi bật

- ⏳ **Đếm ngược thông minh:** Tự động tính chính xác số ngày còn lại đến Giáng Sinh (25/12).
- 🎨 **Nghệ thuật ASCII:** Render dòng chữ `MERRY XMAS` siêu ngầu bằng `figlet` khi đúng thời khắc.
- 🔔 **Thông báo hệ thống:** Tận dụng IPC Kernel Android bắn `termux-notification` trực tiếp lên Status bar *kèm rung bần bật* .
- 🚀 **Tự động hóa 100%:** Nhét vào `.zshrc` / `.bashrc` để tự động kiểm tra mỗi khi mở Terminal.

---

## 🛠️ Hướng dẫn cài đặt môi trường (Termux)

### Bước 1: Cài đặt các gói phụ thuộc (Dependencies)
- Mở Termux lên và phăng mớ lệnh sau:

+ ``bash
+ ``pkg update && pkg upgrade -y
+ `pkg install python git figlet termux-api -y


### Bước 2: Tải dự án về máy
+ `bash
+ ``git clone https://github.com/TENTAIKHOAN/giang-sinh-an-lanh.git
+ ``cd giang-sinh-an-lanh

### Bước 3: Cấu hình tự động chạy (`.zshrc`)
- Thêm dòng sau vào cuối file `~/.zshrc` hoặc `~/.bashrc`:

+ `bash
+ `python ~/giang-sinh-an-lanh/idk.py
---
## 👨‍💻 Cách hoạt động (Under the hood)

- Script `idk.py` sử dụng thư viện `subprocess` để giao tiếp trực tiếp với hệ thống Android:
 + 1. Đọc thời gian thực qua module `datetime`.
+ . So sánh khoảng thời gian trọn vẹn của ngày 25/12.
+ . Thực thi tiến trình con `figlet` và gọi dịch vụ API của Termux để render notification.

---

## 📜 License
Distributed under the MIT License.
