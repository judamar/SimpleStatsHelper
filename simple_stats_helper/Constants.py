ServerPath = 'server/'
WorldPath = ServerPath + 'world/'
Prefix = '!!stats'
PluginName = 'SimpleStatsHelper'
ScoreboardName = PluginName
UUIDFile = 'plugins/' + PluginName + '/uuid.json'
RankAmount = 15
rankColor = ['§b', '§d', '§e', '§f']
HelpMessage = '''------MCD SimpleStatsHelper v1.0------
Plugin para las estadisticas, de locos
§a【Formato】§r
§7''' + Prefix + '''§r Mostrar informacion de ayuda
§7''' + Prefix + ''' query §b[Jugador] §6[Categoria] §e[Estadistica] §7(-uuid)§r §7(-tell)§r
§7''' + Prefix + ''' rank §6[Categoria] §e[Contenido] §7(-bot)§r §7(-tell)§r
§7''' + Prefix + ''' scoreboard §6[Categoria] §e[Contenido] §7(-bot)§r
§7''' + Prefix + ''' scoreboard show§r Mostrar la scoreboard
§7''' + Prefix + ''' scoreboard hide§r Ocultar la scoreboard
§7''' + Prefix + ''' refreshUUID§r Actualizar la lista de UUID del jugador, Usar despues de recargar el complemento.
§a【Descripcion de parametros】§r
§6[Categorias:]§r: §6killEntity§r, §6drop§r, §6pickup§r, §6useItem§r, §6mineBlock§r, §6breakItem§r, §6craft§r
El contenido anterior no necesita tener el prefijo Minecraft.
§7(-uuid)§r: Reemplazar el nombre del jugador con uuid; §7(-bot)§r: Estadisticas de bot; §7(-tell)§r: Solo visible para ti; §7(-all)§r: Listar todos los elementos
§a【Ejemplos】§r
§7''' + Prefix + ''' query §bjudamar §6useItem §ewater_bucket§r
§7''' + Prefix + ''' rank §6custom §etime_since_rest §7-bot§r
§7''' + Prefix + ''' scoreboard §6mineBlock §estone§r
'''