from apps.stores.models import db, Store
import pandas as pd


def list_stores():
    return Store.query.all()


def get_store(store_id):
    return Store.query.get(store_id)


def create_store(store_data):
    store = Store(**store_data)
    db.session.add(store)
    db.session.commit()

    return store


def update_store(store_id, store_data):
    store = Store.query.get(store_id)

    if not store:
        return None

    store.name = store_data['name']
    store.location = store_data['location']
    store.owner = store_data['owner']
    store.year_stablished = store_data['year_stablished']
    store.number_employees = store_data['number_employees']

    db.session.commit()

    return store


def delete_store(store_id):

    try:
        store = Store.query.get(store_id)
        db.session.delete(store)
        db.session.commit()
    except:
        db.session.rollback()
        return False

    return True


def import_stores_from_csv(file):

    try:

        data = pd.read_csv(file)

        stores_to_add = []

        for index, row in data.iterrows():

            if row['StoreID'] is None:

                store = Store(
                    name=row['StoreName'],
                    location=row['Location'],
                    owner=row['Owner'],
                    year_stablished=row['EstablishedYear'],
                    number_employees=row['NumberOfEmployees']
                )
                stores_to_add.append(store)

            else:

                store = Store(
                    # aqui teriamos casting diferente de int caso os IDs fossem de outros tipos, como UUIDs
                    id=row['StoreID'],
                    name=row['StoreName'],
                    location=row['Location'],
                    owner=row['Owner'],
                    year_stablished=row['EstablishedYear'],
                    number_employees=row['NumberOfEmployees']
                )
                stores_to_add.append(store)

        # bulk insert para evitar que seja feito o insert de cada row individualmente
        db.session.bulk_save_objects(stores_to_add)
        db.session.commit()
        
        return stores_to_add

    except Exception as e:
        db.session.rollback()
        print(e)
        return None
