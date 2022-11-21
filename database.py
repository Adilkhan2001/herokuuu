import psycopg2


# Connection
# conn = psycopg2.connect(user = "postgres", password = "Gre_Database_1963_@", host = "localhost", port = "5432", database = "assignment2")
conn = psycopg2.connect("postgres://admin:Vg73NQVC8q7aKSxz2h1TSdaDn5js6lJZ@dpg-cdtjkc1a6gdu24a3t650-a.oregon-postgres.render.com/assignment2_2y3p")

cursor = conn.cursor()
    
# CREATE
def add_country(country_cname, country_population):
    record = (country_cname, country_population)
    query = '''INSERT INTO public.country("cname", "population") VALUES (%s, %s)'''
    cursor.execute(query,record)
    conn.commit()

def add_disease_type(DT_id, DT_description):
    record = (DT_id, DT_description)
    query = '''INSERT INTO public.diseasetype("id", "description") VALUES (%s, %s)'''
    cursor.execute(query,record)
    conn.commit()

def add_disease(D_diseaseCode, D_pathogen, D_description, D_id):
    record = (D_diseaseCode, D_pathogen, D_description, D_id)
    query = '''INSERT INTO public.disease("diseaseCode", "pathogen", "description", "id") VALUES (%s, %s, %s, %s)'''
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

def add_discover(DS_cname, DS_disease_code, DS_date):
    record = (DS_cname, DS_disease_code, DS_date)
    query = '''INSERT INTO public.discover("cname", "diseaseCode", "firstEncDate") VALUES (%s, %s, %s)'''
    a = 0
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

def add_user(U_email, U_name, U_surname, U_salary, U_phone, U_cname):
    record = (U_email, U_name, U_surname, U_salary, U_phone, U_cname)
    query = '''INSERT INTO public.users("email", "name", "surname", "salary", "phone", "cname") VALUES (%s, %s, %s, %s, %s, %s)'''
    a = 0
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

def add_doctor(DC_email, DC_degree):
    record = (DC_email, DC_degree)
    query = '''INSERT INTO public.doctor("email", "degree") VALUES (%s, %s)'''
    a = 0
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

def add_specialization(S_id, S_email):
    record = (S_id, S_email)
    query = '''INSERT INTO public.specialize("id", "email") VALUES (%s, %s)'''
    a = 0
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

def add_ps(PS_email, PS_department):
    record = (PS_email, PS_department)
    query = '''INSERT INTO public.publicservant("email", "department") VALUES (%s, %s)'''
    a = 0
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

def add_rec(R_email, R_cname, R_dc, R_td, R_tp):
    record = (R_email, R_cname, R_dc, R_td, R_tp)
    query = '''INSERT INTO public.record("email", "cname", "diseaseCode", "totalDeaths", "totalPatients") VALUES (%s, %s, %s, %s, %s)'''
    a = 0
    try:
        cursor.execute(query,record)
        a=1
    except:
        conn.rollback()
        a = -1
    conn.commit()
    return a

# READ

def view_country():
    cursor.execute('''SELECT * FROM public.country''')
    res = cursor.fetchall()
    return res

def view_dt():
    cursor.execute('''SELECT * FROM public.diseasetype ORDER BY id ASC''')
    res = cursor.fetchall()
    return res

def view_d():
    cursor.execute('''SELECT * FROM public.disease''')
    res = cursor.fetchall()
    return res

def view_ds():
    cursor.execute('''SELECT * FROM public.discover''')
    res = cursor.fetchall()
    return res

def view_u():
    cursor.execute('''SELECT * FROM public.users''')
    res = cursor.fetchall()
    return res

def view_dc():
    cursor.execute('''SELECT * FROM public.doctor''')
    res = cursor.fetchall()
    return res

def view_s():
    cursor.execute('''SELECT * FROM public.specialize''')
    res = cursor.fetchall()
    return res

def view_ps():
    cursor.execute('''SELECT * FROM public.publicservant''')
    res = cursor.fetchall()
    return res

def view_r():
    cursor.execute('''SELECT * FROM public.record''')
    res = cursor.fetchall()
    return res

# UPDATE

def get_country(country):
    record = (country,)
    query = ''' SELECT * FROM public.country WHERE cname = %s'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_country(old_country_cname,new_country_population):
    record = (new_country_population, old_country_cname)
    query = '''  UPDATE public.country SET population = %s WHERE cname = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_dt(selected_dt):
    record = (selected_dt,)
    query = ''' SELECT * FROM public.diseasetype WHERE id = %s ORDER BY id ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_dt(old_dt_id, DT_description):
    record = (DT_description, old_dt_id)
    query = '''  UPDATE public.diseasetype SET description = %s WHERE id = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_d(selected_d):
    record = (selected_d,)
    query = ''' SELECT * FROM public.disease D WHERE D."diseaseCode" = %s ORDER BY D."diseaseCode" ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_d(old_d_disease_code, D_pathogen, D_description, D_id):
    record = ( D_pathogen, D_description, D_id, old_d_disease_code)
    query = '''  UPDATE public.disease SET "pathogen" = %s, "description" = %s, "id" = %s WHERE "diseaseCode" = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_ds(country, dc):
    record = (country, dc)
    query = ''' SELECT * FROM public.discover DS WHERE DS."cname" = %s AND DS."diseaseCode" = %s ORDER BY DS."cname" ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_discover(old_ds_cname, old_ds_dc, DS_date):
    record = ( DS_date, old_ds_cname, old_ds_dc)
    query = '''  UPDATE public.discover SET "firstEncDate" = %s WHERE "cname" = %s AND "diseaseCode" = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_d(selected_u):
    record = (selected_u,)
    query = ''' SELECT * FROM public.users WHERE email = %s ORDER BY email ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_user(old_email, U_name, U_surname, U_salary, U_phone, U_cname):
    record = (U_name, U_surname, U_salary, U_phone, U_cname, old_email)
    query = '''  UPDATE public.users SET "name" = %s, "surname" = %s, "salary" = %s, "phone" = %s, "cname" = %s WHERE "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_dc(selected_dc):
    record = (selected_dc,)
    query = ''' SELECT * FROM public.doctor WHERE email = %s ORDER BY email ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_doctor(old_email, DC_degree):
    record = ( DC_degree, old_email )
    query = '''  UPDATE public.doctor SET "degree" = %s WHERE "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_s(id, email):
    record = (email, id)
    query = ''' SELECT * FROM public.specialize WHERE email = %s AND id = %s ORDER BY id ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_specialization(old_id, old_email, S_id, S_email):
    record = (S_id, S_email, old_id, old_email )
    query = '''  UPDATE public.specialize SET "id" = %s, "email" = %s WHERE "id" = %s AND "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_ps(selected_ps):
    record = (selected_ps,)
    query = ''' SELECT * FROM public.publicservant WHERE email = %s ORDER BY email ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def updated_ps(PS_email, PS_department, old_email):
    record = (PS_email, PS_department, old_email )
    query = '''  UPDATE public.publicservant SET "email" = %s, "department" = %s WHERE "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def get_r(email, name, dc):
    record = (email, name, dc)
    query = ''' SELECT * FROM public.record WHERE "email" = %s AND "cname" = %s AND "diseaseCode" = %s ORDER BY "email" ASC'''
    cursor.execute(query, record)
    res = cursor.fetchall()
    return res
def update_rec(R_email, R_cname, R_dc, R_td, R_tp, old_rec_email, old_rec_cname, old_rec_dc):
    record = ( R_email, R_cname, R_dc, R_td, R_tp, old_rec_email, old_rec_cname, old_rec_dc )
    query = '''  UPDATE public.record SET "email" = %s, "cname" = %s, "diseaseCode" = %s, "totalDeaths" = %s, "totalPatients" = %s WHERE "email" = %s AND "cname" = %s AND "diseaseCode" = %s '''
    cursor.execute(query, record)
    conn.commit()

# DELETE

def del_country(selected_country):
    record = ( selected_country, )
    query = '''  DELETE FROM public.country WHERE "cname" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_dt(selected_dt):
    record = ( selected_dt, )
    query = '''  DELETE FROM public.diseasetype WHERE "id" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_disease(selected_d):
    record = ( selected_d, )
    query = '''  DELETE FROM public.disease WHERE "diseaseCode" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_discover(cname, dc):
    record = ( cname, dc )
    query = '''  DELETE FROM public.discover WHERE "cname" = %s AND "diseaseCode" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_user(selected_u):
    record = ( selected_u, )
    query = '''  DELETE FROM public.users WHERE "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_doc(selected_dc):
    record = ( selected_dc, )
    query = '''  DELETE FROM public.doctor WHERE "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_spec(id, email):
    record = ( id, email )
    query = '''  DELETE FROM public.specialize WHERE "id" = %s AND "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_ps(selected_ps):
    record = ( selected_ps, )
    query = '''  DELETE FROM public.publicservant WHERE "email" = %s '''
    cursor.execute(query, record)
    conn.commit()

def del_rec(email, cnanme, dc):
    record = ( email, cnanme, dc )
    query = '''  DELETE FROM public.record WHERE "email" = %s AND "cname" = %s AND "diseaseCode" = %s '''
    cursor.execute(query, record)
    conn.commit()