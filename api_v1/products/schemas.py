# from pydantic import BaseModel, ConfigDict




# class ProductBase(BaseModel):
#     name: str
#     discription: str
#     price: int

# class ProductCreate(BaseModel):
#     pass


# class Product(ProductBase):
#     model_config = ConfigDict(from_attributes=True)
#     id: int
    


from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int