from rest_framework import serializers

class SpErametRefVehiculesMiniSerializer(serializers.Serializer):
    id_vehicule = serializers.IntegerField()
    numero_train = serializers.CharField()
    macro_type = serializers.CharField(max_length=200)  # Field name made lowercase.
    type = serializers.CharField(max_length=200)  # Field name made lowercase.
    proprietaire = serializers.CharField(max_length=200)  # Field name made lowercase.
    commentaire = serializers.CharField(max_length=200)  # Field name made lowercase.
    active = serializers.BooleanField()  # Field name made lowercase.
    created_by = serializers.CharField(max_length=50)  # Field name made lowercase.
    created_utc = serializers.DateTimeField()  # Field name made lowercase.
    modified_by = serializers.CharField(max_length=50)  # Field name made lowercase.
    modified_utc = serializers.DateTimeField()  # Field name made lowercase.
    
class SpErametVtrainSegmentMiniSerializer(serializers.Serializer):
    id_mega_train = serializers.FloatField()  # Field name made lowercase.
    numero_train = serializers.CharField(max_length=200)  # Field name made lowercase.
    seq = serializers.FloatField()  # Field name made lowercase.
    gare_ou_canton = serializers.CharField(max_length=200)  # Field name made lowercase.
    statut = serializers.CharField(max_length=200)  # Field name made lowercase.
    dt_from = serializers.DateTimeField()  # Field name made lowercase.
    dt_to = serializers.DateTimeField()  # Field name made lowercase.
    distance_parcourue = serializers.FloatField()  # Field name made lowercase.
    temps_traversee_en_h = serializers.FloatField()  # Field name made lowercase.
    poste_setrag = serializers.CharField(max_length=200)  # Field name made lowercase.
    jour_setrag = serializers.DateTimeField()  # Field name made lowercase.
    nombre_wagons = serializers.FloatField()  # Field name made lowercase.
    tonnage_brut = serializers.FloatField()  # Field name made lowercase.
    longueur_m = serializers.FloatField()  # Field name made lowercase.
    nombre_wagons_vides = serializers.FloatField()  # Field name made lowercase.
    nombre_wagons_pleins = serializers.FloatField()  # Field name made lowercase.
    dernier_wagon = serializers.CharField(max_length=100)  # Field name made lowercase.
    all_locomotives = serializers.CharField(max_length=200)  # Field name made lowercase.
    id_segment = serializers.FloatField()  # Field name made lowercase.
    
class SpErametVwagonSerializer(serializers.Serializer):
    rr_vehiclenumber = serializers.CharField(max_length=200)  # Field name made lowercase.
    rp_id_mega_train = serializers.FloatField()
    donnee_active_oui_non = serializers.CharField(max_length=200)
    rp_numero_train = serializers.CharField(max_length=200)
    rp_sens = serializers.CharField(max_length=200)
    type_ligne = serializers.CharField(max_length=200)
    rp_seq_min = serializers.IntegerField()
    rp_gare_ou_canton_min = serializers.CharField(max_length=200)
    rp_dt_from_min = serializers.DateTimeField()
    rp_seq_max = serializers.IntegerField()
    rp_gare_ou_canton_max = serializers.CharField(max_length=200)
    rp_dt_to_max = serializers.DateTimeField()
    rr_max_product = serializers.CharField(max_length=200)
    rr_max_recipient = serializers.CharField(max_length=200)
    rr_max_weight = serializers.FloatField()
    indic_1_temps_du_trajet_en_h = serializers.FloatField()
    indic_2_temps_en_canton_du_trajet_en_h = serializers.FloatField()
    indic_3_distance_du_trajet_en_km = serializers.FloatField()
    indic_4_vitesse_moyenne_du_trajet = serializers.FloatField()
    indic_5_temps_attente_en_h_avec_trajet_precedent = serializers.FloatField()
    indic_6_temps_attente_en_h_avec_trajet_suivant = serializers.FloatField()
    indic_7_temps_rotation_en_h_avec_trajet_precedent_meme_sens = serializers.FloatField()
    indic_8_temps_rotation_en_h_avec_trajet_suivant_meme_sens = serializers.FloatField()
    indic_numero_20 = serializers.FloatField()
    indic_numero_21 = serializers.FloatField()
    indic_numero_22 = serializers.FloatField()
    indic_numero_23 = serializers.FloatField()
    indic_numero_24 = serializers.FloatField()
    indic_numero_25 = serializers.FloatField()
    indic_numero_26 = serializers.FloatField()
    indic_numero_27 = serializers.FloatField()
    indic_numero_28 = serializers.FloatField()
    indic_numero_29 = serializers.FloatField()
    indic_numero_30 = serializers.FloatField()
    indic_numero_31 = serializers.FloatField()
    indic_numero_32 = serializers.FloatField()
    indic_numero_33 = serializers.FloatField()
    indic_numero_34 = serializers.FloatField()
    indic_numero_35 = serializers.FloatField()
    id_mega_train_trajet_precedent = serializers.FloatField()
    rp_numero_train_trajet_precedent = serializers.CharField(max_length=200)
    rp_seq_min_trajet_precedent = serializers.IntegerField()
    rp_gare_ou_canton_min_trajet_precedent = serializers.CharField(max_length=200)
    rp_dt_from_min_trajet_precedent = serializers.DateTimeField()
    rp_seq_max_trajet_precedent = serializers.IntegerField()
    rp_gare_ou_canton_max_trajet_precedent = serializers.CharField(max_length=200)
    rp_dt_to_max_trajet_precedent = serializers.DateTimeField()
    id_mega_train_trajet_suivant = serializers.FloatField()
    rp_numero_train_trajet_suivant = serializers.CharField(max_length=200)
    rp_seq_min_trajet_suivant = serializers.IntegerField()
    rp_gare_ou_canton_min_trajet_suivant = serializers.CharField(max_length=200)
    rp_dt_from_min_trajet_suivant = serializers.DateTimeField()
    rp_seq_max_trajet_suivant = serializers.IntegerField()
    rp_gare_ou_canton_max_trajet_suivant = serializers.CharField(max_length=200)
    rp_dt_to_max_trajet_suivant = serializers.DateTimeField()
    id_mega_train_trajet_precedent_meme_sens = serializers.FloatField()
    rp_numero_train_trajet_precedent_meme_sens = serializers.CharField(max_length=200)
    rp_seq_min_trajet_precedent_meme_sens = serializers.IntegerField()
    rp_gare_ou_canton_min_trajet_precedent_meme_sens = serializers.CharField(max_length=200)
    rp_dt_from_min_trajet_precedent_meme_sens = serializers.DateTimeField()
    rp_seq_max_trajet_precedent_meme_sens = serializers.IntegerField()
    rp_gare_ou_canton_max_trajet_precedent_meme_sens = serializers.CharField(max_length=200)
    rp_dt_to_max_trajet_precedent_meme_sens = serializers.DateTimeField()
    id_mega_train_trajet_suivant_meme_sens = serializers.FloatField()
    rp_numero_train_trajet_suivant_meme_sens = serializers.CharField(max_length=200)
    rp_seq_min_trajet_suivant_meme_sens = serializers.IntegerField()
    rp_gare_ou_canton_min_trajet_suivant_meme_sens = serializers.CharField(max_length=200)
    rp_dt_from_min_trajet_suivant_meme_sens = serializers.DateTimeField()
    rp_seq_max_trajet_suivant_meme_sens = serializers.IntegerField()
    rp_gare_ou_canton_max_trajet_suivant_meme_sens = serializers.CharField(max_length=200)
    rp_dt_to_max_trajet_suivant_meme_sens = serializers.DateTimeField()
    question_data_1_ubiquite = serializers.CharField(max_length=200, )
    question_data_2_discontinuite_dans_les_gares = serializers.CharField(max_length=200)
    question_data_3_temps_retournement_trop_court = serializers.CharField(max_length=200)
    question_data_4_non_alternance_pair_impair = serializers.CharField(max_length=200)
    question_data_numero_10 = serializers.CharField(max_length=200)
    question_data_numero_11 = serializers.CharField(max_length=200)
    question_data_numero_12 = serializers.CharField(max_length=200)
    question_data_numero_13 = serializers.CharField(max_length=200)
    question_data_numero_14 = serializers.CharField(max_length=200)
    question_data_numero_15 = serializers.CharField(max_length=200)
    question_data_numero_16 = serializers.CharField(max_length=200)
    question_data_numero_17 = serializers.CharField(max_length=200)
    question_data_numero_18 = serializers.CharField(max_length=200)
    question_data_numero_19 = serializers.CharField(max_length=200)
    question_data_numero_20 = serializers.CharField(max_length=200)
    commentaire = serializers.CharField(max_length=400)
    creation_date = serializers.DateTimeField()
    statut_du_trajet_du_vehicule = serializers.CharField(max_length=50)