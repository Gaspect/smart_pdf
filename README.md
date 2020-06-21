# Smart Pdf

Un API para el análisis de artículos y documentos científicos no estructurados en formato pdf.

## Requisitos

1. Python  == 3.8
2. Django >= 3.0.5
3. djangorestframework >= 3.11.0
4. PyPDF4 >= 3.4

## Uso

En la carpeta raíz correr el siguiente comando:

```bash
python manage.py runserver
```

## Extender y contribuir

Asuma un conjunto de clases implementadas por usted solo para el propósito de este tutorial.

```python
from extractor_base import extractor

class TitleExtractor(extractor.Extractor):
    class_alias = 'title' # esto se usa para construir la url asociada a la clase

    # el metodo principal que procesa un pdf y devuelve un diccionario con la información.

    def get_info(self, pdf:I)->dict:
        pass # asuma su implementación

class AutorExtractor(extractor.Extractor)):
    class_alias = 'autor'
    def get_info(self, pdf:I)->dict:
        pass # asuma su implementación
```

Para propósito generla estamos haciendo la configuración de las urls en api/urls.py. 
Por las características de la clase Extractor se contruye un conjunto de instancias de forma recursiva.

```python
# Asumiendo que usted importó las clases anteriores
tree = Extractor(TitleExtractor(),AutorExtractor())
urlpatterns = url(tree)
```

El método url construye un listado de urls validos recorriendo el árbol. Saber para propósito general que la información que provee la url es la información del nodo asociado junto a la de sus hijos. (Aceptamos sugerencias con el fin de "automatizar" la integración y contrución de nuevos fragmentos del API)

## Licencia

GNU-GPL, ver el archivo LICENCE

---
Nota: Este archivo aún esta sujeto a cambios a medida que avance el proyecto.
