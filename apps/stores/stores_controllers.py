from flask import Blueprint, jsonify, request, render_template,abort
from apps.stores.stores_service import StoreServices
from apps.stores.serializers import store_serializers

stores_bp = Blueprint('stores', __name__, url_prefix='/stores')

@stores_bp.before_request
def before_request():
    # before request é utilizado para realizar acoes antes de cada requisição
    # pode ser utilizado por exemplo para validacao de tokens de autenticacao/autorizacao
    # a titulo de exemplo, vamos utilizar para mostrar o endpoint e url da requisição
    print('endpoint: %s, url: %s, path: %s' % (
        request.endpoint,
        request.url,
        request.path))


@stores_bp.route('/', methods=['GET'])
def index():
    return render_template(template_name_or_list='csv-import.html')


@stores_bp.route('/import-csv', methods=['POST'])
def import_csv():

    if request.method == 'POST':

        file = request.files['file']

        if file.filename == '':
            return {'message': 'No selected file'}, 400

        response = StoreServices.import_stores_from_csv(file)

        if response and response is not None:
            message = 'Stores imported successfully, imported {} stores'.format(len(response))
            return message, 200

        return abort(500,description="Error importing stores")


@stores_bp.route('/list', methods=['GET'])
def list_stores():

    stores = StoreServices.list_stores()
    return jsonify([store_serializers(store) for store in stores]), 200


@stores_bp.route('/find/<store_id>', methods=['GET'])
def get_store(store_id):

    store = StoreServices.get_store(store_id)

    if not store:
        return abort(404,description="Store not found")

    return jsonify(store_serializers(store)), 200


@stores_bp.route('/create', methods=['POST'])
def create_store():
    if request.method == 'POST':
        store = StoreServices.create_store(request.get_json())

        return {
            'id': store.id,
            'name': store.name,
            'location': store.location,
            'owner': store.owner,
            'year_stablished': store.year_stablished,
            'number_employees': store.number_employees
        }, 201


@stores_bp.route('/update/<store_id>', methods=['PUT'])
def update_store(store_id):
    if request.method == 'PUT':
        store = StoreServices.update_store(store_id, request.get_json())

        if not store:
            return abort(404,description="Store not found")

        return {
            'id': store.id,
            'name': store.name,
            'location': store.location,
            'owner': store.owner,
            'year_stablished': store.year_stablished,
            'number_employees': store.number_employees
        }, 200


@stores_bp.route('/delete/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    if request.method == 'DELETE':
        store = StoreServices.delete_store(store_id)

        if store:
            return {'message': 'Store deleted'}, 200
        else:
             return abort(404,description="Store not found")
