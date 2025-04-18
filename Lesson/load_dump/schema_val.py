from marshmallow import Schema, fields, ValidationError
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="club.log",
    filemode="a",
    encoding="utf-8",
)


class ExpectedSchema(Schema):
    club_name = fields.String(required=True)
    club_country = fields.String(required=True)
    club_value = fields.Integer(required=False)
    club_owner = fields.String(required=True)
    club_president = fields.String(required=True)
    club_manager = fields.String(required=True)
