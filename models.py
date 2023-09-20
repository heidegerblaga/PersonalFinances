from sqlalchemy import (create_engine,Column,
                        Integer,String,Date,Float,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (sessionmaker,relationship)
from psql import engine


Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

dbConnection = engine.connect()

print('hehe')

class Shopping(Base):
    __tablename__ = 'outgoings'

    id = Column(Integer, primary_key=True)
    merchant_name = Column('merchant_name', String)
    total = Column('total', Float)
    date = Column('date', Date)
    filename = Column('filename', String)
    products = relationship("Products", back_populates="shopping",
                            cascade="all,delete, delete-orphan")

    def __repr__(self):
        return f'Merchant name: {self.merchant_name} total: {self.total} Date of shopping: {self.date} filename: {self.filename}'


class Products(Base):
    __tablename__ = 'shopping'

    id = Column(Integer, primary_key=True)
    item = Column('item',String)
    price = Column('price',Float)
    quantity = Column('quantity', Float)
    shopping_id = Column(Integer,ForeignKey("shopping.id"))
    shopping = relationship("Shopping",back_populates="products")

class Merchant(Base):
    __tablename__ = 'merchant'

    id = Column(Integer, primary_key=True)
    merchant_name = Column('merchant_name',String)
    









if __name__ == '__main__':
    Base.metadata.create_all(engine)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
