import psycopg2
from psycopg2 import Error

from db.db_config import DB_CONFIG


class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            return True
        except Error as e:
            print(f"Ошибка подключения: {e}")
            return False

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None, fetch=False):
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

    def get_all_animals(self):
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
            FROM public.animals a
            JOIN public.zones z ON a.zone_id = z.zone_id
            JOIN public.employees k ON a.keeper_id = k.employee_id
            JOIN public.employees v ON a.vet_id = v.employee_id
            ORDER BY a.animal_id
        """
        return self.execute_query(query, fetch=True)

    def get_animal_by_id(self, animal_id):
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
            FROM public.animals a
            JOIN public.zones z ON a.zone_id = z.zone_id
            JOIN public.employees k ON a.keeper_id = k.employee_id
            JOIN public.employees v ON a.vet_id = v.employee_id
            WHERE a.animal_id = %s
        """
        result = self.execute_query(query, (animal_id,), fetch=True)
        return result[0] if result else None

    def get_bird_details(self, animal_id):
        query = """
            SELECT country_code, country_name, departure_date, arrival_date
            FROM public.bird_details
            WHERE animal_id = %s
        """
        result = self.execute_query(query, (animal_id,), fetch=True)
        return result[0] if result else None

    def get_reptile_details(self, animal_id):
        query = """
            SELECT normal_temperature, hibernation_start, hibernation_end
            FROM public.reptile_details
            WHERE animal_id = %s
        """
        result = self.execute_query(query, (animal_id,), fetch=True)
        return result[0] if result else None

    def add_animal(self, name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id):
        query = """
            INSERT INTO public.animals (name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING animal_id
        """
        result = self.execute_query(
            query, (name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id), fetch=True
        )
        return result[0][0] if result else None

    def add_bird_details(self, animal_id, country_code, country_name, departure_date, arrival_date):
        query = """
            INSERT INTO public.bird_details (animal_id, country_code, country_name, departure_date, arrival_date)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (animal_id) DO UPDATE
            SET country_code = EXCLUDED.country_code,
                country_name = EXCLUDED.country_name,
                departure_date = EXCLUDED.departure_date,
                arrival_date = EXCLUDED.arrival_date
        """
        return self.execute_query(query, (animal_id, country_code, country_name, departure_date, arrival_date))

    def add_reptile_details(self, animal_id, normal_temperature, hibernation_start, hibernation_end):
        query = """
            INSERT INTO public.reptile_details (animal_id, normal_temperature, hibernation_start, hibernation_end)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (animal_id) DO UPDATE
            SET normal_temperature = EXCLUDED.normal_temperature,
                hibernation_start = EXCLUDED.hibernation_start,
                hibernation_end = EXCLUDED.hibernation_end
        """
        return self.execute_query(query, (animal_id, normal_temperature, hibernation_start, hibernation_end))

    def update_animal(self, animal_id, name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id):
        query = """
            UPDATE public.animals
            SET name = %s, birth_date = %s, gender = %s, animal_type = %s,
                zone_id = %s, keeper_id = %s, vet_id = %s
            WHERE animal_id = %s
        """
        return self.execute_query(
            query, (name, birth_date, gender, animal_type, zone_id, keeper_id, vet_id, animal_id)
        )

    def update_bird_details(self, animal_id, country_code, country_name, departure_date, arrival_date):
        self.execute_query("DELETE FROM public.reptile_details WHERE animal_id = %s", (animal_id,))
        return self.add_bird_details(animal_id, country_code, country_name, departure_date, arrival_date)

    def update_reptile_details(self, animal_id, normal_temperature, hibernation_start, hibernation_end):
        self.execute_query("DELETE FROM public.bird_details WHERE animal_id = %s", (animal_id,))
        return self.add_reptile_details(animal_id, normal_temperature, hibernation_start, hibernation_end)

    def clear_special_details(self, animal_id):
        self.execute_query("DELETE FROM public.bird_details WHERE animal_id = %s", (animal_id,))
        self.execute_query("DELETE FROM public.reptile_details WHERE animal_id = %s", (animal_id,))

    def delete_animal(self, animal_id):
        query = "DELETE FROM public.animals WHERE animal_id = %s"
        return self.execute_query(query, (animal_id,))

    def get_all_zones(self):
        query = "SELECT zone_id, zone_name FROM public.zones ORDER BY zone_name"
        return self.execute_query(query, fetch=True)

    def get_all_employees(self):
        query = 'SELECT employee_id, full_name, "role" FROM public.employees ORDER BY full_name'
        return self.execute_query(query, fetch=True)

    def get_keepers(self):
        query = """
            SELECT employee_id, full_name
            FROM public.employees
            WHERE "role" = 'Смотритель'
            ORDER BY full_name
        """
        return self.execute_query(query, fetch=True)

    def get_vets(self):
        query = """
            SELECT employee_id, full_name
            FROM public.employees
            WHERE "role" = 'Ветеринар'
            ORDER BY full_name
        """
        return self.execute_query(query, fetch=True)

    def get_employees_full(self):
        query = """
            SELECT 
                e.employee_id,
                e.full_name,
                e.birth_date,
                e.phone,
                e.marital_status,
                e."role",
                e.spouse_id,
                s.full_name AS spouse_name
            FROM public.employees e
            LEFT JOIN public.employees s ON e.spouse_id = s.employee_id
            ORDER BY e.employee_id
        """
        return self.execute_query(query, fetch=True)

    def get_employee_by_id(self, emp_id):
        query = """
            SELECT employee_id, full_name, birth_date, phone, marital_status, "role", spouse_id
            FROM public.employees
            WHERE employee_id = %s
        """
        res = self.execute_query(query, (emp_id,), fetch=True)
        return res[0] if res else None

    def add_employee(self, full_name, birth_date, phone, marital_status, role, spouse_id=None):
        query = """
            INSERT INTO public.employees (full_name, birth_date, phone, marital_status, "role", spouse_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING employee_id
        """
        res = self.execute_query(query, (full_name, birth_date, phone, marital_status, role, spouse_id), fetch=True)
        new_id = res[0][0] if res else None
        if new_id and spouse_id:
            self.execute_query(
                "UPDATE public.employees SET spouse_id = NULL WHERE spouse_id = %s AND employee_id != %s",
                (spouse_id, new_id)
            )
            self.execute_query(
                "UPDATE public.employees SET spouse_id = %s, marital_status = 'В браке' WHERE employee_id = %s",
                (new_id, spouse_id)
            )
        return new_id

    def update_employee(self, emp_id, full_name, birth_date, phone, marital_status, role, spouse_id=None):
        self.execute_query("UPDATE public.employees SET spouse_id = NULL WHERE spouse_id = %s", (emp_id,))
        query = """
            UPDATE public.employees
            SET full_name = %s, birth_date = %s, phone = %s,
                marital_status = %s, "role" = %s, spouse_id = %s
            WHERE employee_id = %s
        """
        ok = self.execute_query(query, (full_name, birth_date, phone, marital_status, role, spouse_id, emp_id))
        if ok and spouse_id:
            self.execute_query(
                "UPDATE public.employees SET spouse_id = NULL WHERE spouse_id = %s AND employee_id != %s",
                (spouse_id, emp_id)
            )
            self.execute_query(
                "UPDATE public.employees SET spouse_id = %s, marital_status = 'В браке' WHERE employee_id = %s",
                (emp_id, spouse_id)
            )
        return ok

    def delete_employee(self, emp_id):
        self.execute_query("UPDATE public.employees SET spouse_id = NULL WHERE spouse_id = %s", (emp_id,))
        return self.execute_query("DELETE FROM public.employees WHERE employee_id = %s", (emp_id,))

    def get_diet_types_summary(self):
        """Возвращает уникальные типы рационов, количество рационов в каждом типе и их список через запятую"""
        query = """
            SELECT 
                diet_type,
                COUNT(diet_id) AS diets_count,
                STRING_AGG(diet_name, ', ' ORDER BY diet_name) AS diet_names
            FROM public.diets
            GROUP BY diet_type
            ORDER BY diet_type
        """
        return self.execute_query(query, fetch=True)

    def get_distinct_diet_types(self):
        query = "SELECT DISTINCT diet_type FROM public.diets ORDER BY diet_type"
        rows = self.execute_query(query, fetch=True) or []
        return [r[0] for r in rows]

    def add_diet_type_with_first_diet(self, diet_type, first_diet_name):
        """Добавляет новый тип рациона вместе с первым рационом этого типа"""
        query = """
            INSERT INTO public.diets (diet_type, diet_name)
            VALUES (%s, %s)
            RETURNING diet_id
        """
        res = self.execute_query(query, (diet_type, first_diet_name), fetch=True)
        return res[0][0] if res else None

    def rename_diet_type(self, old_type_name, new_type_name):
        """Переименовывает тип рациона во всех записях таблицы diets"""
        query = "UPDATE public.diets SET diet_type = %s WHERE diet_type = %s"
        return self.execute_query(query, (new_type_name, old_type_name))

    def delete_diet_type(self, diet_type):
        """Удаляет все рационы указанного типа (если они не используются в истории)"""
        query = "DELETE FROM public.diets WHERE diet_type = %s"
        return self.execute_query(query, (diet_type,))

    def get_all_diets(self):
        query = """
            SELECT diet_id, diet_name, diet_type
            FROM public.diets
            ORDER BY diet_id
        """
        return self.execute_query(query, fetch=True)

    def get_diet_by_id(self, diet_id):
        query = "SELECT diet_id, diet_name, diet_type FROM public.diets WHERE diet_id = %s"
        res = self.execute_query(query, (diet_id,), fetch=True)
        return res[0] if res else None

    def add_diet(self, diet_name, diet_type):
        query = """
            INSERT INTO public.diets (diet_name, diet_type)
            VALUES (%s, %s)
            RETURNING diet_id
        """
        res = self.execute_query(query, (diet_name, diet_type), fetch=True)
        return res[0][0] if res else None

    def update_diet(self, diet_id, diet_name, diet_type):
        query = """
            UPDATE public.diets
            SET diet_name = %s, diet_type = %s
            WHERE diet_id = %s
        """
        return self.execute_query(query, (diet_name, diet_type, diet_id))

    def delete_diet(self, diet_id):
        query = "DELETE FROM public.diets WHERE diet_id = %s"
        return self.execute_query(query, (diet_id,))

    def get_diet_history(self):
        query = """
            SELECT 
                adh.history_id,
                a.animal_id,
                a.name AS animal_name,
                d.diet_id,
                d.diet_name,
                d.diet_type,
                adh.start_date,
                adh.end_date
            FROM public.animal_diet_history adh
            JOIN public.animals a ON adh.animal_id = a.animal_id
            JOIN public.diets d ON adh.diet_id = d.diet_id
            ORDER BY adh.start_date DESC, adh.history_id DESC
        """
        return self.execute_query(query, fetch=True)

    def get_diet_history_by_id(self, history_id):
        query = """
            SELECT history_id, animal_id, diet_id, start_date, end_date
            FROM public.animal_diet_history
            WHERE history_id = %s
        """
        res = self.execute_query(query, (history_id,), fetch=True)
        return res[0] if res else None

    def assign_diet_to_animal(self, animal_id, diet_id, start_date, end_date=None):
        close_prev = """
            UPDATE public.animal_diet_history
            SET end_date = %s
            WHERE animal_id = %s AND end_date IS NULL AND start_date <= %s
        """
        self.execute_query(close_prev, (start_date, animal_id, start_date))

        query = """
            INSERT INTO public.animal_diet_history (animal_id, diet_id, start_date, end_date)
            VALUES (%s, %s, %s, %s)
        """
        return self.execute_query(query, (animal_id, diet_id, start_date, end_date))

    def update_diet_history(self, history_id, animal_id, diet_id, start_date, end_date=None):
        query = """
            UPDATE public.animal_diet_history
            SET animal_id = %s, diet_id = %s, start_date = %s, end_date = %s
            WHERE history_id = %s
        """
        return self.execute_query(query, (animal_id, diet_id, start_date, end_date, history_id))

    def finish_current_diet(self, history_id, end_date):
        query = "UPDATE public.animal_diet_history SET end_date = %s WHERE history_id = %s"
        return self.execute_query(query, (end_date, history_id))

    def delete_diet_history(self, history_id):
        query = "DELETE FROM public.animal_diet_history WHERE history_id = %s"
        return self.execute_query(query, (history_id,))

    def get_full_animal_report(self, animal_type, name):
        query = """
            SELECT 
                a.animal_id,
                a.name,
                a.birth_date,
                a.gender,
                a.animal_type,
                z.zone_name,
                z.description AS zone_desc,
                k.full_name AS keeper_name,
                k.phone AS keeper_phone,
                v.full_name AS vet_name,
                v.phone AS vet_phone,
                d.diet_id,
                d.diet_name,
                d.diet_type
            FROM public.animals a
            JOIN public.zones z ON a.zone_id = z.zone_id
            JOIN public.employees k ON a.keeper_id = k.employee_id
            JOIN public.employees v ON a.vet_id = v.employee_id
            LEFT JOIN LATERAL (
                SELECT adh.diet_id
                FROM public.animal_diet_history adh
                WHERE adh.animal_id = a.animal_id
                  AND (adh.end_date IS NULL OR adh.end_date >= CURRENT_DATE)
                ORDER BY adh.start_date DESC, adh.history_id DESC
                LIMIT 1
            ) cur_adh ON TRUE
            LEFT JOIN public.diets d ON cur_adh.diet_id = d.diet_id
            WHERE a.animal_type = %s AND LOWER(a.name) = LOWER(%s)
            ORDER BY a.animal_id
        """
        return self.execute_query(query, (animal_type, name), fetch=True)

    def get_animal_diet_history_list(self, animal_id):
        query = """
            SELECT d.diet_id, d.diet_name, d.diet_type, adh.start_date, adh.end_date
            FROM public.animal_diet_history adh
            JOIN public.diets d ON adh.diet_id = d.diet_id
            WHERE adh.animal_id = %s
            ORDER BY adh.start_date DESC
        """
        return self.execute_query(query, (animal_id,), fetch=True)

    def get_married_couples_report(self):
        query = """
            SELECT 
                e1.full_name AS emp1_name,
                e1.birth_date AS emp1_birth,
                e1.phone AS emp1_phone,
                e1."role" AS emp1_role,
                e2.full_name AS emp2_name,
                e2.birth_date AS emp2_birth,
                e2.phone AS emp2_phone,
                e2."role" AS emp2_role
            FROM public.employees e1
            JOIN public.employees e2 ON e1.spouse_id = e2.employee_id
            WHERE e1.employee_id < e2.employee_id
               OR (e2.spouse_id IS DISTINCT FROM e1.employee_id)
            ORDER BY e1.full_name
        """
        return self.execute_query(query, fetch=True)

    def get_animals_diets_on_date(self, target_date):
        query = """
            SELECT 
                a.animal_id,
                a.name,
                a.animal_type,
                d.diet_id,
                d.diet_name,
                d.diet_type,
                adh.start_date,
                adh.end_date
            FROM public.animals a
            LEFT JOIN public.animal_diet_history adh
                ON a.animal_id = adh.animal_id
                AND adh.start_date <= %s
                AND (adh.end_date IS NULL OR adh.end_date >= %s)
            LEFT JOIN public.diets d ON adh.diet_id = d.diet_id
            WHERE a.birth_date <= %s
            ORDER BY a.animal_id
        """
        return self.execute_query(query, (target_date, target_date, target_date), fetch=True)