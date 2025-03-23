from PlaceTable import PlaceTable
db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = PlaceTable(db_connection_string)

def test_insert():
    body = db.get_places() # список БД до внесения изменений
    len_before = len(body)

    new_id = 6
    name = "Testin"
    db.new_insert(new_id, name)

    body2 = db.get_places() # результат после добавления
    len_after = len(body2)

    size = 145
    db.update(size,new_id)
    body3 = db.get_places() # результат после изменения

    db.delete(new_id)
    body4 = db.get_places()
    len_delete = len(body4)

    assert len_after - len_before == 1
    assert body2[5][0] == new_id
    assert body2[5][1] == name
    assert body3[5][2] == size
    assert body3[5][1] == name
    assert body3[5][0] == new_id
    assert len_before == len_delete
