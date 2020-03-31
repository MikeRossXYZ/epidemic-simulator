class Table:
    name = ""
    records = {}

class TableRecord:
    criteria = {}
    value = None
    key = None

def tbl_get(tbl_dict, name):
    if name in tbl_dict:
        return tbl_dict[name]
    else:
        return None

def tbl_lookup_value(tbl, criteria):
    key = _tbl_record_criteria_key(criteria)
    if key in tbl.records:
        return tbl.records[key].value
    else:
        return None

def tbl_insert_record(tbl, criteria, value):
    key = _tbl_record_criteria_key(criteria)
    
    if key in tbl.records:
        rec = tbl.records.pop(key)
        del rec

    record = TableRecord()
    record.key = key
    record.criteria = criteria
    record.value = value
    
    tbl.records[key] = record

def _tbl_record_criteria_key(criteria):
    criteria_lst = [(key, val) for key, val in criteria.items()]
    criteria_sorted_tuple_lst = sorted(criteria_lst, key=lambda criterion: criterion[0])
    return "__".join([x[0] + "_" + x[1] for x in criteria_sorted_tuple_lst])

