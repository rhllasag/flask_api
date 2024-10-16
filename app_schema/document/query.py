import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel

class Department(MongoengineObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (Node,)
        
class Role(MongoengineObjectType):
    class Meta:
        model = RoleModel
        interfaces = (Node,)

class Employee(MongoengineObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (Node,)    
            
    
class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(Employee)
    all_role = MongoengineConnectionField(Role)
    role = graphene.Field(Role)