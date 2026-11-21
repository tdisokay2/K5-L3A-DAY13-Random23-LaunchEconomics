# Báo cáo cá nhân — TranXuanTruong-2A202603617

## 1. Thông tin thành viên

- Họ tên: Trần Xuân Trường
- MSSV: 2A202603617
- Email: 2A202603617@student.vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ (TV4)
- Nhánh làm việc: `truong`

## 2. Phần việc phụ trách

- **Giai đoạn Chuẩn bị:** Điền thông tin nhóm và thành viên vào `TEAM.md`, tạo cấu trúc và khung mẫu 7 mục cho hồ sơ Launch v0.
- **Nhiệm vụ A & B (CP1, CP2):** Tiếp nhận kết quả đối chiếu số liệu từ TV1 và TV2; cập nhật các con số CPS (4.472 đ [simulated]), chi phí toàn hệ thống (0,49× baseline), top 3 yếu tố nhạy nhất và rủi ro kinh tế vào `ho_so_launch_v0.md`.
- **Nhiệm vụ C (CP3):** Gắn nhãn độc lập 20 ca lỗi theo Google PAIR (Bộ nhãn 2), đối chiếu với TV3 (Nguyễn Triều Dương) đạt đồng thuận 100% (20/20 ca); cập nhật Mục 5 vào hồ sơ launch.
- **Nhiệm vụ D (CP4):** Rà soát các thông số kế hoạch pilot phân cụm (20 can thiệp vs 20 đối chứng, MDE = 0,06, n = 859, m ≥ 299); kiểm tra 4 luật dừng theo chuẩn NẾU–TRONG–THÌ–KHÔNG THÌ và cơ chế rollback 30 phút.
- **Nhiệm vụ E (CP5):** Chủ trì xây dựng file `report/team/chi_so.md` (3 metric trace, 2 metric tự đề xuất, 11 telemetry events có `trace_id`); chốt hoàn thiện trang hồ sơ `ho_so_launch_v0.md` với đề xuất Go có điều kiện.
- **Tổng kết & Nộp bài:** Soạn thảo báo cáo nhóm `report/team/group_report.md` và rà soát checklist toàn bộ file trước khi nộp.

## 3. Đóng góp cụ thể

- Trực tiếp xây dựng và hoàn thiện bộ Hồ sơ Launch v0 đúng 1 trang A4, bảo đảm tuân thủ nghiêm ngặt mọi quy tắc của Gate 2a (gắn nhãn `simulated`, quy định vai trò chịu trách nhiệm cụ thể, không sử dụng từ cấm "production").
- Thiết lập đặc tả danh mục 11 Telemetry Events trong `chi_so.md` có đầy đủ thuộc tính `trace_id` để kiểm tra chéo liên kết với 5 ca khắc phục lỗi trong `bang_loi.md`.
- Soạn thảo 4 điều kiện ràng buộc có tính thực thi cao kèm deadline cụ thể cho đề xuất "Go có điều kiện" để bảo vệ trước hội đồng phản biện.
- Thực hiện gắn nhãn độc lập 20 ca lỗi trong 8 phút, đạt tỉ lệ đồng thuận tuyệt đối 20/20 với TV3.

## 4. Bằng chứng

- **Files phụ trách chính:**
  - `report/team/ho_so_launch_v0.md`
  - `report/team/chi_so.md`
  - `report/team/group_report.md`
  - `TEAM.md`
- **Bộ nhãn lỗi cá nhân (Bộ 2):** Đã đối chiếu và ghi nhận trong `report/team/bang_loi.md`.
- **Các commit trên Git:** Thực hiện trên nhánh `truong` và tạo Pull Request merge vào `main`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini CLI.
- **Mục đích sử dụng:** Hỗ trợ tính toán nhanh các công thức thống kê (cỡ mẫu phân cụm NormalDist, kiểm tra độ nhạy), gợi ý định dạng telemetry event chuẩn và rà soát các tiêu chí Rubric tránh bị trừ điểm.
- **Cách tự kiểm tra kết quả:** Tự đối chiếu lại mọi con số với slide đáp án của giảng viên (sai số 0,00%), chạy kiểm tra code thực tế trên terminal `python lab13.py`, và kiểm tra cú pháp file YAML bằng `yaml.safe_load`.

## 6. Tự đánh giá

- **Mức độ hoàn thành công việc:** 100% (hoàn thành đúng và trước thời hạn tất cả các checkpoint từ CP0 đến CP5).
- **Điểm tự đánh giá:** 10/10.
