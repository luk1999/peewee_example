from playhouse.migrate import migrate


def forwards(migrator):
    migrate(
        migrator.add_index("author", ("date_of_birth",), False),
        migrator.add_index("book", ("year",), False),
    )


def backwards(migrator):
    migrate(
        migrator.drop_index("author", "author_date_of_birth"),
        migrator.drop_index("book", "book_year"),
    )
