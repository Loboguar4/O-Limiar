# O LIMIAR ~~ v2.2.0
### *Dungeon Crawl RPG de Terminal*

> *"Ninguém jamais retornou."*

**O Limiar** é um dungeon crawler RPG rodando inteiramente no terminal, escrito em Python. Inspirado em Rogue (1980), o jogo une geração procedural de labirintos, combate tático por turnos e atmosfera Dark Fantasy / Cosmic Horror numa aventura solitária e punitiva pelas profundezas de uma masmorra que parece ter vontade própria.

---

## Instalação e Execução

**Requisitos:** Python 3.10+, terminal com suporte a Unicode (recomendado: fonte SimSun-ExtG ≤ 20pt para melhor visualização das ASCII arts).

```bash
git clone https://github.com/Loboguar4/O-Limiar.git
cd O-Limiar
python main.py
```

Sem dependências externas além da biblioteca padrão do Python.

---

## Sobre o Jogo

O jogador acorda diante de um portão de pedra negra. Um ser sem nome — o Porteiro do Limiar — aguardava. Não por acidente. As masmorras abaixo não são reais da forma que o mundo entende realidade: são uma armadilha viva tecida em torno do Olho de Vecna, um artefato que se tornou autoconsciente e consome almas.

A única saída é descer. Encontrar o Olho. E destruí-lo.

Não há sistema de level up. A dificuldade escala com a profundidade. Cada run dura em torno de 35 a 60 minutos — curta, imprevisível, brutal.

---

## Classes e Subclasses

| Classe | Subclasse | Estilo de Jogo |
|---|---|---|
| **Guerreiro** | Bárbaro | Dano bruto, Fúria Berserker, resistência alta |
| **Guerreiro** | Cavaleiro | Disciplina, Contra-Ataque passivo, Golpes Sequenciais |
| **Mago** | Mago Azul | Suporte arcano, Toque de Cura, poder elemental |
| **Mago** | Mago Negro | Drenar Vida, Onda de Almas, necromancia |
| **Ladino** | Ladrão | Furtividade, Evasão, recursos e oportunismo |
| **Ladino** | Assassino | Golpe Sorrateiro, Veneno na Lâmina, críticos 19–20 |

Cada classe possui habilidades únicas com cooldown, efeitos dependentes de arma e bônus variáveis por subclasse em itens especiais (ex: Arco Élfico dá 50% de disparo duplo para o Ladino, 35% para o Guerreiro, 20% para o Mago).

---

## Sistema de Combate

- Combate por turnos com menu de ações: Atacar, Habilidade/Magia, Usar Item, Fugir
- **Comandos inválidos consomem o turno** — cooldowns avançam
- Armas com efeitos passivos por classe (fogo, choque, veneno, drenagem, sangramento, terror)
- Críticos (20 natural), armaduras, resistências mágicas e imunidades por tipo de inimigo
- DoTs (veneno, sangramento, fogo, choque) processados no início de cada round
- Emboscada: inimigo que alcança o jogador na exploração ataca primeiro, com tela dedicada de aviso

### Habilidades Especiais

| Habilidade | Classe | Efeito |
|---|---|---|
| Investida Feroz | Guerreiro / Bárbaro | 2d+arma×2 de dano, +3 acerto, -2 CA até próximo turno |
| Golpes Sequenciais | Guerreiro / Bárbaro | 3 golpes independentes com dano+arma cada |
| Contra-Ataque | Guerreiro / Cavaleiro | Revida automaticamente o próximo ataque inimigo; cooldown 4t após disparar |
| Golpe Sorrateiro | Ladino | 2d+arma+d8+bônus invisibilidade, 70% de envenenar |
| Evasão | Ladino | 60% de desviar os próximos 3 ataques |
| Veneno na Lâmina | Ladino | Golpe imediato + veneno potente + 3 ataques seguintes envenenam |

---

## Sistema de Labirinto

### Andar 1 — Superfície
Hub central conectado a 4 regiões (Norte, Sul, Leste, Oeste). Cada região gera entre 4 e 12 salas 4×4 conectadas proceduralmente. Salas são geradas ao ser visitadas pela primeira vez.

### Andares Profundos — AndarLabirinto
Cada descida cria um `AndarLabirinto` independente com topologia em árvore. Escadas de descida `>` levam a salas com a **mesma coordenada** no andar seguinte — caminhos distintos levam a lugares distintos. Nem toda ramificação tem continuidade; becos sem saída são intencionais. A escada de volta `<` é sempre garantida nas salas de entrada.

**Progressão:**

| Andar | Inimigos presentes |
|---|---|
| 1–2 | Ratos, Goblins, Esqueletos, Vermes |
| 3–4 | Orcs, Arqueiros das Trevas, Carnicais |
| 5–7 | Gárgulas, Campeões da Morte, Sacerdotes, Arautos |
| 8+ | Cavaleiros Sem Nome, Dracoliches, Serpentes Abissais, Espectros |
| Andar 7+ | **Modo Extremo** ativado |
| Andar 14+ | Escadaria final — **Olho de Vecna** pode surgir |

---

## Mapa e Legenda

```
╔──────────────╗
║ ▒  ▒  ▒  ▒  ║
║███ ?  >  ●  ║
║ ▒  ? ███ ▒  ║
║ ▒  ▒  ▒  ▒  ║
╚──────────────╝

●  Jogador          >  Escada desce      <  Escada sobe
!  Inimigo          ?  Item no chão      +  Estrutura
▐f▌ Tocha de parede ▐█▌ Porta trancada   X  Saída final (boss)
███ Parede (bloqueia luz, magia e flechas)
```

As bordas do mapa 4×4 são transponíveis — atravessá-las muda de sala ou região.

---

## Itens e Armas

### Armas

| Arma | Efeito Especial |
|---|---|
| Espada Curta / Longa / Adaga | Ataque corpo a corpo |
| Arco Élfico | Range 3, disparo duplo (20–50% por classe), requer flechas |
| Arco da Ruína | Range 3, disparo duplo 15%, dropado de Arqueiros das Trevas |
| Machado Anão Flamejante | DoT de fogo, crítico elemental por classe |
| Manoplas do Trovão | Choque, 20% paralisar 1t (Guerreiro) |
| Adaga Envenenada | 50–90% envenenar por 3–5 turnos (varia por classe) |
| Lâmina Drenante | Roubo de vida; Ladino drena 50% + DoT de drenagem |
| Machado do Sangramento | Sangramento 4–6 turnos (varia por classe) |
| Espada Fantasma | Ignora CA; 25–45% aterrorizar (paralisa 1t) |
| Espada dos Mártires | +1 ataque permanente por kill (máx +5) |
| Cajado de Gelo | Somente Magos; crítico paralisa 1t |
| Orbe Mental de Vecna | +15% poder mágico total |
| Cajado de Osso | +1 magia para Magos |
| Cajado do Fogo Descendente | Dano elemental de fogo. Com Códice: desbloqueia Bola de Fogo |

### Itens de Flechas
Flechas são contadas por **unidade** (0.05kg/unidade), aparecem no inventário como slot virtual, podem ser coletadas em quantidade parcial e recuperadas de inimigos atingidos.

### Consumíveis e Equipamentos Notáveis

| Item | Efeito |
|---|---|
| Diário Perdido | Revela lore; salva o jogo automaticamente |
| Vela Votiva | Revela armadilhas (tipo, posição, efeito) e itens no chão |
| Pó de Revelação | Revela armadilhas com posição |
| Runa do Limiar | Teletransporta ao hub central |
| Grimório Portal | Mago atravessa paredes |
| Grimório das Almas | Onda de Almas (AoE necrótica) |
| Grimório do Colapso | Paralisa inimigo por 2 turnos |
| Tomo da Entropia | Efeito aleatório por turno em combate |
| Lâmina Especular | Reflete 30% do dano físico recebido |
| Corrente do Espectro | Ladino: 50% negar dano físico por round |
| Coroa dos Condenados | +4 CA permanente; inimigos te percebem primeiro |
| Botas do Caçador de Monstros | 30% resistir a veneno/maldição/paralisia; reduz duração |
| Elmo do Caçador de Monstros | +2 CA permanente; 25% dissipar controle mágico |
| Botas Encantadas | Somente Magos: +8% poder mágico total |
| Códice dos Segredos Elementais | Desbloqueia Bola de Fogo, Relâmpago e Inverno Netuniano |
| Chapéu Cósmico | 25% absorver ataques/magias para o vazio cósmico; +1 CA |

---

## Sistema de Save / Load

Saves em JSON em `~/.o_limiar/saves/`. O estado preservado inclui:

- Personagem completo (HP, CA, ataque, inventário, equipamentos, flechas, subclasse, efeitos)
- Posição exata (andar, sala, coordenadas no mapa 4×4)
- Contexto de navegação (região, sala, histórico de escadas e retornos)
- Topologia de andares gerados (entradas de cada andar — garante escadas de volta)
- Modo Extremo, diários lidos, progresso

O labirinto é regenerado com inimigos e itens novos, mas a topologia de rotas e escadas é preservada pelas coordenadas de entrada salvas.

**Grimório de Aventuras:** menu de saves com suporte a exclusão por índice (`del 2, 4`) e renumeração automática dos slots restantes.

---

## Sessão Zero — O Porteiro do Limiar

Antes de entrar nas masmorras, o Porteiro conduz uma entrevista narrativa. Respostas dissertativas detectam palavras-chave e concedem bônus mecânicos reais (ataque, HP, CA, habilidades, itens). As motivações reconhecidas abrangem arquétipos de Lovecraft, Kafka, Borges, Poe, Camus, Dostoiévski, Nietzsche e outros.

Cada subclasse recebe um equipamento inicial fixo e uma escolha de item extra entre 4 opções temáticas.

---

## Sistema de Iluminação e Linha de Visão

Paredes `███` bloqueiam completamente:
- **Luz** do jogador e de tochas fixadas em outras paredes (LOS por Bresenham)
- **Magia** direcionada (Míssil Mágico, Drenar Vida, Colapso)
- **Flechas** do arco (exploração e combate)

Inimigos fora da luz não aparecem na lista de alvos de arco ou magia.

---

## Inimigos

| Tier | Inimigos | Andares |
|---|---|---|
| 1 | Rato Carniceiro, Goblin Furtivo, Esqueleto Guardião, Verme das Entranhas, Carniçal da Profundeza | 1–2 |
| 2 | Orc Berserker, Arqueiro das Trevas | 3–4 |
| 3 | Sacerdote Devorador, Arauto do Vazio, Gárgula de Pedra, Campeão da Morte | 5–7 |
| 4 | Cavaleiro Sem Nome, Serpente Abissal, Dracolich, Espectro das Profundezas | 8+ |
| Chefe | **Olho de Vecna** | Andar 14+ |

---

## Notas de Atualização

### v2.2.0 — Sistema de Magia e Novos Itens (atual)

**Sistema de magia refatorado** — `_magias_disponiveis(alvo)` é a fonte única de verdade para combate e exploração. Menu dinâmico gerado por grimórios/cajados equipados. Verificação de range e LOS centralizada. Exclusividades aplicadas:
- **Grimório das Almas** e **Grimório da Maldição** → exclusivo Mago Negro
- **Toque de Cura** → exclusivo Mago Azul | **Drenar Vida** → exclusivo Mago Negro

**Canal Vital (Mago Azul):** passivo padrão +2 HP/feitiço. Dom na sessão zero reforça para **+4 HP/feitiço**.

**Novos itens mágicos:**
- **Cajado do Fogo Descendente** — dano elemental de fogo em ataques. Com Códice: desbloqueia Bola de Fogo
- **Códice dos Segredos Elementais** — Cajado do Fogo → Bola de Fogo (AoE + DoT); Cajado de Gelo → Inverno Netuniano (paralisa 3t); Manoplas → Relâmpago (choque DoT + atordoa)
- **Chapéu Cósmico** — slot de elmo; 25% absorver ataques/magias para o vazio cósmico; +1 CA

**Novos itens lategame (dificuldade 18+):**
- **Botas do Caçador de Monstros** — 30% resistir completamente a veneno, maldição e paralisia; reduz duração
- **Elmo do Caçador de Monstros** — +2 CA permanente; 25% dissipar efeitos de controle mágico
- **Botas Encantadas** — exclusivo Magos; +8% poder mágico total

**Slots exclusivos por categoria:** Botas (1 de 3 tipos), Elmo (1 de 3 tipos), Armadura (1 de 3 tipos). `_trocar_slot()` ignora itens quebrados.

**Elmo da Fúria — ciclo completo:** durabilidade 3–5 ataques (não expira entre turnos). Investida Feroz usa bônus do elmo. Ao expirar: elmo destruído e removido da build.

**Paralisia corrigida:** verificação centralizada no loop de combate — cobre todos os inimigos independente de como implementam `atacar()`. Decremento após o turno de ação.

**Imunidades ao Orbe da Cegueira:** Serpente Abissal, Verme das Entranhas e Olho de Vecna agora imunes. Sacerdote Devorador: 25% de dissipar cegueira gastando o turno.

**Correções de bugs:** Chapéu Cósmico duplicando na bolsa; Botas do Silêncio desaparecendo; Talismã Protetor expirando imediatamente; cancelar `0` na seleção de alvo conjurava magia; Grimório da Maldição não aparecia no menu.

### v2.1.1 — Itens, Arcos e Spawn

**Elmo da Fúria** — narração de cabeçada/investida ao atacar, mensagem de "chifres quebrados" ao expirar.

**Pedra de Afiar refatorada** — o `+2` é acumulado no nome do item em equipados (`Espada Curta +2 → +4`), nunca em `arma['bonus']` diretamente, eliminando a dupla contagem. Dura 8 ataques. Aviso nos últimos 3. Restaura ao expirar. Não funciona em armas mágicas.

**Sistema de arco `[b]` aprimorado** — só dispara se arco estiver em equipados. Se na bolsa: pergunta antes de equipar. Se 2+ arcos na bolsa: menu de escolha numerado. Se slots cheios: pede substituição. Sem arco em lugar nenhum: mensagem clara.

**Efeitos especiais de armas por classe** — Machado Flamejante, Manoplas, Adaga Envenenada, Lâmina Drenante, Machado do Sangramento e Espada Fantasma têm parâmetros distintos de chance, duração e dano por classe.

**Spawn de inimigos — hierarquia de tier reforçada:**
- Tier 4 (Dracolich, Serpente Abissal, Cavaleiro Sem Nome): sala exclusiva, 1 único inimigo
- Tier 3 (Sacerdote Devorador, Campeão da Morte): sala exclusiva + até 1 seguidor T2 (40%)
- Tier 2: máx 2 inimigos do mesmo tier, sem mistura com T1
- Tier 1: máx 3 inimigos; dois inimigos nunca ocupam a mesma célula

**Correções de bugs:**
- Combate fantasma ao pisar em célula de inimigo morto: `and inimigo.esta_vivo()` adicionado
- Goblin Furtivo dropa itens roubados ao ser derrotado (`_itens_roubados`)
- `_mapa_ref` sincronizado em `_verificar_celula()` — Pó de Revelação e Vela Votiva sempre leem o mapa correto
- Vela Votiva mostra armadilhas (tipo + posição + efeito), inimigos vivos (HP, CA, pos) e itens no chão
- Pó de Revelação mostra armadilhas com tipo e coordenada

### v2.0.0 — O Limiar
- **Renomeado** de *Masmorras Liminares* para **O Limiar**
- **Menu principal** com tela de título ASCII, névoa animada e fade
- **Sistema de Save/Load** completo com preservação de estado de navegação e topologia de andares
- **Grimório de Aventuras**: gerenciamento de saves com exclusão por índice e renumeração

### v1.9.x — Combate à Distância e Labirinto
- **Arco Élfico** com sistema de flechas por unidade (peso 0.05kg/unidade, coleta parcial)
- **Arco da Ruína**: novo arco dropado de Arqueiros das Trevas, disparo duplo 15%
- **Sistema de magia na exploração** `[m]`: Míssil, AoE, Drenar Vida, Colapso, Cura
- **Sistema de arco na exploração** `[b]`: range 3, auto-equip, identificação de inimigos por luz
- Linha de visão (Bresenham) bloqueando luz, magia e flechas por paredes
- **AndarLabirinto** com coordenadas por escada: escadas distintas levam a salas distintas
- Garantia de `escada_subir` em salas de entrada (anti-softlock)
- **Modo Extremo** ativado apenas a partir do andar 7 em profundidade real
- **Olho de Vecna** surge somente a partir do andar 14

### v1.8.x — Itens e Efeitos
- Diário Perdido: lore de Orvyn Tess, Cartógrafo do Rei; salva automaticamente
- Pergaminhos de Mago (Proteção, Lanterna Espiritual): exclusivos para Magos
- Flechas drop: somente de Arqueiros das Trevas e inimigos atingidos por flechas (até 50% de recuperação)
- Efeitos especiais de armas diferenciados por classe do personagem
- Balanceamento: arcos causam d4 (metade de espadas), habilidades especiais incluem bônus de arma
- Habilidade Contra-Ataque refatorada: 1 carga potente, disparo automático, cooldown pós-uso

### v1.7.x — Geração e Navegação
- Sistema de regiões procedurais conectadas por coordenadas
- `_spawn_junto_a()`: spawn após escadas junto à célula da escada usada
- Spawn retorno keyed por `(andar, coord_escada)` — anti-colisão entre múltiplas escadas
- Inimigos poderosos empurrados para andares mais profundos (limiares de tier revisados)
- Emboscada com tela dedicada: exibe ataque recebido antes de limpar a tela

### v1.6.0 — Expansão de Conteúdo
- 10 novos itens comuns, 10 novos itens raros/lendários
- Narração expandida da sessão zero com referências filosófico-literárias
- Comando `r` para Runa do Limiar
- Novos efeitos: Colapso, Corrente do Espectro, Entropia, ácido corrosivo

---

## Créditos

**Desenvolvido por Bandeirinha**  
Para apoiar este e mais projetos: pixgg.com/bandeirinha

ASCII arts: `rotas.py`, `enemies.py`, `structures.py`  
Licença: GNU GPL v3.0 ou posterior

---

*"Atmosférico. Punitivo. Ancestral. No Limiar do Mundo."*
