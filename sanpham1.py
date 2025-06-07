class SanPham:
    def __init__(self,ma_san_pham, ten, gia_ban):
        self.ten = ten
        self.ma_san_pham = ma_san_pham
        self.gia_ban = gia_ban

    def __str__(self):
        return f"Ma san pham: {self.ma_san_pham}, Ten: {self.ten}, Gia ban: {self.gia_ban}\n"
    
class DonHang:
    def __init__(self, ma_don_hang, ngay_lap):
        self.ma_don_hang = ma_don_hang
        self.ngay_lap = ngay_lap
        self.ds_sp = []
    
    def them_san_pham(self,san_pham):
        self.ds_sp.append(san_pham)
    
    def tinh_tong_tien(self):
        tong_tien = 0
        for sp in self.ds_sp:
            tong_tien += sp.gia_ban
        return tong_tien
    def __str__(self):
        tt_san_pham = ""
        for sp in self.ds_sp:
            tt_san_pham += sp.__str__()
        return f"Ma don hang: {self.ma_don_hang}, Ngay lap: {self.ngay_lap}\n" + tt_san_pham
    
    def __add__(self, other):
        don_moi = DonHang(self.ma_don_hang + "+" + other.ma_don_hang, self.ngay_lap)
        don_moi.ds_sp = self.ds_sp + other.ds_sp
        return don_moi
    
class DonHangOnline(DonHang):
    def __init__(self, ma_don_hang, ngay_lap, dia_chi, cuoc_phi):
        super().__init__(ma_don_hang, ngay_lap)
        self.dia_chi = dia_chi
        self.cuoc_phi = cuoc_phi
    
    def tinh_tong_tien(self):
        return super().tinh_tong_tien() + self.cuoc_phi
    
    def __add__(self, other):
        if not isinstance(other, DonHangOnline):
            return NotImplemented
        don_moi = DonHangOnline(
            self.ma_don_hang + "+" + other.ma_don_hang,
            self.ngay_lap,
            self.dia_chi + " & " + other.dia_chi,
            self.cuoc_phi + other.cuoc_phi
        )
        don_moi.ds_sp = self.ds_sp + other.ds_sp
        return don_moi
    
online1 = DonHangOnline("2025",20, "Ha noi",50000) 
online1.them_san_pham(SanPham("1","banh",10000))
online1.them_san_pham(SanPham("2","keo",11000))
online1.them_san_pham(SanPham("3","nuoc",12000))

online2 = DonHangOnline("2025",20, "Ha noi2", 30000)  
online2.them_san_pham(SanPham("4","banh4",10000))
online2.them_san_pham(SanPham("5","keo5",11000))
online2.them_san_pham(SanPham("6","nuoc6",12000))  

print(online1.__str__())
print(online2.__str__())

don3 = online1 + online2
print(don3)

