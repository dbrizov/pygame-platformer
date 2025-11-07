import pathlib


class Data:
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def asset_path(*parts: str) -> pathlib.Path:
        path = Data.BASE_DIR.joinpath(*parts)
        if not path.exists():
            raise FileNotFoundError(f"Asset not found: {path}")
        return path
