# **WAKAME TOOL SEO V2**
## **Tính năng mới trên V2**
- **SEO với từ khóa thương mại (nếu từ khóa đó lọt top 20)**
- **Fix lỗi mất kết nối Internet khi thay đổi địa chỉ MAC và địa chỉ IP.**
- **Thêm các thông báo việc thực hiện thao tác nào đó thất bại.**
- **Quy định các trường hợp khiến SEO thất bại.**
- **Đã có thể tùy chỉnh tốc độ đọc cho hàm SEO.read().**
- **Thêm hàm SEO.toContent(). Là hàm lựa chọn bài báo khi vô trang Tin tức.**
- **Gỡ bỏ hàm SEO.back()**

**Tính năng mới có thể thử nghiệm trực tiếp trên file Test_Dev_SEO.ipynb**
## **Môi trường chạy**
Chạy trên hệ điều hành Windows có cài đặt Anaconda hoặc Python3.7.
Cần chương trình Google Chrome v90.0.4 để thực hiện SEO
## **Hướng dẫn cài đặt**
Lệnh cài đặt các gói cần thiết cho việc SEO
```bash
pip install selenium, wmi, netifaces 
```

## **Hướng dẫn chạy tool SEO**
1. Chạy Jupyter Notebook hoặc Visual Studio Code dưới quyền Adminitrastor
2. Disable tất cả các card mạng không phải là mạng Wifi
3. (Option) Dựa vào các hàm dưới đây sắp xếp để thực hiện thao tác SEO trên trang

| Hàm thuộc SEO | Chức năng | Phạm vi thực hiện | Tỷ lệ SEO Fail |
| :---: | :---: | :---: | :---: |
| search(keywords) | Tìm kiếm từ khóa | Trang tìm kiếm | Thấp |
| toPage() | Từ trang tìm kiếm đi tới Web | Trang tìm kiếm | Trung bình|
| Home() | Tới trang chủ | Trang Web CLB | Không có |
| Courses() | Tới trang Khóa học | Trang Web CLB | Không có |
| About() | Tới Về chúng tôi | Trang Web CLB | Không có |
| News() | Tới trang Tin tức | Trang Web CLB | Không có |
| search_box(keyword) | Search bài viết | Trang Tin tức | Thấp |
| toContent(MAX)| Click ngẫu nhiên 1 bài viết | Trang Tin tức | Thấp |
| delay(time) | Delay trang | Toàn bộ | Không có |
| sc_down() | Cuộn trang xuống | Toàn bộ | Không có |
| sc_up() | Cuộn trang lên | Toàn bộ | Không có |
| read(speed) | Cuộn trang xuống tốc độ chậm | Toàn bộ | Không có |


 