states_needed = set( [ "mt", "wa", "or", "id", "nv", "ut",
                       "са", "az"] )
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


result = set()

while len(states_needed) > 0:
    select = None
    covered_st = set()
    for station, covers in stations.items():
        if len(states_needed & covers) > len(covered_st):
            select = station
            covered_st = covers
    states_needed -= covered_st
    result.add(select)

print(result)