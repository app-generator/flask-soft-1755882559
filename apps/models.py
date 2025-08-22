# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Modemler(db.Model):

    __tablename__ = 'Modemler'

    id = db.Column(db.Integer, primary_key=True)

    #__Modemler_FIELDS__
    imei = db.Column(db.Integer, nullable=True)
    serialno = db.Column(db.Integer, nullable=True)
    cpu_serial = db.Column(db.String(255),  nullable=True)
    uptime = db.Column(db.String(255),  nullable=True)
    ip_add = db.Column(db.String(255),  nullable=True)
    hw_versiyon = db.Column(db.Text, nullable=True)
    sw_versiyon = db.Column(db.Text, nullable=True)
    gsm_module_name = db.Column(db.Text, nullable=True)
    gsm_number = db.Column(db.Integer, nullable=True)
    gsm_signal_level = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Modemler_FIELDS__END

    def __init__(self, **kwargs):
        super(Modemler, self).__init__(**kwargs)


class Meters(db.Model):

    __tablename__ = 'Meters'

    id = db.Column(db.Integer, primary_key=True)

    #__Meters_FIELDS__
    serial = db.Column(db.Integer, nullable=True)
    brands = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    #__Meters_FIELDS__END

    def __init__(self, **kwargs):
        super(Meters, self).__init__(**kwargs)


class Load_Profile(db.Model):

    __tablename__ = 'Load_Profile'

    id = db.Column(db.Integer, primary_key=True)

    #__Load_Profile_FIELDS__
    1.8.0 = db.Column(db.Integer, nullable=True)
    5.8.0 = db.Column(db.Integer, nullable=True)
    8.8.0 = db.Column(db.Integer, nullable=True)
    2.8.0 = db.Column(db.Integer, nullable=True)
    6.8.0 = db.Column(db.Integer, nullable=True)
    7.8.0 = db.Column(db.Integer, nullable=True)
    32.7.0 = db.Column(db.Integer, nullable=True)
    52.7.0 = db.Column(db.Integer, nullable=True)
    72.7.0 = db.Column(db.Integer, nullable=True)
    31.7.0 = db.Column(db.Integer, nullable=True)
    51.7.0 = db.Column(db.Integer, nullable=True)
    71.7.0 = db.Column(db.Integer, nullable=True)
    33.7.0 = db.Column(db.Integer, nullable=True)
    53.7.0 = db.Column(db.Integer, nullable=True)
    73.7.0 = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    read_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Load_Profile_FIELDS__END

    def __init__(self, **kwargs):
        super(Load_Profile, self).__init__(**kwargs)


class All_Tariff(db.Model):

    __tablename__ = 'All_Tariff'

    id = db.Column(db.Integer, primary_key=True)

    #__All_Tariff_FIELDS__
    1.8.0 = db.Column(db.Integer, nullable=True)
    5.8.0 = db.Column(db.Integer, nullable=True)
    8.8.0 = db.Column(db.Integer, nullable=True)
    read_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    32.7.0 = db.Column(db.Integer, nullable=True)
    52.7.0 = db.Column(db.Integer, nullable=True)
    72.7.0 = db.Column(db.Integer, nullable=True)

    #__All_Tariff_FIELDS__END

    def __init__(self, **kwargs):
        super(All_Tariff, self).__init__(**kwargs)



#__MODELS__END
