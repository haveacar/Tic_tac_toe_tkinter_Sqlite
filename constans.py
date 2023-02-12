
import pathlib
# database patch
DB_URL = pathlib.Path(__file__).parent.joinpath("data_base_tic.db")


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS "game stats" (
	"name"	TEXT,
	"user"	INTEGER,
	"computer"	INTEGER,
	PRIMARY KEY("name")
);
"""

SELECT_NAMES = 'SELECT name from "game stats"'


