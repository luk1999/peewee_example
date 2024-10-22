from playhouse.migrate import SqliteMigrator

from migrations.m_0001 import backwards as backwards_0, forwards as forwards_0
from models import db

migrator = SqliteMigrator(db)


def forwards():
    print("Applying migration 0...")
    forwards_0(migrator)
    print("Done")


def backwards():
    print("Unapplying migration 0...")
    backwards_0(migrator)
    print("Done")
