from sqlite3 import connect

DB_FILE = "data.db"
TABLE_NAME = "products"

con = connect(DB_FILE)
cur = con.cursor()


def create_table():
    with con:
        cur.execute(
            f"""
                    CREATE TABLE {TABLE_NAME}
                        (id INTEGER PRIMARY KEY,
                        product_name TEXT,
                        description TEXT,
                        unit TEXT,
                        category TEXT,
                        price INTEGER,
                        stock INTEGER
                        )"""
        )
    con.commit()


def insert_data(
    product_name,
    unit,
    category,
    price=0,
    stock=0,
    description="",
):
    with con:
        cur.execute(
            f"""INSERT INTO {TABLE_NAME} (
                    id,
                    product_name,
                    description,
                    unit,
                    category,
                    price,
                    stock
        ) VALUES (NULL,?,?,?,?,?,?)""",
            (
                product_name,
                description,
                unit,
                category,
                price,
                stock,
            ),
        )
        con.commit()


def update_data(
    id,
    product_name,
    description,
    unit,
    category,
    price,
    stock,
):
    with con:
        cur.execute(
            f"""UPDATE {TABLE_NAME}
             SET 
                    product_name=?,
                    description=?,
                    unit=?,
                    category=?,
                    price=?,
                    stock=?
         WHERE id=?""",
            (
                product_name,
                description,
                unit,
                category,
                price,
                stock,
                id,
            ),
        )
        con.commit()


def delete_data(id):
    with con:
        cur.execute(
            f"DELETE FROM {TABLE_NAME} WHERE id=?",
            (id,),
        )
        con.commit()


def get_products():
    with con:
        cur.execute(f"SELECT * FROM {TABLE_NAME}")
        products = cur.fetchall()

    return products


def get_product_by_id(id):
    with con:
        cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE id=?", (id,))
        product = cur.fetchone()

    return product


def get_product_by_name(product_name):
    with con:
        cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE product_name=?", (product_name,))
        product = cur.fetchone()

    return product
