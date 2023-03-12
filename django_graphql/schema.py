import graphene
from graphene_django import DjangoObjectType
from books.models import Books, Category


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "name", "author", "category")


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "books")


class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_books(root, info):
        return Books.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

