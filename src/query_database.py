import pandas as pd

def get_datas(cur, id):
    return_response = {}

    # Fetching data for front page
    with open("./sql/return_desc.sql", 'r') as file:
        query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["desc"] = data[0][0]


    # Fetching data for first table
    with open("./sql/return_all_incidents.sql", 'r') as file:
        query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["incidents"] = data


    # Fetching data for second table
    with open("./sql/get_incidents_on_posts.sql", 'r') as file:
        query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["posts"] = data

    posts_distinct = []

    for elem in data:
        if elem[2] not in posts_distinct:
            posts_distinct.append([elem[2], elem[3]])
    
    return_response["posts_distinct"] = posts_distinct
    
    return return_response
