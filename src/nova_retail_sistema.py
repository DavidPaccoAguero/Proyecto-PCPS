"""Módulo de gestión de ventas de Nova Retail."""

def validar_stock(stock_actual, cantidad):
    """Verifica si existe stock suficiente."""
    return stock_actual >= cantidad


def calcular_total(cantidad, precio_unitario, igv_porcentaje):
    """Calcula el total de la venta incluyendo IGV."""
    subtotal = precio_unitario * cantidad
    igv = subtotal * igv_porcentaje
    return subtotal + igv


def actualizar_stock(stock_actual, cantidad):
    """Actualiza el stock después de una venta."""
    return stock_actual - cantidad
