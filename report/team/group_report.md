# Báo cáo nhóm · Lab 13: Launch & Economics

Báo cáo ngắn gọn tổng hợp quá trình định giá agent và xây dựng kế hoạch thử nghiệm pilot (Gate 2a) cho Trợ lý hoàn phí LogiX-VN.

## 1. Thông tin nhóm

- Tên nhóm: Nhóm 23 (Random23)
- Lớp: L3A (AI20K K5)
- Thành viên và phân vai chi tiết: Xem tại [`TEAM.md`](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Trả lời 4 câu hỏi sống còn cho Gate 2a: (1) Chi phí thật cho mỗi việc thành công (CPS); (2) Nhân viên có sẵn sàng sử dụng; (3) Phân loại và khắc phục lỗi khi có sự cố; (4) Thiết kế thử nghiệm pilot có đối chứng và đủ bằng chứng thống kê.
- **Cách tiếp cận:**
  - Áp dụng khung kinh tế học **Cost-of-Pass** để tính toán toàn bộ chi phí phát sinh từ trace thực tế (token, tool) kết hợp chi phí can thiệp của con người (xem lại, làm lại).
  - Phân loại lỗi theo hướng dẫn **Google PAIR** (5 loại lỗi) với cơ chế phòng ngừa đo được bằng telemetry.
  - Thiết kế thử nghiệm ngẫu nhiên phân cụm (**Cluster RCT**) có nhóm đối chứng đồng thời, xác định trần hiệu dụng cụm và chấp nhận đánh đổi thống kê rõ ràng.

## 3. Giải pháp từng nhiệm vụ

- **Nhiệm vụ A (Mô hình chi phí):** Xây dựng hàm `mo_hinh()` trong [`src/lab13.py`](../../src/lab13.py), tính toán CPS từ 1.624 lần chạy và 1.200 yêu cầu. Xác định loại trừ `quoc_te` (1,88× baseline) và `doi_tac` (0,85×) ra khỏi phạm vi pilot; chỉ giữ lại `noi_dia` (0,22×) và `hang_nang` (0,69×) ([`bang_chi_phi.md`](bang_chi_phi.md)).
- **Nhiệm vụ B (Bảng độ nhạy):** Khảo sát 9 kịch bản biến thiên. Phát hiện chi phí nhạy cảm nhất với thời gian của nhân viên (Làm lại: +51,8%, Xem lại: +40,7%), trong khi giá token chỉ ảnh hưởng rất nhỏ (+5,6%).
- **Nhiệm vụ C (Bảng lỗi & Khắc phục):** Hai người gắn nhãn độc lập 20 ca lỗi theo Google PAIR đạt đồng thuận 100%. Chọn 5 ca đại diện xây dựng giải pháp chặn lỗi có telemetry event và vai trò phụ trách ([`bang_loi.md`](bang_loi.md)).
- **Nhiệm vụ D (Kế hoạch pilot):** Thiết kế kế hoạch thử nghiệm phân cụm theo 20 nhân viên đối chứng vs 20 nhân viên can thiệp, chấp nhận MDE = 6 điểm phần trăm ($m \ge 299$, $n = 859/\text{nhóm}$, $DE = 6,96$). Xây dựng 3 luật dừng nghiêm ngặt theo mẫu NẾU–TRONG–THÌ–KHÔNG THÌ ([`pilot_plan.yaml`](pilot_plan.yaml)).
- **Nhiệm vụ E (Chỉ số & Hồ sơ Launch v0):** Đặc tả 10 telemetry events có `trace_id`, thiết lập 3 rủi ro kinh tế lớn ([`chi_so.md`](chi_so.md)), và đúc kết hồ sơ Launch v0 1 trang với đề xuất **Go có điều kiện** ([`ho_so_launch_v0.md`](ho_so_launch_v0.md)).

## 4. Kết quả

- **Chi phí mỗi việc thành công (CPS):** Đạt **4.472 đ** [simulated] (gấp 16,3 lần hoá đơn token+tool là 275 đ/yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí).
- **So với tự làm (12.000 đ):** CPS toàn hệ thống là **5.865 đ/yêu cầu = 0,49× baseline** [simulated]. Trong phạm vi `noi_dia` + `hang_nang` cộng chi phí cố định (40 tr/tháng) là **4.599 đ = 0,38× baseline** [simulated].
- **Chỉ số đo thử trên trace:** Tỉ lệ hoàn thành trong 24h & không mở lại 7 ngày đạt **82,83%**; tỉ lệ bỏ qua gợi ý là **27,12%**; tỉ lệ mở lại trong 7 ngày là **4,25%**.
- **Đề xuất cuối cùng:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang`, kèm 4 điều kiện tiên quyết (vá lỗi khóa chống trùng/sổ cái, phê duyệt MDE 6 điểm, bật đủ telemetry event đo thời gian thực, và ban hành lộ trình giảm xem lại theo bậc).

## 5. Khó khăn và cách xử lý

1. **Nguy cơ xem lại 100% làm đội chi phí:** Phân tích độ nhạy B4 chỉ ra nếu duy trì xem lại 100% thì chi phí lên tới 11.743 đ – 12.414 đ (0,98× – 1,03×), gần như không tiết kiệm. *Cách xử lý:* Đưa vào điều kiện ràng buộc trong hồ sơ Gate 2a yêu cầu giảm xem lại theo bậc xuống 20% và 5% khi tỉ lệ sửa/bỏ < 15%.
2. **Thiếu cỡ mẫu khi phân cụm theo nhân viên:** Với 40 nhân viên (20 cụm/nhóm), cỡ mẫu hiệu dụng tối đa chỉ đạt 1.000, không đủ cho MDE 5 điểm ($n=1.251$). *Cách xử lý:* Nâng MDE lên 6 điểm ($n=859$, yêu cầu $m \ge 299$ đơn/người) và công khai đánh đổi (power giảm còn 0,64 nếu chênh lệch thực tế là 5 điểm).

## 6. Tổng hợp đóng góp

Nhóm làm việc song song theo 4 nhánh git:
- **TV1 (nhánh `code`):** Triển khai code A1–A4 trong `lab13.py`, ba phép thử đạt 100%.
- **TV2 (nhánh `economics`):** Tính toán đối chiếu, chạy độ nhạy B1–B4, hoàn thiện `bang_chi_phi.md`.
- **TV3 (nhánh `pilot-errors`):** Chủ trì gắn nhãn bộ 1, tổng hợp `bang_loi.md`, hoàn thiện `pilot_plan.yaml` và `phieu_cham.md`.
- **TV4 (nhánh `reports`):** Gắn nhãn bộ 2; chủ trì `chi_so.md`, chốt `ho_so_launch_v0.md`, tổng hợp `group_report.md` và `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu thời gian xem lại và làm lại hiện tại vẫn là dữ liệu mô phỏng (`_simulated`). Cần thay thế bằng số liệu bấm giờ thực tế từ telemetry sau tuần chạy đầu tiên (rollout 0.10).
- Chưa có mô hình machine learning để phân loại tự động độ tin cậy của đề xuất nhằm tự động hóa việc bỏ qua bước xem lại đối với các ca có xác suất đúng cao.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*.
- Hướng dẫn thực hành Lab 13 - Gate 2a Launch Economics (AI20K K5).
