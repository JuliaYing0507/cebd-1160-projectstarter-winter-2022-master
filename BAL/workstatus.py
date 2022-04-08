import DAL.db as d

dta = d.DB()

def get_students_data():
    return dta.execute_select_query("StatsCan", "WorkStatus", params={'is_student': "True"})

def get_full_dataset():
    return dta.execute_select_query("StatsCan", "WorkStatus")


def get_province_data(_province: str):
    return dta.execute_select_query("StatsCan", "WorkStatus", params={'prov_name': _province})

def get_data_per_lfs_code(_lfs_code: str):
    return dta.execute_select_query("StatsCan", "WorkStatus", params={'lfsstat': _lfs_code})