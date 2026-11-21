# Team

## Thông tin nhóm

- Tên nhóm: Random23
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Random23-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: `main` (tổng hợp qua PR từ 4 nhánh cá nhân: `thanhthuy`, `manh`, `duongnguyen`, `truong`)

## Thành viên và Phân vai

| STT | Họ tên | MSSV | Email | GitHub | Vai trò chính | Nhánh Git |
| --: | ------ | ---- | ----- | ------ | ------------- | --------- |
|   1 | Nguyễn Thị Thanh Thúy | 2A202603523 | thanhthuy02072004@gmail.com | Ththuy | Người viết code (CP1 A1–A4; kiểm tra code sau giải lao) | `thanhthuy` |
|   2 | Hồ Đức Mạnh | 2A202603609 | hoducmanh822005@gmail.com | hoducmanhtemperature | Người kiểm số (Tính tay đối chiếu; B1–B4; tiếp quản code D1) | `manh` |
|   3 | Nguyễn Triều Dương | 2A202603524 | victorytop54321@gmail.com |  tdisokay2 | Người gắn nhãn 1 (Chủ trì CP3 `bang_loi.md`, CP4 `pilot_plan.yaml`, `phieu_cham.md`) | `duongnguyen` |
|   4 | Trần Xuân Trường | 2A202603617 | truongxuan2834@gmail.com | XuanTruong28 | Người gắn nhãn 2 kiêm giữ hồ sơ (Chủ trì `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`) | `truong` |

Bốn vai của lab:
- **Người viết code (Nguyễn Thị Thanh Thúy):** Viết và chạy `src/lab13.py` (A1–A4, B1–B4), kiểm tra môi trường đa nền tảng.
- **Người kiểm số (Hồ Đức Mạnh):** Tính tay đối chiếu; tiếp quản code D1; hoàn thiện `report/team/bang_chi_phi.md`.
- **Người gắn nhãn 1 (Nguyễn Triều Dương):** Gắn nhãn độc lập 20 ca lỗi bộ 1; hoàn thiện `bang_loi.md` và `pilot_plan.yaml`.
- **Người gắn nhãn 2 kiêm giữ hồ sơ (Trần Xuân Trường):** Gắn nhãn độc lập bộ 2; chủ trì `chi_so.md`, tổng hợp `ho_so_launch_v0.md` 7 mục và `group_report.md`.

## Chi tiết đóng góp của từng thành viên

### Nguyễn Thị Thanh Thúy — Người viết code (TV1)
- **Phần việc phụ trách:** Triển khai mã nguồn mô hình chi phí trong `src/lab13.py` (A1–A4, B1–B4), hỗ trợ và kiểm tra chạy code D1.
- **Đóng góp cụ thể:** Hoàn thiện 3 hàm toán học A1 đạt 100% test case (1,20 · 1,25 · 1,25); viết hàm `mo_hinh()` tính toán chính xác các cấu phần chi phí từ 1.624 trace runs và 1.200 requests; chạy kiểm định cross-machine đảm bảo code không lỗi.
- **Bằng chứng:** File `src/lab13.py`, commit trên nhánh `thanhthuy`, terminal in kết quả A1–A4, B1–B4.

### Hồ Đức Mạnh — Người kiểm số (TV2)
- **Phần việc phụ trách:** Kiểm toán số liệu đối chiếu, chạy khảo sát độ nhạy B1–B4, tiếp quản code D1 cỡ mẫu, hoàn thiện `report/team/bang_chi_phi.md`.
- **Đóng góp cụ thể:** Đối chiếu sai số 0,00% với slide đáp án; phân tích chi phí toàn hệ thống (B3) và rủi ro xem lại 100% (B4); triển khai code tính toán 5 câu cỡ mẫu D1a–D1e trong `lab13.py`.
- **Bằng chứng:** File `report/team/bang_chi_phi.md`, code D1 trong `src/lab13.py`, commit trên nhánh `manh`.

### Nguyễn Triều Dương — Người gắn nhãn 1 & Thiết kế Pilot (TV3)
- **Phần việc phụ trách:** Gắn nhãn 20 ca lỗi độc lập bộ 1; hoàn thiện `report/team/bang_loi.md`, `report/team/pilot_plan.yaml` và `phieu_cham.md`.
- **Đóng góp cụ thể:** Phân loại 20 ca lỗi theo Google PAIR đạt đồng thuận 100%; xây dựng 5 giải pháp khắc phục có telemetry event và vai trò phụ trách; thiết kế kế hoạch pilot phân cụm 20 vs 20 nhân viên với 4 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ.
- **Bằng chứng:** File `report/team/bang_loi.md`, `report/team/pilot_plan.yaml` trên nhánh `duongnguyen`.

### Trần Xuân Trường — Người gắn nhãn 2 kiêm Giữ hồ sơ (TV4)
- **Phần việc phụ trách:** Gắn nhãn 20 ca lỗi độc lập bộ 2; chủ trì `report/team/chi_so.md`, tổng hợp `report/team/ho_so_launch_v0.md`, `report/team/group_report.md` và `TEAM.md`.
- **Đóng góp cụ thể:** Xây dựng danh mục 11 telemetry events có `trace_id` liên kết bảng lỗi; thiết lập 3 rủi ro kinh tế lớn; hoàn thiện hồ sơ Launch v0 1 trang đủ 7 mục với đề xuất Go có điều kiện bảo vệ trước hội đồng Gate 2a.
- **Bằng chứng:** Các file `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md` trên nhánh `truong`.
