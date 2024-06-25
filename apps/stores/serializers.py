    # pode ser utilizado alguma biblioteca de serialização de dados, no caso optei
    # por fazer manualmente.
def store_serializers(store):
    return {
        'id': store.id,
        'name': store.name,
        'location': store.location,
        'owner': store.owner,
        'year_stablished': store.year_stablished,
        'number_employees': store.number_employees
    }