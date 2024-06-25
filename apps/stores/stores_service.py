from apps.stores import stores_repository

class StoreServices:
    def list_stores():
        return stores_repository.list_stores()

    def get_store(store_id):
        return stores_repository.get_store(store_id)

    def create_store(store_data):
        return stores_repository.create_store(store_data)

    def update_store(store_id, store_data):
        return stores_repository.update_store(store_id, store_data)

    def delete_store(store_id):
        return stores_repository.delete_store(store_id)

    def import_stores_from_csv(file):
        return stores_repository.import_stores_from_csv(file)