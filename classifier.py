RULES = [
    (["helpdesk", "spare part"], 3),
    (["vip", "complaint", "assurance"], 4),
    (["site keeper", "maintenance"], 5),
    (["pln", "kva", "power"], 6),
    (["installation", "commissioning", "onsite"], 7),
]

HIERARCHY = {
    1: "Managed Services",
    2: "Helpdesk & Support Services",
    3: "Services Package",
    4: "Network & Site Assurance",
    5: "Site Operation Services",
    6: "Infrastructure & Power Support",
    7: "Onsite Technical Support Services"
}

def classify_item(desc):
    desc = str(desc).lower()
    stop_level = 3

    for keywords, level in rules:
        if any(k in desc for k in keywords):
            stop_level = max(stop_level, level)

    return {f"L{i}": HIERARCHY[i] if i <= stop_level else "" for i in range(1, 8)}
