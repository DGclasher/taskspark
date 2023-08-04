import graphene
from .models import Task
from graphene_django import DjangoObjectType


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("__all__")


class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)
    task_by_id = graphene.Field(TaskType, id=graphene.Int())
    task_by_due = graphene.List(TaskType, date=graphene.Date())

    def resolve_all_tasks(root, info, **kwargs):
        return Task.objects.all()

    def resolve_task_by_id(root, info, id):
        return Task.objects.get(pk=id)

    def resolve_task_by_due(root, info, date):
        return Task.objects.filter(due_date=date)


class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        due_date = graphene.Date(required=False)
    task = graphene.Field(TaskType)

    def mutate(self, info, title, description, due_date=None):
        task = Task.objects.create(
            title=title, description=description, due_date=due_date)
        return CreateTask(task=task)


class UpdateInput(graphene.InputObjectType):
    title = graphene.String(required=False)
    description = graphene.String(required=False)
    due_date = graphene.Date(required=False)
    is_completed = graphene.Boolean(required=False)


class UpdateTask(graphene.Mutation):
    class Arguments:
        task_id = graphene.Int(required=True)
        task_data = UpdateInput(required=False)
    task = graphene.Field(TaskType)

    def mutate(self, info, task_id, task_data=None):
        task = Task.objects.get(pk=task_id)
        if task_data:
            for field, value in task_data.items():
                if value:
                    setattr(task, field, value)
            task.save()
        return UpdateTask(task=task)


class DeleteTask(graphene.Mutation):
    class Arguments:
        task_id = graphene.Int(required=True)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()
            return DeleteTask(success=True, message="Task deleted successfully.")
        except Task.DoesNotExist:
            return DeleteTask(success=False, message="Task does not exist.")


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
