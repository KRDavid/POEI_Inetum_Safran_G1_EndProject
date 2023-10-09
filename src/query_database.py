import pandas as pd

def get_datas(cur, id):
    return_response = {}

    # Fetching data for front page
    with open("./sql/return_desc.sql", 'r') as file:
        query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["desc"] = data


    # Fetching data for first table
    with open("./sql/return_all_incidents.sql", 'r') as file:
        query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["incidents"] = data


    # Fetching data for second table
    with open("./sql/return_posts.sql", 'r') as file:
        query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["posts"] = data


    # Fetching data for third table
    with open("./sql/select_incident.sql", 'r') as file:
            query = file.read()

    res = cur.execute(query, (str(id)))
    data = res.fetchall()
    return_response["selected_incidents"] = data
    
    return return_response
