from shopbox.model.project import Project


class ProjectDAO(Project):
    @classmethod
    async def get_project(cls, project_name):
        project = await cls.query.where(cls.name == project_name).gino.first()
        return project

    @classmethod
    async def get_projects(cls):
        return await cls.query.gino.all()
