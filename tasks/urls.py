from django.urls import path
from tasks.schema import schema
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
