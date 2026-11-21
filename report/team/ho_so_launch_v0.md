# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Random23 · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (gấp 16,3 lần hoá đơn token+tool 275 đ; chi phí nhân viên chiếm 92,5% tổng chi phí) | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương (+23,1%); Giá token chỉ tác động +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Toàn hệ thống: 5.865 đ/yêu cầu = 0,49× baseline (12.000 đ); Trong phạm vi noi_dia (0,22×) và hang_nang (0,69×) cộng chi phí cố định là 4.599 đ = 0,38× [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (994/1.200); Dùng: 27,12% bỏ qua gợi ý (48/177); An toàn: 4,25% mở lại trong 7 ngày (51/1.200) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20/20 ca lỗi đạt 100% đồng thuận giữa TV3 và TV4 theo 5 loại Google PAIR (4 User, 5 System, 4 Context, 4 Limitation, 3 Silent); 5 ca khắc phục mẫu (ca 9, 7, 18, 4, 17) có telemetry event đo được và vai trò phụ trách cụ thể | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên (20 đối chứng vs 20 can thiệp), MDE = 0,06 (power 0,80, n = 859/nhóm, m ≥ 299); 4 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Duy trì xem lại 100% làm CPS đội lên 11.743 đ – 12.415 đ (0,98× – 1,03× baseline) triệt tiêu hiệu quả kinh tế; Làm lại tăng gấp đôi đẩy CPS lên 6.787 đ (+51,8%) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho kế hoạch thử nghiệm pilot trong phạm vi hẹp (`noi_dia` và `hang_nang`, loại bỏ `quoc_te` và `doi_tac`), với 4 điều kiện ràng buộc:

- **Điều kiện 1:** Kỹ sư trưởng agent triển khai hoàn tất bản vá xử lý khóa chống trùng (idempotency key) và đối soát sổ cái hai chiều (ca 7, ca 20) trước ngày 2026-12-15.
- **Điều kiện 2:** Giám đốc vận hành LogiX-VN ký văn bản chính thức chấp thuận đánh đổi nâng mức chênh phát hiện tối thiểu (MDE) lên 6 điểm phần trăm (với power đạt 0,64 nếu chênh lệch thực tế là 5 điểm) trước ngày 2026-12-20.
- **Điều kiện 3:** Kỹ sư trưởng agent kích hoạt đầy đủ 10 telemetry events chuẩn có gắn `trace_id`; Trưởng nhóm CSKH thay thế toàn bộ số phút giả lập bằng thời gian đo thực tế trên giao diện ngay sau tuần rollout đầu tiên (bước 0.10) trước ngày 2026-12-28.
- **Điều kiện 4:** PM trợ lý hoàn phí và Trưởng nhóm CSKH ban hành quy trình giảm tỉ lệ xem lại theo bậc (xuống 20% rồi 5%) khi tỉ lệ sửa/bỏ < 15%, tránh rủi ro duy trì xem lại 100% làm chi phí cao hơn nhân viên tự làm, trước ngày 2027-01-02.
