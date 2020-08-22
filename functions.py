import os


def backup(database):
    os.system(
        'PGPASSWORD="%(PASSWORD)s" pg_dump '
        '--host %(HOST)s '
        '--port %(PORT)s '
        '--username "%(USER)s" '
        '--role "%(USER)s" '
        '--schema "public" '
        '--format custom '
        '--blobs '
        '--no-password '
        '--encoding UTF8 '
        '--verbose '
        '--file "%(NAME)s.backup" "%(NAME)s"' % database)


def restore(database):
    os.system(
        'PGPASSWORD="%(PASSWORD)s" pg_restore '
        '--host %(HOST)s '
        '--port %(PORT)s '
        '--username "%(USER)s" '
        '--dbname "%(NAME)s" '
        '--role "%(USER)s" '
        '--no-owner '
        '--verbose "%(NAME)s.backup"' % database)
        
