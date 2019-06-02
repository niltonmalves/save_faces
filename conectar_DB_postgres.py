import psycopg2

# # Connect to an existing database
conn = psycopg2.connect(dbname="dw.dados", user="postgres", password="postgres")
# # Open a cursor to perform database operations
cur = conn.cursor()

# # # Execute a command: this creates a new table
# # cur.execute("SELECT * from produto;")

dict = { 'cliente1': [1, 2, 4, 4.54545643287], 'cliente2': [2, 3, 3, 4.7484]}
www2 = { '75': '2', '79': '3'}
www3 = 0
#para usar numero com muitas casas decimais no postgresql a coluna deve ser do tipo "numeric"
namedict = ({"first_name":"Joshua", "ec":"12.53456655767"},
            {"first_name":"Steven", "ec":"11.4556747748672"},
            {"first_name":"David", "ec":"52.5"})

namedict2 = {"first_name":"Joshua", "ec":"qaw",
            "first_name":"Steven", "ec":"wdf",
            "first_name":"David", "ec":"asdewsf"}
            
     
cur = conn.cursor()
cur.executemany("""INSERT INTO bar4(first_name,ec) VALUES (%(first_name)s, %(ec)s)""", namedict2)


# # Execute a command: this creates a new table
# cur.execute("CREATE TABLE test2 (id serial PRIMARY KEY, num integer, data varchar);")


# # # Pass data to fill a query placeholders and let Psycopg perform
# # # the correct conversion (no more SQL injections!)
# for row in www2:
    # cur.execute("INSERT INTO test2 (num, data) VALUES (%s, %s)", row)

# cur.execute("INSERT INTO enco_frame (f1,f2,	f3,	f4,	f5,	f6,	f7,	f8,	f9,	f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,
# f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,
# f42,	f43,	f44,	f45,	f46,	f47,	f48,	f49,	f50,	f51,	f52,	f53,	f54,	f55,	f56,	f57,
# f58,	f59,	f60,	f61,	f62,	f63,	f64,	f65,	f66,	f67,	f68,	f69,	f70,	f71,	f72,	f73,	f74,	f75,	f76,	f77,	f78,
	# f79,	f80,	f81,	f82,	f83,	f84,	f85,	f86,	f87,	f88,	f89,	f90,	f91,	f92,	f93,	f94,	f95,	f96,	f97,	f98,	f99,
	# f100,	f101,	f102,	f103,	f104,	f105,	f106,	f107,	f108,	f109,	f110,	f111,	f112,	f113,	f114,	f115,	f116,	f117,	f118,	f119,	f120,
	# f121,	f122,	f123,	f124,	f125,	f126,	f127,	f128)
# Values (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s
# )",
# (1	1,265656565	3,265656565	5,265656565	7,265656565	9,265656565	11,26565656	13,26565656	15,26565656	17,26565656	19,26565656	21,26565656	23,26565656	25,26565656	27,26565656	29,26565656	31,26565656	33,26565656	35,26565656	37,26565656	39,26565656	41,26565656	43,26565656	45,26565656	47,26565656	49,26565656	51,26565656	53,26565656	55,26565656	57,26565656	59,26565656	61,26565656	63,26565656	65,26565656	67,26565656	69,26565656	71,26565656	73,26565656	75,26565656	77,26565656	79,26565656	81,26565656	83,26565656	85,26565656	87,26565656	89,26565656	91,26565656	93,26565656	95,26565656	97,26565656	99,26565656	101,2656566	103,2656566	105,2656566	107,2656566	109,2656566	111,2656566	113,2656566	115,2656566	117,2656566	119,2656566	121,2656566	123,2656566	125,2656566	127,2656566	129,2656566	131,2656566	133,2656566	135,2656566	137,2656566	139,2656566	141,2656566	143,2656566	145,2656566	147,2656566	149,2656566	151,2656566	153,2656566	155,2656566	157,2656566	159,2656566	161,2656566	163,2656566	165,2656566	167,2656566	169,2656566	171,2656566	173,2656566	175,2656566	177,2656566	179,2656566	181,2656566	183,2656566	185,2656566	187,2656566	189,2656566	191,2656566	193,2656566	195,2656566	197,2656566	199,2656566	201,2656566	203,2656566	205,2656566	207,2656566	209,2656566	211,2656566	213,2656566	215,2656566	217,2656566	219,2656566	221,2656566	223,2656566	225,2656566	227,2656566	229,2656566	231,2656566	233,2656566	235,2656566	237,2656566	239,2656566	241,2656566	243,2656566	245,2656566	247,2656566	249,2656566	251,2656566	253,2656566);")





# teste_enco = econ_rosto
# for row in teste_enco:
    
    # cur.execute("INSERT INTO enco_frame2 VALUES (%s,%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s
# )", row)


# # Query the database and obtain data as Python objects
# cur.execute("SELECT * FROM test2;")
# cur.fetchone()
# (1, 100, "abc'def")

# # Make the changes to the database persistent
conn.commit()

# # # Close communication with the database
cur.close()
# #conn.close()
cur = conn.cursor()


# #cur.execute("CREATE TABLE extratobancos11 (id serial primary key, dia date, lancamento character varying(80), doc integer, credito bigint, debito bigint, saldo bigint, banco character varying(15));")




import psycopg2
from psycopg2.extras import Json


def insert_into_table(data):
    # preparing geometry json data for insertion
    for item in data:
        item['geom'] = Json(item['geometry'])

    with psycopg2.connect(database='dw.dados', user='postgres', password='postgres', host='localhost') as conn:
        with conn.cursor() as cursor:
            query = """
                INSERT into 
                    data_load 
                    (iso_code, l_postcode, r_postcode, link_id, geom) 
                VALUES 
                    (%(iso_code)s, %(l_postcode)s, %(r_postcode)s, %(link_id)s, st_geomfromgeojson(%(geom)s));
            """
            cursor.executemany(query, data)

        conn.commit()
