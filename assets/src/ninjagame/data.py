from pathlib import Path


class Data:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def asset_path(*parts: str) -> Path:
        path = Data.BASE_DIR.joinpath(*parts)
        if not path.exists():
            raise FileNotFoundError(f"Asset not found: {path}")
        return path
