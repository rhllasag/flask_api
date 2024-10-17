import graphene
#from .document import Mutation as SchemeMutation, Query as SchemeQuery
from .document import Query as SchemeQuery

#class Mutation(SchemeMutation,graphene.ObjectType):
#    pass
class Query(SchemeQuery,graphene.ObjectType):
    pass

#schema = graphene.Schema(query=Query, mutation=Mutation, types=[Department, Employee, Role])
#schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)