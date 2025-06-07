class CauThu:
    def __init__(self, ho_ten, vi_tri, quoc_tich):
        self.ho_ten = ho_ten
        self.vi_tri = vi_tri
        self.quoc_tich = quoc_tich

    def __str__(self):
        return f"Ho ten: {self.ho_ten}, vi tri: {self.vi_tri}, quoc tich: {self.quoc_tich}"
    
class DoiBong:
    def __init__(self, ten_doi, huan_luyen_vien):
        self.ten_doi = ten_doi
        self.huan_luyen_vien = huan_luyen_vien
        self.danh_sach_ct = []

    def them_cau_thu(self, cau_thu):
        self.danh_sach_ct.append(cau_thu)

    def __str__(self):
        cau_thu_str = '\n'.join(str(c) for c in self.danh_sach_ct)
        return f"Tên đội: {self.ten_doi}\nHuấn luyện viên: {self.huan_luyen_vien}\nDanh sách cầu thủ:\n{cau_thu_str}"
    
    def __add__(self, other):
        doi_moi = DoiBong(self.ten_doi + " + " + other.ten_doi,
                          self.huan_luyen_vien + " / " + other.huan_luyen_vien)
        doi_moi.danh_sach_ct = self.danh_sach_ct + other.danh_sach_ct
        return doi_moi
    
class DoiTuyenQuocGia(DoiBong):
    def __init__(self, ten_doi, huan_luyen_vien, quoc_gia):
        super().__init__(ten_doi, huan_luyen_vien,)
        self.quoc_gia = quoc_gia
    def __str__(self):
        return f"Quoc gia: {self.quoc_gia}\n" + super().__str__()
    

DTQG1 = DoiTuyenQuocGia("Viet nam","Pack", "VN")
DTQG1.them_cau_thu(CauThu("Nguyen van Sang","Thu mon", "Viet Nam"))
DTQG1.them_cau_thu(CauThu("Nguyen van Sang1","Thu mon1", "Viet Nam1"))
DTQG1.them_cau_thu(CauThu("Nguyen van Sang2","Thu mon2", "Viet Nam2"))
DTQG1.them_cau_thu(CauThu("Nguyen van Sang3","Thu mon3", "Viet Nam3"))

DTQG2 = DoiTuyenQuocGia("Viet nam2","Pack2", "VN2")
DTQG2.them_cau_thu(CauThu("Nguyen van Sang9","Thu mon9", "Viet Nam9"))
DTQG2.them_cau_thu(CauThu("Nguyen van Sang8","Thu mon8", "Viet Nam8"))
DTQG2.them_cau_thu(CauThu("Nguyen van Sang7","Thu mon7", "Viet Nam7"))
DTQG2.them_cau_thu(CauThu("Nguyen van Sang6","Thu mon6", "Viet Nam6"))

DTQGm = DTQG1 + DTQG2

print(DTQGm.__str__())
    