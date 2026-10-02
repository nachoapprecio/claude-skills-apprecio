# Configuración

## Rutas locales

- **Carpeta de conocimiento de Apprecio**: `<PENDIENTE: ruta completa a la carpeta Apprecio>`
  Léela al inicio de cada sesión de AEO. De ahí salen posicionamiento, productos, casos de uso y vocabulario de marca.
- **Registro de prompts**: `<carpeta Apprecio>/aeo/prompts-registry.md`
- **Informes generados**: `<carpeta Apprecio>/aeo/informes/`

Si la carpeta de conocimiento no está en los directorios permitidos, pide la ruta al usuario en vez de improvisar con contexto genérico.

## Carpeta de Drive para los informes

https://drive.google.com/drive/folders/1ADCXPHXD-yXLpXZKfwVVhmV5wLU481D4

El informe se sube ahí como documento compatible con Google Docs (.docx). Si en la sesión no hay forma de escribir en Drive, deja el archivo en `<carpeta Apprecio>/aeo/informes/` y avisa que la subida quedó pendiente.

## Mercados

| País | `location` | `language` | Marca | Notas de vocabulario |
|---|---|---|---|---|
| Chile | Chile | es | Apprecio | "colaboradores", "clima laboral", "fuerza de venta", "canje" |
| Perú | Peru | es | Apprecio | "colaboradores", "incentivos", "reconocimiento laboral" |
| Colombia | Colombia | es | Apprecio | "colaboradores", "bienestar laboral", "salario emocional" |
| México | Mexico | es | **Dcanje** | "colaboradores", "vales", "prestaciones", "clima organizacional" |
| España | Spain | es | Apprecio | "empleados", "retribución flexible", "beneficios sociales", "RRHH" |

México opera con marca propia. Los prompts de México deben estar pensados para que aparezca Dcanje, y el análisis de ese mercado se lee por separado.

España es mercado de entrada, así que la visibilidad parte cerca de cero. No lo trates como un problema de rendimiento durante los primeros ciclos: ahí el objetivo es aparecer, no ganar share of voice.

## Soluciones y su traducción a lenguaje de comprador

Los prompts se escriben con las palabras del comprador, no con los nombres internos de producto.

| Solución | Cómo lo busca la gente |
|---|---|
| Teams Motivation | reconocimiento a empleados, beneficios, clima laboral, cultura, regalos de cumpleaños corporativos |
| Force Manager | incentivos por ventas, concursos comerciales, programas para fuerza de venta, incentivos de canal y distribuidores |
| Smart Loyalty | programas de puntos, fidelización de clientes, recompensas, engagement de clientes |

## Competidores a vigilar

Base internacional: Cobee, Awardco, Bonusly, Workhuman, Reward Gateway.

Completa la lista con los competidores locales por mercado que estén en la carpeta de conocimiento antes de analizar share of voice. Un share of voice calculado contra la lista equivocada lleva a conclusiones equivocadas.

## Registro de prompts

HubSpot guarda `location` en el prompt pero no lo expone como filtro en las métricas. Los filtros disponibles son ICP, producto, tema, idioma, fase del journey y estado de tracking. Para poder analizar por país hay que mantener el registro local.

Formato de cada fila:

```
| promptId | país | fase | tema | texto | fecha de alta | hipótesis |
```

Actualízalo cada vez que se creen prompts, en el mismo turno en que se crean. Si se pierde el registro, la única forma de reconstruir el país es leyendo prompt por prompt en la interfaz de HubSpot.
