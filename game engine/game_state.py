# DATA PEMAIN
pemain = ["Player", "CPU"]

# GILIRAN
giliran = 0  # 0 = Player, 1 = CPU

# SKOR
skor_player = 0
skor_cpu = 0

# STATUS
status = "berlangsung"

# JUMLAH LANGKAH
jumlah_langkah = 0

# PEMENANG
pemenang = ""

# UKURAN PAPAN
ukuran_papan = 3

def proses_giliran(jumlah_sos):
    global giliran
    global skor_player, skor_cpu
    global jumlah_langkah, status, pemenang

    if status == "berlangsung":

        jumlah_langkah = jumlah_langkah + 1

        # Menambahkan skor
        if giliran == 0:
            skor_player = skor_player + jumlah_sos
        else:
            skor_cpu = skor_cpu + jumlah_sos

        # Memeriksa papan penuh
        if jumlah_langkah == ukuran_papan * ukuran_papan:
            status = "selesai"

            if skor_player > skor_cpu:
                pemenang = "Player"

            elif skor_cpu > skor_player:
                pemenang = "CPU"

            else:
                pemenang = "Seri"

        else:
            # Berganti giliran jika tidak ada SOS
            if jumlah_sos == 0:

                if giliran == 0:
                    giliran = 1
                else:
                    giliran = 0
