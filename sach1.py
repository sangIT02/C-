class TacGia:
    def __init__(self, ten, quoc_tich,):
        self.ten = ten
        self.quoc_tich = quoc_tich

    def __str__(self):
        return f"Ten: {self.ten}, Quoc tich: {self.quoc_tich}"
    
class Sach:
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia:TacGia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.nam_xuat_ban = nam_xuat_ban
        self.tac_gia = tac_gia
        
    def __str__(self):
        return f"Ma sach: {self.ma_sach}, Ten sach: {self.ten_sach}, Nam xuat ban: {self.nam_xuat_ban}, "+ self.tac_gia.__str__()
    
    def get_tuoi_sach(self):
        return 2025 - int(self.nam_xuat_ban)
    def __add__(self, other):
        return "Tong hop: "+self.ten_sach +"&" + other.ten_sach


        
class GiaoTrinh(Sach):
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia, mon_hoc):
        super().__init__(ma_sach, ten_sach, nam_xuat_ban, tac_gia)
        self.mon_hoc = mon_hoc
    
class ThamKhao(Sach):
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia, linh_vuc):
        super().__init__(ma_sach, ten_sach, nam_xuat_ban, tac_gia)
        self.linh_vuc = linh_vuc

danh_sach = [
    GiaoTrinh("2022", "Lap trinh python", 2017, TacGia("Ha Huy","Viet Nam"), "python"),
    ThamKhao("2021", "Dia ly", 2019, TacGia("Xuan quynh","Viet Nam"), "dia li")
]
for sach in danh_sach:
    print(sach.__str__())

print(danh_sach[0] + danh_sach[1])