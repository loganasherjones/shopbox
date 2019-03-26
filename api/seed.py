# -*- coding: utf-8 -*-
import asyncio
import lorem
import sys
from lorem.text import TextLorem
from shopbox.model import db
from shopbox.model.project import Project

sdlorem = TextLorem(prange=(3, 5))


async def create():
    for i in range(1000):
        await Project.create(
            name=f"project{i}",
            display_name=f"Project {i}",
            short_description=sdlorem.paragraph(),
            long_description=lorem.text(),
        )


async def delete():
    await Project.delete.gino.all()


async def count():
    print(await db.func.count(Project.id).gino.scalar())


async def main():
    if len(sys.argv) < 2:
        print("Need a command.")
        sys.exit(1)

    command = sys.argv[1]
    await db.set_bind("postgresql://postgres:@localhost/shopbox")
    if command == "create":
        await create()
    elif command == "count":
        await count()
    elif command == "delete":
        await delete()
    else:
        print(f"Invalid command {command}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
