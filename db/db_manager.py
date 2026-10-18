import psycopg2
from psycopg2 import Error

from db.db_config import DB_CONFIG


class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def connect(self): # connect to db
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            return True
        except Error as e:
            print(f"Ошибка подключения: {e}")
            return False
    
    def disconnect(self): # disconnect from db
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def execute_query(self, query, params=None, fetch=False): # for execuring all querys
        try:
            self.cursor.execute(query, params)
            if fetch:
                return self.cursor.fetchall()
            self.conn.commit()
            return True
        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            self.conn.rollback()
            return False
    
# querys for labwork
# getting info
    
    def get_all_animals(self): # animals and their info
        query = """
            SELECT 
                a.animal_id,
                a.name,
                a.birth_date,
                a.gender,
                a.animal_type,
                z.zone_name,
                k.full_name AS keeper_name,
                v.full_name AS vet_name
            FROM animals a
            JOIN zones z ON a.zone_id = z.zone_id
            JOIN employees k ON a.keeper_id = k.employee_id
            JOIN employees v ON a.vet_id = v.employee_id
            ORDER BY a.animal_id
        """
        return self.execute_query(query, fetch=True)
    
    def get_animal_by_id(self, animal_id): # special animal info by id
        query = """
            SELECT 
                a.animal_id,
                a.name,
                a.birth_date,
                a.gender,
                a.animal_type,
                a.zone_id,
                a.keeper_id,
                a.vet_id,
                z.zone_name,
                k.full_name AS keeper_name,
                v.full_name AS vet_name
            FROM animals a
            JOIN zones z ON a.zone_id = z.zone_id
            JOIN employees k ON a.keeper_id = k.employee_id
            JOIN employees v ON a.vet_id = v.employee_id
            WHERE a.animal_id = %s
        """
        result = self.execute_query(query, (animal_id,), fetch=True)
        return result[0] if result else None
    
    def get_bird_details(self, animal_id): # bird detail by id
        query = """
            SELECT country_code, country_name, departure_date, arrival_date
            FROM bird_details
            WHERE animal_id = %s
        """
        result = self.execute_query(query, (animal_id,), fetch=True)
        return result[0] if result else None
    
    def get_reptile_details(self, animal_id): # reptile detail by id
        query = """
            SELECT normal_temperature, hibernation_start, hibernation_end
            FROM reptile_details
            WHERE animal_id = %s
        """
        result = self.execute_query(query, (animal_id,), fetch=True)
        return result[0] if result else None

 # adding

    def add_animal(self, name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id): # add new animal
        query = """
            INSERT INTO animals (name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING animal_id
        """
        result = self.execute_query(query, (name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id), fetch=True)
        return result[0][0] if result else None
    
    def add_bird_details(self, animal_id, country_code, country_name, departure_date, arrival_date): # add details about birds
        query = """
            INSERT INTO bird_details (animal_id, country_code, country_name, departure_date, arrival_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        return self.execute_query(query, (animal_id, country_code, country_name, departure_date, arrival_date))
    
    def add_reptile_details(self, animal_id, normal_temperature, hibernation_start, hibernation_end): # add details about reptiles
        query = """
            INSERT INTO reptile_details (animal_id, normal_temperature, hibernation_start, hibernation_end)
            VALUES (%s, %s, %s, %s)
        """
        return self.execute_query(query, (animal_id, normal_temperature, hibernation_start, hibernation_end))
    
    def update_animal(self, animal_id, name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id): # update info about animal
        query = """
            UPDATE animals
            SET name = %s, birth_date = %s, gender = %s, animal_type = %s,
                zone_id = %s, keeper_id = %s, vet_id = %s
            WHERE animal_id = %s
        """
        return self.execute_query(query, (name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id, animal_id))
    
    def update_bird_details(self, animal_id, country_code, country_name, departure_date, arrival_date): # update info about bird
        query = """
            UPDATE bird_details
            SET country_code = %s, country_name = %s, departure_date = %s, arrival_date = %s
            WHERE animal_id = %s
        """
        return self.execute_query(query, (country_code, country_name, departure_date, arrival_date, animal_id))
    
    def update_reptile_details(self, animal_id, normal_temperature, hibernation_start, hibernation_end): # update info about reptile
        query = """
            UPDATE reptile_details
            SET normal_temperature = %s, hibernation_start = %s, hibernation_end = %s
            WHERE animal_id = %s
        """
        return self.execute_query(query, (normal_temperature, hibernation_start, hibernation_end, animal_id))
    
    def delete_animal(self, animal_id): # delete animal info
        query = "DELETE FROM animals WHERE animal_id = %s"
        return self.execute_query(query, (animal_id,))

# getting extra data   

    def get_all_zones(self): # all zones
        query = "SELECT zone_id, zone_name FROM zones ORDER BY zone_name"
        return self.execute_query(query, fetch=True)
    
    def get_all_employees(self): # all employees
        query = "SELECT employee_id, full_name, role FROM employees ORDER BY full_name"
        return self.execute_query(query, fetch=True)
    
    def get_keepers(self): # all keepers
        query = "SELECT employee_id, full_name FROM employees WHERE role = 'Смотритель' ORDER BY full_name"
        return self.execute_query(query, fetch=True)
    
    def get_vets(self): # all vets
        query = "SELECT employee_id, full_name FROM employees WHERE role = 'Ветеринар' ORDER BY full_name"
        return self.execute_query(query, fetch=True)