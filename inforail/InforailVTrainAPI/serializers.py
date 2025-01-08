from rest_framework import serializers

class SpErametVtrainMiniSerializer(serializers.Serializer):
    id_mega_train = serializers.FloatField()  # Field name made lowercase.
    numero_train = serializers.CharField(max_length=200)  # Field name made lowercase.
    categorie_train = serializers.CharField(max_length=200)  # Field name made lowercase.
    sens = serializers.CharField(max_length=200)  # Field name made lowercase.
    situation_du_train = serializers.CharField(max_length=200)  # Field name made lowercase.
    gare_ou_canton_from = serializers.CharField(max_length=200)  # Field name made lowercase.
    gare_ou_canton_to = serializers.CharField(max_length=200)  # Field name made lowercase.
    real_dt_from = serializers.DateTimeField()  # Field name made lowercase.
    real_dt_to = serializers.DateTimeField()  # Field name made lowercase.
    real_temps_parc_h_en_canton = serializers.FloatField()  # Field name made lowercase.
    real_temps_parc_h_en_gare = serializers.FloatField()  # Field name made lowercase.
