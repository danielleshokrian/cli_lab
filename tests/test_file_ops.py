import os
import tempfile
from file_ops import save_json, load_json

def test_save_and_load_json():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    filepath = tmp.name
    tmp.close()

    data = [{"id": 1, "name": "Alice"}]
    save_json(filepath, data)

    loaded = load_json(filepath)
    assert loaded == data

    os.remove(filepath)

def test_load_nonexistent_file():
    data = load_json("nonexistent.json")
    assert data == []
