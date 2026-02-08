from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from extension import db
from resources.brands import BrandResource, BrandResourceList
from resources.clothings import ClothingResources, ClothingList
from resources.customers import CustomerResources, CustomerList
from resources.favorite_brands import FavoriteBandResource, FavoriteBrandList
from resources.favorite_clothes import FavoriteClothingResource, FavoriteClothingList
from resources.outfits import OutfitResources, OutfitList
from resources.preferences import PreferenceResource, PreferenceList
from resources.saved_outfits import SavedOutfitResource, SavedOutfitList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate()

migrate.init_app(app, db)

api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(PreferenceResource, '/api/preferences/')
api.add_resource(PreferenceList, '/api/preferences/<int:preference_id>')
api.add_resource(OutfitResources, '/api/outfits/')
api.add_resource(OutfitList, '/api/outfits/<int:outfit_id>')
api.add_resource(CustomerResources, '/api/customers/')
api.add_resource(CustomerList, '/api/customers/<int:customer_id>')
api.add_resource(ClothingResources, '/api/clothing/')
api.add_resource(ClothingList, '/api/clothing/<int:clothing_id>')
api.add_resource(BrandResource, '/api/brands/')
api.add_resource(BrandResourceList, '/api/brands/<int:brand_id>')
api.add_resource(FavoriteBandResource, '/api/favorite_brands/')
api.add_resource(FavoriteBrandList, '/api/favorite_brands/<int:favorite_brand_id>')
api.add_resource(FavoriteClothingResource, '/api/favorite_clothes/')
api.add_resource(FavoriteClothingList, '/api/favorite_clothes/<int:favorite_clothing_id>')
api.add_resource(SavedOutfitResource, '/api/saved_outfits/')
api.add_resource(SavedOutfitList, '/api/saved_outfits/<int:saved_outfit_id>')

if __name__ == '__main__':
    app.run(debug=True)
