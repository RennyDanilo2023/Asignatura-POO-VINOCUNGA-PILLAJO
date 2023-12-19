class Restaurant:
    """
    Clase para representar un restaurante con una lista de mesas y un menú.
    Permite a los clientes hacer una reserva de mesa y realizar pedidos de alimentos.
    """
    
    def __init__(self, name):
        self.name = name
        self.tables = [Table(i+1) for i in range(10)]  # 10 mesas para el ejemplo
        self.menu = {
            'Pizza': 10.00,
            'Pasta': 8.50,
            'Ensalada': 5.00
        }
    
    def reserve_table(self, table_number):
        """ Reserva una mesa si está disponible. """
        if self.tables[table_number - 1].is_available:
            self.tables[table_number - 1].reserve()
            return f"Mesa {table_number} reservada con éxito."
        else:
            return f"Mesa {table_number} ya está reservada."
    
    def order_food(self, table_number, food_item):
        """ Realiza un pedido de comida si el artículo está en el menú. """
        if food_item in self.menu:
            self.tables[table_number - 1].order.append((food_item, self.menu[food_item]))
            return f"Pedido de {food_item} para la mesa {table_number} realizado."
        else:
            return f"El artículo {food_item} no está en el menú."


class Table:
    """
    Clase para representar una mesa en el restaurante.
    Mantiene el estado de la reserva y los pedidos realizados.
    """
    
    def __init__(self, number):
        self.number = number
        self.is_available = True
        self.order = []
    
    def reserve(self):
        """ Marca la mesa como reservada. """
        self.is_available = False
    
    def release(self):
        """ Libera la mesa y la marca como disponible. """
        self.is_available = True
        self.order.clear()


# Ejemplo de uso de las clases:
# Crear un restaurante
my_restaurant = Restaurant("La Buena Mesa")

# Reservar una mesa
print(my_restaurant.reserve_table(5))

# Hacer un pedido de comida
print(my_restaurant.order_food(5, 'Pizza'))

# Hacer otro pedido en la misma mesa
print(my_restaurant.order_food(5, 'Ensalada'))

# Intentar reservar una mesa ya reservada
print(my_restaurant.reserve_table(5))

# Ver los pedidos de una mesa
print(f"Pedidos para la mesa 5: {my_restaurant.tables[4].order}")
