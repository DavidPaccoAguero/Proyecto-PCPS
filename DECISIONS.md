# DECISIONS

| Fecha | Decisión | Justificación |
|---------|---------|---------|
| 06/10/2026 | Agregar una descripción general al inicio del módulo `nova_retail_sistema.py`. | El módulo no contaba con documentación que explicara su propósito. Se añadió una docstring para mejorar la comprensión y mantenibilidad del código. |
| 06/10/2026 | Analizar las responsabilidades de la función `procesar_venta()`. | Se identificó que la función realizaba validación de stock, cálculo de ventas y actualización de inventario, concentrando múltiples responsabilidades. |
| 06/10/2026 | Crear la función `validar_stock()`. | La validación de stock constituye una responsabilidad independiente que puede reutilizarse y probarse de manera aislada. |
| 06/10/2026 | Crear la función `calcular_total()`. | El cálculo del subtotal, IGV y total corresponde a una responsabilidad distinta de la validación y la gestión de inventario. |
| 06/10/2026 | Crear la función `actualizar_stock()`. | La actualización de inventario representa una responsabilidad específica que debe mantenerse separada del resto de operaciones. |
| 06/10/2026 | Aplicar el Principio de Responsabilidad Única (SRP). | Se buscó que cada función tenga una única responsabilidad y un único motivo para cambiar. |
| 06/10/2026 | Eliminar la mezcla entre lógica de negocio y salida por consola. | Se retiraron las instrucciones `print()` para que las funciones únicamente se encarguen del procesamiento de datos. |
| 06/10/2026 | Incorporar docstrings en cada función. | Se documentó el propósito de cada función para facilitar la comprensión, el mantenimiento y la generación de documentación técnica. |
| 06/10/2026 | Reemplazar una función compleja por funciones especializadas. | Cuando una función realiza demasiadas tareas resulta más difícil de entender, más difícil de mantener y más difícil de probar mediante pruebas unitarias. |
