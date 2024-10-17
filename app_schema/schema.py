import graphene
from .document import Mutation as SchemeMutation, Query as SchemeQuery
from .document import Department, Role, Employee

class Mutation(SchemeMutation,graphene.ObjectType):
    pass

class Query(SchemeQuery,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Department, Employee, Role])