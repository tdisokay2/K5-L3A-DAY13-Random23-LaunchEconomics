# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Random23
- Nhóm được chấm: 3Mien

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện phù hợp với chi phí phạm vi chọn 4.599 đ/việc và 5.784 đ khi giảm nửa khối lượng, đều dưới baseline 12.000 đ (simulated). Hồ sơ nêu cả tình huống bất lợi: xem lại 100% lên 12.415 đ và power chỉ 0,64 ở tác động 5 điểm; yêu cầu đo chi phí thật và chưa mở rộng khi thiếu bằng chứng. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Các cụm chi phí và độ nhạy trong bản gửi có nhãn simulated hoặc trạng thái Giả lập. Phạm vi giới hạn ở `noi_dia` và `hang_nang`; loại `quoc_te` 22.515 đ và `doi_tac` 10.215 đ (simulated) vì chi phí/điều khoản. Nhóm đối tác vẫn dưới baseline 12.000 đ, nên cần bằng chứng điều khoản để xác nhận lý do loại. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có phân ngẫu nhiên 20/20 cụm, 299 yêu cầu/người, 5.980/nhóm, DE 6,96 và mẫu hiệu dụng 859,20. Tuy nhiên, bản gửi chỉ nêu có 4 luật dừng, chưa cho thấy ngưỡng, thời hạn xử lý và người có quyền dừng; lưu lượng ≥570/ngày và roster 40 người tại 12 depot cũng đang chờ xác minh. Chưa đủ bằng chứng để đạt mức 10 theo rubric. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất pilot nội địa và hàng nặng có cơ sở kinh tế, nhưng chỉ cho phép bật pilot sau khi nghiệm thu các điều kiện trước khởi động; chưa chấp thuận mở rộng. Điểm 25/30 là đánh giá sơ bộ phần hội đồng C6–C8 theo nội dung hồ sơ launch v0 được cung cấp, cần xác nhận khi duyệt chéo. Chưa có các tệp A2–B4, bảng lỗi, chỉ số, code và YAML của chính nhóm 3Mien để đối chiếu; không dùng tệp của Random23 để xác nhận thay và không quy đổi thành điểm /100.

1. Hồ sơ phân biệt hóa đơn 274,7 đ/yêu cầu với chi phí 4.472 đ/việc thành công; có tình huống giảm khối lượng và xem lại 100%. Cần mở A2–B4 để kiểm tra mẫu số, phút lao động và cách phân bổ cố định; chưa thể xác nhận phép tính chỉ từ bản tóm tắt.
2. Mục tiêu 40 × 299 = 11.960 yêu cầu trong 21 ngày cần khoảng 569,5/ngày. Trước bật pilot, cần log 4 tuần theo từng nhân viên cho đúng hai loại yêu cầu và roster 40 người/12 depot; mẫu CSV 20 người/6 depot chưa chứng minh đủ tải. Nếu kéo dài lên 28 ngày, cập nhật đồng bộ lịch tăng bước, theo dõi và quyết định.
3. Cần trình đủ 4 luật dừng theo NẾU–TRONG–THÌ–KHÔNG THÌ, có ngưỡng đo được, cửa sổ đo, thời hạn phản ứng, người có quyền dừng và xử lý nếu không khắc phục được. Có thể nâng C8 lên 10/10 khi YAML và bằng chứng lưu lượng đáp ứng đầy đủ.
4. Trước bật pilot, cần nghiệm thu khóa chống trùng, chỉ báo “đã hoàn” sau ghi sổ `ok`, event có `trace_id` và tắt trong 30 phút. Cần log hoặc biên bản kiểm tra từng điều kiện, do kỹ sư trưởng agent xác nhận trước mốc dự kiến 29/11/2026.
5. Power 0,80 ở MDE 6 điểm không bảo đảm cận dưới khoảng tin cậy 95% đạt +5 điểm. Trước pilot, ghi rõ phương pháp ước lượng có xét cụm và định nghĩa theo dõi 7 ngày cho ca đóng trễ; nếu chưa đạt thì tiếp tục nghiên cứu.
6. Các vai “Người viết code”, “Người kiểm số” cần ánh xạ sang người có quyền nghiệm thu/vận hành. Giữ nhãn simulated ngay cạnh 22.515 đ và 10.215 đ để tránh mất ngữ cảnh khi trích riêng.

**Một câu hỏi cho đội trình:** Hãy trình log 4 tuần chứng minh đủ ≥570 yêu cầu đủ điều kiện/ngày cho 40 nhân viên, cùng YAML ghi đủ ngưỡng, thời hạn và người có quyền dừng của cả 4 luật. Nếu không đủ tải để đạt 299 yêu cầu/người trong 21 ngày, ai phê duyệt lịch mới và mốc quyết định thay đổi thế nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** Dự thảo: Chưa có log thật 4 tuần chứng minh đủ ≥570 yêu cầu/ngày; phải xác minh đủ 299 yêu cầu/người trước khi bật. YAML quy định: hoàn trùng/báo hoàn sai → Giám đốc vận hành tắt trong 30 phút; mở lại >6% hoặc cao hơn đối chứng ≥2 điểm trong 3 lần kiểm tra ngày liên tiếp (ca đủ theo dõi, ≥100 ca/nhóm) → tắt trong 30 phút; chi phí >8.000 đ/việc trong 2 tuần liên tiếp → PM dừng mở rộng, đề xuất thu hẹp trong 1 ngày; sửa/bỏ >40% trong tuần → Trưởng nhóm CSKH rà soát trong 3 ngày. Nếu thiếu tải, Giám đốc vận hành duyệt kéo giai đoạn chính lên 28 ngày trước khi bật; mốc quyết định dự kiến chuyển sang 02/02/2027. Thiếu mẫu hoặc theo dõi thì chưa mở rộng.
