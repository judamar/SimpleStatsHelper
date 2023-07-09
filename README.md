# SimpleStatsHelper
-------

Un [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) plugin para un ayudante de estadísticas que consulta/ranquea/enumera varias estadísticas usando un marcador.

Versiones disponibles: 1.12 servidores

# Descripción del formato

¡`! !stats` Mostrar información de ayuda

¡`! !stats save` <substitute name> <stat category> <stat content> <title> Guardar un marcador rápido

¡`! !stats del` <sinónimo> Eliminar un marcador rápido

¡`! !stats list` Lista los marcadores rápidos guardados
 
¡`! !stats query` <player> <stat category> <stat content> [<-uuid>] [<-tell>]

¡`! !stats query` <player> <generic name> [<-uuid>] [<-tell>]

¡`! !stats rank` <stat category> <stat content> (-bot) [<-tell>]

¡`! !stats rank` <nombre genérico> (-bot) [<-dicho>]

¡`! !stats scoreboard` <stat category> <stat content> (-bot) (-tell>)

¡`! !stats scoreboard` <nombre del sustituto> Mostrar un marcador rápido

¡`! !stats scoreboard show` Mostrar el marcador de este plugin

¡`! !stats scoreboard hide` Ocultar el marcador del plugin

## Descripción del parámetro

<categoría de estadísticas>: killed, killed_by, dropped, picked_up, used, mined, broken, crafted, custom, killed, <contenido de estadísticas> de killed_by para [bioid]

<stats> para picked_up, used, mined, broken, crafted son item/cube ids

<stats> para custom ver archivo json para stats, o [MC Wiki](https://minecraft.fandom.com/zh/wiki/%E7%BB%9F%E8%AE%A1%E4%BF%A1%E6%81%AF)

Lo anterior no necesita ser prefijado con minecraft

[<-uuid>]: reemplaza el nombre del jugador con uuid; (-bot): estadísticas bot con cam; [<-tell>]: sólo visible para ti mismo

## Ejemplo

¡`! !stats save fly custom aviate_one_cm lista de vuelo`

¡`! !stats query Fallen_Breath used water_bucket` `!

¡`! ``stats rank custom time_since_rest -bot``

¡`! !stats scoreboard mined stone `

# archivo de configuración

`server_path`: ruta para trabajar en el servidor

`world_folder`: La carpeta del archivo. El archivo se encuentra en la ruta de trabajo del servidor

¡`save_world_on_query`: si se usa o no el comando `! !stats query` con el comando `/save-all` para guardar el mundo

¡`save_world_on_rank`: si usar o no el comando `! !stats rank` con la orden `/save-all` para salvar el mundo

¡`save_world_on_scoreboard`: si usar o no el comando `! !stats scoreboard` con la orden `/save-all` para salvar el mundo

`player_name_blacklist`: Una lista de cadenas que almacenan una lista negra de jugadores que se usará para las consultas, los jugadores que se encuentren en ella no serán contados. Cada cadena es una cadena de patrón de expresión regular, pero si el nombre de un jugador coincide con cualquiera de estas cadenas de patrón, ese jugador será ignorado
