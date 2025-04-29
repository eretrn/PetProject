import psycopg2


def select(ID):
    try:
        con = psycopg2.connect(dbname='Train_Schedule', user='postgres', password='12qw', host='localhost')
        cursor = con.cursor()
        qwery = f'''SELECT * FROM public."imdb" WHERE id='{ID}';'''
        cursor.execute(qwery)
        data = cursor.fetchall()
        con.close()
        return data

    except Exception as err:
        print(err)
