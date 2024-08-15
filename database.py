import psycopg2


class DataBase:
    def __init__(self, name, password, host, user):
        self.database = psycopg2.connect(
            database=name,
            password=password,
            host=host,
            user=user
        )

    def manager(self, sql, *args, commit: bool = False,
                fetchone: bool = False,
                fetchall: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    return db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()

    def create_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            full_name VARCHAR(80),
            contact VARCHAR(20) UNIQUE
        )'''
        self.manager(sql, commit=True)

    def insert_user_tg(self, telegram_id):
        sql = '''INSERT INTO users(telegram_id) VALUES(%s)
                  ON CONFLICT DO NOTHING'''
        return self.manager(sql, (telegram_id,), commit=True)

    def check_user_id(self, telegram_id):
        sql = '''SELECT * FROM users WHERE telegram_id = %s'''
        return self.manager(sql, telegram_id, fetchone=True)

    def save_user(self, full_name, contact, telegram_id):
        sql = '''UPDATE users SET full_name=%s, contact=%s WHERE telegram_id = %s'''
        self.manager(sql, full_name, contact, telegram_id)

    def create_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            category_id SERIAL PRIMARY KEY,
            category VARCHAR(60) UNIQUE
        )'''
        self.manager(sql, commit=True)

    def create_products(self):
        sql = '''CREATE TABLE IF NOT EXISTS products(
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(60) UNIQUE,
            price INTEGER,
            image TEXT,
            category INTEGER REFERENCES categories(category_id)
        )'''
        self.manager(sql, commit=True)

    def insert_categories(self, category):
        sql = '''INSERT INTO categories(category) VALUES (%s)
        ON CONFLICT DO NOTHING'''
        self.manager(sql, (category,), commit=True)

    def get_categories(self):
        sql = '''SELECT category FROM categories'''
        return self.manager(sql, fetchall=True)

    def insert_product(self, product_name, price, image, category):
        sql = '''INSERT INTO products(product_name, price, image, category)
         VALUES(%s,%s,%s,%s)
         ON CONFLICT DO NOTHING'''
        self.manager(sql, product_name, price, image, category, commit=True)

    def get_product(self, category):
        sql = '''SELECT * FROM products WHERE category = (SELECT category_id FROM categories WHERE category_id = %s)'''
        return self.manager(sql, category, fetchall=True)

    def get_product_by_category(self, category_name):
        sql = '''SELECT * FROM products
         WHERE category=(SELECT category_id FROM categories WHERE category = %s)'''
        return self.manager(sql, category_name, fetchall=True)


    def get_images(self, category_id):
        sql = '''SELECT image FROM products'''
        return self.manager(sql, category_id,fetchall=True)

    def product_info(self, product_id):
        sql = '''SELECT * FROM products WHERE product_id=%s'''
        return self.manager(sql, product_id, fetchone=True)


    def get_users(self):
        sql = '''SELECT COUNT(*) FROM users '''
        return self.manager(sql, fetchall=True)



    def get_users_id(self):
        sql = '''SELECT telegram_id FROM users'''
        return self.manager(sql, fetchall=True)


    def get_category_del(self):
        sql = '''SELECT category, category_id FROM categories'''
        return self.manager(sql, fetchall=True)

    def return_category_id(self, category):
        sql = '''SELECT category_id FROM categories WHERE category=%s'''
        return self.manager(sql, (category,), fetchone=True)


    def get_products_by_delete(self):
        sql = '''SELECT product_name, product_id FROM products'''
        return self.manager(sql, fetchall=True)

    def insert_category(self, category):
        sql = '''INSERT INTO categories(category) values (%s)
        ON CONFLICT DO NOTHING'''
        return self.manager(sql, (category,), commit=True)

