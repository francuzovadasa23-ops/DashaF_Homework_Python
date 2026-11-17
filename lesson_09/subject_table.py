from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "select_by_id": text("SELECT * FROM subject "
                             "WHERE subject_id = :id_to_select"),
        "insert_new": text("INSERT INTO subject"
                           "(\"subject_id\", \"subject_title\") "
                           "VALUES (:new_subject_id, :new_subject_title)"),
        "delete_by_id": text("DELETE FROM subject "
                             "WHERE subject_id = :id_to_delete"),
        "update_by_id": text("UPDATE subject "
                             "SET subject_id = :new_subject_id, "
                             "subject_title = :new_subject_title "
                             "WHERE subject_id = :old_subject_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_subject_by_id(self, subject_id):
        result = self.__db.execute(self.__scripts["select_by_id"],
                                   id_to_select=subject_id).fetchone()
        return result

    def create(self, subject_id, subject_title):
        self.__db.execute(self.__scripts["insert_new"],
                          new_subject_id=subject_id,
                          new_subject_title=subject_title)

    def delete_id(self, subject_id):
        self.__db.execute(self.__scripts["delete_by_id"],
                          id_to_delete=subject_id)

    def update(self, old_subject_id, new_subject_id, new_subject_title):
        self.__db.execute(self.__scripts["update_by_id"],
                          old_subject_id=old_subject_id,
                          new_subject_id=new_subject_id,
                          new_subject_title=new_subject_title)
