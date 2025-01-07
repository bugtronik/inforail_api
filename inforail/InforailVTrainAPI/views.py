from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SpErametVtrainMini
from .serializers import SpErametVtrainMiniSerializer
from django.core.paginator import Paginator, EmptyPage

@api_view(['GET', 'POST'])
def trains(request):
    
    trains = SpErametVtrainMini.objects.raw(
        """SELECT ID_MEGA_TRAIN,
                  [NUMERO_TRAIN]
                  ,[CATEGORIE_TRAIN]
                  ,FORMAT(REAL_DT_FROM, 'yyyy-MM-dd') AS "REAL_DT_FROM"
                  ,FORMAT([REAL_DT_TO], 'yyyy-MM-dd') AS "REAL_DT_TO"
            	  ,FORMAT([REAL_DT_FROM], 'HH:mm') AS "[REAL_DT_FROM"
            	  ,FORMAT([REAL_DT_TO], 'HH:mm') AS "REAL_DT_TO"
                  ,[REAL_TEMPS_PARC_H_EN_CANTON]
                  ,[REAL_TEMPS_PARC_H_EN_GARE]
            FROM [tcs].[SP_ERAMET_VTRAIN_MINI]
            WHERE CATEGORIE_TRAIN IN ('Voyageurs express', 'Voyageurs omnibus')
            AND FORMAT(REAL_DT_TO, 'yyyy-MM-dd') BETWEEN '2024-12-01' AND '2024-12-31'
            """
    )
    
    perpage = request.query_params.get('perpage', default=20)
    page = request.query_params.get('page', default=1)
    paginator = Paginator(trains,per_page=perpage)
    try:
        trains = paginator.page(number=page)
    except EmptyPage:
        trains = []
    serialized_trains = SpErametVtrainMiniSerializer(trains, many=True)
    return Response(serialized_trains.data)