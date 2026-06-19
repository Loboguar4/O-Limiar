# O LIMIAR ~~ v2.3.1
### *Dungeon Crawl RPG de Terminal*

<pre>
.........:......:..
.......:..........                               ......
......::... .::...                            .............
.......:....::...                           ................
......:..::::....                          ...:..::.:........
.....::^::.::...                           ..::..::::....:....
.......:::..:...                          ..::::.:.::.....:..:.
..:...:::::::...                          ...::::::::...:.:.....
...::.:..:^^:.:..                      ....     .::::...::::..::.
:::.:...^:^7!:::.                    .....       .....:::::::.:::.
.::::...:^~!7^...                      ...       .    .::::::::::::.
.:::::..:^^~!~:.::                     ......   ..::.   ::::::::..::..
:.:~......:::^!^:^~.                   . ..::.    :~~:  .:^:::::...::::::..
::::...  ...::^~^^^.               .   ..  ....   .:^:   ..:::::.:::::::::::..
:^^^::^:. .^^.. .:.              .::.  ..      .            .:..:..:::::::::::.
:::::~~~~....  :!.              .::::. ......    .. ... ... ..::........:::..:.
:::^^^::~!.   .7:              .::::...............................::::.......:.
:^^~^:.:^^.:^~~~.             .::::................:...............:::....::...:.
..::^^..::~~~7!^.            .:::.. .....................................:::::::.
....:.:.^:~7!?J7.          ..:... . .............:.........::.::.::::::::::::::.:.
:.::^::~~~^^^!77^         .:.........   ............::...:::::::.....:::::::::::::
:::^^^:!^::^:!~!^        ..........  ...:^::::... ..........::::::::::......::::::.
^^^^::.~^:^~~^:!:       .......     ...::7^~::.....  .......::::::::::::.:....::::.
::^:::::^^:!~:^~      .........     ...^^!^~:........ .........::::::::::....::::::.
:^^::^^:^~~!^^!^     .....:.. .     ...:^^~~^.......... .........:::::..::::.....:::
.::^^:::^~^^^~7~.    .....:...     .....^:^~~:..........   ..........::....:::::::::.
.^^~!:::~^^^^~!~:     ...::...     .....^^^~~:...........     .........::::.:::::::::.
.:^^~!^:!!~~~^::.     ...::...     .....^^^~~^...................::::::.:::::::::::::.
....:^!7777~~^^!      ...::...     .....^^^~~^.............::::....:::::.::::::::::.:.
....:^^!???7!~~!.     ..:::....   ......::..::.::..::.::::::.................:..:::..
.....:^^??7!7!!!^     ..:::....   ........:^:...............        .........:....::.
::...:^!??!!~~~!~     ..:.:...  . .......::.............            ......:........:.
^~^:...^7?~:::~~:     ...:....... ....................     . ...... ......:..:.....:.
^~~~~:..^!^..:~^^.    ...:........................      . .......... ......:.:.......
:~!!!^:..!~:^~~~7.    ...:............ .......:...   ......:::................:.:....
:~!77!:.:^~^^77^:     ...:...........  ...^:.~!.   ...:.::.:.:::............:.:......
~^~!7!^^!~^:^7Y~.     ...:.............  :^:~!!.  .:..:..:.::::..... .......::.......
~~~!77!~~7!!^~J^.     ...:...........:.  .~~!!!:.........:.:::..............:.......
~~~!!~7!~7?!:!Y7:     ..::..........::....~~~!!^...:.....:..::::::......:.:..:::....
~~^^^:!7!?77!?JY?...  ..::..........:.....^~~!!~........:::.:::::....::.:.:.::::....
~!^:^::~77?777J?J7.......:................:~~!!~...:..:.:::.:::::.:..::.:..::.::...    .
:!?~::!7!~7J77??Y7.................::.....:~~!!!:..::::.:::.:::::::..:.....::.::::.             ....
:^7J7~~!77!7777?JJ?. ..............:.......~~!!!^..:::::.::.:::::::..:.:...:::::::. ....     .......
~^^!7?~^!J77!7JJ?JJ! .......:..........:...~!!!!^..::::.....:::::::.::.....::::::...................
^~~^:~7~~77!!!???77:....:..............:.:.^!!7!~..::::.....:::::::.::....::::::::..................
</pre>

---

As nações civilizadas foram destruídas. Sem mais impérios dinásticos, sem mais colônias. O mundo se tornou tribal e bárbaro novamente.

Pode um lugar tão isolado e geograficamente inabitável afetar uma ordem mundial inteira? Talvez, com conhecimento oculto e entendimento dos limiares entre diferentes mundos. Tudo está naquele lugar, como diz em lendas e canções, em diversos continentes.

Nenhuma grande expedição conseguiu encontrar o Limiar do Mundo. Alguns médiuns e astrólogos acreditam que o portão do Limiar só se abre para peregrinos suficientemente acostumados com o isolamento nas cordilheiras de rochas negras, ricas em metais pesados e musgos comestíveis. E desses, nenhum acaba retornando.

---

## Instalação e Execução

**Requisitos:** Python 3.10+, terminal com suporte a Unicode (recomendado: fonte SimSun-ExtG ≤ 20pt).

```bash
git clone https://github.com/Loboguar4/O-Limiar.git
cd O-Limiar
python main.py
```

Sem dependências externas além da biblioteca padrão do Python.

---

## Sobre o Jogo

**O Limiar** é um dungeon crawler RPG rodando inteiramente no terminal, escrito em Python. Inspirado em Rogue (1980), une geração procedural de labirintos e combate tático por turnos. Solitário e punitivo.

O jogador acorda diante de um portão de pedra negra. Um ser sem nome — o Porteiro do Limiar — aguardava. As masmorras abaixo não são reais da forma que o mundo entende realidade: são uma armadilha viva tecida em torno do Olho de Vecna, um artefato que se tornou autoconsciente e consome almas.

A única saída é descer. Encontrar o Olho. E destruí-lo.

Não há level up. A dificuldade escala com a profundidade. Cada run dura em torno de 35 a 60 minutos — curta, imprevisível, brutal.

---

## Classes e Subclasses

| Classe | Subclasse | Estilo de Jogo |
|---|---|---|
| **Guerreiro** | Bárbaro | Dano bruto, Fúria Berserker, alta resistência |
| **Guerreiro** | Cavaleiro | Disciplina, Contra-Ataque passivo, Golpes Sequenciais |
| **Mago** | Mago Azul | Suporte arcano, Toque de Cura, Canal Vital passivo |
| **Mago** | Mago Negro | Drenar Vida, Onda de Almas, necromancia e maldição |
| **Ladino** | Ladrão | Furtividade, Evasão, recursos e oportunismo |
| **Ladino** | Assassino | Golpe Sorrateiro, Veneno na Lâmina, críticos 19–20 |

---

## Sistema de Combate

- Combate por turnos: Atacar, Habilidade/Magia, Usar Item, Fugir
- **Comandos inválidos consomem o turno** — cooldowns avançam
- Críticos (20 natural), armaduras, resistências mágicas e imunidades por tipo de inimigo
- DoTs (veneno, sangramento, fogo, choque) processados por turno
- Emboscada: inimigo que alcança o jogador na exploração ataca primeiro

### Habilidades Especiais

| Habilidade | Classe | Efeito |
|---|---|---|
| Investida Feroz | Guerreiro | 2d+arma×2, +3 acerto, -2 CA; usa bônus do Elmo da Fúria |
| Golpes Sequenciais | Guerreiro | 3 golpes independentes |
| Contra-Ataque | Cavaleiro | Revida automaticamente o próximo ataque; cooldown 4t |
| Golpe Sorrateiro | Ladino | 2d+arma+d8, 70% de envenenar |
| Evasão | Ladino | 60% de desviar os próximos 3 ataques |
| Veneno na Lâmina | Ladino | Golpe + veneno potente + 3 ataques seguintes envenenam |

---

## Sistema de Magia

Magias disponíveis via menu dinâmico por subclasse e grimórios equipados.

| Magia | Quem pode | Condição |
|---|---|---|
| Míssil Mágico | Todos os Magos | sempre |
| Explosão Arcana | Todos os Magos | sempre (AoE range 2) |
| Onda de Almas | **Mago Negro** | Grimório das Almas equipado |
| Colapso | Todos os Magos | Grimório do Colapso equipado |
| Toque de Cura | **Mago Azul** | subclasse |
| Drenar Vida | **Mago Negro** | subclasse |
| Maldição | **Mago Negro** | Grimório da Maldição equipado |
| Bola de Fogo | Todos os Magos | Cajado do Fogo + Códice Elemental |
| Inverno Netuniano | Todos os Magos | Cajado de Gelo + Códice Elemental |
| Relâmpago | Todos os Magos | Manoplas do Trovão + Códice Elemental |
| Portal | Todos os Magos | Grimório Portal equipado |

**Canal Vital (Mago Azul):** passivo padrão +2 HP/feitiço. Dom na sessão zero reforça para +4 HP/feitiço.

---

## Labirinto e Progressão

| Andar | Inimigos presentes |
|---|---|
| 1–2 | Ratos, Goblins, Esqueletos, Vermes, Carnicais |
| 3–4 | Orcs, Arqueiros das Trevas |
| 5–7 | Gárgulas, Campeões da Morte, Sacerdote †, Arautos |
| 8+ | Cavaleiros, Dracolich †, Serpente Abissal †, Espectros |
| Andar 7–10+ | **Modo Extremo** ativado progressivamente |
| Andar 14+ | **Olho de Vecna** pode surgir |

† Inimigo único por run — aparece no máximo uma vez.

---

## Chefes Secundários (Únicos por Run)

| Chefe | Drop garantido | Bônus permanente |
|---|---|---|
| **Sacerdote Devorador** | Grimório das Almas +N | +30% HP máximo do Sacerdote |
| **Serpente Abissal** | Presa Abissal +N | +20% HP máximo da Serpente |
| **Dracolich** | Cristal da Vingança Dracônica | — |
| **Cavaleiro Sem Nome** | Espada dos Mártires +N, Espada Fantasma +N ou Lâmina Drenante +N | — |

---

## Modo Extremo da Dungeon

A partir do andar 7, as profundezas mudam. Uma narrativa ao estilo da sessão zero anuncia a transição: nome da zona corrompida, frases atmosféricas com delay, alertas mecânicos. Altares de sangue surgem já a partir da dificuldade 30.

- Andar 7–8: 40% de chance por sala nova
- Andar 9: 70% de chance
- Andar 10+: garantido

---

## Itens e Armas

### Armas Notáveis

| Arma | Efeito |
|---|---|
| Arco Élfico | Range 3, disparo duplo 20–50% por classe |
| Machado Anão Flamejante | DoT de fogo, crítico elemental |
| Espada Fantasma | Ignora CA; 25–45% aterrorizar |
| Cajado de Gelo | Só Magos; crítico paralisa 1t |
| Cajado do Fogo Descendente | Só Magos; fogo passivo + DoT. Com Códice: Bola de Fogo |
| Presa Abissal *(lendária)* | Drop da Serpente Abissal; veneno duplo escalável em todo ataque |

### Equipamentos e Consumíveis

| Item | Efeito |
|---|---|
| Talismã Protetor | Equipa na build; absorve 1 crítico (dano > 10 → 3); quebra ao usar. Empilhável |
| Cristal da Vingança Dracônica | Drop do Dracolich; enfraquece o Olho de Vecna em combate |
| Pergaminho de Proteção | +CA por 8 rodadas |
| Elmo da Fúria | Durabilidade [dur:N] visível na bolsa; preservada ao desequipar |
| Botas do Caçador de Monstros | 30% resistir a veneno, maldição e paralisia |
| Elmo do Caçador de Monstros | +2 CA; 25% dissipar controle mágico |
| Botas Encantadas | Só Magos; +8% poder mágico total |
| Códice dos Segredos Elementais | Desbloqueia Bola de Fogo, Inverno Netuniano e Relâmpago |
| Chapéu Cósmico | Slot de elmo; 25% absorver ataques e magias para o vazio cósmico |

### Slots Exclusivos (1 por build)

Botas, Elmo, Armadura e Capa/Manto têm slot exclusivo. Ao equipar um segundo item do mesmo slot, o jogo pergunta qual substituir.

---

## Estruturas Especiais

| Estrutura | Efeito |
|---|---|
| Altar Antigo | Cura HP ou concede bônus espiritual |
| Altar de Sangue | Late game (dif >= 30); buffs fortes com custo de HP |
| Círculo Mágico | Restaura magia e +INT para Magos |
| Estátua Enigmática | 35–70% de spawnar item raro |
| Portal do Vazio | Teleporta para sala com escada de descida |

---

## Sistema de Save / Load

Saves em JSON em `~/.o_limiar/saves/`. Preserva personagem, posição, topologia de andares, inimigos únicos já derrotados e modo extremo.

---

## Inimigos

| Tier | Inimigos | Andares |
|---|---|---|
| 1 | Rato Carniceiro, Goblin Furtivo, Esqueleto Guardião, Verme das Entranhas, Carniçal | 1+ (persiste) |
| 2 | Orc Berserker, Arqueiro das Trevas | 3+ |
| 3 | Sacerdote Devorador †, Arauto do Vazio, Gárgula de Pedra, Campeão da Morte | 5+ |
| 4 | Cavaleiro Sem Nome, Serpente Abissal †, Dracolich †, Espectro das Profundezas | 8+ |
| Chefe | **Olho de Vecna** | Andar 21+ |

† Único por run.

---

## Notas de Atualização

### v2.3.1 — Escadarias e Elmo da Fúria

**Escadarias ao Carregar Jogo:** Bug corrigido. Escadarias de subida e de descida são garantidos agora ao cerregar jogo.

**Elmo da Fúria:** Persistência de durabilidade corrigida. Swaps não permitem mais resetar status do Elmo.

### v2.3.0 — Chefes, Modo Extremo e Refinamentos (atual)

**Inimigos únicos:** Dracolich, Serpente Abissal e Sacerdote Devorador aparecem no máximo uma vez por run. Registrados em `_unicos_spawados`, persistido no save.

**Drops de chefes:** itens lendários garantidos ao derrotar cada chefe secundário. Sacerdote e Serpente transferem bônus permanente de HP.

**Novos itens lendários:** Presa Abissal (veneno duplo escalável) e Cristal da Vingança Dracônica (enfraquece o Olho de Vecna).

**Modo extremo narrativo:** trigger corrigido para andares profundos. Sequência ao estilo sessão zero com `NOMES_REGIOES_EXTREMAS` e `DESCRICOES_EXTREMAS`. Trigger: andar 7–8 (40%), andar 9 (70%), andar 10+ (garantido).

**Elmo da Fúria — medidor [dur:N]:** durabilidade visível na bolsa. Swap e desequipar preservam o contador.

**Diário Perdido:** surge a partir do andar 3. Chance 40–55%.

**Portal do Vazio:** teleporta à sala com escada de descida. `KeyError` corrigido via `mapa_estrutura_ref`.

**Talismã Protetor:** interceptado no loop de combate. Multi-talismã: ao quebrar, ativa o próximo automaticamente.

### v2.2.0 — Sistema de Magia e Novos Itens

Sistema de magia refatorado. Exclusividades por subclasse. Novos grimórios elementais. Slots exclusivos de equipamento.

### v2.1.1 — Itens, Arcos e Spawn

Elmo da Fúria com narração. Pedra de Afiar refatorada. Sistema de arco aprimorado. Hierarquia de tier reforçada.

### v2.0.0 — O Limiar

Renomeado de *Masmorras Liminares*. Menu principal com ASCII. Save/Load completo.

---

## Créditos

**Desenvolvido por Bandeirinha**  
Para apoiar: pixgg.com/bandeirinha  
Licença: GNU GPL v3.0 ou posterior

---

*"Ninguém jamais retornou."*
