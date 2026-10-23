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

# 5. Fungsi pengira matrik (yang anda tanya tadi - tak perlu ubah apa-apa dalam ni)
def get_group_states(matric_numbers: list[int], all_states: list[str]) -> list[str]:
    """
    Owner: Role 1. Reviewed by: Role 2.
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
    Owner: Role 1 (Data Steward). Reviewed by: Role 2 (Structures Engineer).
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
