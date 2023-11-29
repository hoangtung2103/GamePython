import unicodedata

class ThiSinh:
    next_id = 1  # Biến class để tự động tăng mã thí sinh

    def __init__(self, ho_ten, diem_thi, dan_toc, khu_vuc):
        self.id = ThiSinh.next_id
        ThiSinh.next_id += 1
        self.ho_ten = self.chuan_hoa_ho_ten(ho_ten)
        self.diem_thi = diem_thi
        self.dan_toc = dan_toc
        self.khu_vuc = khu_vuc

    def chuan_hoa_ho_ten(self, ho_ten):
        return ' '.join([word.capitalize() for word in ho_ten.split()])

    def tinh_diem_uu_tien(self):
        diem_uu_tien = 0
        if self.khu_vuc == 1:
            diem_uu_tien += 1.5
        elif self.khu_vuc == 2:
            diem_uu_tien += 1
        if self.dan_toc != "Kinh":
            diem_uu_tien += 1.5
        return diem_uu_tien

    def tong_diem(self):
        return self.diem_thi + self.tinh_diem_uu_tien()

    def trang_thai_trung_tuyen(self, diem_chuan):
        if self.tong_diem() >= diem_chuan:
            return "Do"
        else:
            return "Truot"

if __name__ == '__main__':
    n = int(input().strip())
    danh_sach_thi_sinh = []

    for _ in range(n):
        ho_ten = input().strip()
        diem_thi = float(input().strip())
        dan_toc = input().strip()
        khu_vuc = int(input().strip())

        ts = ThiSinh(ho_ten, diem_thi, dan_toc, khu_vuc)
        danh_sach_thi_sinh.append(ts)

    diem_chuan = 20.5

    # Sắp xếp danh sách theo tổng điểm giảm dần và mã thí sinh tăng dần
    danh_sach_thi_sinh.sort(key=lambda ts: (-ts.tong_diem(), ts.id))

    # In danh sách đã sắp xếp
    for ts in danh_sach_thi_sinh:
        tong_diem = round(ts.tong_diem(), 1)
        trang_thai = ts.trang_thai_trung_tuyen(diem_chuan)
        print(f'TS{ts.id:02d} {ts.ho_ten} {tong_diem} {trang_thai}')
