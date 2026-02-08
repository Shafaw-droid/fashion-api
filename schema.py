from flask_restful import fields

from model import Clothing

BrandField = {
    'brand_id': fields.Integer,
    'brand_name': fields.String,
    'brand_country': fields.String,
    'founder_yr': fields.Integer
}

ClothingField = {
    'clothing_id': fields.Integer,
    'clothing_name': fields.String,
    'category': fields.String,
    'size': fields.String,
    'colour': fields.String,
    'price': fields.Float,
    'brand': fields.Nested(BrandField),
}

OutfitField = {
    'outfit_id': fields.Integer,
    'outfit_name': fields.String,
    'occasion': fields.String,
    'season': fields.String,
}

StylingPreferenceField = {
    'preference_id': fields.Integer,
    'preferred_style': fields.String,
    'preferred_color': fields.String,
    'preferred_fit': fields.String,
    'preferred_season': fields.String,
    'budget_range': fields.String,
}

FavoriteBrandField = {
    'favorite_brand_id': fields.Integer,
    'customer_id': fields.Integer,
    'brand': fields.Nested(BrandField),
}

FavoriteClothingField = {
    'favorite_clothing_id': fields.Integer,
    'customer_id': fields.Integer,
    'clothing': fields.Nested(ClothingField)
}

SavedOutfitField = {
    'saved_outfit_id': fields.Integer,
    'customer_id': fields.Integer,
    'outfit': fields.Nested(OutfitField),
}

CustomerField = {
    'customer_id': fields.Integer,
    'customer_name': fields.String,
    'contact': fields.String,
    'gender': fields.String,
    'dob': fields.DateTime,

    'preferences': fields.List(fields.Nested(StylingPreferenceField)),
    'favorite_brands': fields.List(fields.Nested(FavoriteBrandField)),
    'favorite_clothes': fields.List(fields.Nested(FavoriteClothingField)),
    'saved_outfits': fields.List(fields.Nested(SavedOutfitField)),
}
