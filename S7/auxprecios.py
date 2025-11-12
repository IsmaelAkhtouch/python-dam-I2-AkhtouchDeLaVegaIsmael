
def precio_medio(precios):
    """Devuelve el precio medio de la lista."""
    if not precios:
        return 0
    return sum(precios) / len(precios)


def precio_maximo(precios):
    """Devuelve el precio máximo."""
    if not precios:
        return None
    return max(precios)


def precio_minimo(precios):
    """Devuelve el precio mínimo."""
    if not precios:
        return None
    return min(precios)


def total_precios(precios):
    """Devuelve la suma total de los precios."""
    return sum(precios)


def resumen_precios(precios):
    """Muestra un resumen con todas las métricas."""
    media = precio_medio(precios)
    maximo = precio_maximo(precios)
    minimo = precio_minimo(precios)
    total = total_precios(precios)

    return {
        "Total de productos" : len(precios),
        "Precio total" : round(total,2),
        "Precio medio" : round(media,2),
        "Precio más alto" : round(maximo,2),
        "Precio más bajo" : round(minimo)
    }