from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SpErametRefVehiculesMini, SpErametVtrainSegmentMini, SpErametVwagon
from .serializers import SpErametRefVehiculesMiniSerializer, SpErametVtrainSegmentMiniSerializer, SpErametVwagonSerializer
from django.core.paginator import Paginator, EmptyPage

@api_view(['GET'])
def tcs(request):
    
    tcs = SpErametVtrainSegmentMini.objects.raw(
        """SELECT *
            FROM [tcs].[SP_ERAMET_VTRAIN_SEGMENT_MINI] AS VSM
            WHERE FORMAT(VSM.JOUR_SETRAG, 'yyyy-MM-dd') BETWEEN '2025-01-01' AND '2025-01-02';
        """
    )
    perpage = request.query_params.get('perpage', default=20)
    page = request.query_params.get('page', default=1)
    paginator = Paginator(tcs,per_page=perpage)
    try:
        tcs = paginator.page(number=page)
    except EmptyPage:
        tcs = []
    serialized_tcs = SpErametVtrainSegmentMiniSerializer(tcs, many=True)
    print(serialized_tcs.data)
    return Response(serialized_tcs.data)