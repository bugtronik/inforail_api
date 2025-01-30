from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AuthUsers
from .serializers import AuthUsersSerializer
from django.core.paginator import Paginator, EmptyPage

@api_view(['GET', 'POST'])
def users(request):
    users = AuthUsers.objects.raw(
        """select * from setrag.auth_users
        """
    )
    perpage = request.query_params.get('perpage', default=20)
    page = request.query_params.get('page', default=1)
    paginator = Paginator(users,per_page=perpage)
    try:
        users = paginator.page(number=page)
    except EmptyPage:
        users = []
    serialized_users = AuthUsersSerializer(users, many=True)
    print(serialized_users.data)
    return Response(serialized_users.data)