# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu của nhóm can thiệp được nhân viên mở bằng trợ lý | Số yêu cầu nhân viên nhóm can thiệp có mở giao diện trợ lý chia cho tổng số yêu cầu được phân công | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu ngẫu nhiên hằng tuần | Số yêu cầu phát hiện lệch tiền giữa số đã hoàn và số đúng qua kiểm tra mẫu chia cho tổng số mẫu kiểm tra | Không cần tính |

> **Lưu ý:** Chỉ số trong đợt chạy thử là 82,83%; không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử chưa có nhóm đối chứng đồng thời.

## Danh sách event

Hệ thống ghi nhận 11 event telemetry chuẩn, mỗi event bắt buộc có `trace_id` để nối liền với trace của agent:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id, loai, so_tien, arm, trace_id` | Khi khách bấm gửi yêu cầu hoàn phí |
| `input_validation_failed` | App / Gateway | `field, error_type, reason, trace_id` | Khi khách nhập sai mã/thông tin (bắt lỗi Ca 9) |
| `agent_run_completed` | Agent | `attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần agent chạy (kể cả khi gặp lỗi) |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id, so_tien_de_xuat, trace_id` | Khi đề xuất hoàn tiền của agent hiện lên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id` | Khi nhân viên bấm duyệt, sửa hoặc bỏ qua gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai, ly_do, trace_id` | Khi nhân viên hoàn thành xử lý lại ca bị lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien, ket_qua, trace_id` | Khi lệnh chuyển tiền/ghi nhận hoàn tiền vào sổ cái (đối soát Ca 7, Ca 20) |
| `handoff_to_staff` | Agent | `reason, tom_tat, trace_id` | Khi agent thất bại sau số lần chạy tối đa hoặc thiếu dữ liệu (Ca 4, Ca 13) |
| `ticket_closed` | Hệ thống ticket | `closed_at, duration_hours, trace_id` | Khi ticket hoàn phí được đóng hoàn tất |
| `ticket_reopened` | Khách hàng | `reopened_at, reason, trace_id` | Khi khách hàng mở lại ticket trong vòng 7 ngày (theo dõi Ca 10, Ca 18) |
| `audit_sample_checked` | Kế toán nội bộ | `so_tien_da_hoan, so_tien_dung, is_match, trace_id` | Khi kiểm toán viên kiểm tra mẫu ngẫu nhiên hằng tuần (bắt lỗi ngầm Ca 5, Ca 17) |

**Kiểm tra chéo với bảng khắc phục lỗi (CP3):**
- **Ca 9 (Do người dùng):** Đo bằng tỉ lệ phát sinh event `input_validation_failed` có `reason = invalid_tracking_code` > 2% tổng số yêu cầu trong ngày.
- **Ca 7 & Ca 20 (Hệ thống):** Đối soát giữa event `agent_suggestion_shown` (báo thành công) và `refund_ledger_write` (ghi sổ thành công với `idempotency_key`), ngưỡng cảnh báo là có $\ge 1$ ca lệch.
- **Ca 18 (Ngữ cảnh):** Bắt qua thuộc tính `reason = thac_mac_so_tien` trong event `ticket_reopened`.
- **Ca 4 & Ca 13 (Giới hạn):** Bắt qua event `handoff_to_staff` với `reason = thieu_du_lieu` hoặc `reason = ngoai_pham_vi`.
- **Ca 5 & Ca 17 (Ngầm):** Bắt qua event `audit_sample_checked` có `is_match = False` qua kiểm tra mẫu ngẫu nhiên 100 đơn/tuần.

**Kiểm tra chéo:**
- **Chỉ số chính:** Tính từ thời gian đóng trong `ticket_closed` (hiệu giữa `closed_at` và `created_at` $\le 24$ giờ) và không tồn tại event `ticket_reopened` có cùng `trace_id` trong vòng 7 ngày.
- **Chỉ số dùng:** Đếm số event `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo` chia cho tổng số event `staff_review_decision`.
- **Chỉ số an toàn:** Đếm số event `ticket_reopened` phát sinh trong vòng 7 ngày chia cho tổng số event `refund_request_created`.
- **Chỉ số dùng tự đề xuất:** Đếm số event `agent_suggestion_shown` chia cho số event `refund_request_created` được gán cho nhóm can thiệp (`arm == 'treatment'`).
- **Chỉ số an toàn tự đề xuất:** Đếm số event `audit_sample_checked` có `is_match == False` chia cho tổng số event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Các rủi ro lớn nhất trích xuất trực tiếp từ mô hình phân tích độ nhạy:

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng +51,8%, lên mức 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần vượt quá 7% (đợt chạy thử là 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp phạm vi chỉ còn noi_dia, tạm dừng hang_nang và rà soát ngay 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài | Chi phí tăng vọt lên 11.743 đ (0,98× baseline), hoặc 12.414 đ (1,03× baseline nếu tính 15,3 phút/ca) [simulated] — triệt tiêu hiệu quả tiết kiệm | Tỉ lệ yêu cầu cần xem lại vẫn còn > 50% ở cuối giai đoạn rollout 0.25 | Thực hiện giảm xem lại theo bậc (giảm dần về 20% rồi 5%) nếu tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng bị chia nhỏ: đội thêm +1.185 đ/việc ở mức 45.000 yc/tháng, và đội thêm +2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Số lượng yêu cầu thành công mỗi tuần đạt dưới 50% kế hoạch dự kiến | Giữ nguyên quy mô pilot không mở rộng, đàm phán lại chi phí hạ tầng máy chủ cố định | PM trợ lý hoàn phí |
