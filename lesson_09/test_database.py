from subject_table import SubjectTable


db = SubjectTable("postgresql://postgres:postgres123@localhost:5432/QA")


def test_get_subjects():
    db_result = db.get_subjects()
    assert len(db_result) > 0


def test_insert():
    subject_id = 17
    subject_title = 'Geometry'
    db.create(subject_id, subject_title)

    new_subject = db.get_subject_by_id(subject_id)

    db.delete_id(subject_id)

    assert new_subject[0] == subject_id
    assert new_subject[1] == subject_title


def test_update():
    subject_id = 17
    subject_title = 'Geometry'
    db.create(subject_id, subject_title)

    new_subject_id = 18
    new_subject_title = 'Painting'
    db.update(subject_id, new_subject_id, new_subject_title)

    updated_subject = db.get_subject_by_id(new_subject_id)

    db.delete_id(new_subject_id)

    assert updated_subject[0] == new_subject_id
    assert updated_subject[1] == new_subject_title

    old_subject = db.get_subject_by_id(subject_id)
    assert old_subject is None


def test_delete():
    subject_id = 17
    subject_title = 'Geometry'
    db.create(subject_id, subject_title)

    db.delete_id(subject_id)

    new_subject = db.get_subject_by_id(subject_id)

    assert new_subject is None
