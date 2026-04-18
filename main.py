from datetime import datetime

joriy_yil = 2026
ro_yxat = [("Ali", "2001-01-01"), ("Vali", "2005-06-01"), ("Jalol", "2010-09-01")]

for ism, tugilgan_sana in ro_yxat:
    tugilgan_yil = int(tugilgan_sana.split('-')[0])
    yosh = joriy_yil - tugilgan_yil
    print(f"{ism} — {yosh} yosh")
