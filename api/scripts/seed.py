# -*- coding: utf-8 -*-

import os
import sys
import lorem
from lorem.text import TextLorem

APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(APP_DIR)

from shopbox.db.session import Session
from shopbox.db_models.project import Project

session = Session()
sd_lorem = TextLorem(prange=(3, 4))


def create_project(index):
    session.add(
        Project(
            id=index,
            name=f"project{index}",
            display_name=f"Project {index}",
            short_description=sd_lorem.paragraph(),
            long_description=lorem.text(),
        )
    )


def create_projects(num):
    for i in range(num):
        create_project(i)
    session.commit()


def main():
    command = "count" if len(sys.argv) < 2 else sys.argv[1]
    if command == "count":
        print(f"Number of projects:  {session.query(Project).count()}")
    elif command == "create":
        create_projects(1864)
    elif command == "delete":
        session.query(Project).delete()
        session.commit()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
