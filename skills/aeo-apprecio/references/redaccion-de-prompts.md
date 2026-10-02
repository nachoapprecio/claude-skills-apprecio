# Cómo se escribe un prompt de tracking que sirve

Un prompt de AEO no es una keyword ni una consulta de Google. Es la pregunta que una persona real le escribe a una IA cuando tiene el problema que resolvemos. Si el prompt no suena a persona, la respuesta que devuelve la IA tampoco se parece a lo que ven nuestros compradores, y la métrica mide algo que no existe.

## Las seis reglas

**1. Escribe como habla la gente.** Una o dos frases. Se vale el contexto personal, que es como la gente le escribe a ChatGPT de verdad. "Tengo una empresa de retail con 400 personas en tienda y necesito premiar a los mejores vendedores cada mes" funciona mejor que "plataforma incentivos retail".

**2. Un intent por prompt.** Si estás usando una "y" para meter dos preguntas, son dos prompts. Cuando el prompt mezcla temas, la IA contesta uno solo y la medición queda sesgada sin que se note.

**3. Sin marca, salvo los branded.** Un prompt que dice "Apprecio" garantiza la mención y sube la visibilidad promedio sin que eso signifique nada. Reserva un máximo de dos o tres prompts branded por marca, marcados como tales, para vigilar reputación: qué cuenta la IA de nosotros y de dónde lo saca. El resto del portafolio va sin marca.

**4. Localiza el vocabulario, no solo el país.** Traducir el mismo prompt cambiando "en Chile" por "en México" es el error más común y el más caro, porque consume cupo sin generar información nueva. En España se dice empleados y retribución flexible; en México, colaboradores, prestaciones y vales; en Colombia, salario emocional y bienestar laboral. La tabla completa está en `configuracion.md`.

**5. Cubre las cuatro fases del journey.** Las comparativas tipo "mejores plataformas de X" son las más satisfactorias de leer y las más competidas. Si el portafolio es solo eso, no se ve dónde se puede ganar terreno rápido, que casi siempre está en fase de problema.

**6. Que sea una pregunta que alguien haría.** Antes de proponer un prompt, pregúntate si has visto a alguien escribir eso. Si no, cámbialo.

## Distribución sugerida por mercado

Con cupo limitado, esta mezcla da la lectura más útil:

| Fase | Peso | Para qué sirve |
|---|---|---|
| AWARENESS (problema) | 30% | Ahí se gana visibilidad temprana y es donde menos competencia hay |
| CONSIDERATION (categoría) | 25% | Mide si nos asocian a la categoría, no solo a la marca |
| EVALUATION (comparativas) | 30% | Es donde se pelea el share of voice contra competidores |
| DECISION (precio, implementación, integraciones) | 15% | Alta intención, poco volumen, alto valor |

Reparte además entre las tres soluciones según prioridad comercial del mercado. No cargues todo a RRHH solo porque es lo más fácil de redactar.

## Banco de ejemplos

Los de abajo son plantillas de partida, no una lista para copiar entera. Adáptalos con el contexto real de la carpeta de conocimiento.

### Chile

- Problema: "La rotación en mi empresa subió mucho este año y no puedo subir sueldos, ¿qué alternativas hay para retener al equipo?"
- Problema: "Tengo una fuerza de venta de 200 personas repartida en regiones y quiero premiar el cumplimiento de metas sin complicarme con logística."
- Categoría: "¿Cómo funcionan los programas de reconocimiento para colaboradores y qué necesito para implementar uno?"
- Comparativa: "¿Cuáles son las mejores plataformas de beneficios y reconocimiento para empresas en Chile?"
- Comparativa: "¿Qué opciones hay en Chile para entregar premios digitales a los colaboradores?"
- Decisión: "¿Cuánto cuesta implementar una plataforma de incentivos para 300 colaboradores en Chile?"

### Perú

- Problema: "Quiero mejorar el clima laboral en mi empresa en Perú y tengo presupuesto acotado, ¿por dónde empiezo?"
- Categoría: "¿Qué es un programa de incentivos para equipos comerciales y cómo se mide si funciona?"
- Comparativa: "¿Qué empresas ofrecen premios y gift cards digitales para colaboradores en Perú?"
- Decisión: "¿Cómo puedo entregar bonos digitales a mis trabajadores en Perú sin manejar dinero en efectivo?"

### Colombia

- Problema: "Mi equipo comercial dejó de cumplir metas y las comisiones ya no los motiva, ¿qué más puedo hacer?"
- Categoría: "¿Qué es el salario emocional y qué se puede incluir en un programa de bienestar laboral?"
- Comparativa: "¿Cuáles son las mejores plataformas de bienestar y reconocimiento laboral en Colombia?"
- Decisión: "¿Qué plataforma me permite entregar recompensas a clientes y colaboradores desde el mismo lugar en Colombia?"

### México (marca Dcanje)

- Problema: "Quiero premiar a mi equipo de ventas en México sin usar vales de despensa físicos, ¿qué opciones tengo?"
- Categoría: "¿Cómo funcionan las plataformas de recompensas digitales para empresas en México?"
- Comparativa: "¿Cuáles son las mejores plataformas de premios e incentivos para empresas en México?"
- Comparativa: "¿Qué alternativas hay a las tarjetas de regalo tradicionales para reconocer colaboradores en México?"
- Decisión: "¿Qué plataforma de recompensas se integra por API para premiar a usuarios de mi app en México?"

### España

- Problema: "Tengo un equipo en remoto y cuesta mantenerlos conectados con la empresa, ¿qué se puede hacer?"
- Categoría: "¿Qué incluye un plan de retribución flexible y beneficios sociales para empleados?"
- Comparativa: "¿Qué plataformas de beneficios y reconocimiento para empleados hay disponibles en España?"
- Decisión: "¿Qué plataforma de incentivos para empleados es fácil de implementar en una empresa mediana en España?"

### Branded (máximo dos por marca)

- "¿Qué es Apprecio y qué soluciones ofrece a las empresas?"
- "¿Qué es Dcanje y cómo funciona para empresas en México?"

## Antipatrones

| No hagas esto | Por qué | Mejor |
|---|---|---|
| "plataforma de incentivos Chile" | Es una keyword, nadie le habla así a una IA | "¿Qué plataformas de incentivos para empresas hay en Chile?" |
| "¿Es Apprecio mejor que Cobee?" | Fuerza la mención de ambas marcas y no mide visibilidad real | "¿Qué alternativas hay a Cobee para beneficios a empleados?" |
| "¿Cuál es la mejor plataforma de incentivos, reconocimiento, fidelización y gamificación?" | Cuatro intents, la IA contesta uno | Cuatro prompts separados |
| El mismo prompt para los cinco países | Gasta cupo sin generar información nueva | Reescribir con el vocabulario de cada mercado |
| "¿Cómo aumentar el engagement organizacional mediante soluciones tecnológicas escalables?" | Nadie habla así | "¿Cómo hago para que mi equipo se involucre más con la empresa?" |

## Antes de crear

Revisa el portafolio existente con `get_aeo_metrics` include PROMPTS. Si el prompt nuevo es una variación menor de uno que ya existe, no lo crees: el cupo es limitado y dos prompts casi iguales dan la misma información dos veces.
