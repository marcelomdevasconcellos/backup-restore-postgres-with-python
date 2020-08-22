# backup-restore-postgres-with-python

ATTENTION: This script require pg_dump and pg_restore installed.

1) Create env_example based .env;

```
DATABASE_SOURCE=psql://user:pass@host:port/name
DATABASE=psql://user:pass@host:port/name
```

* Configure source database in DATABASE_SOURCE variable;
* Configure destiny database in DATABASE variable;

2) Execute: 

```
python backup_restore.py
```
