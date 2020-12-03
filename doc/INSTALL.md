# 0 Download

    git clone git@github.com:linzhi2013/specimen_bioseq_system.git
    tar zxvf specimen_bioseq_system-2.0.tar.gz
    cd specimen_bioseq_system-2.0

# 1. Dependencies

    conda create -n django-3.1.2 -c anaconda -c conda-forge django=3.1.2 django-import-export=2.4.0 django-grappelli=2.14.2 djangorestframework=3.12.1 biopython postgresql psycopg2

Now we have an envionment called `django-3.1.2`, all the commands below must be ran within this environment.

    source activate django-3.1.2
    pip3 install pyconcrete

# 2. Postgres database initiation

    source activate django-3.1.2

Choose a path for Postgres to store data, e.g. `$HOME/my_postgres`

    initdb -D $HOME/my_postgres  -U postgres

when this is done, you will get something like:

    initdb: warning: enabling "trust" authentication for local connections
    You can change this by editing pg_hba.conf or using the option -A, or
    --auth-local and --auth-host, the next time you run initdb.

    Success. You can now start the database server using:

        pg_ctl -D /Users/mengguanliang/my_postgres -l logfile start


## 2.1 start the Postgres

Now customize the `port` by editing the file `$HOME/my_postgres/postgresql.conf`, for example:

    port = 5444

Now starting your database with command:

    pg_ctl -D $HOME/my_postgres -l logfile start


## 2.2 Create database

Create a database for this specimen information managment system:

    createdb -p 5444 -U postgres django_specimendb


And create another database for BioSQL database (for storing biological sequence etc.):

    createdb -p 5444 -U postgres django_biosql


## 2.3 Load database schemen for the `django_biosql` database

Find the file `biosql/sql/biosqldb-pg.sql`, then do:

    psql -p 5444  -U postgres  django_biosql < biosql/sql/biosqldb-pg.sql

## 2.4 Load taxonomy database into the `django_biosql` database

Find the script `biosql/scripts/load_ncbi_taxonomy.pl`.

    perl biosql/scripts/load_ncbi_taxonomy.pl --dbname django_biosql --driver Pg --dbuser postgres --port 5444 --download

This step can take half an hour.

If you meet Perl module problems, just install related Perl modules first.


## 2.5 Update database setting in `specimendb/settings.py` file

Find and update to:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'django_specimendb',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5444',
        }
    }

    BIOSQLDB_SETTING = {
        'driver': "psycopg2",
        'user': "postgres",
        'passwd': "",
        'host': "127.0.0.1",
        'port': 5444,
        'db': "django_biosql",
        'subdb': "seqdb"
    }


# 3. `specimen_bioseq_system` initiation

Find the script file `specimen_bioseq_system/manage.py`.
Do:

    python3 manage.py makemigrations
    python3 manage.py migrate --run-syncdb

Then:

    python3 manage.py createsuperuser

It will ask you for a superuser name and password (e.g., username: `django`, passoword: `django123`), which will be used to login the system from a browser later.


Now you're ready to use the system!

    python3 manage.py runserver

Copy the URL (`http://127.0.0.1:8000/admin/`) printed out by this command to your browser, login the database with previously created account and password (e.g., username: `django`, passoword: `django123`) and enjoy it!

From now on, you can do the rest of the jobs on the website only!


# 4. Copyright
Copyright (c) 2020-2021 Guanliang Meng. All rights reserved.

This file is part of the Specimen Bioseq System.

The Specimen Bioseq System is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

**The Specimen Bioseq System is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.**  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the Specimen Bioseq System. If not, see <http://www.gnu.org/licenses/>.

