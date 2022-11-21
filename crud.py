import streamlit as st
import pandas as pd
import database as db

def main():
    st.title("CRUD operations")
    
    menu = ["Create", "Read", "Update", "Delete"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == 'Create':
        
        # Country V
        st.subheader("Add Country")
        county_cname_col, country_population_col = st.columns(2)
        with county_cname_col:
            county_cname = st.text_area("Country name")
        with country_population_col:
            country_population = st.text_area("Country population")
        if st.button("Add Country"):
            db.add_country(county_cname,country_population)
            st.success("New COUNTRY was successfully added: {}".format(county_cname))

        
        # Disease Type V
        st.subheader("Add Disease Type")
        DT_id_col, DT_description_col = st.columns(2)
        with DT_id_col:
            DT_id = st.text_area("Disease Type ID")
        with DT_description_col:
            DT_description = st.text_area("Disease Type description")
        if st.button("Add Disease Type"):
            db.add_disease_type(DT_id, DT_description)
            st.success("New DISEASE TYPE was successfully added: {}".format(DT_id))

        # Disease V

        st.subheader("Add Disease")
        st.text("Warning! Before adding new disease make sure that disease ID exists in Disease Type table!")

        D_disease_code_col, D_pathogen_col, D_description_col, D_id_col = st.columns(4)

        with D_disease_code_col:
            D_disease_code = st.text_area("Disease Code")
        with D_pathogen_col:
            D_pathogen = st.text_area("Disease Pathogen")
        with D_description_col:
            D_description = st.text_area("Disease Description")
        with D_id_col:
            D_id = st.text_area("Disease ID")

        if st.button("Add Disease"):
            db.add_disease(D_disease_code, D_pathogen, D_description, D_id)
            st.success("New DISEASE was successfully added: {}".format(D_disease_code))

    # Discover V
    st.subheader("Add Discover")
    st.text("Warning")
    DS_cname_col, DS_disease_code_col, DS_date_col = st.columns(3)
    with DS_cname_col:
        DS_cname = st.text_area("Discover Country")
    with DS_disease_code_col:
        DS_disease_code = st.text_area("Discover Disease Code")
    with DS_date_col:
         DS_date = st.date_input("First Encounter Date")
    
    if st.button("Add Discover"):
        db.add_discover(DS_cname, DS_disease_code, DS_date)
        st.success("New DISCOVER was successfully added: {}".format(DS_cname))
    
    # Users V
    st.subheader("Add User")
    U_email_col, U_name_col, U_surname_col, U_salary_col, U_phone_col, U_cname_col = st.columns(6)
    with U_email_col:
        U_email = st.text_area("User's Email")
    with U_name_col:
        U_name = st.text_area("User's Name")
    with U_surname_col:
        U_surname = st.text_area("User's Surname")
    with U_salary_col:
        U_salary = st.text_area("User's Salary")
    with U_phone_col:
        U_phone = st.text_area("User's Phone")
    with U_cname_col:
        U_cname = st.text_area("User's Country")

    if st.button("Add User"):
            db.add_user(U_email, U_name, U_surname, U_salary, U_phone, U_cname)
            st.success("New USER was successfully added: {}".format(U_name))

    # Doctor
    st.subheader("Add Doctor")
    DC_email_col, DC_degree_col = st.columns(2)
    with DC_email_col:
        DC_email = st.text_area("Doctor's Email")
    with DC_degree_col:
        DC_degree = st.text_area("Doctor's Degree")
    
    if st.button("Add Doctor"):
        db.add_doctor(DC_email, DC_degree)
        st.success("New DOCTOR was successfully added: {}".format(DC_email))

    # Specialize V
    st.subheader("Add Specialization")
    S_id_col, S_email_col = st.columns(2)
    with S_id_col:
        S_id = st.text_area("Specialization ID")
    with S_email_col:
        S_email = st.text_area("Specialization Email")
    
    if st.button("Add Specialization"):
        db.add_specialization(S_id, S_email)
        st.success("New SPECIALIZATION was successfully added!")
    
    # Public Servant V
    st.subheader("Add Public Servant")
    PS_email_col, PS_department_col = st.columns(2)
    with PS_email_col:
        PS_email = st.text_area("Public Servant's Email")
    with PS_department_col:
        PS_department = st.text_area("Public Servant's Department")
    
    if st.button("Add Public Servant"):
        db.add_ps(PS_email, PS_department)
        st.success("New Public Servant was successfully added: {}".format(PS_email))

    # Record V
    st.subheader("Add Record")
    R_col_email, R_col_cname, R_col_dc, R_col_td, R_col_tp = st.columns(5)
    with R_col_email:
        R_email = st.text_area("Record Email")
    with R_col_cname:
        R_cname = st.text_area("Record Country")
    with R_col_dc:
        R_dc = st.text_area("Record Disease Code")
    with R_col_td:
        R_td = st.text_area("Record Total Deaths")
    with R_col_tp:
        R_tp = st.text_area("Record Total Patients")
    
    if st.button("Add Record"):
        db.add_rec(R_email, R_cname, R_dc, R_td, R_tp)
        st.success("New Record was successfully added!")
    
    

    st.header("-------------------------------------------------------------")


    if choice == 'Read':
        st.header("View Data")

        # Country V
        res_c = db.view_country()
        with st.expander("View Country"):
            df = pd.DataFrame(res_c, columns=["Country Name", "Population"])
            st.dataframe(df)

        # Disease Type V

        res_dt = db.view_dt()
        with st.expander("View Disease Type"):
            df = pd.DataFrame(res_dt, columns=["ID", "Description"])
            st.dataframe(df)
        
        # Disease V
        res_d = db.view_d()
        with st.expander("View Disease"):
            df = pd.DataFrame(res_d, columns=["Disease Code", "Pathogen", "Description", "ID"])
            st.dataframe(df)

        # Discover V
        res_ds = db.view_ds()
        with st.expander("View Discover"):
            df = pd.DataFrame(res_ds, columns=["Country Name", "Disease Code", "First Encounter Date"])
            st.dataframe(df)

        # Users V
        res_u = db.view_u()
        with st.expander("View Users"):
            df = pd.DataFrame(res_u, columns=["Email", "Name", "Surname", "Salary", "Phone Number", "Country"])
            st.dataframe(df)

        # Doctor V
        res_dc = db.view_dc()
        with st.expander("View Doctors"):
            df = pd.DataFrame(res_dc, columns=["Email", "Degree"])
            st.dataframe(df)

        # Specialize V
        res_s = db.view_s()
        with st.expander("View Specialization"):
            df = pd.DataFrame(res_s, columns=["ID", "Email"])
            st.dataframe(df)

        # Public Servant V
        res_ps = db.view_ps()
        with st.expander("View Public Servant"):
            df = pd.DataFrame(res_ps, columns=["Email", "Department"])
            st.dataframe(df)
        
        # Record V
        res_r = db.view_r()
        with st.expander("View Record"):
            df = pd.DataFrame(res_r, columns=["Email", "Country", "Disease Code", "Total Deaths", "Total Patients"])
            st.dataframe(df)

    st.header("-------------------------------------------------------------")
    
    if choice == 'Update':
        st.subheader("Update Data")
    #  -----------------------
        
        st.subheader("Current Data")
        res_c = db.view_country()
        with st.expander("View Country"):
            df = pd.DataFrame(res_c, columns=["Country Name", "Population"])
            st.dataframe(df)

        # Disease Type V

        res_dt = db.view_dt()
        with st.expander("View Disease Type"):
            df = pd.DataFrame(res_dt, columns=["ID", "Description"])
            st.dataframe(df)
        
        # Disease V
        res_d = db.view_d()
        with st.expander("View Disease"):
            df = pd.DataFrame(res_d, columns=["Disease Code", "Pathogen", "Description", "ID"])
            st.dataframe(df)

        # Discover V
        res_ds = db.view_ds()
        with st.expander("View Discover"):
            df = pd.DataFrame(res_ds, columns=["Country Name", "Disease Code", "First Encounter Date"])
            st.dataframe(df)

        # Users V
        res_u = db.view_u()
        with st.expander("View Users"):
            df = pd.DataFrame(res_u, columns=["Email", "Name", "Surname", "Salary", "Phone Number", "Country"])
            st.dataframe(df)

        # Doctor V
        res_dc = db.view_dc()
        with st.expander("View Doctors"):
            df = pd.DataFrame(res_dc, columns=["Email", "Degree"])
            st.dataframe(df)

        # Specialize V
        res_s = db.view_s()
        with st.expander("View Specialization"):
            df = pd.DataFrame(res_s, columns=["ID", "Email"])
            st.dataframe(df)

        # Public Servant V
        res_ps = db.view_ps()
        with st.expander("View Public Servant"):
            df = pd.DataFrame(res_ps, columns=["Email", "Department"])
            st.dataframe(df)
        
        # Record V
        res_r = db.view_r()
        with st.expander("View Record"):
            df = pd.DataFrame(res_r, columns=["Email", "Country", "Disease Code", "Total Deaths", "Total Patients"])
            st.dataframe(df)

    #  -----------------------
        st.subheader("Update Country")
        country_list = [i[0] for i in db.view_country()]
        selected_country = st.selectbox("Country update", country_list)
        selected_res_country =  db.get_country(str(selected_country))
        if selected_res_country:
            old_country_cname = selected_res_country[0][0]
            old_country_population = selected_res_country[0][1]

            county_cname_col, country_population_col = st.columns(2)
            with county_cname_col:
                new_county_cname = st.text_area("Update Country name", old_country_cname)
            with country_population_col:
                new_country_population = st.text_area("Update Country population", old_country_population)
            if st.button("Update Country"):
                db.update_country(old_country_cname,new_country_population)
                st.success("COUNTRY <{}> was updated added!".format(old_country_cname))
    #  -----------------------
        st.subheader("Update Disease Type")
        dt_list = [i[0] for i in db.view_dt()]
        selected_dt = st.selectbox("Disease type update", dt_list)
        selected_res_dt = db.get_dt(selected_dt)
        
        if selected_res_dt:
            old_dt_id = selected_res_dt[0][0]
            old_dr_desc = selected_res_dt[0][1]
            DT_id_col, DT_description_col = st.columns(2)
            with DT_id_col:
                DT_id = st.text_area("Update Disease Type ID", old_dt_id)
            with DT_description_col:
                DT_description = st.text_area("Update Disease Type description", old_dr_desc)
            if st.button("Update Disease Type"):
                db.update_dt(old_dt_id, DT_description)
                st.success("DISEASE TYPE <{}> was successfully updated!".format(DT_id))
    #  -----------------------
        st.subheader("Update Disease")
        d_list = [i[0] for i in db.view_d()]
        selected_d = st.selectbox("Disease update", d_list)
        selected_res_d = db.get_d(selected_d)

        if selected_res_d:
            old_d_disease_code = selected_res_d[0][0]
            old_d_pathogen = selected_res_d[0][1]
            old_d_descriprion = selected_res_d[0][2]
            old_d_id = selected_res_d[0][3]

            D_disease_code_col, D_pathogen_col, D_description_col, D_id_col = st.columns(4)

            with D_disease_code_col:
                D_disease_code = st.text_area("Update Disease Code", old_d_disease_code)
            with D_pathogen_col:
                D_pathogen = st.text_area("Update Disease Pathogen", old_d_pathogen)
            with D_description_col:
                D_description = st.text_area("Update Disease Description", old_d_descriprion)
            with D_id_col:
                D_id = st.text_area("Disease ID", old_d_id)

            if st.button("Update Disease"):
                db.update_d(old_d_disease_code, D_pathogen, D_description, D_id)
                st.success("DISEASE <{}> was successfully updated!".format(D_disease_code))
        #  -----------------------
        st.subheader("Update Discover")
        ds_list = [i[0] for i in db.view_ds()]
        ds_list2 = [i[1] for i in db.view_ds()]
        ds_list3 = []
        for i in range(len(ds_list)):
            ds_list3.append((ds_list[i], ds_list2[i]))

        selected_ds = st.selectbox("Discover update", ds_list3)

        selected_res_ds = db.get_ds(str(selected_ds[0]), str(selected_ds[1])) 
        
        if selected_res_ds:
            old_ds_cname = selected_ds[0]
            old_ds_dc = selected_ds[1]
            DS_cname_col, DS_disease_code_col, DS_date_col = st.columns(3)
            with DS_cname_col:
                DS_cname = st.text_area("Update Discover Country", old_ds_cname)
            with DS_disease_code_col:
                DS_disease_code = st.text_area("Update Discover Disease Code", old_ds_dc)
            with DS_date_col:
                DS_date = st.date_input("Update First Encounter Date", )
            
            if st.button("Update Discover"):
                db.update_discover(old_ds_cname, old_ds_dc, DS_date)
                st.success("DISCOVER <{}, {}> was successfully updated!".format(old_ds_cname, old_ds_dc))
        #  -----------------------
        st.subheader("Update Users")
        u_list = [i[0] for i in db.view_u()]
        selected_u = st.selectbox("User's update", u_list)
        selected_res_u = db.get_d(selected_u)

        if selected_res_u:
            old_email = selected_res_u[0][0]
            U_email_col, U_name_col, U_surname_col, U_salary_col, U_phone_col, U_cname_col = st.columns(6)
            with U_email_col:
                U_email = st.text_area("User's Email", old_email)
            with U_name_col:
                U_name = st.text_area("Update User's Name")
            with U_surname_col:
                U_surname = st.text_area("Update User's Surname")
            with U_salary_col:
                U_salary = st.text_area("Update User's Salary")
            with U_phone_col:
                U_phone = st.text_area("Update User's Phone")
            with U_cname_col:
                U_cname = st.text_area("Update User's Country")

            if st.button("Update User"):
                db.update_user(old_email, U_name, U_surname, U_salary, U_phone, U_cname)
                st.success("USER <{}> was successfully updated".format(old_email))
        #  ----------------------------
        st.subheader("Update Doctor")
        dc_list = [i[0] for i in db.view_dc()]
        selected_dc = st.selectbox("Doctor's update", dc_list)
        selected_res_dc = db.get_dc(selected_dc)
        if selected_res_dc:
            old_email = selected_res_dc[0][0]
            DC_email_col, DC_degree_col = st.columns(2)
            with DC_email_col:
                DC_email = st.text_area("Update Doctor's Email",old_email)
            with DC_degree_col:
                DC_degree = st.text_area("Update Doctor's Degree", selected_res_dc[0][1])
    
            if st.button("Update Doctor"):
                db.update_doctor(old_email, DC_degree)
                st.success("DOCTOR <{}> was successfully updated!".format(old_email))
        #  ----------------------------
        st.subheader("Update Specialize")

        ds_list_s = [i[0] for i in db.view_s()]
        ds_list2_s = [i[1] for i in db.view_s()]
        ds_list3_s = []
        for i in range(len(ds_list_s)):
            ds_list3_s.append((ds_list_s[i], ds_list2_s[i]))

        selected_s = st.selectbox("Specialize update", ds_list3_s)

        selected_res_s = db.get_s(str(selected_s[0]), str(selected_s[1])) 

        if selected_res_s:
            S_id_col, S_email_col = st.columns(2)
            old_id = selected_res_s[0][0]
            old_email = selected_res_s[0][1]
            with S_id_col:
                S_id = st.text_area("Update Specialization ID", old_id)
            with S_email_col:
                S_email = st.text_area("Update Specialization Email", old_email)
            if st.button("Update Specialization"):
                db.update_specialization(old_id, old_email, S_id, S_email)
                st.success("SPECIALIZATION was successfully updated!")
            
        #  ----------------------------
        st.subheader("Update Public Servant")
        ps_list = [i[0] for i in db.view_ps()]
        selected_ps = st.selectbox("Public Servant's update", ps_list)
        selected_res_ps = db.get_ps(selected_ps)

        if selected_res_ps:
            old_email = selected_res_ps[0][0]
            PS_email_col, PS_department_col = st.columns(2)
            with PS_email_col:
                PS_email = st.text_area("Update Public Servant's Email", old_email)
            with PS_department_col:
                PS_department = st.text_area("Update Public Servant's Department", selected_res_ps[0][1])
            if st.button("Update Public Servant"):
                db.updated_ps(PS_email, PS_department, old_email)
                st.success("Public Servant <{}> was successfully updated!".format(old_email))
        #  ----------------------------
        st.subheader("Update Record")
        r_list_1 = [i[0] for i in db.view_r()]
        r_list_2 = [i[1] for i in db.view_r()]
        r_list_3 = [i[2] for i in db.view_r()]
        r_list_4 = []

        for i in range(len(r_list_1)):
            r_list_4.append((r_list_1[i], r_list_2[i], r_list_3[i]))

        selected_r = st.selectbox("Record update", r_list_4)
        selected_res_r = db.get_r(selected_r[0], selected_r[1], selected_r[2])

        if selected_res_r:
            R_col_email, R_col_cname, R_col_dc, R_col_td, R_col_tp = st.columns(5)
            old_rec_email = selected_res_r[0][0]
            old_rec_cname = selected_res_r[0][1]
            old_rec_dc = selected_res_r[0][2]

            with R_col_email:
                R_email = st.text_area("Update Record Email", old_rec_email)
            with R_col_cname:
                R_cname = st.text_area("Update Record Country", old_rec_cname)
            with R_col_dc:
                R_dc = st.text_area("Update Record Disease Code", old_rec_dc)
            with R_col_td:
                R_td = st.text_area("Update Record Total Deaths")
            with R_col_tp:
                R_tp = st.text_area("Update Record Total Patients")
            
    
        if st.button("Update Record"):
            db.update_rec(R_email, R_cname, R_dc, R_td, R_tp, old_rec_email, old_rec_cname, old_rec_dc)
            st.success("Record <{},{},{}> was successfully updated!".format(old_rec_email, old_rec_cname, old_rec_dc))
            
    st.header("-------------------------------------------------------------")


    if choice == 'Delete':
        st.subheader("Delete Data")

        st.subheader("Current Data")
        res_c = db.view_country()
        with st.expander("View Country"):
            df = pd.DataFrame(res_c, columns=["Country Name", "Population"])
            st.dataframe(df)

        # Disease Type V

        res_dt = db.view_dt()
        with st.expander("View Disease Type"):
            df = pd.DataFrame(res_dt, columns=["ID", "Description"])
            st.dataframe(df)
        
        # Disease V
        res_d = db.view_d()
        with st.expander("View Disease"):
            df = pd.DataFrame(res_d, columns=["Disease Code", "Pathogen", "Description", "ID"])
            st.dataframe(df)

        # Discover V
        res_ds = db.view_ds()
        with st.expander("View Discover"):
            df = pd.DataFrame(res_ds, columns=["Country Name", "Disease Code", "First Encounter Date"])
            st.dataframe(df)

        # Users V
        res_u = db.view_u()
        with st.expander("View Users"):
            df = pd.DataFrame(res_u, columns=["Email", "Name", "Surname", "Salary", "Phone Number", "Country"])
            st.dataframe(df)

        # Doctor V
        res_dc = db.view_dc()
        with st.expander("View Doctors"):
            df = pd.DataFrame(res_dc, columns=["Email", "Degree"])
            st.dataframe(df)

        # Specialize V
        res_s = db.view_s()
        with st.expander("View Specialization"):
            df = pd.DataFrame(res_s, columns=["ID", "Email"])
            st.dataframe(df)

        # Public Servant V
        res_ps = db.view_ps()
        with st.expander("View Public Servant"):
            df = pd.DataFrame(res_ps, columns=["Email", "Department"])
            st.dataframe(df)
        
        # Record V
        res_r = db.view_r()
        with st.expander("View Record"):
            df = pd.DataFrame(res_r, columns=["Email", "Country", "Disease Code", "Total Deaths", "Total Patients"])
            st.dataframe(df)


        # ----------------------------
        #  Country
        country_list = [i[0] for i in db.view_country()]
        selected_country = st.selectbox("Country delete", country_list)
        st.warning("Are you sure to delete country <{}> ?".format(selected_country))
        if st.button("Delete Country"):
            db.del_country(selected_country)
            st.success("<{}> was successfully deleted!".format(selected_country))
        
        # Disease Type
        dt_list = [i[0] for i in db.view_dt()]
        selected_dt = st.selectbox("Disease type delete", dt_list)
        st.warning("Are you sure to delete disease type <{}> ?".format(selected_dt))
        if st.button("Delete Disease Type"):
            db.del_dt(selected_dt)
            st.success("<{}> was successfully deleted!".format(selected_dt))
        # Disease
        d_list = [i[0] for i in db.view_d()]
        selected_d = st.selectbox("Disease delete", d_list)
        st.warning("Are you sure to delete disease type <{}> ?".format(selected_d))
        if st.button("Delete Disease"):
            db.del_disease(selected_d)
            st.success("<{}> was successfully deleted!".format(selected_d))
        # Discover
        ds_list = [i[0] for i in db.view_ds()]
        ds_list2 = [i[1] for i in db.view_ds()]
        ds_list3 = []
        for i in range(len(ds_list)):
            ds_list3.append((ds_list[i], ds_list2[i]))

        selected_ds = st.selectbox("Discover delete", ds_list3)

        st.warning("Are you sure to delete discover <{}> ?".format(selected_d))
        if st.button("Delete Discover"):
            db.del_discover(selected_ds[0], selected_ds[1])
            st.success("<{}> was successfully deleted!".format(selected_ds))

        # User
        u_list = [i[0] for i in db.view_u()]
        selected_u = st.selectbox("User's delete", u_list)
        st.warning("Are you sure to delete user <{}> ?".format(selected_u))
        if st.button("Delete User"):
            db.del_user(selected_u)
            st.success("<{}> was successfully deleted!".format(selected_u))

        # Doctor
        dc_list = [i[0] for i in db.view_dc()]
        selected_dc = st.selectbox("Doctor's delete", dc_list)
        st.warning("Are you sure to delete doctor <{}> ?".format(selected_dc))
        if st.button("Delete Doctor"):
            db.del_doc(selected_dc)
            st.success("<{}> was successfully deleted!".format(selected_dc))
        # Specialize
        ds_list_s = [i[0] for i in db.view_s()]
        ds_list2_s = [i[1] for i in db.view_s()]
        ds_list3_s = []
        for i in range(len(ds_list_s)):
            ds_list3_s.append((ds_list_s[i], ds_list2_s[i]))
        selected_s = st.selectbox("Specialize delete", ds_list3_s)
        st.warning("Are you sure to delete specialization <{}> ?".format(selected_s))
        if st.button("Delete Specialization"):
            db.del_spec(selected_s[0], selected_s[1])
            st.success("<{}> was successfully deleted!".format(selected_s))

        # Public Servant
        ps_list = [i[0] for i in db.view_ps()]
        selected_ps = st.selectbox("Public Servant's update", ps_list)
        st.warning("Are you sure to delete Public Servant <{}> ?".format(selected_ps))
        if st.button("Delete Public Servant"):
            db.del_ps(selected_ps)
            st.success("<{}> was successfully deleted!".format(selected_ps))
        # Record
        r_list_1 = [i[0] for i in db.view_r()]
        r_list_2 = [i[1] for i in db.view_r()]
        r_list_3 = [i[2] for i in db.view_r()]
        r_list_4 = []

        for i in range(len(r_list_1)):
            r_list_4.append((r_list_1[i], r_list_2[i], r_list_3[i]))

        selected_r = st.selectbox("Record update", r_list_4)
        st.warning("Are you sure to delete Record <{}> ?".format(selected_r))
        if st.button("Delete Record"):
            db.del_rec(selected_r[0],selected_r[1],selected_r[2])
            st.success("<{}> was successfully deleted!".format(selected_r))
            

if __name__ == '__main__':
    main()