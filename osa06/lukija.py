from pathlib import Path


def lue_tyontekijat() -> str:
    csv: Path = Path(__file__).parent / "tyontekijat.csv"

    if not csv.exists():
        raise FileNotFoundError("Tiedostoa ei löydy")

    sisalto: str = csv.read_text(encoding="utf-8")
    return sisalto


def tulosta_rivinumeroin(teksti: str) -> None:
    rivit = teksti.splitlines()
    i = 0

    for rivi in rivit:
        print(i, rivi)
        i += 1


txt = lue_tyontekijat()
tulosta_rivinumeroin(txt)
