def test_storage_write_read():
    from arca_memory.storage import save_phase, load_phase
    save_phase("quantum", "neutral")
    assert load_phase("quantum") == "neutral"
