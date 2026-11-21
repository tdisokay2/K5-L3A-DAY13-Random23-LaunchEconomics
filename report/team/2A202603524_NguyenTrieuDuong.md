# Báo cáo cá nhân — Nguyễn Triều Dương — 2A202603524

## 1. Thông tin thành viên

- Họ tên: Nguyễn Triều Dương
- MSSV: 2A202603524
- Email: victorytop54321@gmail.com
- GitHub: tdisokay2
- Vai trong nhóm: Người gắn nhãn 1 (TV3), phụ trách phân tích lỗi và thiết kế pilot.
- Nhánh làm việc: duongnguyen; bài nhóm được tổng hợp trên main.

## 2. Phần việc phụ trách

Phụ trách CP3 trong report/team/bang_loi.md: cung cấp bộ nhãn 1 cho 20 ca lỗi, đối chiếu bộ nhãn 2 và xây dựng bảng khắc phục năm loại lỗi. Phụ trách bản dự thảo CP4 trong report/team/pilot_plan.yaml: phạm vi, chia nhóm, điều kiện dừng và rollback; phối hợp TV2 đối chiếu D1 và TV4 liên kết chỉ số/event. Được phân công ghi phiếu duyệt chéo nhưng chưa có kết quả thực tế để điền.

## 3. Đóng góp cụ thể

- Cung cấp 20 nhãn và giải thích theo nguyên nhân gốc, thuộc năm loại Google PAIR. Hai bộ nhãn ban đầu được lưu riêng; đồng thuận 20/20 = 100%. Khi mô tả bộ 2 có khác biệt với đề, đã chuyển xác nhận của TV4 để chốt nhãn theo đề gốc và giữ nguyên nội dung ban đầu làm bằng chứng.
- Hoàn thiện với hỗ trợ Codex bảng khắc phục ca 9, 7, 18, 4, 17, đủ năm loại. Mỗi dòng có event, ngưỡng, tần suất, hành động và một vai trò phụ trách. Đây là đề xuất thiết kế, chưa phải kết quả triển khai.
- Soạn pilot giới hạn noi_dia và hang_nang, có đối chứng đồng thời, ngẫu nhiên theo nhân viên, phân tầng depot và biện pháp giảm ảnh hưởng chéo.
- Đối chiếu phương án 20 nhân viên/nhóm, 299 yêu cầu/người, DE = 6,96, cỡ mẫu hiệu dụng khoảng 859/nhóm cho MDE 6 điểm. Nếu tác động thật là 5 điểm, power chỉ khoảng 0,64. Code D1 trong file nộp chính do TV2 thực hiện.
- Bổ sung bốn luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ, vai trò có quyền xử lý và rollback về nhân viên tự làm. Lịch và các lựa chọn pilot vẫn cần được nhóm chốt.
- Phối hợp tổng hợp các commit đã push lên main, giữ code A/B/D1 của thành viên phụ trách và bằng chứng CP3.

## 4. Bằng chứng

| Commit hoặc file | Nội dung |
| --- | --- |
| f1fb17e | Bộ nhãn 1 đủ 20 ca và giải thích do tôi cung cấp |
| 9afa8ce | Bộ nhãn 2, tính đồng thuận và ghi khác biệt mô tả |
| 1747ebc | Xác nhận của TV4, nhãn thống nhất và bảng khắc phục năm loại |
| a95a701, 576ac26 | Chuẩn bị và cập nhật bản pilot theo bằng chứng A/B |
| report/team/bang_loi.md | Hai bộ nhãn, đồng thuận và khắc phục |
| report/team/pilot_plan.yaml | Thiết kế pilot, luật dừng và rollback |
| src/tv3_pilot_checks.py | Script đối chiếu D1/baseline được chuẩn bị với AI |

## 5. Công cụ AI đã dùng

Dùng ChatGPT/Codex để giải thích yêu cầu, kiểm tra lập luận, định dạng hai bộ nhãn đã cung cấp, tính đồng thuận, hỗ trợ soạn khắc phục/pilot, kiểm tra YAML và thao tác Git. Không ghi nhãn do AI tạo thành kết quả độc lập của thành viên.

Các kiểm tra đã thực hiện với hỗ trợ Codex: đối chiếu mô tả với đề DOCX, đếm lại 20 cặp nhãn, kiểm tra đủ năm loại khắc phục, chạy script D1/baseline, đọc YAML bằng yaml.safe_load và đối chiếu code A/B/D1. Tôi đã xem xét bảng nhãn và chuyển xác nhận của TV4. Các phép chạy bằng công cụ là kiểm tra có hỗ trợ AI; không coi đó là bằng chứng tôi tự chạy trên một máy khác.

## 6. Tự đánh giá

Đã hoàn thành phần phân loại, đối chiếu và bảng khắc phục CP3; xây dựng bản pilot có đối chứng, giới hạn phạm vi, luật dừng và người phụ trách. Hiểu rằng đồng thuận cần đối chiếu đúng mô tả ca, cỡ mẫu theo cụm bị giới hạn bởi số nhân viên và dữ liệu chạy thử không đối chứng chưa chứng minh tác động của trợ lý.

Cần phối hợp chốt lịch và các lựa chọn pilot, thống nhất mã event với chi_so.md, bổ sung thời điểm chốt nhãn và ghi phiếu duyệt chéo khi có hoạt động thực tế. Chưa nhận là đã chạy pilot, sửa lỗi hệ thống hay có kết quả hội đồng.
