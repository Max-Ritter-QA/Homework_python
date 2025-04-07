from PlaceTable import PlaceTable
db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = PlaceTable(db_connection_string)

def test_update():
    new_id = 6
    name = "Testing_update"
    db.new_insert(new_id, name)

    size = 14
    db.update(size,new_id)
    body3 = db.get_places() # результат после изменения

    db.delete(new_id)

    assert body3[5][2] == size
    assert body3[5][1] == name
    assert body3[5][0] == new_id

def test_insert():
    body = db.get_places()  # список БД до внесения изменений
    len_before = len(body)

    new_id = 6
    name = "Testing_insert"
    db.new_insert(new_id, name)

    body2 = db.get_places()  # результат после добавления
    len_after = len(body2)

    db.delete(new_id)
    assert len_after - len_before == 1
    assert body2[5][0] == new_id
    assert body2[5][1] == name

def test_delete():
    body = db.get_places()
    len_before = len(body)

    new_id = 6
    name = "Testing_delete"
    db.new_insert(new_id, name)

    db.delete(new_id)
    body2 = db.get_places()
    len_delete = len(body2)

    assert len_before == len_delete
