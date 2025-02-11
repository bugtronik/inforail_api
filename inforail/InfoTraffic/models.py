# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SpErametCodeEquipementGmao(models.Model):
    ordre_tri = models.IntegerField(db_column='ORDRE_TRI')  # Field name made lowercase.
    code_canton = models.TextField(db_column='CODE_CANTON', blank=True, null=True)  # Field name made lowercase.
    code_canton_ou_gare = models.TextField(db_column='CODE_CANTON_OU_GARE', blank=True, null=True)  # Field name made lowercase.
    canton = models.TextField(db_column='CANTON', blank=True, null=True)  # Field name made lowercase.
    code_equipement = models.TextField(db_column='CODE_EQUIPEMENT')  # Field name made lowercase.
    designation = models.TextField(db_column='DESIGNATION', blank=True, null=True)  # Field name made lowercase.
    pk_debut = models.TextField(db_column='PK_DEBUT', blank=True, null=True)  # Field name made lowercase.
    pk_fin = models.TextField(db_column='PK_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_CODE_EQUIPEMENT_GMAO'


class SpErametElementDeVoie(models.Model):
    ev_id_elm = models.IntegerField(db_column='EV_ID_ELM')  # Field name made lowercase.
    ev_nom_mac = models.CharField(db_column='EV_NOM_MAC', max_length=200)  # Field name made lowercase.
    ev_km_ini = models.DecimalField(db_column='EV_KM_INI', max_digits=6, decimal_places=3)  # Field name made lowercase.
    ev_km_fim = models.DecimalField(db_column='EV_KM_FIM', max_digits=6, decimal_places=3)  # Field name made lowercase.
    sens = models.CharField(db_column='SENS', max_length=200)  # Field name made lowercase.
    longueur_en_m = models.IntegerField(db_column='LONGUEUR_EN_M')  # Field name made lowercase.
    pk_milieu_de_l_element = models.DecimalField(db_column='PK_MILIEU_DE_L_ELEMENT', max_digits=6, decimal_places=3)  # Field name made lowercase.
    element_en_gare_ou_canton = models.CharField(db_column='ELEMENT_EN_GARE_OU_CANTON', max_length=200)  # Field name made lowercase.
    estacoes_es_id_efe = models.CharField(db_column='ESTACOES_ES_ID_EFE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gare_d_appartenance = models.CharField(db_column='GARE_D_APPARTENANCE', max_length=200)  # Field name made lowercase.
    pk_milieu_gare_ou_canton = models.DecimalField(db_column='PK_MILIEU_GARE_OU_CANTON', max_digits=6, decimal_places=3)  # Field name made lowercase.
    pk_lat_milieu_gare_ou_canton = models.DecimalField(db_column='PK_LAT_MILIEU_GARE_OU_CANTON', max_digits=18, decimal_places=9)  # Field name made lowercase.
    pk_lon_milieu_gare_ou_canton = models.DecimalField(db_column='PK_LON_MILIEU_GARE_OU_CANTON', max_digits=18, decimal_places=9)  # Field name made lowercase.
    gare_d_avant = models.CharField(db_column='GARE_D_AVANT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gare_d_apres = models.CharField(db_column='GARE_D_APRES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='COMMENTAIRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    ev_id_elm_px = models.IntegerField(db_column='EV_ID_ELM_PX', blank=True, null=True)  # Field name made lowercase.
    canton_d_avant = models.CharField(db_column='CANTON_D_AVANT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    canton_d_apres = models.CharField(db_column='CANTON_D_APRES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    num_sequence = models.IntegerField(db_column='NUM_SEQUENCE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_ELEMENT_DE_VOIE'


class SpErametGareOuCantonTcsOuInforail(models.Model):
    gare_ou_canton_tcs = models.CharField(db_column='GARE_OU_CANTON_TCS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gare_ou_canton_rv = models.CharField(db_column='GARE_OU_CANTON_rv', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_GARE_OU_CANTON_TCS_OU_INFORAIL'


class SpErametKpi01MonthlyOperations(models.Model):
    id_mega_train = models.IntegerField(blank=True, null=True)
    numero_train = models.CharField(max_length=100, blank=True, null=True)
    situation_du_train = models.CharField(max_length=100, blank=True, null=True)
    sens_du_train = models.CharField(max_length=100, blank=True, null=True)
    categorie_train = models.CharField(max_length=100, blank=True, null=True)
    date_depart_train = models.DateTimeField(blank=True, null=True)
    date_arrivee_train = models.DateTimeField(blank=True, null=True)
    temps_trajet_aller_n1 = models.FloatField(blank=True, null=True)
    temps_entre_1_et_2 = models.FloatField(blank=True, null=True)
    temps_trajet_aller_n2 = models.FloatField(blank=True, null=True)
    temps_entre_2_et_3 = models.FloatField(blank=True, null=True)
    temps_de_cycle = models.FloatField(blank=True, null=True)
    tonnage_transporte = models.FloatField(blank=True, null=True)
    nombre_de_wagons = models.IntegerField(blank=True, null=True)
    id_mega_train_plus_un = models.IntegerField(blank=True, null=True)
    numero_train_plus_un = models.IntegerField(blank=True, null=True)
    situation_du_train_plus_un = models.CharField(max_length=100, blank=True, null=True)
    sens_du_train_plus_un = models.CharField(max_length=100, blank=True, null=True)
    date_depart_train_plus_un = models.DateTimeField(blank=True, null=True)
    date_arrivee_train_plus_un = models.DateTimeField(blank=True, null=True)
    id_mega_train_plus_deux = models.IntegerField(blank=True, null=True)
    numero_train_plus_deux = models.CharField(max_length=100, blank=True, null=True)
    situation_du_train_plus_deux = models.CharField(max_length=100, blank=True, null=True)
    sens_du_train_plus_deux = models.CharField(max_length=100, blank=True, null=True)
    date_depart_train_plus_deux = models.DateTimeField(blank=True, null=True)
    date_arrivee_train_plus_deux = models.DateTimeField(blank=True, null=True)
    id_mega_train_moins_un = models.IntegerField(blank=True, null=True)
    numero_train_moins_un = models.CharField(max_length=100, blank=True, null=True)
    situation_du_train_moins_un = models.CharField(max_length=100, blank=True, null=True)
    sens_du_train_moins_un = models.CharField(max_length=100, blank=True, null=True)
    date_depart_train_moins_un = models.DateTimeField(blank=True, null=True)
    date_arrivee_train_moins_un = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    createdutc = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)
    modifiedutc = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_KPI_01_MONTHLY_OPERATIONS'


class SpErametRefVehiculesMini(models.Model):
    id_vehicule = models.IntegerField(db_column='ID_VEHICULE', blank=True, null=True)  # Field name made lowercase.
    nom_vehicule = models.CharField(db_column='NOM_VEHICULE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    macro_type = models.CharField(db_column='MACRO_TYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    proprietaire = models.CharField(db_column='PROPRIETAIRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    commentaire = models.TextField(db_column='Commentaire', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_utc = models.DateTimeField(db_column='CREATED_UTC', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='MODIFIED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_utc = models.DateTimeField(db_column='MODIFIED_UTC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_REF_VEHICULES_MINI'


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
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
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


class SpErametVtrainMetaDonneesJournalMavagha(models.Model):
    taskwagonid = models.IntegerField(blank=True, null=True)
    id_mega_train = models.IntegerField(blank=True, null=True)
    flipping_id = models.IntegerField(blank=True, null=True)
    type_wagon = models.CharField(max_length=100, blank=True, null=True)
    position_wagon = models.IntegerField(blank=True, null=True)
    position_wagon_corrigee = models.IntegerField(blank=True, null=True)
    numero_wagon = models.CharField(max_length=100, blank=True, null=True)
    nature_chargement = models.CharField(max_length=100, blank=True, null=True)
    poids_chargement = models.FloatField(blank=True, null=True)
    taskid = models.IntegerField(blank=True, null=True)
    taskname = models.CharField(max_length=100, blank=True, null=True)
    taskactiontype = models.CharField(max_length=100, blank=True, null=True)
    taskcode = models.CharField(max_length=100, blank=True, null=True)
    taskgroup = models.CharField(max_length=100, blank=True, null=True)
    tare_wagon = models.FloatField(blank=True, null=True)
    origine_chargement = models.CharField(max_length=100, blank=True, null=True)
    id_nature_chargement = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    createdutc = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)
    modifiedutc = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_META_DONNEES_JOURNAL_MAVAGHA'


class SpErametVtrainMini(models.Model):
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN', blank=True, null=True)  # Field name made lowercase.
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


class SpErametVtrainSituation(models.Model):
    id_mega_train = models.FloatField(db_column='ID_MEGA_TRAIN', blank=True, null=True)  # Field name made lowercase.
    numero_train = models.CharField(db_column='NUMERO_TRAIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dt_from = models.DateTimeField(db_column='DT_FROM', blank=True, null=True)  # Field name made lowercase.
    min_seq_situation = models.FloatField(db_column='MIN_SEQ_SITUATION', blank=True, null=True)  # Field name made lowercase.
    max_seq_situation = models.FloatField(db_column='MAX_SEQ_SITUATION', blank=True, null=True)  # Field name made lowercase.
    min_gare_ou_canton_situation = models.CharField(db_column='MIN_GARE_OU_CANTON_SITUATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    max_gare_ou_canton_situation = models.CharField(db_column='MAX_GARE_OU_CANTON_SITUATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_situation = models.FloatField(db_column='NOMBRE_WAGONS_SITUATION', blank=True, null=True)  # Field name made lowercase.
    tonnage_brut_situation = models.FloatField(db_column='TONNAGE_BRUT_SITUATION', blank=True, null=True)  # Field name made lowercase.
    longueur_m_situation = models.FloatField(db_column='LONGUEUR_M_SITUATION', blank=True, null=True)  # Field name made lowercase.
    num_eot_situation = models.FloatField(db_column='NUM_EOT_SITUATION', blank=True, null=True)  # Field name made lowercase.
    dernier_wagon_situation = models.CharField(db_column='DERNIER_WAGON_SITUATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_vides_situation = models.FloatField(db_column='NOMBRE_WAGONS_VIDES_SITUATION', blank=True, null=True)  # Field name made lowercase.
    nombre_wagons_pleins_situation = models.FloatField(db_column='NOMBRE_WAGONS_PLEINS_SITUATION', blank=True, null=True)  # Field name made lowercase.
    all_locomotives_situation = models.CharField(db_column='ALL_LOCOMOTIVES_SITUATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datasource = models.CharField(db_column='DATASOURCE', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VTRAIN_SITUATION'


class SpErametVwagon(models.Model):
    rr_vehiclenumber = models.CharField(db_column='rr_VehicleNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rp_id_mega_train = models.FloatField(blank=True, null=True)
    donnee_active_oui_non = models.CharField(max_length=200, blank=True, null=True)
    rp_numero_train = models.CharField(max_length=200, blank=True, null=True)
    rp_sens = models.CharField(max_length=200, blank=True, null=True)
    type_ligne = models.CharField(max_length=200, blank=True, null=True)
    rp_seq_min = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_min = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from_min = models.DateTimeField(blank=True, null=True)
    rp_seq_max = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_max = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_to_max = models.DateTimeField(blank=True, null=True)
    rr_max_product = models.CharField(max_length=200, blank=True, null=True)
    rr_max_recipient = models.CharField(max_length=200, blank=True, null=True)
    rr_max_weight = models.FloatField(blank=True, null=True)
    indic_1_temps_du_trajet_en_h = models.FloatField(blank=True, null=True)
    indic_2_temps_en_canton_du_trajet_en_h = models.FloatField(blank=True, null=True)
    indic_3_distance_du_trajet_en_km = models.FloatField(blank=True, null=True)
    indic_4_vitesse_moyenne_du_trajet = models.FloatField(blank=True, null=True)
    indic_5_temps_attente_en_h_avec_trajet_precedent = models.FloatField(blank=True, null=True)
    indic_6_temps_attente_en_h_avec_trajet_suivant = models.FloatField(blank=True, null=True)
    indic_7_temps_rotation_en_h_avec_trajet_precedent_meme_sens = models.FloatField(blank=True, null=True)
    indic_8_temps_rotation_en_h_avec_trajet_suivant_meme_sens = models.FloatField(blank=True, null=True)
    indic_numero_20 = models.FloatField(blank=True, null=True)
    indic_numero_21 = models.FloatField(blank=True, null=True)
    indic_numero_22 = models.FloatField(blank=True, null=True)
    indic_numero_23 = models.FloatField(blank=True, null=True)
    indic_numero_24 = models.FloatField(blank=True, null=True)
    indic_numero_25 = models.FloatField(blank=True, null=True)
    indic_numero_26 = models.FloatField(blank=True, null=True)
    indic_numero_27 = models.FloatField(blank=True, null=True)
    indic_numero_28 = models.FloatField(blank=True, null=True)
    indic_numero_29 = models.FloatField(blank=True, null=True)
    indic_numero_30 = models.FloatField(blank=True, null=True)
    indic_numero_31 = models.FloatField(blank=True, null=True)
    indic_numero_32 = models.FloatField(blank=True, null=True)
    indic_numero_33 = models.FloatField(blank=True, null=True)
    indic_numero_34 = models.FloatField(blank=True, null=True)
    indic_numero_35 = models.FloatField(blank=True, null=True)
    id_mega_train_trajet_precedent = models.FloatField(blank=True, null=True)
    rp_numero_train_trajet_precedent = models.CharField(max_length=200, blank=True, null=True)
    rp_seq_min_trajet_precedent = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_min_trajet_precedent = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from_min_trajet_precedent = models.DateTimeField(blank=True, null=True)
    rp_seq_max_trajet_precedent = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_max_trajet_precedent = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_to_max_trajet_precedent = models.DateTimeField(blank=True, null=True)
    id_mega_train_trajet_suivant = models.FloatField(blank=True, null=True)
    rp_numero_train_trajet_suivant = models.CharField(max_length=200, blank=True, null=True)
    rp_seq_min_trajet_suivant = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_min_trajet_suivant = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from_min_trajet_suivant = models.DateTimeField(blank=True, null=True)
    rp_seq_max_trajet_suivant = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_max_trajet_suivant = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_to_max_trajet_suivant = models.DateTimeField(blank=True, null=True)
    id_mega_train_trajet_precedent_meme_sens = models.FloatField(blank=True, null=True)
    rp_numero_train_trajet_precedent_meme_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_seq_min_trajet_precedent_meme_sens = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_min_trajet_precedent_meme_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from_min_trajet_precedent_meme_sens = models.DateTimeField(blank=True, null=True)
    rp_seq_max_trajet_precedent_meme_sens = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_max_trajet_precedent_meme_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_to_max_trajet_precedent_meme_sens = models.DateTimeField(blank=True, null=True)
    id_mega_train_trajet_suivant_meme_sens = models.FloatField(blank=True, null=True)
    rp_numero_train_trajet_suivant_meme_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_seq_min_trajet_suivant_meme_sens = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_min_trajet_suivant_meme_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from_min_trajet_suivant_meme_sens = models.DateTimeField(blank=True, null=True)
    rp_seq_max_trajet_suivant_meme_sens = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_max_trajet_suivant_meme_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_to_max_trajet_suivant_meme_sens = models.DateTimeField(blank=True, null=True)
    question_data_1_ubiquite = models.CharField(max_length=200, blank=True, null=True)
    question_data_2_discontinuite_dans_les_gares = models.CharField(max_length=200, blank=True, null=True)
    question_data_3_temps_retournement_trop_court = models.CharField(max_length=200, blank=True, null=True)
    question_data_4_non_alternance_pair_impair = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_10 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_11 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_12 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_13 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_14 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_15 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_16 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_17 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_18 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_19 = models.CharField(max_length=200, blank=True, null=True)
    question_data_numero_20 = models.CharField(max_length=200, blank=True, null=True)
    commentaire = models.CharField(max_length=400, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    statut_du_trajet_du_vehicule = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VWAGON'


class SpErametVwagonSegment(models.Model):
    rp_id_mega_train = models.FloatField(blank=True, null=True)
    rp_idtrainrelevevehicule = models.CharField(db_column='rp_IdTrainReleveVehicule', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rr_id_version_releve_vehicule = models.CharField(max_length=200, blank=True, null=True)
    rr_vehiclenumber = models.CharField(db_column='rr_VehicleNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    donnee_active_oui_non = models.CharField(max_length=200, blank=True, null=True)
    rp_seq = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton = models.CharField(max_length=200, blank=True, null=True)
    type_gare_ou_canton = models.CharField(max_length=200, blank=True, null=True)
    rp_numero_train = models.CharField(max_length=200, blank=True, null=True)
    rp_sens = models.CharField(max_length=200, blank=True, null=True)
    rp_statut = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from = models.DateTimeField(blank=True, null=True)
    rp_dt_to = models.DateTimeField(blank=True, null=True)
    rp_distance_parcourue = models.FloatField(blank=True, null=True)
    rp_temps_traversee_en_h = models.FloatField(blank=True, null=True)
    rp_poste_setrag = models.CharField(max_length=200, blank=True, null=True)
    rp_jour_setrag = models.DateTimeField(blank=True, null=True)
    rp_id_segment = models.FloatField(blank=True, null=True)
    rr_rang_du_releve = models.IntegerField(blank=True, null=True)
    rr_id_releve_vehicule = models.CharField(max_length=200, blank=True, null=True)
    rr_trainnumber = models.CharField(max_length=200, blank=True, null=True)
    rr_businessid_releve = models.CharField(db_column='rr_BusinessId_releve', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rr_station = models.CharField(max_length=200, blank=True, null=True)
    rr_gare_ou_canton_tcs = models.CharField(max_length=200, blank=True, null=True)
    rr_position = models.IntegerField(db_column='rr_Position', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(max_length=800, blank=True, null=True)
    rr_product = models.CharField(max_length=200, blank=True, null=True)
    rr_recipient = models.CharField(max_length=200, blank=True, null=True)
    rr_weight = models.FloatField(blank=True, null=True)
    rr_tareweight = models.FloatField(blank=True, null=True)
    rr_length = models.FloatField(blank=True, null=True)
    rp_seq_min = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_min = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_from_min = models.DateTimeField(blank=True, null=True)
    rp_seq_max = models.IntegerField(blank=True, null=True)
    rp_gare_ou_canton_max = models.CharField(max_length=200, blank=True, null=True)
    rp_dt_to_max = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SP_ERAMET_VWAGON_SEGMENT'
