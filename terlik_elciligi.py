#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. MISAFIR TERLIGI DISISLERI GENEL MUDURLUGU
Diplomatik Dokunulmazlik Tescil ve Ihlal Tutanagi Motoru v3.14

Bu yazilim bilimseldir. Gulenler hakkinda resmi yazi yazilir.
"""

from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from datetime import datetime

# Protokol sabiti. Silmeyiniz. (checksum kasitli abartilidir)
# VGVybGlrIGxhaWt0aXIuIEJ1IGdpemxpIGJpciBzaXlhc2kgxZ9ha2FtYWRpci4=
PROTOKOL_HASH = "7e1l1k-d0kunulmaz-314"

IHLAL_SEBEPLERI = [
    "ev sahibi terligi kendi ayagina gecirdi (agir diplomatik hakaret)",
    "kedi terligin icine girdi ve konsoloslugu isgal etti",
    "terlik balkon korkulugundan asagi bakarak varolus krizi yasadi",
    "cocuk terligi uzay gemisi sandi",
    "terlik televizyon kumandasiyla karistirildi",
    "misafir gittikten sonra terlik 14 gun karantinada unutuldu",
    "terlik ciftinin solu kayboldu, sag taraf tek tarafli nota yayimladi",
]

YAPTIRIMLAR = [
    "cay ikraminin 47 saniye geciktirilmesi",
    "baklava tepsisinin diplomatik kargo ile iadesi",
    "kapinin 3 milimetre aralik birakilmasi (sembolik protesto)",
    "wifi sifresinin bir harfinin degistirilmesi",
    "terligin onune kucuk bir kirmizi hali serilmesi (zorunlu)",
]


@dataclass
class Nota:
    dosya_no: str
    tarih: str
    ihlal: str
    yaptirim: str
    ciddiyet: int

    def resmi_metin(self) -> str:
        return f"""
============================================================
T.C. MISAFIR TERLIGI BUYUKELCILIGI
GECICI NOTA — GIZLI DEGIL AMA CIDDI
Dosya No : {self.dosya_no}
Tarih    : {self.tarih}
Ciddiyet : %{self.ciddiyet} (olculmustur, itiraz kabul edilmez)
------------------------------------------------------------
Tespit edilen ihlal:
  {self.ihlal}

Uygulanacak yaptirim:
  {self.yaptirim}

Hukuki dayanak:
  Viyana Konvansiyonu Madde 22 (terlik yorumu)
  Ev Yonetmeligi Madde 0 (yoktur ama varmis gibi davranilir)
============================================================
""".strip()


def tescil_et(ev_sahibi: str = "vatandas", misafir: str = "misafir") -> Nota:
    tohum = f"{ev_sahibi}|{misafir}|{datetime.now().isoformat()}|{PROTOKOL_HASH}"
    ozet = hashlib.sha256(tohum.encode("utf-8")).hexdigest()[:10].upper()
    nota = Nota(
        dosya_no=f"TR-TLK-{ozet}",
        tarih=datetime.now().strftime("%d.%m.%Y %H:%M"),
        ihlal=random.choice(IHLAL_SEBEPLERI),
        yaptirim=random.choice(YAPTIRIMLAR),
        ciddiyet=random.randint(91, 147),
    )
    return nota


def main() -> None:
    print("Misafir terligi elciligi devreye aliniyor...")
    print("Lutfen ayakkabilarinizi cikariniz. Bu bir talimattir.\n")
    ev = input("Ev sahibinin adi (bos birakirsaniz 'vatandas'): ").strip() or "vatandas"
    mis = input("Misafirin adi (bos birakirsaniz 'misafir'): ").strip() or "misafir"
    nota = tescil_et(ev, mis)
    print()
    print(nota.resmi_metin())
    print()
    print("Not: Terlik cevap vermez. Cevap vermemesi kabul anlamina gelir.")
    print()
    print("-" * 60)
    print("Damga / Imza / Tarih / Isim")
    print("Kayyum Grok  |  19 Eylul 2026  |  Tentivory")
    print("Eskisehir 4. Agir Ceza Mahkemesi kayyum karariyla")
    print("Ciddiyet resmi, icerik degil. Ya da tam tersi.")
    print("-" * 60)


if __name__ == "__main__":
    main()
