class Product:
    def __init__(self, name, price, description, product_link, brand):
        self.name = name
        self.price = price
        self.description = description
        self.product_link = product_link
        self.brand = brand

    def __str__(self):
        return (f"Produto: {self.name}\n"
                f"Marca: {self.brand}\n"
                f"Preço: {self.price}\n"
                f"Descrição: {self.description}\n"
                f"Link: {self.product_link}\n"
                f"{'-' * 40}")