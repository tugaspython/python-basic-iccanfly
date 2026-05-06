import pytest
from kalkulator import tambah, kurang, kali, bagi

# ==========================================
# TEST UNTUK FUNGSI TAMBAH (5 Kasus)
# ==========================================
def test_tambah():
    # 1. Penjumlahan dua angka positif
    assert tambah(5, 3) == 8
    
    # 2. Penjumlahan dua angka negatif
    assert tambah(-5, -3) == -8
    
    # 3. Penjumlahan angka positif dan negatif
    assert tambah(5, -3) == 2
    
    # 4. Penjumlahan dengan angka nol
    assert tambah(0, 7) == 7
    
    # 5. Penjumlahan bilangan desimal (float)
    assert tambah(2.5, 3.1) == 5.6

# ==========================================
# TEST UNTUK FUNGSI KURANG (5 Kasus)
# ==========================================
def test_kurang():
    # 6. Pengurangan dua angka positif
    assert kurang(10, 4) == 6
    
    # 7. Pengurangan dua angka negatif
    assert kurang(-10, -4) == -6
    
    # 8. Pengurangan angka kecil dengan angka besar
    assert kurang(5, 10) == -5
    
    # 9. Pengurangan dengan angka nol
    assert kurang(8, 0) == 8
    
    # 10. Pengurangan bilangan desimal (float)
    assert kurang(5.5, 2.2) == 3.3

# ==========================================
# TEST UNTUK FUNGSI KALI (5 Kasus)
# ==========================================
def test_kali():
    # 11. Perkalian dua angka positif
    assert kali(4, 5) == 20
    
    # 12. Perkalian angka negatif dan positif
    assert kali(-4, 5) == -20
    
    # 13. Perkalian dua angka negatif
    assert kali(-4, -5) == 20
    
    # 14. Perkalian dengan angka nol
    assert kali(7, 0) == 0
    
    # 15. Perkalian bilangan desimal (float)
    assert kali(2.5, 2.0) == 5.0

# ==========================================
# TEST UNTUK FUNGSI BAGI (5 Kasus)
# ==========================================
def test_bagi():
    # 16. Pembagian angka positif yang habis dibagi
    assert bagi(20, 4) == 5.0
    
    # 17. Pembagian angka negatif dengan positif
    assert bagi(-20, 4) == -5.0
    
    # 18. Pembagian angka nol dengan angka lain
    assert bagi(0, 5) == 0.0
    
    # 19. Pembagian yang menghasilkan bilangan desimal
    assert bagi(5.5, 2.0) == 2.75
    
    # 20. Penanganan error: Pembagian dengan nol
    assert bagi(5, 0) == "Error: Pembagian dengan nol"
