
import graphene
from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel
from .query import Role

class IntroduceRole(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    mutation = graphene.Field(lambda: Role)
    #@classmethod
    def mutate(self, info, name):
        mutation = RoleModel(name=name)
        mutation.save()
        return IntroduceRole(mutation=mutation)
    
class Mutation(graphene.ObjectType):
    introduceRole = IntroduceRole.Field()
