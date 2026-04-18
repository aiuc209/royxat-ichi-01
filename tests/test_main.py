import pytest
from datetime import datetime

def hisobla(roxyat):
    joriy_yil = 2026
    natijalar = []
    for ism, tugilgan_sana in roxyat:
        tugilgan_yil, tugilgan_oy, tugilgan_kun = map(int, tugilgan_sana.split('-'))
        yosh = joriy_yil - tugilgan_yil
        if (datetime(joriy_yil, 1, 1) - datetime(joriy_yil, tugilgan_oy, tugilgan_kun)).days < 0:
            yosh -= 1
        natijalar.append(f"{ism} — {yosh} yosh")
    return natijalar

@pytest.mark.parametrize("roxyat, natija", [
    ([("Ali", "2000-01-01")], ["Ali — 26 yosh"]),
    ([("Vali", "2001-12-31")], ["Vali — 24 yosh"]),
    ([("Jasur", "1990-06-15")], ["Jasur — 35 yosh"]),
    ([("Dilnoza", "2010-08-20")], ["Dilnoza — 15 yosh"]),
])
def test_hisobla(roxyat, natija):
    assert hisobla(roxyat) == natija
