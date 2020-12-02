#!/usr/bin/env python
#####################################################
# Copyright (c) 2020-2021 Guanliang Meng. All rights reserved.
#
# This file is part of the Specimen Bioseq System.
#
# The Specimen Bioseq System is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# The Specimen Bioseq System is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# the Specimen Bioseq System. If not, see <http://www.gnu.org/licenses/>.

#####################################################

"""Django's command-line utility for administrative tasks."""
import pyconcrete

import os
import sys

message = '''
Copyright (c) 2020-2021 Guanliang Meng. All rights reserved.

This file is part of the Specimen Bioseq System.

The Specimen Bioseq System is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

The Specimen Bioseq System is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the Specimen Bioseq System. If not, see <http://www.gnu.org/licenses/>.
'''

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'specimendb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(message)
    main()
