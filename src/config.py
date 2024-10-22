from pathlib import Path

BASE_APP_DIR = Path(__file__).parent.parent

DATABASE = {
    "database": str(BASE_APP_DIR / "db.sqlite"),
}
