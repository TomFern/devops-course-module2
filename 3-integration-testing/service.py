from datastore import store_value, get_value

def process_and_store(key, raw_value):
    processed_value = raw_value.strip().upper()
    store_value(key, processed_value)
    return processed_value

def retrieve_processed(key):
    value = get_value(key)
    return value.lower() if value else None
