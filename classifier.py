RULES = [
    (["helpdesk", "spare part"], 2),          # L2-01 / L4-02
    (["vip", "complaint", "assurance"], 1),  # L4-01 / L5-01 / L5-02
    (["site", "maintenance", "pm", "cm"], 5),# L5-04 / L5-05 / L4-03 / L4-04
    (["pln", "kva", "power"], 6),            # L5-10 / L6-08 / L7-07
    (["installation", "commissioning", "rru", "odu", "idu", "hardware"], 7), # L5-06, L5-07, L5-08, L5-09, L4-07 / L4-10
    (["optimization", "monitoring", "oss", "rf"], 4), # L4-08 / L4-09 / L3-08 / L3-09
    (["transport", "microwave", "link"], 5), # L4-10 / L4-11 / L3-11
]


HIERARCHY = {
    1: "Customer & Service Assurance",
    2: "Network Operations & Maintenance",
    3: "Network Deployment & Installation",
    4: "Network Optimization & Performance",
    5: "Transmission & Transport Services",
    6: "Power & Infrastructure Services",
    7: "Onsite Technical Support"
}

def classify_item(desc):
    desc = str(desc).lower()
    stop_level = 3

    for keywords, level in rules:
        if any(k in desc for k in keywords):
            stop_level = max(stop_level, level)

    return {f"L{i}": HIERARCHY[i] if i <= stop_level else "" for i in range(1, 8)}
