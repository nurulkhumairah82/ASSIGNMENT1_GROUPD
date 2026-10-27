# solution.py

# 1. Senarai 16 buah negeri di Malaysia (ikut abjad)
STATES = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", 
    "Sarawak", "Selangor", "Terengganu", "W.P. Kuala Lumpur", 
    "W.P. Labuan", "W.P. Putrajaya"
]

# 2. Tahun untuk data pendapatan
SURVEY_YEARS = [2016, 2019, 2020, 2022, 2024]

# 3. Tahun untuk data kemiskinan
POVERTY_YEARS = [2019, 2020, 2022, 2024]

# 4. Pembahagian wilayah negeri
REGIONS = {
    "Northern": ["Perlis", "Kedah", "Pulau Pinang", "Perak"],
    "Central": ["Selangor", "W.P. Kuala Lumpur", "W.P. Putrajaya", "Negeri Sembilan"],
    "Southern": ["Melaka", "Johor"],
    "East Coast": ["Kelantan", "Terengganu", "Pahang"],
    "East Malaysia": ["Sabah", "Sarawak", "W.P. Labuan"],
}

# 5. Fungsi pengira matrik
def get_group_states(matric_numbers: list[int], all_states: list[str]) -> list[str]:
    """
    Owner: Siti Nurin Saffiyah Binti Abd Samad (Role 1-Data Steward) Reviewed by: Nur Dayana Anis Binti Azhar (Role 2-Structures Engineer)
    """
    sorted_matrics = sorted(matric_numbers)
    group_states = []
    
    for matric in sorted_matrics:
        remainder = matric % len(all_states)
        idx = remainder
        
        while all_states[idx] in group_states:
            idx = (idx + 1) % len(all_states)
            
        group_states.append(all_states[idx])
        
    return group_states
#Task 1
def validate_records(records: list[dict], required_keys: tuple[str, ...]) -> None:
    """
    Menyemak dan memastikan rekod data lengkap dan sah.
    Owner: Siti Nurin Saffiyah Binti Abd Samad (Role 1-Data Steward) Reviewed by: Nur Dayana Anis Binti Azhar (Role 2-Structures Engineer)
    """
    # 1. Semak sama ada records ialah list
    if not isinstance(records, list):
        raise TypeError("Ralat: Data records mestilah dalam bentuk senarai (list).")
    
    # 2. Semak jika records kosong
    if len(records) == 0:
        raise ValueError("Ralat: Data records tidak boleh kosong.")
    
    seen_keys = set()
    
    for rec in records:
        # 3. Semak jika ada item yang bukan dictionary (dict)
        if not isinstance(rec, dict):
            raise TypeError("Ralat: Setiap rekod di dalam records mestilah berbentuk kamus (dict).")
        
        # 4. Semak jika ada kunci wajib (required_keys) yang hilang
        for key in required_keys:
            if key not in rec:
                raise KeyError(f"Ralat: Rekod kehilangan kunci wajib '{key}'.")
        
        # 5. Semak jika ada rekod bertindih/pendua bagi (state, date)
        state_date = (rec.get("state"), rec.get("date"))
        if state_date in seen_keys:
            raise ValueError(f"Ralat: Rekod bertindih (pendua) dijumpai untuk: {state_date}")
        seen_keys.add(state_date)
#Task 2        
import numpy as np

def to_float(value) -> float:
    """
    Menukar nilai kepada float, dan mengembalikan np.nan jika None.
    Owner: Nur Dayana Anis Binti Azhar (Role 2-Structures Engineer) Reviewed by: Siti Nurin Saffiyah Binti Abd Samad (Role 1-Data Steward)
    """
    if value is None:
        return np.nan
    return float(value)


def index_by_key(records: list[dict]) -> dict:
    """
    Mengembalikan dictionary berkunci (state, year) daripada senarai rekod.
    Owner: Nur Dayana Anis Binti Azhar (Role 2-Structures Engineer) Reviewed by: Siti Nurin Saffiyah Binti Abd Samad (Role 1-Data Steward)
    """
    indexed = {}
    for record in records:
        state = record["state"]
        year = int(record["date"][:4]) # Ambil 4 huruf pertama tarikh sebagai tahun
        key = (state, year)
        
        if key in indexed:
            raise ValueError(f"Ralat: Kunci bertindih (duplicate key) ditemui untuk {key}")
        indexed[key] = record
        
    return indexed


def join_records(income_records: list[dict], poverty_records: list[dict]):
    """
    Memadankan rekod pendapatan dan kemiskinan mengikut kunci (state, year).
    Owner: Nur Dayana Anis Binti Azhar (Role 2-Structures Engineer) Reviewed by: Siti Nurin Saffiyah Binti Abd Samad (Role 1-Data Steward)
    """
    income_indexed = index_by_key(income_records)
    poverty_indexed = index_by_key(poverty_records)
    
    income_keys = set(income_indexed.keys())
    poverty_keys = set(poverty_indexed.keys())
    
    common_keys = income_keys.intersection(poverty_keys)
    income_only = income_keys - poverty_keys
    poverty_only = poverty_keys - income_keys
    
    joined = []
    for key in common_keys:
        inc = income_indexed[key]
        pov = poverty_indexed[key]
        # Gabungkan data pendapatan dan kemiskinan
        combined = {**inc, **pov}
        joined.append(combined)
        
    return joined, income_only, poverty_only
