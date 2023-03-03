def ParseToDict(cursor):
    records = cursor.fetchall()
    description = cursor.description
    columnnames = []
    for des in description:
        columnnames.append(des[0])
    data = []
    for row in records:
        data.append(dict(zip(columnnames, list(row))))
    return data
def ParseToOne(cursor):
    row = cursor.fetchone()
    description = cursor.description
    columnnames = []
    for des in description:
        columnnames.append(des[0])
    data=dict(zip(columnnames, list(row)))
    return data
