import psycopg2

def insert_schedule(id, art, st_n):
    try:
        con = psycopg2.connect(dbname='test_train', user='postgres', password='12qw', host='localhost')
        cursor = con.cursor()
        if art !='Null':
            query = f'''INSERT INTO public."schedule" 
            VALUES ('{6013}', '{id}', '{art}', '{st_n}');'''
        else:
            query = f'''INSERT INTO public."schedule"  
                        VALUES ('{6013}', '{id}', Null, '{st_n}');'''
            miss = f'''INSERT INTO public.miss_stations
                        VALUES ('{6013}',{id})'''
            cursor.execute(miss)
        cursor.execute(query)
        con.commit()
    except Exception as err:
        print(err)

def insert_stations(id, station_name):
    try:
        con = psycopg2.connect(dbname='test_train', user='postgres', password='12qw', host='localhost')
        cursor = con.cursor()
        qwery = f'''INSERT INTO public."stations" 
        VALUES ('{id}', '{station_name}');'''
        cursor.execute(qwery)
        con.commit()
    except Exception as err:
        print(err)
def insert_days(id, works):
    try:
        con = psycopg2.connect(dbname='test_train', user='postgres', password='12qw', host='localhost')
        cursor = con.cursor()
        if works == 'ежедневно':
            qwery = f'''INSERT INTO public."working_days" 
                    VALUES ('{id}', 'monday'),
                           ('{id}', 'tueday'),
                           ('{id}', 'wednesday'),
                           ('{id}', 'thursday'),
                           ('{id}', 'friday'),
                           ('{id}', 'saturday'), 
                           ('{id}', 'sunday');'''
        elif works == 'рабочим':
            qwery = f'''INSERT INTO public."working_days" 
                    VALUES ('{id}', 'monday'),
                           ('{id}', 'tueday'),
                           ('{id}', 'wednesday'),
                           ('{id}', 'thursday'),
                           ('{id}', 'friday');'''
        else:
            qwery = f'''INSERT INTO public."working_days" 
                    VALUES ('{id}', 'saturday'), 
                           ('{id}', 'sunday');'''
        cursor.execute(qwery)
        con.commit()
    except Exception as err:
        print(err)

