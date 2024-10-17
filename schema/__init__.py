import graphene
from .query import Query
from .query import Department
from .query import Employee
from .query import Role
from .mutation import Mutation
# Combining Query and Mutation into a single schema
schema = graphene.Schema(query=Query, mutation=Mutation, types=[Department, Employee, Role])