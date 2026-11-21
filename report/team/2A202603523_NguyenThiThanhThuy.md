# Báo cáo cá nhân — Nguyễn Thị Thanh Thúy (2A202603523)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Thanh Thúy
- MSSV: 2A202603523
- Email: thanhthuy02072004@gmail.com
- Vai trong nhóm: Người viết code — phụ trách mô hình chi phí A1–A4, độ nhạy B1–B4 và tính cỡ mẫu D1.

## 2. Phần việc phụ trách

Phụ trách phần lập trình mô hình chi phí A1–A4; triển khai phân tích độ nhạy B1–B4; tính cỡ mẫu D1 và hoàn thiện nội dung thiết kế pilot D2 trong `report/team/pilot_plan.yaml`. Cập nhật các báo cáo chi phí, rủi ro kinh tế và tóm tắt kết quả tại `bang_chi_phi.md`, `chi_so.md`, `ho_so_launch_v0.md` và `group_report.md`.

## 3. Đóng góp cụ thể

Triển khai mô hình từ toàn bộ trace, gồm cả lần chạy lỗi; cộng chi phí nhân viên từ các cột `*_simulated` và chia cho số yêu cầu thành công. Tách kết quả theo bốn loại yêu cầu, chọn phạm vi pilot `noi_dia` + `hang_nang`, rồi đánh giá chi phí cố định. CP2 gồm 9 kịch bản B1, kịch bản ghép B2, tổng chi phí toàn hệ thống ở B3 và hai giả định thời gian xem lại 100% ở B4. CP4 tính các phương án D1, đánh giá power nếu hiệu quả thật chỉ tăng 5 điểm, rồi ghi rõ đánh đổi MDE 6 điểm và cách phân nhóm nhân viên.

## 4. Bằng chứng

Đường dẫn: `src/lab13.py`; `report/team/bang_chi_phi.md`; `report/team/pilot_plan.yaml`; `report/team/chi_so.md`; `report/team/ho_so_launch_v0.md`; `report/team/group_report.md`. Commit trên nhánh `thanhthuy`: `7d259a4` (mô hình A1–A4), `83d5b61` (Checkpoint 1), `72a51a5` (Checkpoint 2); CP4 đã hoàn tất trong working tree, chưa commit. Kết quả: A2 4.472 đ/việc; A4 4.599 đ/việc ở 45.000 yêu cầu/tháng; B2 xếp hạng làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%); B3 chọn giới hạn 2 lần theo tổng chi phí hệ thống (6.901.220 đ); B4 11.743–12.415 đ/việc tùy giả định làm lại. D1: 1.251/nhánh cho MDE 5 điểm; phương án 20/20 chấp nhận MDE 6 điểm với 859 mẫu hiệu dụng/nhánh và 299 yêu cầu/người (DE=6,96); nếu hiệu quả thật là 5 điểm thì power khoảng 0,64. Kế hoạch D2 phân nhóm ngẫu nhiên theo nhân viên, phân tầng theo depot. Các ước tính dùng thời gian nhân viên giả lập được gắn nhãn `simulated`.

## 5. Công cụ AI đã dùng

Đã dùng Codex để đọc yêu cầu, hỗ trợ triển khai code và biên tập báo cáo. Tôi tự kiểm tra bằng cách chạy `python lab13.py` trên CSV, xác nhận ba phép thử A1 đạt và đối chiếu đầu ra B1–B4, D1 với số hướng dẫn. Tôi cũng nạp `pilot_plan.yaml` bằng `yaml.safe_load`, kiểm tra đủ ba luật dừng và rà không còn dấu hỏi trong phần cấu hình.

## 6. Tự đánh giá

Hoàn thành phần code A/B, tính D1 trước khi chọn thiết kế, phân biệt cỡ mẫu hiệu dụng với số yêu cầu thô và ghi rõ hạn chế power khi chấp nhận MDE 6 điểm. Phần phân loại lỗi C và các chỉ số E vẫn cần thành viên được phân công hoàn thiện trước khi chốt hồ sơ nhóm.
