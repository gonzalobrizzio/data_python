# data_python
Test de Python 2.7

En qué requerimiento implementarías una cola de mensajes en una solución orientada a datos? Que lenguaje utilizarías y porque?
En un requerimiento que obtengas información en tiempo real, es decir, constantemente, que no sea del tipo batch. Utilizaría Apache Kafka, el cual va dejando los mensajes en una cola y Spark los va tomando, o se podrían trabajar con python estos mensajes siempre y cuando cumpla el requerimiento.

Que experiencia posees sobre py spark o spark scala? Contar breves experiencias, en caso de contar experiencia con otro framework de procesamiento distribuido, dar detalles también.
No tengo experiencia con ninguna de las 2, mi única experiencia actual fue con Spark + Java en un TP integrador de la facultad, donde lo utilizabamos con aplicaciones web

Qué funcionalidad podrías expandir desde el area de ingeniería de datos con una API y arquitectónicamente como lo modelarías?
Implementaría el consumo de los datos (que provienen de Kafka) y realizaría la ingesta con una API la cual derivaría con algún proceso en la generación de datos para distintos reportes (se me ocurrió esto, porque en el laburo lo hago mucho, de traer desde APIs diaramente, y luego modelar algo que le sirva a los chicos de BI/Science para que generen los distintos tableros/reportes que les sean necesarios al cliente)