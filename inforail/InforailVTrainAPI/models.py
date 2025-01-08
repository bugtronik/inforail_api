# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SpErametVtrain(models.Model):
    version_from = models.DateTimeField(db_column='VERSION_FROM', blank=True, null=True)  # Field name made lowercase.
    version_to = models.DateTimeField(db_column='VERSION_TO', blank=True, null=True)  # Field name made lowercase.
    is_current = models.CharField(db_column='IS_CURRENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN', blank=True, null=True)  # Field name made lowercase.
    numero_train = models.CharField(db_column='NUMERO_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dt_from = models.DateTimeField(db_column='DT_FROM', blank=True, null=True)  # Field name made lowercase.
    dt_to = models.DateTimeField(db_column='DT_TO', blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_from = models.CharField(db_column='GARE_OU_CANTON_FROM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_to = models.CharField(db_column='GARE_OU_CANTON_TO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_to_or_destination = models.CharField(db_column='GARE_OU_CANTON_TO_OR_DESTINATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sens = models.CharField(db_column='SENS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    categorie_train = models.CharField(db_column='CATEGORIE_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    situation_du_train = models.CharField(db_column='SITUATION_DU_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locomotive = models.CharField(db_column='LOCOMOTIVE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    real_dt_from = models.DateTimeField(db_column='REAL_DT_FROM', blank=True, null=True)  # Field name made lowercase.
    real_dt_to = models.DateTimeField(db_column='REAL_DT_TO', blank=True, null=True)  # Field name made lowercase.
    real_gare_ou_canton_from = models.CharField(db_column='REAL_GARE_OU_CANTON_FROM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    real_gare_ou_canton_to = models.CharField(db_column='REAL_GARE_OU_CANTON_TO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    real_distance_parcourue_tot = models.FloatField(db_column='REAL_DISTANCE_PARCOURUE_TOT', blank=True, null=True)  # Field name made lowercase.
    real_temps_parc_h_en_canton = models.FloatField(db_column='REAL_TEMPS_PARC_H_EN_CANTON', blank=True, null=True)  # Field name made lowercase.
    real_temps_parc_h_en_gare = models.FloatField(db_column='REAL_TEMPS_PARC_H_EN_GARE', blank=True, null=True)  # Field name made lowercase.
    real_temps_attente_h_en_gare = models.FloatField(db_column='REAL_TEMPS_ATTENTE_H_EN_GARE', blank=True, null=True)  # Field name made lowercase.
    real_temps_expedit_h_en_gare = models.FloatField(db_column='REAL_TEMPS_EXPEDIT_H_EN_GARE', blank=True, null=True)  # Field name made lowercase.
    distance_a_parcourir = models.FloatField(db_column='DISTANCE_A_PARCOURIR', blank=True, null=True)  # Field name made lowercase.
    comilog_dt_from = models.DateTimeField(db_column='COMILOG_DT_FROM', blank=True, null=True)  # Field name made lowercase.
    comilog_dt_to = models.DateTimeField(db_column='COMILOG_DT_TO', blank=True, null=True)  # Field name made lowercase.
    all_locomotives = models.CharField(db_column='ALL_LOCOMOTIVES', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN'


class SpErametVtrainMetaDonnees(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_mega_train = models.IntegerField(db_column='Id_Mega_Train')  # Field name made lowercase.
    id_mega_train_precedent = models.IntegerField(db_column='Id_Mega_Train_Precedent', blank=True, null=True)  # Field name made lowercase.
    id_mega_train_suivant = models.IntegerField(db_column='Id_Mega_Train_Suivant', blank=True, null=True)  # Field name made lowercase.
    releve_a_renseigner = models.BooleanField(db_column='Releve_A_Renseigner')  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50)  # Field name made lowercase.
    createdutc = models.DateTimeField(db_column='CreatedUtc')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifiedutc = models.DateTimeField(db_column='ModifiedUtc', blank=True, null=True)  # Field name made lowercase.
    commentaire_releve = models.TextField(db_column='Commentaire_Releve', blank=True, null=True)  # Field name made lowercase.
    flipping_id = models.IntegerField(blank=True, null=True)
    trainjournalid = models.IntegerField(blank=True, null=True)
    date_mad_setrag_selon_comilog = models.DateTimeField(blank=True, null=True)
    temps_trajet_aller = models.FloatField(blank=True, null=True)
    temps_entre_1_et_2 = models.FloatField(blank=True, null=True)
    temps_trajet_retour = models.FloatField(blank=True, null=True)
    temps_entre_2_et_3 = models.FloatField(blank=True, null=True)
    temps_de_cycle = models.FloatField(blank=True, null=True)
    id_mega_train_suivant_n2 = models.IntegerField(blank=True, null=True)
    flipping_id_precedent = models.IntegerField(blank=True, null=True)
    trainjournalid_precedent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_META_DONNEES'


class SpErametVtrainMini(models.Model):
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN',primary_key=True)  # Field name made lowercase.
    numero_train = models.CharField(db_column='NUMERO_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    categorie_train = models.CharField(db_column='CATEGORIE_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sens = models.CharField(db_column='SENS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    situation_du_train = models.CharField(db_column='SITUATION_DU_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_from = models.CharField(db_column='GARE_OU_CANTON_FROM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_to = models.CharField(db_column='GARE_OU_CANTON_TO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    real_dt_from = models.DateTimeField(db_column='REAL_DT_FROM', blank=True, null=True)  # Field name made lowercase.
    real_dt_to = models.DateTimeField(db_column='REAL_DT_TO', blank=True, null=True)  # Field name made lowercase.
    real_temps_parc_h_en_canton = models.FloatField(db_column='REAL_TEMPS_PARC_H_EN_CANTON', blank=True, null=True)  # Field name made lowercase.
    real_temps_parc_h_en_gare = models.FloatField(db_column='REAL_TEMPS_PARC_H_EN_GARE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_MINI'


class SpErametVtrainMiniV2(models.Model):
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN', blank=True, null=True)  # Field name made lowercase.
    numero_train = models.TextField(db_column='NUMERO_TRAIN', blank=True, null=True)  # Field name made lowercase.
    categorie_train = models.TextField(db_column='CATEGORIE_TRAIN', blank=True, null=True)  # Field name made lowercase.
    sens = models.TextField(db_column='SENS', blank=True, null=True)  # Field name made lowercase.
    situation_du_train = models.TextField(db_column='SITUATION_DU_TRAIN', blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_from = models.TextField(db_column='GARE_OU_CANTON_FROM', blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_to = models.TextField(db_column='GARE_OU_CANTON_TO', blank=True, null=True)  # Field name made lowercase.
    real_dt_from = models.DateTimeField(db_column='REAL_DT_FROM', blank=True, null=True)  # Field name made lowercase.
    real_dt_to = models.DateTimeField(db_column='REAL_DT_TO', blank=True, null=True)  # Field name made lowercase.
    real_temps_parc_h_en_canton = models.FloatField(db_column='REAL_TEMPS_PARC_H_EN_CANTON', blank=True, null=True)  # Field name made lowercase.
    real_temps_parc_h_en_gare = models.FloatField(db_column='REAL_TEMPS_PARC_H_EN_GARE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_MINI_V2'


class SpErametVtrainSegment(models.Model):
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN', blank=True, null=True)  # Field name made lowercase.
    numero_train = models.CharField(db_column='NUMERO_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    version_from = models.DateTimeField(db_column='VERSION_FROM', blank=True, null=True)  # Field name made lowercase.
    version_to = models.DateTimeField(db_column='VERSION_TO', blank=True, null=True)  # Field name made lowercase.
    is_current = models.CharField(db_column='IS_CURRENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton = models.CharField(db_column='GARE_OU_CANTON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dt_from = models.DateTimeField(db_column='DT_FROM', blank=True, null=True)  # Field name made lowercase.
    dt_to = models.DateTimeField(db_column='DT_TO', blank=True, null=True)  # Field name made lowercase.
    locomotive = models.CharField(db_column='LOCOMOTIVE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(db_column='STATUT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trace = models.CharField(db_column='TRACE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    seq = models.FloatField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.
    distance_parc_totale = models.FloatField(db_column='DISTANCE_PARC_TOTALE', blank=True, null=True)  # Field name made lowercase.
    distance_parcourue = models.FloatField(db_column='DISTANCE_PARCOURUE', blank=True, null=True)  # Field name made lowercase.
    distance_parc_totale_canton = models.FloatField(db_column='DISTANCE_PARC_TOTALE_CANTON', blank=True, null=True)  # Field name made lowercase.
    distance_parcourue_canton = models.FloatField(db_column='DISTANCE_PARCOURUE_CANTON', blank=True, null=True)  # Field name made lowercase.
    temps_traversee_totale_en_h = models.FloatField(db_column='TEMPS_TRAVERSEE_TOTALE_EN_H', blank=True, null=True)  # Field name made lowercase.
    temps_traversee_en_h = models.FloatField(db_column='TEMPS_TRAVERSEE_EN_H', blank=True, null=True)  # Field name made lowercase.
    temps_traversee_canton_totale_en_h = models.FloatField(db_column='TEMPS_TRAVERSEE_CANTON_TOTALE_EN_H', blank=True, null=True)  # Field name made lowercase.
    temps_traversee_canton_en_h = models.FloatField(db_column='TEMPS_TRAVERSEE_CANTON_EN_H', blank=True, null=True)  # Field name made lowercase.
    expedition_dt_from = models.DateTimeField(db_column='EXPEDITION_DT_FROM', blank=True, null=True)  # Field name made lowercase.
    expedition_dt_to = models.DateTimeField(db_column='EXPEDITION_DT_TO', blank=True, null=True)  # Field name made lowercase.
    other_expeditions = models.CharField(db_column='OTHER_EXPEDITIONS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    elements_de_voie_parcourus = models.FloatField(db_column='ELEMENTS_DE_VOIE_PARCOURUS', blank=True, null=True)  # Field name made lowercase.
    max_ev_id_elm = models.FloatField(db_column='MAX_EV_ID_ELM', blank=True, null=True)  # Field name made lowercase.
    interactions_cnt = models.FloatField(db_column='INTERACTIONS_CNT', blank=True, null=True)  # Field name made lowercase.
    double_cnt = models.FloatField(db_column='DOUBLE_CNT', blank=True, null=True)  # Field name made lowercase.
    se_fait_doubler_cnt = models.FloatField(db_column='SE_FAIT_DOUBLER_CNT', blank=True, null=True)  # Field name made lowercase.
    croise_cnt = models.FloatField(db_column='CROISE_CNT', blank=True, null=True)  # Field name made lowercase.
    poste_setrag = models.CharField(db_column='POSTE_SETRAG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_segment = models.FloatField(db_column='ID_SEGMENT', blank=True, null=True)  # Field name made lowercase.
    nums_train_interaction = models.CharField(db_column='NUMS_TRAIN_INTERACTION', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ids_train_interaction = models.CharField(db_column='IDS_TRAIN_INTERACTION', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    jour_setrag = models.DateTimeField(db_column='JOUR_SETRAG', blank=True, null=True)  # Field name made lowercase.
    scenario_interaction = models.CharField(db_column='SCENARIO_INTERACTION', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    adherence_horaire_start_s = models.FloatField(db_column='ADHERENCE_HORAIRE_START_S', blank=True, null=True)  # Field name made lowercase.
    adherence_horaire_end_s = models.FloatField(db_column='ADHERENCE_HORAIRE_END_S', blank=True, null=True)  # Field name made lowercase.
    trace_tm_id_trm = models.FloatField(db_column='TRACE_TM_ID_TRM', blank=True, null=True)  # Field name made lowercase.
    sens = models.CharField(db_column='SENS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nombre_wagons = models.FloatField(db_column='NOMBRE_WAGONS', blank=True, null=True)  # Field name made lowercase.
    tonnage_brut = models.FloatField(db_column='TONNAGE_BRUT', blank=True, null=True)  # Field name made lowercase.
    longueur_m = models.FloatField(db_column='LONGUEUR_M', blank=True, null=True)  # Field name made lowercase.
    num_eot = models.FloatField(db_column='NUM_EOT', blank=True, null=True)  # Field name made lowercase.
    dernier_wagon = models.CharField(db_column='DERNIER_WAGON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_vides = models.FloatField(db_column='NOMBRE_WAGONS_VIDES', blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_pleins = models.FloatField(db_column='NOMBRE_WAGONS_PLEINS', blank=True, null=True)  # Field name made lowercase.
    all_locomotives = models.CharField(db_column='ALL_LOCOMOTIVES', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_SEGMENT'


class SpErametVtrainSegmentMini(models.Model):
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN', blank=True, null=True)  # Field name made lowercase.
    numero_train = models.CharField(db_column='NUMERO_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    seq = models.FloatField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton = models.CharField(db_column='GARE_OU_CANTON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(db_column='STATUT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dt_from = models.DateTimeField(db_column='DT_FROM', blank=True, null=True)  # Field name made lowercase.
    dt_to = models.DateTimeField(db_column='DT_TO', blank=True, null=True)  # Field name made lowercase.
    distance_parcourue = models.FloatField(db_column='DISTANCE_PARCOURUE', blank=True, null=True)  # Field name made lowercase.
    temps_traversee_en_h = models.FloatField(db_column='TEMPS_TRAVERSEE_EN_H', blank=True, null=True)  # Field name made lowercase.
    poste_setrag = models.CharField(db_column='POSTE_SETRAG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    jour_setrag = models.DateTimeField(db_column='JOUR_SETRAG', blank=True, null=True)  # Field name made lowercase.
    nombre_wagons = models.FloatField(db_column='NOMBRE_WAGONS', blank=True, null=True)  # Field name made lowercase.
    tonnage_brut = models.FloatField(db_column='TONNAGE_BRUT', blank=True, null=True)  # Field name made lowercase.
    longueur_m = models.FloatField(db_column='LONGUEUR_M', blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_vides = models.FloatField(db_column='NOMBRE_WAGONS_VIDES', blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_pleins = models.FloatField(db_column='NOMBRE_WAGONS_PLEINS', blank=True, null=True)  # Field name made lowercase.
    dernier_wagon = models.CharField(db_column='DERNIER_WAGON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    all_locomotives = models.CharField(db_column='ALL_LOCOMOTIVES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_segment = models.FloatField(db_column='ID_SEGMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_SEGMENT_MINI'
