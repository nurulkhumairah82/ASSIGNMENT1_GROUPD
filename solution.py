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
