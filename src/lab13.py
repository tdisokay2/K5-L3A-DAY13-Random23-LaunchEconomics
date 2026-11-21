"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p must be in (0, 1]')
    if k is None:
        return 1.0 / p
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be a positive integer or None')
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p must be in (0, 1]')
    if k is None:
        return 1.0
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be a positive integer or None')
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    success = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / success


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhánh cho kiểm định hai tỷ lệ độc lập, làm tròn lên."""
    if not 0 < p1 < p2 < 1:
        raise ValueError('Require 0 < p1 < p2 < 1')
    if not 0 < alpha < 1 or not 0 < power < 1:
        raise ValueError('alpha and power must be in (0, 1)')
    normal = NormalDist()
    z_alpha = normal.inv_cdf(1 - alpha / 2)
    z_power = normal.inv_cdf(power)
    p_bar = (p1 + p2) / 2
    numerator = (z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
                 + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(numerator / (p2 - p1) ** 2)


def cong_suat_hai_ty_le(p1, p2, n_moi_nhanh, alpha=0.05):
    """Xấp xỉ power hai phía theo hiệu ứng arcsine (Cohen h)."""
    normal = NormalDist()
    z_alpha = normal.inv_cdf(1 - alpha / 2)
    h = 2 * math.asin(math.sqrt(p2)) - 2 * math.asin(math.sqrt(p1))
    noncentrality = abs(h) * math.sqrt(n_moi_nhanh / 2)
    return (normal.cdf(-z_alpha - noncentrality)
            + normal.cdf(noncentrality - z_alpha))


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        if not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('max_lan_chay must be a positive integer or None')
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    token = tien_token.sum()
    tool = tien_tool.sum()
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    return dict(token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem_lai,
                lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else math.nan,
                hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan)


if __name__ == '__main__':
    # Keep Vietnamese status labels printable in Windows consoles using legacy code pages.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # A3 · Chi phí theo loại yêu cầu
    print('A3 · Chi phí theo loại')
    for loai in reqs['loai'].drop_duplicates():
        loai_reqs = reqs[reqs['loai'] == loai]
        subset = mo_hinh(runs, loai_reqs)
        n_req = len(loai_reqs)
        print(f'{loai:12s} yc={n_req:4d} thanh_cong={subset["thanh_cong"]:4d} '
              f'ty_le={subset["thanh_cong"] / n_req:.1%} '
              f'lan_chay/yc={loai_reqs["so_lan_chay"].mean():.2f} '
              f'cps={subset["cps"]:,.0f}d so_voi_baseline={subset["cps"] / BASELINE:.2f}x')
    # A4 · Phân bổ 40 triệu đồng/tháng cho phạm vi pilot.
    pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pilot_cost = mo_hinh(runs, pilot)
    # Giữ mẫu số là toàn bộ mẫu để khớp tỷ lệ thành công của phạm vi trên tổng tải.
    pilot_success_rate = pilot_cost['thanh_cong'] / len(reqs)
    monthly_success = 45000 * pilot_success_rate
    fixed_per_success = 40_000_000 / monthly_success
    half_volume_fixed = fixed_per_success * 2
    print('A4 · Chi phí cố định')
    print(f'pham_vi=noi_dia+hang_nang thanh_cong_mau={pilot_cost["thanh_cong"]} '
          f'ty_le={pilot_success_rate:.1%} thanh_cong_thang={monthly_success:,.0f}')
    print(f'chi_phi_co_dinh/viec={fixed_per_success:,.0f}d '
          f'tong_cps={pilot_cost["cps"] + fixed_per_success:,.0f}d')
    print(f'nua_san_luong: chi_phi_co_dinh/viec={half_volume_fixed:,.0f}d '
          f'tong_cps={pilot_cost["cps"] + half_volume_fixed:,.0f}d')
    # B1 · Đổi từng yếu tố, mỗi lần chỉ thay một tham số.
    kich_ban = {
        'Gia token gap doi': dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi': dict(he_so_xem_lai=2),
        'Xem lai giam mot nua': dict(he_so_xem_lai=0.5),
        'Lam lai gap doi': dict(he_so_lam_lai=2),
        'Lam lai giam mot nua': dict(he_so_lam_lai=0.5),
        'Luong tang 25%': dict(luong_phut=2500),
        'Toi da 2 lan chay': dict(max_lan_chay=2),
        'Chi 1 lan chay': dict(max_lan_chay=1),
    }
    print('B1 · Do nhay tung yeu to (CPS, thay doi so voi A2)')
    ket_qua_b1 = {}
    for ten, tham_so in kich_ban.items():
        ket_qua_b1[ten] = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi = (ket_qua_b1[ten] / ket_qua['cps'] - 1) * 100
        print(f'{ten:24s} {ket_qua_b1[ten]:8,.0f}d {thay_doi:+6.1f}%')

    # B2 · Kịch bản kết hợp và xếp hạng theo tác động tuyệt đối lên CPS.
    ket_hop = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f'B2 · Token gap doi + xem lai gap doi: {ket_hop["cps"]:,.0f}d '
          f'({(ket_hop["cps"] / ket_qua["cps"] - 1) * 100:+.1f}%)')
    anh_huong = {
        'So ca lam lai': max(abs(ket_qua_b1['Lam lai gap doi'] / ket_qua['cps'] - 1),
                             abs(ket_qua_b1['Lam lai giam mot nua'] / ket_qua['cps'] - 1)),
        'Ty le xem lai': max(abs(ket_qua_b1['Xem lai gap doi'] / ket_qua['cps'] - 1),
                             abs(ket_qua_b1['Xem lai giam mot nua'] / ket_qua['cps'] - 1)),
        'Luong nhan vien': abs(ket_qua_b1['Luong tang 25%'] / ket_qua['cps'] - 1),
        'Gia token': abs(ket_qua_b1['Gia token gap doi'] / ket_qua['cps'] - 1),
        'Gioi han retry': abs(ket_qua_b1['Chi 1 lan chay'] / ket_qua['cps'] - 1),
    }
    hang = sorted(anh_huong, key=anh_huong.get, reverse=True)
    print('B2 · Ba yeu to anh huong manh nhat: ' + ', '.join(hang[:3]))

    # B3 · So sánh CPS và chi phí toàn hệ thống khi giới hạn số lần chạy.
    print('B3 · Gioi han chay lai (chi phi don vi: dong)')
    for gioi_han in (1, 2, 3):
        gioi_han_cost = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - gioi_han_cost['thanh_cong']
        chi_phi_he_thong = gioi_han_cost['tong'] + BASELINE * khong_thanh_cong
        print(f'{gioi_han} lan: tong_tro_ly={gioi_han_cost["tong"]:,.0f}d '
              f'khong_thanh_cong={khong_thanh_cong} '
              f'toan_he_thong={chi_phi_he_thong:,.0f}d cps={gioi_han_cost["cps"]:,.0f}d')

    # B4 · Xem lại 100% các yêu cầu pilot có gợi ý (ít nhất một run status=ok).
    pilot_ids = pilot['request_id']
    pilot_runs = runs[runs['request_id'].isin(pilot_ids)]
    ids_co_goi_y = pilot_runs.loc[pilot_runs['status'] == 'ok', 'request_id'].unique()
    pilot_lam_lai = pilot[pilot['ket_qua'] == 'lam_lai']
    pilot_token_tool = (
        pilot_runs['tokens_in'].sum() / 1000 * GIA_VAO
        + pilot_runs['tokens_out'].sum() / 1000 * GIA_RA
        + pilot_runs['tool_calls'].sum() * GIA_TOOL
    )
    so_phut_xem_lai_moi_ca = 5
    so_phut_lam_lai_moi_ca = 9
    b4_tong = (pilot_token_tool + len(ids_co_goi_y) * so_phut_xem_lai_moi_ca * LUONG_PHUT
               + len(pilot_lam_lai) * so_phut_lam_lai_moi_ca * LUONG_PHUT)
    b4_thanh_cong = int((pilot['ket_qua'] == 'thanh_cong').sum())
    b4_cps = b4_tong / b4_thanh_cong
    # Dùng mức trung bình toàn bộ ca làm lại theo hướng dẫn, rồi áp dụng cho 48 ca pilot.
    lam_lai_phut_thuc_te = round(reqs.loc[
        reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'
    ].mean(), 1)
    b4_tong_thuc_te = (pilot_token_tool + len(ids_co_goi_y) * so_phut_xem_lai_moi_ca * LUONG_PHUT
                       + len(pilot_lam_lai) * lam_lai_phut_thuc_te * LUONG_PHUT)
    b4_cps_thuc_te = b4_tong_thuc_te / b4_thanh_cong
    print(f'B4 · Pilot review 100%: n={len(pilot)}, goi_y={len(ids_co_goi_y)}, '
          f'thanh_cong={b4_thanh_cong}, token_tool={pilot_token_tool:,.0f}d')
    print(f'B4 · 9 phut lam lai/ca: tong={b4_tong:,.0f}d cps={b4_cps:,.0f}d '
          f'({b4_cps / BASELINE:.2f}x baseline)')
    print(f'B4 · {lam_lai_phut_thuc_te:.1f} phut lam lai/ca theo simulated: '
          f'tong={b4_tong_thuc_te:,.0f}d cps={b4_cps_thuc_te:,.0f}d '
          f'({b4_cps_thuc_te / BASELINE:.2f}x baseline)')

    # D1 · Cỡ mẫu: baseline 70%, alpha 5%, power 80%, ICC 0,02.
    baseline = 0.70
    alpha = 0.05
    power = 0.80
    icc = 0.02
    n_5pp = co_mau_hai_ty_le(baseline, baseline + 0.05, alpha, power)
    de_m75 = 1 + (75 - 1) * icc
    n_clustered_5pp = math.ceil(n_5pp * de_m75)
    staff_per_arm_5pp = math.ceil(n_clustered_5pp / 75)
    n_6pp = co_mau_hai_ty_le(baseline, baseline + 0.06, alpha, power)
    staff_clusters = 20
    max_eff_20_staff = staff_clusters / icc
    effective_20_staff_m75 = staff_clusters * 75 / de_m75
    max_eff_6_depots = 6 / icc
    m_for_6pp = math.ceil(n_6pp * (1 - icc) / (staff_clusters - n_6pp * icc))
    de_for_6pp = 1 + (m_for_6pp - 1) * icc
    power_5pp_at_859 = cong_suat_hai_ty_le(baseline, baseline + 0.05, n_6pp, alpha)
    print('D1 · Co mau moi nhanh')
    print(f'a) Chia theo yeu cau, MDE 5 diem: {n_5pp:,}')
    print(f'b) Nhan vien, m=75: DE={de_m75:.2f}; n={n_clustered_5pp:,}/nhanh; '
          f'{staff_per_arm_5pp} nhan vien/nhanh ({staff_per_arm_5pp * 2} tong, khong du 40)')
    print(f'c) 20 nhan vien/nhanh: gioi han tren c/ICC={max_eff_20_staff:,.0f}; '
          f'neu m=75 thi n_hieu_dung={effective_20_staff_m75:,.1f}; deu < {n_5pp:,}')
    print(f'd) 6 depot/nhanh: gioi han tren c/ICC={max_eff_6_depots:,.0f}')
    print(f'e) MDE 6 diem: n={n_6pp:,}/nhanh; 20 nhan vien can m={m_for_6pp} '
          f'yeu cau/nhan vien (DE={de_for_6pp:.2f}); neu MDE that 5 diem, '
          f'power~{power_5pp_at_859:.2f}')
