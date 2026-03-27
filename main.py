"""
# O LIMIAR — ver. 2.0.0
# Anteriormente: Masmorras Liminares

    "Atmosférico. Primitivo. Ancestral. No Limiar do Mundo."
    "Ninguém jamais retornou."

# Copyright (C) 2025 Bandeirinha
# Licensed under the GNU GPL v3.0 or later
# Para apoiar: pixgg.com/bandeirinha

# ─────────────────────────────────────────────────────────────────────
# NOTAS DE ATUALIZAÇÃO v2.0.0 — O LIMIAR
# ─────────────────────────────────────────────────────────────────────
#
# RENOMEADO: "Masmorras Liminares" → "O LIMIAR"
#   Tela de título ASCII renovada com fade e névoa animada.
#
# SISTEMA DE SAVE / LOAD (completo):
#   Saves em JSON (~/.o_limiar/saves/). Preserva: personagem completo,
#   posição exata no labirinto (andar, sala, xy), estado de navegação
#   (em_andar_profundo, sala_no_andar, regiao_atual_key, sala_pos),
#   topologia de andares (entradas por andar → garantia de escadas de
#   volta), spawn_retorno (contexto de cada escada usada), modo_extremo.
#   O labirinto regenera inimigos/itens novos mas preserva rotas e
#   escadas de subida via coordenadas de entrada salvas.
#
# GRIMÓRIO DE AVENTURAS (menu de saves):
#   - Exclusão por índice: "del 2" ou "del 1, 3"
#   - Prévia dos registros a excluir + confirmação
#   - Renumeração automática dos slots restantes
#   - Loop interno — tela atualiza após cada ação
#
# ─────────────────────────────────────────────────────────────────────
# NOTAS DE ATUALIZAÇÃO v1.9.x — COMBATE À DISTÂNCIA E LABIRINTO
# ─────────────────────────────────────────────────────────────────────
#
# SISTEMA DE ARCO:
#   Arco Élfico: range 3, disparo duplo por classe (Ladino 50%,
#   Guerreiro 35%, Mago 20%). Auto-reequip ao usar [b].
#   Arco da Ruína: novo arco dropado de Arqueiros das Trevas; disparo
#   duplo 15%, bônus ligeiramente menor que o Élfico.
#   Flechas por unidade: peso 0.05kg/unidade, coleta parcial,
#   recuperação de até 50% das flechas cravadas em inimigos abatidos.
#   Slot virtual no inventário [e] com menu de descarte por quantidade.
#
# MAGIA NA EXPLORAÇÃO [m]:
#   Míssil Mágico, Onda de Almas, Explosão Arcana (AoE), Toque de
#   Cura (Mago Azul), Drenar Vida (Mago Negro), Colapso. Todos com
#   cooldown, range 3 e linha de visão obrigatória.
#
# LINHA DE VISÃO (Bresenham):
#   Paredes bloqueiam luz (jogador + tochas de parede), magia
#   direcionada e flechas. Inimigos fora da luz não aparecem como
#   alvos. Tochas só iluminam células que elas mesmas podem "ver".
#
# LABIRINTO POR COORDENADAS:
#   Cada escada de descida leva a uma sala com coordenada única no
#   andar seguinte (base × 100 + pos_escada). Salas distintas de um
#   mesmo andar não colidem. Escada de subida é invariante garantida
#   em runtime (sala() verifica e cria se ausente). Becos sem saída
#   são intencionais e válidos — o jogador usa < para backtracking.
#
# PROGRESSÃO POR PROFUNDIDADE:
#   Modo Extremo: apenas a partir do andar 7, somente quando em andar
#   profundo (nunca por exploração do andar 1).
#   Olho de Vecna: surge a partir do andar 14 (antes: 33).
#   Inimigos por tier:
#     Tier 1 (andar 1–2): Ratos, Goblins, Esqueletos, Vermes
#     Tier 2 (andar 3–4): Orcs, Arqueiros
#     Tier 3 (andar 5–7): Gárgulas, Campeões, Sacerdotes, Arautos
#     Tier 4 (andar 8+):  Cavaleiros, Dracolichis, Serpentes, Espectros
#
# ─────────────────────────────────────────────────────────────────────
# NOTAS DE ATUALIZAÇÃO v1.8.x — ITENS, EFEITOS E COMBATE
# ─────────────────────────────────────────────────────────────────────
#
# DIÁRIO PERDIDO:
#   3 por sessão, colocados aleatoriamente. Leitura revela lore de
#   Orvyn Tess (Cartógrafo do Rei). Salva o jogo automaticamente.
#
# EFEITOS ESPECIAIS POR CLASSE:
#   Machado Flamejante, Manoplas do Trovão, Adaga Envenenada, Lâmina
#   Drenante, Machado do Sangramento e Espada Fantasma têm parâmetros
#   distintos (chance, duração, dano, efeito bônus) por classe.
#
# BALANCEAMENTO DE DANO:
#   Arcos causam d4 (≈ metade das espadas).
#   Habilidades especiais incluem bônus de arma no cálculo.
#   Contra-Ataque refatorado: 1 carga, disparo automático no próximo
#   ataque inimigo, cooldown 4t após disparar ou desativar manualmente.
#
# COMBATE — AJUSTES:
#   Comandos inválidos consomem o turno (cooldowns avançam).
#   Emboscada com tela dedicada: exibe estado + ataque antes de
#   limpar a tela, com [ ENTER ] para reagir.
#   Arco em combate: integrado na opção 1 quando ativo como arma
#   principal ("1 - Atacar 🏹 (flechas restantes: N)").
#
# ─────────────────────────────────────────────────────────────────────
# NOTAS DE ATUALIZAÇÃO v1.6.0 — EXPANSÃO DE CONTEÚDO
# ─────────────────────────────────────────────────────────────────────
#
# 10 NOVOS ITENS COMUNS:
#   Vela Votiva, Poção de Sangue, Garrafa de Ácido, Armadura de Couro,
#   Luvas de Combate, Talismã Protetor, Pó de Gelo, Amuleto Arcano,
#   Amuleto de Deflexão, Capa Encantada.
#
# 10 NOVOS ITENS RAROS/LENDÁRIOS:
#   Espada dos Mártires, Corrente do Espectro, Grimório do Colapso,
#   Runa do Limiar, Olho Necromântico, Lâmina Especular,
#   Coroa de Espinhos de Ferro, Algemas dos Condenados,
#   Tomo da Entropia, Cálice de Sangue Antigo.
#
# Novos efeitos: Colapso (paralisia + CA -6), reflexo de espelho,
# corrente espectral, entropia por turno, ácido corrosivo (-CA).
# Comando 'r': Runa do Limiar fora do combate.
"""

import random
import os
import time
import json
import datetime

from rotas import warrior, knight, spell, wizard, rogue, rogue2
from enemies import scavenger_rat, goblin, guardian_skeleton, skull_archer, carniçal_profano, verme_das_entranhas, sacerdote_devorador, cavaleiro_sem_nome, arauto_do_vazio, serpente_abissal, warrior_orc, gargula, death_champion, vecnas_eye, vecna_meets, vecna_sees_everything, dracolich, reaper
from structures import stairway, statue, wall, dungeon, dungeon2, dungeon3, magic_circle, magic_circle_blink, altar, lost_garden

# ========================
# NOMES DE REGIÕES
# ========================

NOMES_REGIOES_NORMAIS = [
    "Catacumbas dos Esquecidos",
    "Cripta do Sangue Antigo",
    "Labirinto dos Ossos",
    "Salão das Lamentações",
    "Câmara das Almas Perdidas",
    "Corredor da Podridão",
]

NOMES_REGIOES_EXTREMAS = [
    "Abismo de Vecna",
    "Câmara dos Eternamente Condenados",
    "Fenda do Caos Primordial",
    "Sepulcro da Danação Absoluta",
    "Antecâmara do Fim",
    "Trono da Agonia Perpétua",
]

DESCRICOES_EXTREMAS = [
    "☠️  O ar aqui queima os pulmões. Algo muito antigo e muito mau desperta...",
    "💀 A escuridão pulsa. As paredes sangram. Você não deveria estar aqui.",
    "🩸 Sons de ossos quebrando ecoam. A luz de sua tocha treme de medo.",
    "👁️  Olhos invisíveis observam. O chão está quente sob seus pés.",
    "🔥 Esta não é mais uma masmorra — é um sepulcro vivo e faminto.",
]


def escolhe_guerreiro(warrior):
    return random.choice([warrior])

def escolhe_cavaleiro(knight):
    return random.choice([knight])

def escolhe_mago(wizard):
    return random.choice([wizard])

def escolhe_ladino(rogue):
    return random.choice([rogue])

def avanca_dungeon(dungeon, dungeon2, dungeon3, lost_garden):
    return random.choice([dungeon, dungeon2, dungeon3, lost_garden])


# ----------------------------- UTILITÁRIOS -----------------------------
def rolar_dado(lados):
    return random.randint(1, lados)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# =====================================================================
# SISTEMA DE PESO
# =====================================================================

# Capacidade de carga por classe (kg)
CAPACIDADE_PESO = {
    "Guerreiro": 22.0,
    "Ladino":    12.0,
    "Mago":       7.0,
}

# Peso de cada item (kg) — correspondência por substring/nome exato
PESOS_ITENS = {
    # Consumíveis
    'poção de cura':           0.3,
    'poção de força':          0.3,
    'poção de invisibilidade': 0.2,
    'antídoto':                0.2,
    'chave':                   0.1,
    # Armas
    'Espada Curta':            1.0,
    'Lâmina Sombria':          1.8,
    'Arco Élfico':             1.5,
    'Arco da Ruína':           1.8,
    'Flechas (20)':            0.5,
    'Flechas (10)':            0.3,
    'Machado Anão Flamejante': 3.5,
    'Manoplas do Trovão':      2.0,
    'Cajado de Gelo':          2.2,
    'Orbe Mental de Vecna':    0.6,
    'Adaga Envenenada':        0.7,
    # Armaduras / defensivos pesados
    'Armadura de Mithril':     7.5,
    'Escudo dos Condenados':   4.0,
    'Elmo da Fúria':           2.0,
    # Acessórios e vestes
    'Botas do Silêncio':       1.0,
    'Manto das Sombras':       0.8,
    'Anel da Vitalidade':      0.1,
    'Anel de Regeneração':     0.1,
    'Amuleto de Resistência':  0.2,
    'Colar da Fúria Ancestral':0.2,
    # Itens mágicos / grimórios
    'Grimório das Almas':      1.5,
    'Cristal de Mana':         0.4,
    'Tomo de Sabedoria Antiga':1.5,
    'Pergaminho de Proteção':   0.2,
    'Elixir do Berserker':     0.3,
    # Explosivo
    'explosivo arremessável':  1.5,
    # Itens de habilidade especial
    'Grimório Portal':         0.8,
    # ── COMUNS v1 (early-game) ───────────────────────────────────
    'Bandagem':                0.1,
    'Pedra de Afiar':          0.2,
    'Erva Medicinal':          0.1,
    'Adaga Simples':           0.6,
    'Escudo de Madeira':       2.0,
    'Cajado de Osso':          1.2,
    'Capa de Couro':           1.5,
    'Amuleto de Osso':         0.1,
    'Erva do Sono':            0.1,
    'Pó de Revelação':         0.2,
    'Tocha Suja':              0.5,
    'Pergaminho da Lanterna Espiritual': 0.2,
    # ── COMUNS v2 (early-game novos) ─────────────────────────────
    'Vela Votiva':             0.1, # futuramente efeito anti-maldição e spectral
    'Poção de Sangue':         0.3,
    'Garrafa de Ácido':        0.3,
    'Armadura de Couro':       3.0,
    'Escudo de Madeira':       2.5,
    'Armadura do Veterano':    6.0,
    'Machado de Guerra':       4.0,
    'Espada Longa':            2.5,
    'Luvas de Combate':        0.5,
    'Talismã Protetor':        0.1,
    'Pó de Gelo':              0.2,
    'Amuleto Arcano':          0.1,
    'Amuleto de Deflexão':    0.2,
    'Capa Encantada':          1.0,
    # ── RAROS / LENDÁRIOS v1 ─────────────────────────────────────
    'Lâmina Drenante':         2.0,
    'Machado do Sangramento':  4.0,
    'Orbe da Cegueira':        0.5,
    'Grimório da Maldição':    1.8,
    'Coroa dos Condenados':    1.5,
    'Runa de Ressurreição':    0.2,
    'Espada Fantasma':         1.6,
    'Cálice do Sacrifício':    0.4,
    'Anel da Putrefação':      0.1,
    'Tomo do Vazio':           2.0,
    # ── RAROS / LENDÁRIOS v2 (profundezas novas) ─────────────────
    'Espada dos Mártires':     2.5,
    'Corrente do Espectro':    0.3,
    'Grimório do Colapso':     1.8,
    'Runa do Limiar':          0.1,
    'Olho Necromântico':       0.4,
    'Lâmina Especular':        2.0,
    'Coroa de Espinhos de Ferro': 1.2,
    'Rede de Caça':            0.8,
    'Tomo da Entropia':        2.0,
    'Cálice de Sangue Antigo': 0.4,
    'Diário Perdido':          0.3,   # raro — salva o jogo e revela lore
}

DESCRICOES_ITENS = {
    'poção de cura':            "Restaura HP perdido. Simples, mas salva vidas.",
    'poção de força':           "Confere força brutal por 6 turnos.",
    'poção de invisibilidade':  "Torna-o etéreo por 3 turnos. Cuidado com o Olho.",
    'antídoto':                 "Cura qualquer veneno imediatamente.",
    'chave':                    "Abre portas trancadas. Leve e valiosa.",
    'Espada Curta':             "Espada de aço comum. Bônus de ataque e dano.",
    'Lâmina Sombria':           "Aço temperado em trevas. Bônus de ataque e dano.",
    'Arco Élfico':              "Madeira encantada. Range 3. Chance de disparo duplo. Requer flechas.",
    'Arco da Ruína':            "Arco de osso e trevas. Range 3. Ligeiramente mais lento que o Arco Élfico. Requer flechas.",
    'Flechas (20)':             "20 flechas de combate. Necessárias para usar o arco.",
    'Flechas (10)':             "10 flechas de combate. Necessárias para usar o arco.",
    'Machado Anão Flamejante':  "Forjado em lava ancestral. Causa dano de fogo persistente.",
    'Manoplas do Trovão':       "Canais elétricos nas articulações. Choque em cada golpe.",
    'Cajado de Gelo':           "Só magos dominam seu frio. Amplifica magia. Crítico físico ou 20% mágico: paralisa 1 turno.",
    'Orbe Mental de Vecna':     "Pulsa com magia proibida. +15% poder mágico total.",
    'Adaga Envenenada':         "Lâmina banhada em toxina. 70% de envenenar.",
    'Armadura de Mithril':      "Proteção leve e resistente. Alta CA.",
    'Escudo dos Condenados':    "Pesado e amaldiçoado. CA alta + contra-ataque passivo.",
    'Elmo da Fúria':            "Aumenta ataque mas reduz CA. Bônus para o próximo golpe.",
    'Botas do Silêncio':        "Inimigos detectam a ≤2 tiles. 60% de passar despercebido. +15% fuga.",
    'Manto das Sombras':        "Tecido das sombras. 70% fuga e durção de invisib. +2.",
    'Anel da Vitalidade':       "Aumenta HP máximo enquanto equipado.",
    'Anel de Regeneração':      "Restaura 1 HP por turno. Nunca se deve tirar.",
    'Amuleto de Resistência':   "+1 CA e +5 HP enquanto equipado.",
    'Colar da Fúria Ancestral': "Ativa bônus de ataque quando HP < 50%.",
    'Grimório das Almas':       "Desbloqueia Onda de Almas (AoE necrótica) para magos.",
    'Cristal de Mana':          "Acelera recarga de magia 2x. Não acumulativo.",
    'Tomo de Sabedoria Antiga': "Leitura imediata. +3 CA permanente.",
    'Pergaminho de Proteção':    "Somente Magos. Invoca barreira arcana: +CA por 8 rodadas. Pergaminho se dissolve ao uso.",
    'Elixir do Berserker':      "+Ataque por 6 turnos. Beba e lute.",
    'explosivo arremessável':   "Destrói paredes ███ e portas. Lançado em inimigos: alta variância. Risco de auto-dano.",
    'Grimório Portal':          "Permite ao Mago abrir micro-portais em paredes, atravessando-as.",
    # ── COMUNS v1 ────────────────────────────────────────────────────
    'Bandagem':                 "Estanca feridas. +4 HP imediato.",
    'Pedra de Afiar':           "+2 ataque no próximo combate. A borda decide.",
    'Erva Medicinal':           "Neutraliza veneno e restaura 3 HP.",
    'Adaga Simples':            "Arma básica +1 para qualquer classe.",
    'Escudo de Madeira':        "+2 CA. Vai durar até não durar.",
    'Cajado de Osso':           "+1 magia para Magos. Entalhado em osso desconhecido.",
    'Capa de Couro':            "+1 CA. Não impressiona — só protege.",
    'Amuleto de Osso':          "+1 ataque. Feito com o que restou de quem veio antes.",
    'Erva do Sono':             "60% de fazer inimigo perder 1 turno. Use em combate.",
    'Pó de Revelação':          "Uso imediato. Revela e conta armadilhas na sala atual.",
    'Tocha Suja':               "Equipável. Mais tecido e material combustível que a tocha comum.",
    'Pergaminho da Lanterna Espiritual': "Somente Magos. Conjura Lanterna Espiritual por 15 movimentos. A luz arcana esmorece com o tempo.",
    # ── COMUNS v2 ────────────────────────────────────────────────────
    'Vela Votiva':              "Uso imediato. Conta armadilhas e itens ocultos na sala. Alcance e detalhes maiores.",
    'Poção de Sangue':          "Cura 12 HP, mas reduz HP máximo em 2 permanentemente. A sede tem preço.",
    'Garrafa de Ácido':         "Arremessada: corrói armadura do inimigo (-2 CA permanente). Cuidado com respingos.",
    'Armadura de Couro':        "+3 CA. Curtida em sangue de criatura desconhecida. Pesa, mas protege.",
    'Escudo de Madeira':        "Equipável: +2 CA. Rústico mas funcional. Qualquer braço pode carregá-lo.",
    'Armadura do Veterano':     "Equipável: +4 CA. Fundida em batalhas esquecidas. Só cavaleiros a dominam.",
    'Machado de Guerra':        "Arma de duas mãos: +3 ataque, 1d12 dano. Fúria canalizada em ferro.",
    'Espada Longa':             "Arma elegante: +2 ataque, 1d10 dano. Precisão e alcance. Arte marcial.",
    'Luvas de Combate':         "+1 ataque para qualquer classe. O punho é a arma mais antiga.",
    'Talismã Protetor':         "Absorve 1 acerto crítico por combate (se dano > 10, reduz a 3). Quebra depois.",
    'Pó de Gelo':               "60% de paralisar inimigo por 1 turno. Frio que para o coração.",
    'Amuleto Arcano':           "Mago: -1 adicional ao cooldown de magia por turno. O fio entre mente e éter.",
    'Amuleto de Deflexão':     "Passivo equipável: +1 CA permanente + 25% de deflectir ataques físicos, anulando o dano.",
    'Capa Encantada':           "+2 CA + 20% de resistir a magia inimiga. Tecido impregnado em proteção antiga.",
    # ── RAROS v1 ─────────────────────────────────────────────────────
    'Lâmina Drenante':          "A cada acerto, rouba HP do alvo. A lâmina tem sede própria.",
    'Machado do Sangramento':   "Golpes abrem feridas que não fecham. Causa sangramento (DoT físico).",
    'Orbe da Cegueira':         "Cega inimigo por 2 turnos: -4 CA, 50% de errar ataques.",
    'Grimório da Maldição':     "Maldição: dobra o dano recebido pelo alvo por 3 turnos.",
    'Coroa dos Condenados':     "+4 CA permanente. Inimigos te percebem primeiro.",
    'Runa de Ressurreição':     "Uma vez por combate: cai a 0 HP? Permanece com 1.",
    'Espada Fantasma':          "Atravessa armaduras. Ignora CA do alvo nos testes de acerto.",
    'Cálice do Sacrifício':     "Beba: -10 HP próprios, próximo ataque causa dano triplo.",
    'Anel da Putrefação':       "Passivo: 40% de envenenar o alvo em qualquer ataque.",
    'Tomo do Vazio':            "Absorve 1 ataque recebido e devolve o dano ao atacante.",
    # ── RAROS v2 ─────────────────────────────────────────────────────
    'Espada dos Mártires':      "Por cada criatura abatida com ela, +1 ataque permanente (máx +5). Forjada em sangue de santos.",
    'Corrente do Espectro':     "Ladino: 50% de negar dano físico por round. Os mortos não sangram.",
    'Grimório do Colapso':      "Mago: nova magia Colapso — paralisa inimigo por 2 turnos. O espaço implode ao redor.",
    'Runa do Limiar':           "Consumível: teletransporta de volta ao hub central imediatamente. Não funciona no combate.",
    'Olho Necromântico':        "Mago: cada criatura morta em batalha = +1 dano permanente nos feitiços (máx +6).",
    'Lâmina Especular':         "Passivo: reflete 30% do dano físico recebido ao atacante. Lâmina que vira o mundo ao avesso.",
    'Coroa de Espinhos de Ferro': "+3 ataque, -2 CA. Drena 1 HP por turno. O sofrimento sustenta.",
    'Rede de Caça':             "Arremessada em combate: paralisa inimigo por 2 turnos e reduz CA em 4. Clássico de caçadores.",
    'Tomo da Entropia':         "Equipado: efeito aleatório por turno em combate. Pode salvar ou destruir.",
    'Cálice de Sangue Antigo':  "Cura 20 HP instantaneamente. Aplica Maldição em você por 3 turnos.",
    'Diário Perdido':           "Leitura imediata. Salva o progresso e revela o destino de quem veio antes.",
}


def peso_item(nome_item):
    """Retorna o peso de um item dado seu nome (busca por substring)."""
    # Flechas avulsas (qualquer quantidade) — 0.05kg/unidade
    if nome_item.startswith('Flechas ('):
        try:
            qtd = int(nome_item.split('(')[1].rstrip(')'))
            return round(qtd * 0.05, 2)
        except (ValueError, IndexError):
            pass
    for chave, peso in PESOS_ITENS.items():
        if chave in nome_item:
            return peso
    return 0.5  # peso padrão para itens não mapeados


def descricao_item(nome_item):
    """Retorna a descrição de um item dado seu nome."""
    for chave, desc in DESCRICOES_ITENS.items():
        if chave in nome_item:
            return desc
    return "Item misterioso. Seus efeitos são desconhecidos."


# ----------------------------- CLASSES BASE ----------------------------
class Personagem:
    def __init__(self, nome, hp, ac, ataque_bonus, dano_lados, classe, base_ataque_bonus, base_dano_lados):
        self.nome = nome
        self.hp = self.hp_max = hp
        self.ac = ac
        self.base_ac = ac
        self.base_hp_max = hp
        self.ataque_bonus = ataque_bonus
        self.dano_lados = dano_lados
        self.classe = classe
        self.inventario = ['poção de cura']
        self.arma = None
        self.armadura = None
        self.equipados = []
        self.cooldown_magia = 0
        self.bonus_temporario = 0
        self.invisivel = False
        self.pos = (0, 0)
        self.efeitos_ativos = {}
        self.base_ataque_bonus = base_ataque_bonus
        self.base_dano_lados = base_dano_lados
        self.cristal_mana_ativo = False  # Novo item Mago
        # Sistema de peso
        self.capacidade_peso = CAPACIDADE_PESO.get(classe, 10.0)
        # Sistema espiritual (definido na sessão zero)
        self.afinidade_espiritual = False   # True = altares curam sempre; estatuas +drop
        self.altar_oracoes = 0              # conta orações — conversão possível sem afinidade
        # ── Habilidade especial de combate (botão 2 — Guerreiro/Ladino) ──
        # Possíveis valores: None | 'investida' | 'contra-ataque' | 'sequencial'
        #                   | 'sorrateiro' | 'evasao' | 'veneno_lamina'
        self.habilidade_especial = None
        self.cooldown_habilidade = 0        # turnos até re-uso
        self.contra_ataque_ativo = False    # flag: modo contra-ataque passivo ativo
        self.subclasse = None               # Definida na sessão zero (Bárbaro/Cavaleiro/etc)
        self._mapa_ref = None               # Referência ao mapa atual (para Pó de Revelação/Portal)
        self.lanterna_espiritual = 0         # turnos restantes de Lanterna Espiritual (0 = inativa)
        self.flechas = 0                    # quantidade de flechas disponíveis

    @property
    def peso_atual(self):
        """Carga total = bolsa + equipamentos vestidos + flechas avulsas."""
        return round(
            sum(peso_item(i) for i in self.inventario) +
            sum(peso_item(i) for i in self.equipados) +
            round(getattr(self, 'flechas', 0) * 0.05, 2),
            2
        )

    @property
    def peso_bolsa(self):
        return round(
            sum(peso_item(i) for i in self.inventario) +
            round(getattr(self, 'flechas', 0) * 0.05, 2),
            2
        )

    @property
    def peso_vestido(self):
        return round(sum(peso_item(i) for i in self.equipados), 2)

    def pode_carregar(self, item):
        """Retorna True se há capacidade total para o item."""
        # Flechas já têm peso contabilizado via self.flechas — não somar de novo
        if item.startswith('Flechas'):
            return True   # a verificação real é feita em _coletar_flechas
        return self.peso_atual + peso_item(item) <= self.capacidade_peso

    def atacar(self, alvo):
        rolagem = rolar_dado(20)

        # ── Passivos de subclasse ──────────────────────────────────────
        # Bárbaro: Fúria — quando HP < 40%, +3 ataque automático
        bonus_furia_sub = 0
        if getattr(self, 'subclasse', None) == 'Bárbaro' and self.hp < self.hp_max * 0.40:
            bonus_furia_sub = 3
            print("🪓 FÚRIA BÁRBARA! HP crítico — +3 ataque!")

        # Assassino: crit em 19 ou 20 (range expandido)
        e_assassino = getattr(self, 'subclasse', None) == 'Assassino'
        eh_critico = (rolagem == 20) or (e_assassino and rolagem == 19)

        # Colar da Fúria Ancestral — bônus quando HP baixo
        bonus_furia = 0
        if any('Colar da Fúria Ancestral' in eq for eq in self.equipados):
            if self.hp < self.hp_max * 0.5:
                bonus_furia_item = next((eq for eq in self.equipados if 'Colar da Fúria Ancestral' in eq), None)
                if bonus_furia_item and '+' in bonus_furia_item:
                    bonus_furia = int(bonus_furia_item.split('+')[1])
                    print(f"💢 Colar da Fúria Ancestral pulsa! +{bonus_furia} ataque (HP crítico)!")

        total_bonus = self.ataque_bonus + self.bonus_temporario + (self.arma['bonus'] if self.arma else 0) + bonus_furia + bonus_furia_sub
        total = rolagem + total_bonus
        print(f"🎲 Rolagem de ataque: {rolagem} + {total_bonus} vs CA {alvo.ac}")

        # Espada Fantasma: ignora CA do alvo — testa contra CA 0 (sempre acerta se rolar > 0)
        ca_efetiva = alvo.ac
        if self.arma and self.arma.get('especial') == 'ignora_ca':
            ca_efetiva = 1
            print("👻 A Espada Fantasma atravessa as defesas como névoa!")

        dano = 0
        if eh_critico:
            dano = (rolar_dado(self.dano_lados) + (self.arma['dano'] if self.arma else 0)) * 2
            alvo.hp -= dano
            critico_label = "💥 GOLPE LETAL DO ASSASSINO" if (e_assassino and rolagem == 19) else "💥 ACERTO CRÍTICO"
            print(f"{critico_label}! {self.nome} causa {dano} de dano em {alvo.nome}!")
            # Cajado de Gelo — paralisa no crítico físico
            if self.arma and 'Cajado de Gelo' in self.arma.get('nome', ''):
                alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 1}
                print(f"🧊 O frio do Cajado penetra até os ossos — {alvo.nome} paralisa por 1 turno!")
            # Assassino: aplicar veneno automaticamente no crítico
            if e_assassino and not getattr(alvo, 'imune_veneno', False):
                alvo.efeitos_ativos['veneno'] = {'dano': 3, 'turnos': 3}
                print(f"🐍 Assassino: veneno automático no golpe letal! ({alvo.nome} envenena)")
        elif total >= ca_efetiva:
            dano = rolar_dado(self.dano_lados) + (self.arma['dano'] if self.arma else 0)
            # Maldição ativa no alvo dobra o dano
            if alvo.efeitos_ativos.get('maldicao', 0) > 0:
                dano = dano * 2
                print(f"💀 MALDIÇÃO ativa! O dano é DOBRADO: {dano}!")
            alvo.hp -= dano
            print(f"💥 {self.nome} acerta {alvo.nome} com {dano} de dano!")
        else:
            print(f"❌ {self.nome} erra o ataque.")
            # Escudo dos Condenados — contra-ataque passivo (só se errar também)
            if any('Escudo dos Condenados' in eq for eq in self.equipados) and random.random() < 0.2:
                contra = rolar_dado(4)
                alvo.hp -= contra
                print(f"🛡️ O Escudo dos Condenados reage! Contra-ataque automático: {contra} de dano!")
            return

        # ============================
        # ⚡🔥🐍 EFEITOS ESPECIAIS DE ITENS
        # ============================
        if self.arma:
            # ── Machado Flamejante ────────────────────────────────────
            if self.arma['nome'] == 'Machado Flamejante':
                if self.classe == 'Guerreiro':
                    # Guerreiro: dano flamejante maior + DoT mais longo
                    porcentagem = random.randint(18, 30) / 100
                    turnos_fogo = 2
                elif self.classe == 'Ladino':
                    # Ladino: incendeia com mais frequência mas menos intenso
                    porcentagem = random.randint(10, 18) / 100
                    turnos_fogo = 3
                else:
                    porcentagem = random.randint(10, 20) / 100
                    turnos_fogo = 1
                crit_elemental = random.random() < (0.10 if self.classe == 'Guerreiro' else 0.05)
                dano_extra = int(dano * porcentagem * (2 if crit_elemental else 1))
                alvo.hp -= dano_extra
                print(f"🔥 Dano flamejante: +{dano_extra} ({int(porcentagem*100)}% do dano base){' [CRÍTICO ELEMENTAL!]' if crit_elemental else ''}!")
                alvo.efeitos_ativos['fogo'] = {'dano': dano_extra, 'turnos': turnos_fogo}
                print(f"🔥 {alvo.nome} queimará {dano_extra} por {turnos_fogo} turno(s)!")

            # ── Manoplas do Trovão ────────────────────────────────────
            elif self.arma['nome'] == 'Manoplas do Trovão':
                if self.classe == 'Guerreiro':
                    # Guerreiro: choque mais forte, chance de paralisar 1 turno
                    porcentagem = random.randint(15, 28) / 100
                    if random.random() < 0.20:
                        alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 1}
                        print(f"⚡ CHOQUE PARALISANTE! {alvo.nome} perde o próximo turno!")
                elif self.classe == 'Mago':
                    # Mago: amplifica com poder mágico
                    porcentagem = random.randint(20, 35) / 100
                else:
                    porcentagem = random.randint(7, 23) / 100
                crit_elemental = random.random() < (0.12 if self.classe == 'Mago' else 0.05)
                dano_extra = int(dano * porcentagem * (2 if crit_elemental else 1))
                alvo.hp -= dano_extra
                print(f"⚡ Choque elétrico: +{dano_extra} ({int(porcentagem*100)}% do dano base){' [CRÍTICO ELEMENTAL!]' if crit_elemental else ''}!")
                alvo.efeitos_ativos['choque'] = {'dano': dano_extra, 'turnos': 1}
                print(f"⚡ {alvo.nome} sofrerá mais {dano_extra} de choque no próximo turno!")

            # ── Adaga Envenenada ──────────────────────────────────────
            elif self.arma['nome'] == 'Adaga Envenenada':
                if self.classe == 'Ladino':
                    # Ladino: veneno mais forte, mais turnos, chance maior
                    chance_v   = 0.90
                    dano_v     = rolar_dado(4) + 2
                    turnos_v   = 5
                elif self.classe == 'Guerreiro':
                    # Guerreiro: menos preciso com a toxina
                    chance_v   = 0.50
                    dano_v     = rolar_dado(3) + 1
                    turnos_v   = 3
                else:
                    chance_v   = 0.70
                    dano_v     = rolar_dado(3) + 1
                    turnos_v   = 4
                if random.random() < chance_v:
                    if getattr(alvo, 'imune_veneno', False):
                        print(f"🦴 A toxina escorre sem efeito. {alvo.nome} é imune a veneno!")
                    else:
                        alvo.efeitos_ativos['veneno'] = {'dano': dano_v, 'turnos': turnos_v}
                        print(f"🐍 Adaga Envenenada: {alvo.nome} sofrerá {dano_v} HP por {turnos_v} turnos!")

            # ── Lâmina Drenante ───────────────────────────────────────
            elif self.arma['nome'] == 'Lâmina Drenante':
                if self.classe == 'Ladino':
                    # Ladino: drena mais e aplica fraqueza
                    roubado = max(1, dano // 2)
                    alvo.efeitos_ativos['drenagem'] = {'dano': max(1, dano // 4), 'turnos': 2}
                    print(f"🩸 Lâmina Drenante (Ladino): suga {roubado} HP + drenagem contínua!")
                elif self.classe == 'Guerreiro':
                    roubado = max(1, dano // 3)
                    print(f"🩸 Lâmina Drenante: suga {roubado} HP de {alvo.nome}.")
                else:
                    roubado = max(1, dano // 4)
                    print(f"🩸 Lâmina Drenante: suga {roubado} HP de {alvo.nome}.")
                self.hp = min(self.hp + roubado, self.hp_max)
                print(f"   ❤️  +{roubado} HP recuperados!")

            # ── Machado do Sangramento ────────────────────────────────
            elif self.arma['nome'] == 'Machado do Sangramento':
                if not getattr(alvo, 'imune_sangramento', False):
                    if self.classe == 'Guerreiro':
                        # Guerreiro: sangramento mais intenso e duradouro
                        dano_s  = rolar_dado(4) + 2
                        turnos_s = 5
                    elif self.classe == 'Ladino':
                        # Ladino: múltiplas feridas menores que acumulam
                        dano_s  = rolar_dado(3) + 1
                        turnos_s = 6
                    else:
                        dano_s  = rolar_dado(3) + 1
                        turnos_s = 4
                    alvo.efeitos_ativos['sangramento'] = {'dano': dano_s, 'turnos': turnos_s}
                    print(f"🩸 Machado do Sangramento: {alvo.nome} sangrará {dano_s} HP/turno por {turnos_s} turnos!")
                else:
                    print(f"🛡️  {alvo.nome} não sangra — imune!")

            # ── Espada Fantasma ───────────────────────────────────────
            elif self.arma['nome'] == 'Espada Fantasma':
                if self.classe == 'Ladino':
                    # Ladino: susto quase garantido + ignora resistências
                    chance_susto = 0.45
                elif self.classe == 'Mago':
                    # Mago: ressonância arcana amplifica o terror
                    chance_susto = 0.35
                else:
                    chance_susto = 0.25
                if random.random() < chance_susto:
                    alvo.efeitos_ativos['atordoado'] = {'dano': 0, 'turnos': 1}
                    print(f"👻 A lâmina espectral aterroriza {alvo.nome}! Perde próxima ação!")

        # Anel da Putrefação — veneno passivo em qualquer arma
        if dano > 0 and 'putrificacao' in self.efeitos_ativos:
            if random.random() < 0.40 and not getattr(alvo, 'imune_veneno', False):
                dano_v = rolar_dado(3) + 1
                alvo.efeitos_ativos['veneno'] = {'dano': dano_v, 'turnos': 3}
                print(f"☠️  Anel da Putrefação: {alvo.nome} envenenado! {dano_v} HP/turno.")

        # Arco Élfico / Arco da Ruína — verificar flechas antes de atacar
        if self.arma and self.arma['nome'] in ('Arco Élfico', 'Arco da Ruína'):
            if getattr(self, 'flechas', 0) <= 0:
                print(f"🏹 Sem flechas! {self.arma['nome']} é desequipado automaticamente.")
                nome_arco = next((eq for eq in self.equipados if self.arma['nome'] in eq), None)
                if nome_arco:
                    self.equipados.remove(nome_arco)
                    self.inventario.append(nome_arco)
                self.arma = None
                self.atualizar_atributos_equipamento()

        # Arco Élfico — chance de disparo duplo (por classe)
        if self.arma and self.arma['nome'] in ('Arco Élfico', 'Arco da Ruína'):
            self.flechas = max(0, getattr(self, 'flechas', 0) - 1)
            if self.classe == "Mago":
                chance = 0.2
            elif self.classe == "Guerreiro":
                chance = 0.35
            elif self.classe == "Ladino":
                chance = 0.5
            else:
                chance = 0.25

            if random.random() < chance and getattr(self, 'flechas', 0) > 0:
                self.flechas = max(0, self.flechas - 1)
                if self.classe == 'Ladino':
                    time.sleep(1), print(rogue2), time.sleep(1)
                print("🏹 O Arco Élfico dispara uma flecha extra!")
                rolagem_extra = rolar_dado(20)
                total_extra = rolagem_extra + total_bonus
                print(f"🎲 Rolagem extra: {rolagem_extra} + {total_bonus} vs CA {alvo.ac}")
                if rolagem_extra == 20:
                    dano_extra = (rolar_dado(self.dano_lados) + self.arma['dano']) * 2
                    alvo.hp -= dano_extra
                    print(f"💥 ACERTO CRÍTICO EXTRA! Causa {dano_extra} de dano!")
                elif total_extra >= alvo.ac:
                    dano_extra = rolar_dado(self.dano_lados) + self.arma['dano']
                    alvo.hp -= dano_extra
                    print(f"💥 Flecha extra acerta: {dano_extra} de dano!")
                else:
                    print("❌ A flecha extra erra o alvo.")

        # Arco da Ruína — disparo duplo 15% (mais lento, menos confiável)
        elif self.arma and self.arma['nome'] == 'Arco da Ruína':
            self.flechas = max(0, getattr(self, 'flechas', 0) - 1)
            if random.random() < 0.15 and getattr(self, 'flechas', 0) > 0:
                self.flechas = max(0, self.flechas - 1)
                if self.classe == 'Ladino':
                    time.sleep(1), print(rogue2), time.sleep(1)
                print("💀 O Arco da Ruína range e dispara uma flecha extra!")
                rolagem_extra = rolar_dado(20)
                total_extra = rolagem_extra + total_bonus
                if rolagem_extra == 20:
                    dano_extra = (rolar_dado(self.dano_lados) + self.arma['dano']) * 2
                    alvo.hp -= dano_extra
                    print(f"💥 CRÍTICO EXTRA da Ruína! {dano_extra} dano!")
                elif total_extra >= alvo.ac:
                    dano_extra = rolar_dado(self.dano_lados) + self.arma['dano']
                    alvo.hp -= dano_extra
                    print(f"💀 Flecha extra da Ruína acerta: {dano_extra} dano!")
                else:
                    print("❌ A flecha extra da Ruína perde o alvo.")

        # Desequipar arco se flechas acabaram durante o ataque
        if self.arma and self.arma['nome'] in ('Arco Élfico', 'Arco da Ruína') and getattr(self, 'flechas', 0) <= 0:
            print(f"🏹 Flechas esgotadas! {self.arma['nome']} desequipado.")
            nome_arco = next((eq for eq in self.equipados if self.arma['nome'] in eq), None)
            if nome_arco:
                self.equipados.remove(nome_arco)
                self.inventario.append(nome_arco)
            self.arma = None
            self.atualizar_atributos_equipamento()

        if 'forca' not in self.efeitos_ativos and 'berserker' not in self.efeitos_ativos:
            self.bonus_temporario = 0

        # ── Lâmina Envenenada (habilidade especial Ladino) ────────────
        if dano > 0 and 'lamina_envenenada' in self.efeitos_ativos:
            if not getattr(alvo, 'imune_veneno', False):
                dano_v = rolar_dado(4) + 2
                alvo.efeitos_ativos['veneno'] = {'dano': dano_v, 'turnos': 4}
                print(f"🐍 LÂMINA ENVENENADA! {alvo.nome} envenenado: {dano_v} HP por 4 turnos!")

        # ── Sacrifício — dano triplo no próximo ataque ────────────────
        if 'sacrificio' in self.efeitos_ativos and dano > 0:
            dano_extra = dano * 2   # dano já aplicado + 2x = 3x total
            alvo.hp -= dano_extra
            print(f"🏆 SACRIFÍCIO: +{dano_extra} de dano extra (triplo)!")
            del self.efeitos_ativos['sacrificio']

        # ── Espada dos Mártires — acumula ataque por kills ────────────
        if self.arma and self.arma.get('nome') == 'Espada dos Mártires':
            if not alvo.esta_vivo():
                kills = self.efeitos_ativos.get('martires_kills', 0)
                if kills < 5:
                    kills += 1
                    self.efeitos_ativos['martires_kills'] = kills
                    self.ataque_bonus += 1
                    self.base_ataque_bonus += 1
                    print(f"⚔️ Espada dos Mártires: +1 ataque permanente! (total +{kills})")

        # ── Maldição recebida: dobra dano sofrido (verificado no atacante) ──
        # Implementado em Inimigo.atacar — verificar maldicao no alvo

    # ==========================================================
    # Processar efeitos (DoTs, buffs, veneno)
    # ==========================================================
    def processar_efeitos(self):
        """Processa DoTs e buffs ativos — incluindo veneno — no início do turno."""
        remover = []
        for efeito, dados in list(self.efeitos_ativos.items()):
            if isinstance(dados, dict) and 'dano' in dados:
                dano = dados['dano']
                self.hp -= dano
                if efeito == 'veneno':
                    print(f"🐍 VENENO! {self.nome} perde {dano} HP pela toxina!")
                elif efeito == 'veneno_duplo':
                    print(f"☠️  VENENO FORTE! {self.nome} perde {dano} HP — toxina amplificada!")
                elif efeito == 'fogo':
                    print(f"🔥 {self.nome} queima e sofre {dano} de dano!")
                elif efeito == 'choque':
                    print(f"⚡ {self.nome} sofre {dano} de dano elétrico!")
                elif efeito == 'drenagem':
                    print(f"🌑 {self.nome} tem {dano} de vida drenada!")
                elif efeito == 'sangramento':
                    print(f"🩸 SANGRAMENTO! {self.nome} perde {dano} HP — a ferida não fecha!")
                else:
                    print(f"☠️  {self.nome} sofre {dano} de dano por {efeito}!")
                dados['turnos'] -= 1
                if dados['turnos'] <= 0:
                    remover.append(efeito)

        # Cegueira (flag, não dict) — não causa dano mas decrementa
        if 'cegueira' in self.efeitos_ativos and isinstance(self.efeitos_ativos['cegueira'], int):
            self.efeitos_ativos['cegueira'] -= 1
            if self.efeitos_ativos['cegueira'] <= 0:
                remover.append('cegueira')
                print(f"👁️  A névoa diante dos olhos de {self.nome} se dissipa.")

        # Maldição — decrementa; não causa dano direto, mas dobra dano recebido (verificado no atacar())
        if 'maldicao' in self.efeitos_ativos and isinstance(self.efeitos_ativos['maldicao'], int):
            self.efeitos_ativos['maldicao'] -= 1
            if self.efeitos_ativos['maldicao'] <= 0:
                remover.append('maldicao')
                print(f"💀 A maldição em {self.nome} se dissolve em fumaça negra.")

        for efeito in remover:
            if efeito in self.efeitos_ativos:
                del self.efeitos_ativos[efeito]
            if efeito in ('veneno', 'veneno_duplo'):
                print(f"💉 O veneno em {self.nome} foi dissipado.")
            elif efeito == 'fogo':
                print(f"💨 O fogo em {self.nome} se apagou.")
            elif efeito == 'drenagem':
                print(f"✨ A drenagem de vida cessou.")
            elif efeito == 'sangramento':
                print(f"🩹 O sangramento de {self.nome} estancou.")
            elif efeito == 'paralisado':
                # Restaurar CA do Colapso ou Rede de Caça
                pen_ca = self.efeitos_ativos.pop('colapso_ca', 0) + self.efeitos_ativos.pop('rede_ca', 0)
                if pen_ca:
                    self.ac += pen_ca
                    print(f"🔓 {self.nome} se liberta da paralisia! CA restaurada (+{pen_ca}).")

    def usar_magia(self, alvo, mapa_atual=None):
        if self.classe != "Mago":
            print("❌ Apenas magos podem lançar magias!")
            return False
        if self.cooldown_magia > 0:
            print(f"❌ Magia em recarga! ({self.cooldown_magia} turnos restantes)")
            return False

        dist = abs(alvo.pos[0] - self.pos[0]) + abs(alvo.pos[1] - self.pos[1])

        # ── Spells de Subclasse ───────────────────────────────────────
        subclasse = getattr(self, 'subclasse', None)
        tem_portal  = any('Grimório Portal' in eq for eq in self.equipados)
        tem_colapso = any('Grimório do Colapso' in eq for eq in self.equipados)
        tem_almas   = any('Grimório das Almas' in eq for eq in self.equipados)

        # ── Grimório das Almas — Onda de Almas AoE ──────────────────
        if tem_almas:
            print("📖 O Grimório das Almas pulsa! Escolha:")
            print("  1 - Míssil Mágico")
            print("  2 - Onda de Almas")
            if tem_portal:
                print("  3 - Portal de Travessia (atravessa parede)")
            if tem_colapso:
                print("  4 - Colapso (paralisa inimigo 2 turnos)")
            if subclasse == 'Mago Azul':
                print("  5 - Toque de Cura (cura HP, cooldown 3t)")
            elif subclasse == 'Mago Negro':
                print("  5 - Drenar Vida (rouba HP do inimigo, cooldown 4t)")
            sub = input(">> ").strip()
            if sub == '2':
                print("👻 Você libera uma onda de almas aprisionadas!")
                poder_magico = self.calcular_poder_magico_total()
                dano_total = poder_magico + rolar_dado(6) + 4
                alvo.hp -= dano_total
                print(f"💀 Onda de Almas causa {dano_total} de dano mágico necrótico!")
                self.cooldown_magia = 4
                return True
            if sub == '3' and tem_portal:
                return self._usar_portal(mapa_atual)
            if sub == '4' and tem_colapso:
                return self._usar_colapso(alvo)
            if sub == '5':
                if subclasse == 'Mago Azul':
                    return self._usar_toque_cura()
                elif subclasse == 'Mago Negro':
                    return self._usar_drenar_vida(alvo)
        else:
            # Menu simplificado
            opcoes_extra = []
            if tem_portal:
                opcoes_extra.append(('Portal de Travessia', lambda: self._usar_portal(mapa_atual)))
            if tem_colapso:
                opcoes_extra.append(('Colapso (paralisa 2t)', lambda: self._usar_colapso(alvo)))
            if subclasse == 'Mago Azul':
                opcoes_extra.append(('Toque de Cura', lambda: self._usar_toque_cura()))
            elif subclasse == 'Mago Negro':
                opcoes_extra.append(('Drenar Vida', lambda: self._usar_drenar_vida(alvo)))
            if opcoes_extra:
                print("✨ Escolha:")
                print("  1 - Míssil Mágico")
                for i, (nm, _) in enumerate(opcoes_extra, 2):
                    print(f"  {i} - {nm}")
                sub = input(">> ").strip()
                try:
                    idx_e = int(sub) - 2
                    if 0 <= idx_e < len(opcoes_extra):
                        return opcoes_extra[idx_e][1]()
                except (ValueError, IndexError):
                    pass

        if dist > 3:
            print("❌ Alvo fora do alcance!")
            return False

        # ── Linha de visão — parede bloqueia magia ────────────────────
        mapa_ref = getattr(self, '_mapa_ref', None)
        if mapa_ref and hasattr(mapa_ref, 'tem_linha_de_visao'):
            jx, jy = self.pos
            ax, ay = alvo.pos
            if not mapa_ref.tem_linha_de_visao(jx, jy, ax, ay):
                print("❌ Uma parede bloqueia a linha de visão! Magia dissipada.")
                return False

        print("✨ Míssil Mágico lançado!")
        print(spell)

        poder_magico = self.calcular_poder_magico_total()
        print(f"🔮 Poder mágico total: {poder_magico}")

        rolagem = rolar_dado(4) + 3
        print(f"🎲 Rolagem do Míssil Mágico: 1d4 + 3 = {rolagem}")

        # Cajado de Gelo — 20% de acerto crítico mágico (dano dobrado + paralisia 1 turno)
        tem_cajado_gelo = self.arma and 'Cajado de Gelo' in self.arma.get('nome', '')
        critico_gelo = tem_cajado_gelo and random.random() < 0.20

        dano_total = poder_magico + rolagem
        if critico_gelo:
            dano_total = dano_total * 2

        alvo.hp -= dano_total

        # Resistência mágica (Gárgula, Dracolich, Capa Encantada)
        res_inimigo = getattr(alvo, 'resistencia_magica', 0.0)
        if res_inimigo > 0 and random.random() < res_inimigo:
            revertido = max(1, dano_total // 2)
            alvo.hp += revertido
            print(f"🛡️ {alvo.nome} resiste parcialmente à magia! Dano reduzido em {revertido}.")

        if critico_gelo:
            print(f"🧊 ACERTO CRÍTICO GLACIAL! {dano_total} de dano congelante em {alvo.nome}!")
            alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 1}
            print(f"   O frio extremo paralisa {alvo.nome} por 1 turno!")
        else:
            print(f"💥 Míssil Mágico causa {dano_total} de dano mágico em {alvo.nome}!")

        # Canal Vital — cura ao lançar magia
        if 'canal_vital' in self.efeitos_ativos:
            self.hp = min(self.hp + 2, self.hp_max)
            print(f"💖 Canal Vital: +2 HP recuperados.")

        self.cooldown_magia = 5
        return True

    def _usar_toque_cura(self):
        """Mago Azul — Toque de Cura: cura HP, cooldown 3 turnos."""
        poder = self.calcular_poder_magico_total()
        cura = 10 + poder // 2 + rolar_dado(6)
        self.hp = min(self.hp + cura, self.hp_max)
        print(f"💙 TOQUE DE CURA! A luz elemental restaura {cura} HP!")
        time.sleep(1)
        self.cooldown_magia = 3
        return True

    def _usar_drenar_vida(self, alvo):
        """Mago Negro — Drenar Vida: rouba HP do inimigo, cooldown 4 turnos."""
        poder = self.calcular_poder_magico_total()
        dano = poder + rolar_dado(8) + 2
        alvo.hp -= dano
        roubado = dano // 2
        self.hp = min(self.hp + roubado, self.hp_max)
        alvo.efeitos_ativos['maldicao'] = alvo.efeitos_ativos.get('maldicao', 0) + 1
        print(f"💀 DRENAR VIDA! {dano} de dano necrótico em {alvo.nome}!")
        print(f"   🩸 Você absorve {roubado} HP e aplica Maldição (+1 turno)!")
        time.sleep(1)
        self.cooldown_magia = 4
        return True

    def _usar_portal(self, mapa_atual):
        """
        Portal de Travessia: o Mago escolhe uma parede adjacente
        e se teletransporta para o outro lado dela.
        Funciona apenas se a célula do outro lado for livre.
        Cooldown alto.
        """
        if self.cooldown_magia > 0:
            print("❌ Magia em recarga!")
            return False

        print("\n🌀 PORTAL DE TRAVESSIA")
        print("   Escolha a direção da parede a atravessar:")
        print("   w = Norte | s = Sul | a = Oeste | d = Leste | c = cancelar")
        dir_cmd = input("   >> ").lower().strip()

        if dir_cmd == 'c':
            print("   Cancelado.")
            return False

        DIR_MAP_PORTAL = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
        if dir_cmd not in DIR_MAP_PORTAL:
            print("   Direção inválida.")
            return False

        dx, dy = DIR_MAP_PORTAL[dir_cmd]
        px, py = self.pos
        tx, ty = px + dx, py + dy

        if mapa_atual is None:
            print("   ❌ O Mago não tem referência espacial aqui.")
            return False

        W, H = mapa_atual.largura, mapa_atual.altura

        # Verificar se a célula alvo é uma parede
        if not (0 <= tx < W and 0 <= ty < H):
            print("   A borda da sala bloqueia o portal.")
            time.sleep(1)
            return False

        if mapa_atual.matriz[ty][tx] != '#':
            print("   Não há parede aí — o portal se dissolve inutilmente.")
            time.sleep(1)
            self.cooldown_magia = 2   # cooldown de penalidade
            return True

        # Tenta a célula do outro lado da parede
        bx, by = tx + dx, ty + dy
        if not (0 <= bx < W and 0 <= by < H) or mapa_atual.matriz[by][bx] != '.':
            print("   O outro lado da parede está bloqueado. O portal colapsa.")
            time.sleep(1)
            self.cooldown_magia = 2
            return True

        # Sucesso!
        print("   ✨ Uma fenda arcana rasga a pedra...")
        time.sleep(1)
        print("   Você atravessa a parede em um relâmpago de luz violeta.")
        time.sleep(1.5)
        self.pos = (bx, by)
        print(f"   🌀 Portal bem-sucedido! Nova posição: ({bx}, {by}).")
        self.cooldown_magia = 6
        time.sleep(1)
        return True

    def _usar_colapso(self, alvo):
        """
        Grimório do Colapso: paralisa o inimigo por 2 turnos.
        O espaço em torno dele implode e o aprisiona.
        """
        print("📖 O Grimório do Colapso pulsa com padrões que não deveriam existir...")
        time.sleep(1)
        print("   Você recita o encantamento — o ar em torno do inimigo comprime.")
        time.sleep(1.5)
        poder_magico = self.calcular_poder_magico_total()
        dano_colapso = poder_magico + rolar_dado(6) + 2
        alvo.hp -= dano_colapso
        alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 2}
        alvo.efeitos_ativos['colapso_ca'] = 6   # perde 6 CA enquanto paralisado
        alvo.ac = max(1, alvo.ac - 6)
        print(f"   💀 COLAPSO! {alvo.nome} recebe {dano_colapso} de dano e está PARALISADO por 2 turnos!")
        print(f"   🔒 CA de {alvo.nome} reduzida em 6 enquanto paralisado.")
        self.cooldown_magia = 5
        # Olho Necromântico — ganho quando inimigo for morto (verificado em _loot_inimigo)
        # Canal Vital
        if 'canal_vital' in self.efeitos_ativos:
            self.hp = min(self.hp + 2, self.hp_max)
            print(f"💖 Canal Vital: +2 HP.")
        time.sleep(1.5)
        return True

    def usar_pocao(self):
        """Interface rápida de combate: lista numerada, escolhe e usa."""
        if not self.inventario:
            print("🚫 Sem itens no inventário!")
            return
        print("\n🎒 Inventário rápido:")
        for i, item in enumerate(self.inventario):
            print(f"  {i+1:>2}. {item}  ({peso_item(item):.1f}kg)")
        escolha = input("Escolha o número (0 = cancelar): ")
        try:
            idx = int(escolha) - 1
            if idx < 0:
                return
            item = self.inventario.pop(idx)
        except:
            print("❌ Escolha inválida.")
            return
        self._usar_item_direto(item)

    def usar_item_em_combate(self, inimigo):
        """
        Menu unificado de ação rápida em combate. Tudo numérico.
          1 — Trocar arma ativa
          2 — Arremessar explosivo       (só aparece se tiver)
          3 — Usar item da bolsa
          0 — Cancelar
        Retorna True se o turno foi consumido.
        """
        PREFIXOS_ARMA = (
            'Espada Curta','Espada Longa','Lâmina Sombria','Arco Élfico','Arco da Ruína',
            'Machado Anão Flamejante','Cajado de Gelo','Adaga Simples',
            'Adaga Envenenada','Manoplas do Trovão','Orbe Mental de Vecna',
            'Cajado de Osso','Lâmina Drenante','Machado do Sangramento',
            'Espada Fantasma','Machado de Guerra','Espada dos Mártires',
            'Lâmina Especular',
        )
        armas_eq    = [eq for eq in self.equipados  if any(eq.startswith(p) for p in PREFIXOS_ARMA)]
        armas_bolsa = [it for it in self.inventario if any(it.startswith(p) for p in PREFIXOS_ARMA)]
        tem_armas   = bool(armas_eq or armas_bolsa)
        tem_explosivo = 'explosivo arremessável' in self.inventario

        print("\n🎒 Ação rápida:")
        print("  1 — Trocar arma ativa")
        if tem_explosivo:
            print("  2 — Arremessar explosivo 💣")
        print("  3 — Usar item da bolsa")
        print("  0 — Cancelar")
        sub = input("  >> ").strip()

        if sub == '0' or sub == '':
            return False

        # ── 1 — Trocar arma ────────────────────────────────────────────
        if sub == '1':
            if not tem_armas:
                print("❌ Nenhuma arma disponível para alternar.")
                time.sleep(1)
                return False

            arma_ativa_nome = self.arma.get('nome', '') if self.arma else ''
            print("\n⚔️  Armas disponíveis:")
            for i, aeq in enumerate(armas_eq, 1):
                marca = " ◀ ATIVA" if arma_ativa_nome and arma_ativa_nome in aeq else ""
                print(f"  {i}. {aeq}{marca}")
            if armas_bolsa:
                base = len(armas_eq)
                print(f"  — Na bolsa:")
                for i, ab in enumerate(armas_bolsa, base + 1):
                    print(f"  {i}. {ab}  (na bolsa)")
            print("  0. Cancelar")

            todas = armas_eq + armas_bolsa
            sel = input("  Escolha: ").strip()
            if sel == '0' or sel == '':
                return False
            try:
                idx = int(sel) - 1
                if idx < 0 or idx >= len(todas):
                    return False
                escolhida = todas[idx]
            except ValueError:
                return False

            if escolhida in self.inventario:
                if len(self.equipados) >= 6:
                    print("⚠️  Equipamentos cheios! Desequipe algo primeiro.")
                    time.sleep(1.5)
                    return False
                self.inventario.remove(escolhida)
                self.equipados.append(escolhida)

            if self._ativar_arma_por_nome(escolhida):
                print(f"⚔️  {escolhida} ativado!")
                time.sleep(1)
                return True
            else:
                print("❌ Não foi possível ativar essa arma.")
                time.sleep(1)
                return False

        # ── 2 — Explosivo ──────────────────────────────────────────────
        if sub == '2':
            if not tem_explosivo:
                print("❌ Sem explosivos.")
                time.sleep(1)
                return False
            return _combate_explosivo(self, inimigo)

        # ── 3 — Item da bolsa ──────────────────────────────────────────
        if sub == '3':
            if not self.inventario:
                print("🚫 Bolsa vazia!")
                time.sleep(1)
                return False
            print("\n🎒 Bolsa:")
            for i, item in enumerate(self.inventario):
                print(f"  {i+1:>2}. {item}  ({peso_item(item):.1f}kg)")
            escolha = input("  Número (0=cancelar): ").strip()
            try:
                idx = int(escolha) - 1
                if idx < 0 or idx >= len(self.inventario):
                    return False
                item = self.inventario[idx]
            except (ValueError, IndexError):
                return False

        # ── Itens que precisam de alvo ────────────────────────────────
        if item.startswith('Orbe da Cegueira'):
            self.inventario.pop(idx)
            print("🌑 Você arremessa o Orbe da Cegueira!")
            time.sleep(0.8)
            if random.random() < 0.80:
                turnos_cegueira = 2
                inimigo.efeitos_ativos['cegueira'] = turnos_cegueira
                inimigo.efeitos_ativos.pop('cegueira_ca', None)  # limpa flag extra
                # Reduz CA do inimigo temporariamente
                inimigo.ac = max(1, inimigo.ac - 4)
                inimigo.efeitos_ativos['cegueira_ca_pen'] = 4  # para restaurar depois
                print(f"👁️  O Orbe estoura em névoa! {inimigo.nome} está CEGO por {turnos_cegueira} turnos!")
                print(f"   CA reduzida em 4. 50% de errar ataques.")
            else:
                print("   O Orbe erra o alvo e se perde na escuridão. Desperdício.")
            time.sleep(1.5)
            return True

        elif item == 'Garrafa de Ácido':
            self.inventario.pop(idx)
            print("🧪 Você arremessa a Garrafa de Ácido!")
            time.sleep(0.8)
            if random.random() < 0.75:
                pen_ca = 2
                inimigo.ac = max(1, inimigo.ac - pen_ca)
                inimigo.efeitos_ativos['acido_ca'] = pen_ca
                dano_a = rolar_dado(4) + 2
                inimigo.hp -= dano_a
                print(f"   💀 Ácido corrói {inimigo.nome}: -{dano_a} HP e -2 CA permanente!")
                # Auto-dano por respingo (30%)
                if random.random() < 0.30:
                    dano_self = rolar_dado(3)
                    self.hp = max(1, self.hp - dano_self)
                    print(f"   🧪 Respingo de ácido te atinge: -{dano_self} HP.")
            else:
                print(f"   A garrafa erra o alvo e se despedaça no chão.")
            time.sleep(1.5)
            return True

        elif item == 'Pó de Gelo':
            self.inventario.pop(idx)
            print("❄️ Você lança o Pó de Gelo sobre o inimigo!")
            time.sleep(0.8)
            if random.random() < 0.60:
                inimigo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 1}
                print(f"🧊 {inimigo.nome} congela! Perde o próximo turno.")
            else:
                print(f"   O pó se dispersa sem efeito. O frio não encontrou presa.")
            time.sleep(1.5)
            return True

        elif 'Rede de Caça' in item:
            self.inventario.pop(idx)
            print(f"🕸️ Você arremessa a Rede de Caça em {inimigo.nome}!")
            time.sleep(0.8)
            if random.random() < 0.75:
                inimigo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 2}
                pen = 4
                inimigo.ac = max(1, inimigo.ac - pen)
                inimigo.efeitos_ativos['rede_ca'] = pen
                print(f"   🔒 {inimigo.nome} está PRESO na rede! Paralisado por 2 turnos, -4 CA.")
            else:
                print(f"   A rede erra o alvo e cai no chão inutilmente.")
            time.sleep(1.5)
            return True

        elif item == 'Erva do Sono':
            self.inventario.pop(idx)
            print("📖 Você recita a maldição do Grimório...")
            time.sleep(1)
            turnos_m = 3
            inimigo.efeitos_ativos['maldicao'] = turnos_m
            print(f"💀 MALDIÇÃO lançada sobre {inimigo.nome}! Dano recebido dobrado por {turnos_m} turnos!")
            self.cooldown_magia = max(self.cooldown_magia, 3)
            time.sleep(1.5)
            return True

        else:
            # Itens sem alvo — usa normalmente
            self.inventario.pop(idx)
            self._usar_item_direto(item)
            return True

    def _usar_item_direto(self, item):
        """Aplica o efeito de um item já removido do inventário."""

        # ========================
        # ITENS EXISTENTES
        # ========================
        if item == 'poção de cura':
            cura = rolar_dado(8) + 2
            self.hp = min(self.hp + cura, self.hp_max)
            print(f"🧪 Você bebe a poção de cura...")
            time.sleep(1)
            print(f"   ✨ Recupera {cura} HP! ({self.hp}/{self.hp_max})")
            time.sleep(1)

        elif item == 'poção de força':
            forca = rolar_dado(8) + 2
            self.bonus_temporario = forca
            self.efeitos_ativos['forca'] = 6
            print(f"💪 Você engole a poção de força...")
            time.sleep(1)
            print(f"   🔥 Músculos incham com poder! +{forca} ataque por 6 turnos.")
            time.sleep(1)

        elif item == 'poção de invisibilidade':
            self.invisivel = True
            self.efeitos_ativos['invisibilidade'] = 3
            print("👻 Seu corpo começa a dissolver-se no ar...")
            time.sleep(1)
            print("   ✨ Invisibilidade ativada por 3 turnos.")
            time.sleep(1)

        elif item.startswith('Elixir do Berserker'):
            bonus = int(item.split('+')[1])
            self.bonus_temporario = bonus
            self.efeitos_ativos['berserker'] = 6
            print(f"💢 Berserker: +{bonus} ataque por 6 turnos.")

        elif item.startswith('Pergaminho de Proteção'):
            if self.classe != 'Mago':
                print("📜 Este pergaminho só pode ser lido por Magos. As runas se apagam ao seu toque.")
                time.sleep(1.5)
                return
            bonus = int(item.split('+')[1]) if '+' in item else 2
            self.ac += bonus
            self.efeitos_ativos['protecao'] = 8
            self.efeitos_ativos['valor_protecao'] = bonus
            print(f"📜 As runas do pergaminho incendeiam e desaparecem!")
            time.sleep(0.8)
            print(f"   🛡️ PROTEÇÃO ARCANA: +{bonus} CA por 8 rodadas.")

        elif item.startswith('Anel da Vitalidade'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            self.gerenciar_equipamento(item)
            print(f"💖 Anel da Vitalidade equipado! +{bonus} HP máximo enquanto vestido.")

        elif item.startswith('Espada Curta'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            self.arma = {'nome': 'Espada Curta', 'bonus': bonus, 'dano': max(1, bonus)}
            self.gerenciar_equipamento(item)
            print(f"⚔️ Espada Curta equipada! +{bonus} ataque, +{max(1,bonus)} dano.")

        elif item.startswith('Lâmina Sombria'):
            bonus = int(item.split('+')[1])
            self.arma = {'nome': 'Lâmina Sombria', 'bonus': bonus, 'dano': bonus}
            self.gerenciar_equipamento(item)
            print(f"⚔️ Lâmina Sombria equipada (+{bonus} ataque/dano)!")

        elif item.startswith('Arco Élfico'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            self.arma = {'nome': 'Arco Élfico', 'bonus': bonus, 'dano': max(1, bonus)}
            self.gerenciar_equipamento(item)
            flechas_aviso = f" | 🏹 {self.flechas} flechas" if self.flechas > 0 else " | ⚠️  Sem flechas!"
            print(f"🏹 Arco Élfico equipado! +{bonus} ataque/dano. Disparo duplo 25%.{flechas_aviso}")

        elif item.startswith('Arco da Ruína'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            b = max(1, bonus - 1)
            self.arma = {'nome': 'Arco da Ruína', 'bonus': b, 'dano': b}
            self.gerenciar_equipamento(item)
            flechas_aviso = f" | 🏹 {self.flechas} flechas" if self.flechas > 0 else " | ⚠️  Sem flechas!"
            print(f"💀 Arco da Ruína equipado! +{b} ataque/dano. Disparo duplo 15%.{flechas_aviso}")

        elif item.startswith('Flechas'):
            try:
                qtd_item = int(item.split('(')[1].rstrip(')'))
            except (ValueError, IndexError):
                qtd_item = 20 if '20' in item else 10
            print(f"🏹 Pacote de flechas — {qtd_item} disponíveis.")
            _coletar_flechas(self, qtd_item)

        elif item.startswith('Armadura de Mithril'):
            self.gerenciar_equipamento(item)
            print(f"🛡️ Armadura de Mithril equipada!")

        elif item.startswith('Machado Anão Flamejante'):
            bonus = int(item.split('+')[1])
            self.arma = {'nome': 'Machado Flamejante', 'bonus': bonus + 2, 'dano': bonus + 2}
            self.gerenciar_equipamento(item)
            print(f"🔥 Machado Flamejante equipado! +{bonus+2} ataque, +{bonus+2} dano + dano de fogo.")

        elif item.startswith('Elmo da Fúria'):
            bonus = int(item.split('+')[1])
            self.bonus_temporario = bonus
            self.ac -= 1
            self.gerenciar_equipamento(item)
            print(f"🪖 Elmo da Fúria: +{bonus} dano próximo ataque, -1 CA!")

        elif item == 'Botas do Silêncio':
            self.gerenciar_equipamento(item)
            print("👟 Botas do Silêncio equipadas!")
            time.sleep(0.5)
            print("   • Inimigos só te detectam a ≤2 tiles de distância.")
            print("   • 60% de passar despercebido ao pisar na mesma célula.")
            print("   • +15% de chance de fuga em combate.")
            time.sleep(1.5)

        elif item.startswith('Cajado de Gelo'):
            bonus = int(item.split('+')[1])
            if self.classe == 'Mago':
                self.arma = {'nome': 'Cajado de Gelo', 'bonus': bonus + 2, 'dano': bonus + 2}
                self.gerenciar_equipamento(item)
                print(f"🧊 Cajado de Gelo equipado! +{bonus+2} ataque mágico, +{bonus+2} dano. Crít. 20% paralisa.")
            else:
                print("❌ Apenas magos podem usar o Cajado de Gelo.")
                self.inventario.append(item)

        elif item == 'Tomo de Sabedoria Antiga':
            if getattr(self, 'subclasse', None) == 'Bárbaro':
                print("📘 O Bárbaro encarar o tomo com desprezo.")
                time.sleep(0.5)
                print("   \"Palavras em papel não me fazem mais forte.\"")
                print("   ↩️  O tomo volta ao inventário.")
                self.inventario.append(item)
            elif self.classe == 'Mago':
                self.ac += 3
                self.base_ac += 3
                print("📘 O Mago absorve o conhecimento — CA +3!")
            else:
                self.ac += 1
                self.base_ac += 1
                print("📘 Você absorve o que pode do tomo — CA +1.")

        elif item.startswith('Amuleto de Resistência'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            self.gerenciar_equipamento(item)
            print(f"🛡️ Amuleto de Resistência equipado! +1 CA, +{5+bonus} HP máximo.")

        elif item.startswith('Anel de Regeneração'):
            self.gerenciar_equipamento(item)
            print("💍 Anel de Regeneração equipado! Restaura 1 HP por turno.")

        elif item.startswith('Manoplas do Trovão'):
            bonus = int(item.split('+')[1])
            self.arma = {'nome': 'Manoplas do Trovão', 'bonus': bonus + 1, 'dano': bonus + 2}
            self.gerenciar_equipamento(item)
            print(f"⚡ Manoplas do Trovão equipadas! +{bonus+1} ataque, +{bonus+2} dano + elétrico.")

        elif item.startswith('Orbe Mental de Vecna'):
            bonus = int(item.split('+')[1])
            if self.classe == 'Mago':
                self.arma = {'nome': 'Orbe Mental de Vecna', 'bonus': bonus + 2, 'dano': bonus + 1}
                self.gerenciar_equipamento(item)
                print(f"👁️ Orbe de Vecna sintonizado! +{bonus+2} ataque mágico, +{bonus+1} dano, +15% dano sombrio.")
            else:
                print("❌ Apenas magos podem usar o Orbe Mental de Vecna.")
                self.inventario.append(item)

        # ========================
        # NOVOS ITENS — GUERREIRO
        # ========================
        elif item.startswith('Escudo dos Condenados'):
            self.gerenciar_equipamento(item)
            print("🛡️ Escudo dos Condenados equipado! CA alta + 20% de contra-ataque passivo ao errar.")

        elif item.startswith('Colar da Fúria Ancestral'):
            self.gerenciar_equipamento(item)
            print("💢 Colar da Fúria Ancestral equipado! Concede bônus de ataque quando HP < 50%.")

        # ========================
        # NOVOS ITENS — MAGO
        # ========================
        elif item.startswith('Grimório das Almas'):
            if self.classe == 'Mago':
                bonus = int(item.split('+')[1]) if '+' in item else 1
                self.gerenciar_equipamento(item)
                print(f"📖 Grimório das Almas equipado! +{bonus} poder mágico. Desbloqueia Onda de Almas.")
            else:
                print("❌ Apenas magos compreendem o Grimório das Almas.")
                self.inventario.append(item)

        elif item == 'Cristal de Mana':
            if self.classe == 'Mago':
                self.gerenciar_equipamento(item)
                self.cristal_mana_ativo = True
                print("💎 Cristal de Mana equipado! Recarrega magia 2x mais rápido.")
            else:
                print("❌ Apenas magos podem sintonizar o Cristal de Mana.")
                self.inventario.append(item)

        # ========================
        # NOVOS ITENS — LADINO
        # ========================
        elif item.startswith('Adaga Envenenada'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            self.arma = {'nome': 'Adaga Envenenada', 'bonus': bonus + 1, 'dano': max(1, bonus)}
            self.gerenciar_equipamento(item)
            print(f"🗡️ Adaga Envenenada equipada! +{bonus+1} ataque, +{max(1,bonus)} dano. 70% de envenenar.")

        elif item == 'Manto das Sombras':
            self.gerenciar_equipamento(item)
            print("🌑 Manto das Sombras equipado! Chance de fuga 70%. Invisibilidade dura +2 turnos.")

        # ========================
        # ANTÍDOTO — UNIVERSAL
        # ========================
        elif item == 'antídoto':
            removidos = []
            for veneno_efeito in ('veneno', 'veneno_duplo'):
                if veneno_efeito in self.efeitos_ativos:
                    del self.efeitos_ativos[veneno_efeito]
                    removidos.append(veneno_efeito)
            print("💉 Você injeta o antídoto nas veias...")
            time.sleep(1)
            if removidos:
                print(f"   ✅ Veneno neutralizado! A dor some gradualmente.")
            else:
                print(f"   ⚠️  Você não estava envenenado. Antídoto desperdiçado.")
            time.sleep(1)

        elif item == 'chave':
            print("🔑 Você guardou a chave.")
            self.inventario.append(item)

        elif item == 'explosivo arremessável':
            # Em combate: não tem alvo aqui. Retorna ao inventário — combate trata o lance
            print("💣 Explosivo deve ser usado em combate contra um inimigo,")
            print("   ou fora do combate para detonar paredes e portas!")
            print("   → No combate, use a opção de itens e escolha o explosivo.")
            time.sleep(2)
            self.inventario.append(item)   # devolve

        elif 'Grimório Portal' in item:
            self.gerenciar_equipamento(item)
            print("📖 Grimório Portal equipado. Use a magia '3 — Portal' no combate ou movimento.")

        # ========================
        # NOVOS ITENS — COMUNS
        # ========================
        elif item == 'Bandagem':
            self.hp = min(self.hp + 4, self.hp_max)
            print("🩹 Você aperta a bandagem sobre a ferida...")
            time.sleep(0.8)
            print("   ✅ +4 HP recuperados.")
            time.sleep(1)

        elif item == 'Pedra de Afiar':
            self.efeitos_ativos['afiado'] = 1   # 1 combate
            self.bonus_temporario += 2
            print("🗡️ A lâmina canta ao tocar a pedra...")
            time.sleep(0.8)
            print("   ✅ +2 ataque no próximo combate.")
            time.sleep(1)

        elif item == 'Erva Medicinal':
            removidos = [e for e in ('veneno', 'veneno_duplo') if e in self.efeitos_ativos]
            for e in removidos:
                del self.efeitos_ativos[e]
            self.hp = min(self.hp + 3, self.hp_max)
            print("🌿 O sabor amargo da erva limpa o sangue...")
            time.sleep(0.8)
            if removidos:
                print("   ✅ Veneno removido! +3 HP.")
            else:
                print("   ✅ +3 HP. Sem veneno para curar, mas não foi desperdício.")
            time.sleep(1)

        elif item == 'Erva do Sono':
            print("😴 Guarde a erva para usar em combate (opção de item).")
            time.sleep(1.5)
            self.inventario.append(item)

        elif item == 'Pó de Revelação':
            mapa = getattr(self, '_mapa_ref', None)
            print("💨 O pó cintila ao ser lançado no ar...")
            time.sleep(1)
            if mapa is not None:
                armadilhas = [(pos, est.replace('armadilha_', ''))
                              for pos, est in mapa.estruturas.items()
                              if est.startswith('armadilha_')]
                if armadilhas:
                    print(f"   ⚠️  {len(armadilhas)} armadilha(s) detectada(s) nesta sala:")
                    for pos, tipo in armadilhas:
                        print(f"      • {tipo.capitalize()} em ({pos[0]}, {pos[1]})")
                else:
                    print("   ✅ Nenhuma armadilha nesta sala. O caminho está limpo.")
            else:
                print("   ⚠️  O pó revela o contorno de algo oculto... (use fora do combate).")
            time.sleep(1.5)

        elif item == 'Tocha Suja':
            self.gerenciar_equipamento(item)
            print("🔦 Tocha Suja erguida.")
            time.sleep(0.5)
            print("   A chama tremeluz na corrente de ar fétido.")
            print("   ✅ Campo de visão expandido para 2 células.")
            time.sleep(1.5)

        elif item == 'Pergaminho da Lanterna Espiritual':
            if self.classe != 'Mago':
                print("📜 Este pergaminho só pode ser lido por Magos. Os símbolos desvanecem sem deixar rastro.")
                time.sleep(1.5)
                return
            turnos = 15
            self.lanterna_espiritual = turnos
            print("📜 O pergaminho se desfaz em névoa azulada...")
            time.sleep(0.8)
            print(f"   🕯️ LANTERNA ESPIRITUAL conjurada — visão ampliada por {turnos} movimentos!")
            time.sleep(2)

        elif item == 'Diário Perdido':
            # O jogo precisa ser passado — obtido via _mapa_ref.__game se disponível
            game_ref = getattr(self, '_game_ref', None)
            if game_ref is not None:
                _ler_diario(game_ref, self)
            else:
                # Fallback: só exibe o lore sem salvar
                print("📓 Você lê as páginas do diário...")
                time.sleep(1)
                idx = random.randint(0, len(DIARIO_ENTRADAS) - 1)
                titulo, texto = DIARIO_ENTRADAS[idx]
                print(f"\n  {titulo}")
                print("  " + "─" * 52)
                for linha in texto.strip().splitlines():
                    print(f"  {linha}")
                    time.sleep(0.06)
                print("  " + "─" * 52)
                time.sleep(2)

        elif item.startswith('Adaga Simples'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            self.arma = {'nome': 'Adaga Simples', 'bonus': bonus, 'dano': max(1, bonus)}
            self.gerenciar_equipamento(item)
            print(f"🗡️ Adaga Simples equipada! +{bonus} ataque, +{max(1,bonus)} dano.")

        elif item == 'Escudo de Madeira':
            self.gerenciar_equipamento(item)
            print("🛡️ Escudo de Madeira equipado! +2 CA.")

        elif item.startswith('Cajado de Osso'):
            bonus = int(item.split('+')[1]) if '+' in item else 1
            if self.classe == 'Mago':
                self.arma = {'nome': 'Cajado de Osso', 'bonus': bonus, 'dano': 1}
                self.gerenciar_equipamento(item)
                print(f"💀 Cajado de Osso equipado (+{bonus} magia).")
            else:
                print("❌ Apenas magos sentem a ressonância do Cajado de Osso.")
                self.inventario.append(item)

        elif item == 'Capa de Couro':
            self.gerenciar_equipamento(item)
            print("🧥 Capa de Couro vestida. +1 CA.")

        elif item == 'Amuleto de Osso':
            self.gerenciar_equipamento(item)
            print("🦴 Amuleto de Osso pendurado ao pescoço. +1 ataque.")

        # ========================
        # NOVOS ITENS — RAROS
        # ========================
        elif item.startswith('Lâmina Drenante'):
            bonus = int(item.split('+')[1]) if '+' in item else 2
            self.arma = {'nome': 'Lâmina Drenante', 'bonus': bonus, 'dano': bonus,
                         'especial': 'roubo_vida'}
            self.gerenciar_equipamento(item)
            print(f"🩸 LÂMINA DRENANTE equipada (+{bonus})!")
            time.sleep(0.5)
            print("   A lâmina pulsa com sede. Cada acerto rouba vida do alvo.")
            time.sleep(1.5)

        elif item.startswith('Machado do Sangramento'):
            bonus = int(item.split('+')[1]) if '+' in item else 2
            self.arma = {'nome': 'Machado do Sangramento', 'bonus': bonus, 'dano': bonus + 1,
                         'especial': 'sangramento'}
            self.gerenciar_equipamento(item)
            print(f"🩸 MACHADO DO SANGRAMENTO equipado (+{bonus})!")
            time.sleep(0.5)
            print("   Cada golpe abre feridas que o tempo não fecha.")
            time.sleep(1.5)

        elif item.startswith('Orbe da Cegueira'):
            # Consumível de combate — guarda no inventário para uso em combate
            print("👁️ O Orbe pulsa com névoa negra. Use em combate para cegar um inimigo.")
            time.sleep(1)
            self.inventario.append(item)

        elif item.startswith('Grimório da Maldição'):
            if self.classe == 'Mago':
                bonus = int(item.split('+')[1]) if '+' in item else 2
                self.gerenciar_equipamento(item)
                print(f"📖 GRIMÓRIO DA MALDIÇÃO equipado (+{bonus})!")
                time.sleep(0.5)
                print("   Desbloqueia 'Maldição' no menu de magia. O alvo receberá dano dobrado.")
                time.sleep(1.5)
            else:
                print("❌ Apenas magos dominam a linguagem da maldição.")
                self.inventario.append(item)

        elif item == 'Coroa dos Condenados':
            self.gerenciar_equipamento(item)
            self.efeitos_ativos['coroa_atrai'] = 999  # permanente — inimigos preferem atacar o portador
            print("👑 COROA DOS CONDENADOS equipada!")
            time.sleep(0.5)
            print("   +4 CA permanente. Mas os inimigos sentem sua presença.")
            time.sleep(1.5)

        elif item == 'Runa de Ressurreição':
            self.efeitos_ativos['ressurreicao'] = 1   # uma vez por combate
            print("✨ A Runa de Ressurreição brilha em suas mãos e some.")
            time.sleep(0.8)
            print("   ✅ Se cair a 0 HP uma vez neste combate, permanece com 1 HP.")
            time.sleep(1.5)

        elif item.startswith('Espada Fantasma'):
            bonus = int(item.split('+')[1]) if '+' in item else 3
            self.arma = {'nome': 'Espada Fantasma', 'bonus': bonus, 'dano': bonus,
                         'especial': 'ignora_ca'}
            self.gerenciar_equipamento(item)
            print(f"👻 ESPADA FANTASMA equipada (+{bonus})!")
            time.sleep(0.5)
            print("   Atravessa armaduras. Ignora a CA do alvo nos testes de ataque.")
            time.sleep(1.5)

        elif item == 'Cálice do Sacrifício':
            print("🏆 Beba o Cálice em combate (opção de item) para sacrificar HP por dano.")
            time.sleep(1)
            self.inventario.append(item)

        elif item == 'Anel da Putrefação':
            self.gerenciar_equipamento(item)
            self.efeitos_ativos['putrificacao'] = 999   # passivo permanente
            print("💀 ANEL DA PUTREFAÇÃO desliza pelo dedo...")
            time.sleep(0.5)
            print("   ✅ 40% de envenenar o alvo em cada ataque, qualquer arma.")
            time.sleep(1.5)

        elif item.startswith('Tomo do Vazio'):
            self.efeitos_ativos['absorver_ataque'] = 1   # absorve 1 ataque
            print("📕 O TOMO DO VAZIO absorve a luz ao redor.")
            time.sleep(0.8)
            print("   ✅ O próximo ataque que te atingir será absorvido — e devolvido.")
            time.sleep(1.5)

        # ========================
        # COMUNS v2 — NOVOS
        # ========================
        elif item == 'Vela Votiva':
            mapa = getattr(self, '_mapa_ref', None)
            print("🕯️ A Vela Votiva queima com uma chama que nunca deveria existir aqui...")
            time.sleep(1)
            if mapa is not None:
                armadilhas = [(pos, est.replace('armadilha_', ''))
                              for pos, est in mapa.estruturas.items()
                              if est.startswith('armadilha_')]
                efeitos_armadilha = {
                    'espinhos':    'dano físico imediato',
                    'flechas':     'dano físico imediato',
                    'gás venenoso': 'veneno 3 turnos',
                    'bomba mágica': 'dano mágico imediato',
                }
                if armadilhas:
                    print(f"   ⚠️  {len(armadilhas)} armadilha(s) revelada(s):")
                    for pos, tipo in armadilhas:
                        efeito = efeitos_armadilha.get(tipo, 'efeito desconhecido')
                        print(f"      🔺 {tipo.capitalize()} em ({pos[0]}, {pos[1]}) — {efeito}")
                else:
                    print("   ✅ Nenhuma armadilha nesta sala.")
                itens_chao = [(pos, nome) for pos, nome in mapa.itens.items()]
                if itens_chao:
                    print(f"   🎁 {len(itens_chao)} item(ns) no chão:")
                    for pos, nome in itens_chao:
                        print(f"      • {nome} em ({pos[0]}, {pos[1]})")
                else:
                    print("   🔍 Nenhum item no chão desta sala.")
            else:
                print("   ⚠️  A chama vacila — use fora do combate para leitura completa.")
            time.sleep(1.5)

        elif item == 'Poção de Sangue':
            cura = 12
            hpmax_custo = 2
            self.hp = min(self.hp + cura, self.hp_max)
            self.hp_max = max(1, self.hp_max - hpmax_custo)
            self.base_hp_max = max(1, self.base_hp_max - hpmax_custo)
            if self.hp > self.hp_max:
                self.hp = self.hp_max
            print("🩸 Você abre a ampola. O líquido escarlate queima a garganta...")
            time.sleep(1)
            print(f"   ✅ +{cura} HP recuperados.")
            print(f"   ⚠️  HP máximo reduzido permanentemente em {hpmax_custo}. A sede cobra seu tributo.")
            time.sleep(1.5)

        elif item == 'Garrafa de Ácido':
            print("🧪 Guarde o ácido para lançar em combate (opção de item).")
            time.sleep(1)
            self.inventario.append(item)

        elif item == 'Armadura de Couro':
            self.gerenciar_equipamento(item)
            print("🧥 Armadura de Couro vestida. +3 CA.")

        elif item == 'Escudo de Madeira':
            self.gerenciar_equipamento(item)
            print("🛡️ Escudo de Madeira equipado! +2 CA.")

        elif item == 'Armadura do Veterano':
            if getattr(self, 'subclasse', None) == 'Cavaleiro':
                self.gerenciar_equipamento(item)
                print("⚔️ Armadura do Veterano vestida! +4 CA. O metal ecoa vitórias antigas.")
            else:
                print("❌ Apenas Cavaleiros dominam o peso desta armadura.")
                self.inventario.append(item)

        elif item.startswith('Machado de Guerra'):
            bonus = int(item.split('+')[1]) if '+' in item else 0
            atk = bonus + 3
            self.arma = {'nome': 'Machado de Guerra', 'bonus': atk, 'dano': 12}
            self.gerenciar_equipamento(item)
            print(f"🪓 Machado de Guerra empunhado! +{atk} ataque, 1d12 dano.")
            time.sleep(1)

        elif item.startswith('Espada Longa'):
            bonus = int(item.split('+')[1]) if '+' in item else 0
            atk = bonus + 2
            self.arma = {'nome': 'Espada Longa', 'bonus': atk, 'dano': 10}
            self.gerenciar_equipamento(item)
            print(f"⚔️ Espada Longa empunhada! +{atk} ataque, 1d10 dano.")
            time.sleep(1)

        elif item == 'Luvas de Combate':
            self.gerenciar_equipamento(item)
            print("🥊 Luvas de Combate calçadas. +1 ataque.")

        elif item == 'Talismã Protetor':
            self.efeitos_ativos['talisma_protetor'] = 1
            print("🔮 O Talismã Protetor pulsa com proteção antiga...")
            time.sleep(0.8)
            print("   ✅ O próximo acerto crítico (dano > 10) será reduzido a 3 de dano.")
            time.sleep(1)

        elif item == 'Pó de Gelo':
            print("❄️ Guarde o Pó de Gelo para usar em combate (opção de item).")
            time.sleep(1)
            self.inventario.append(item)

        elif item == 'Amuleto Arcano':
            if self.classe == 'Mago':
                self.gerenciar_equipamento(item)
                print("🔮 Amuleto Arcano sintonizado. Cooldown de magia reduz 1 adicional por turno.")
            else:
                print("❌ Apenas magos sentem o elo entre este amuleto e o éter.")
                self.inventario.append(item)

        elif item == 'Amuleto de Deflexão':
            self.gerenciar_equipamento(item)
            print("🛡️ Amuleto de Deflexão equipado! +1 CA + 25% de anular ataques físicos completamente.")
            time.sleep(1)

        elif item == 'Capa Encantada':
            self.gerenciar_equipamento(item)
            print("🧥 Capa Encantada vestida. +2 CA + 20% resistência a magia inimiga.")

        # ========================
        # RAROS v2 — NOVOS
        # ========================
        elif item.startswith('Espada dos Mártires'):
            bonus = int(item.split('+')[1]) if '+' in item else 3
            self.arma = {'nome': 'Espada dos Mártires', 'bonus': bonus, 'dano': bonus + 1}
            self.gerenciar_equipamento(item)
            print(f"⚔️ ESPADA DOS MÁRTIRES equipada (+{bonus})!")
            time.sleep(0.5)
            print("   A cada inimigo morto com ela: +1 ataque permanente (máx +5).")
            time.sleep(1.5)

        elif item == 'Corrente do Espectro':
            if self.classe == 'Ladino':
                self.gerenciar_equipamento(item)
                print("👻 CORRENTE DO ESPECTRO vestida!")
                time.sleep(0.5)
                print("   Passivo: 50% de negar completamente dano físico por round.")
                time.sleep(1.5)
            else:
                print("❌ A Corrente do Espectro sussurra apenas para os que andam nas sombras.")
                self.inventario.append(item)

        elif 'Grimório do Colapso' in item:
            if self.classe == 'Mago':
                self.gerenciar_equipamento(item)
                print("📖 GRIMÓRIO DO COLAPSO equipado!")
                time.sleep(0.5)
                print("   Desbloqueia 'Colapso' no menu de magia: paralisa inimigo por 2 turnos.")
                time.sleep(1.5)
            else:
                print("❌ Apenas um mago compreende as geometrias que o Colapso exige.")
                self.inventario.append(item)

        elif item == 'Runa do Limiar':
            print("🌀 A Runa do Limiar vibra em sua mão — pronta para invocar o retorno.")
            time.sleep(0.8)
            print("   ✅ Fora do combate, use 'r' para teleportar de volta ao hub central.")
            time.sleep(1)
            self.inventario.append(item)

        elif item == 'Olho Necromântico':
            if self.classe == 'Mago':
                self.gerenciar_equipamento(item)
                print("👁️ O OLHO NECROMÂNTICO fita o vazio — e o vazio fita de volta.")
                time.sleep(0.5)
                print("   Cada inimigo morto em batalha: +1 dano mágico permanente (máx +6).")
                time.sleep(1.5)
            else:
                print("❌ O Olho Necromântico precisa de um canal arcano para suas magias.")
                self.inventario.append(item)

        elif item.startswith('Lâmina Especular'):
            bonus = int(item.split('+')[1]) if '+' in item else 3
            self.arma = {'nome': 'Lâmina Especular', 'bonus': bonus, 'dano': bonus}
            self.gerenciar_equipamento(item)
            print(f"🪞 LÂMINA ESPECULAR equipada (+{bonus})!")
            time.sleep(0.5)
            print("   Passivo: reflete 30% do dano físico recebido ao atacante.")
            time.sleep(1.5)

        elif item == 'Coroa de Espinhos de Ferro':
            self.gerenciar_equipamento(item)
            print("👑 COROA DE ESPINHOS DE FERRO forçada na cabeça...")
            time.sleep(0.5)
            print("   +3 ataque, -2 CA. Drena 1 HP por turno. O sofrimento sustenta.")
            time.sleep(1.5)

        elif item == 'Rede de Caça':
            print("🕸️ Guarde a rede para usar em combate contra um inimigo (opção de item).")
            time.sleep(1)
            self.inventario.append(item)

        elif item.startswith('Tomo da Entropia'):
            self.gerenciar_equipamento(item)
            print("📖 TOMO DA ENTROPIA equipado!")
            time.sleep(0.5)
            print("   Cada turno em combate: efeito aleatório — bênção ou maldição.")
            time.sleep(1.5)

        elif item == 'Cálice de Sangue Antigo':
            print("🏺 O Cálice de Sangue Antigo exala um odor de ferro e eternidade...")
            time.sleep(0.8)
            cura = 20
            self.hp = min(self.hp + cura, self.hp_max)
            print(f"   ✅ +{cura} HP restaurados imediatamente.")
            time.sleep(0.5)
            # Aplica maldição em si mesmo
            self.efeitos_ativos['maldicao'] = 3
            print("   ⚠️  O sangue cobra tributo: você está AMALDIÇOADO por 3 turnos.")
            print("   Dano recebido será dobrado durante este período.")
            time.sleep(1.5)

        else:
            print("❓ Sem utilidade agora.")

    def _ativar_arma_por_nome(self, item_nome):
        """
        Ativa item_nome como arma principal (self.arma) sem mover o item.
        Útil para alternar rapidamente entre armas já em equipados ou na bolsa.
        Preserva flags especiais (dreno, sangramento, ignora_ca…).
        Retorna True se o item é uma arma reconhecida.
        """
        n = item_nome
        bonus = int(n.split('+')[1]) if '+' in n else 1

        if n.startswith('Espada Curta'):
            self.arma = {'nome': 'Espada Curta', 'bonus': bonus, 'dano': max(1, bonus)}
        elif n.startswith('Espada Longa'):
            atk = bonus + 2
            self.arma = {'nome': 'Espada Longa', 'bonus': atk, 'dano': 10}
        elif n.startswith('Lâmina Sombria'):
            self.arma = {'nome': 'Lâmina Sombria', 'bonus': bonus, 'dano': bonus}
        elif n.startswith('Arco Élfico'):
            self.arma = {'nome': 'Arco Élfico', 'bonus': bonus, 'dano': max(1, bonus)}
        elif n.startswith('Arco da Ruína'):
            self.arma = {'nome': 'Arco da Ruína', 'bonus': max(1, bonus - 1), 'dano': max(1, bonus - 1)}
        elif n.startswith('Machado Anão Flamejante'):
            self.arma = {'nome': 'Machado Flamejante', 'bonus': bonus + 2, 'dano': bonus + 2}
        elif n.startswith('Cajado de Gelo'):
            self.arma = {'nome': 'Cajado de Gelo', 'bonus': bonus + 2, 'dano': bonus + 2}
        elif n.startswith('Adaga Simples'):
            self.arma = {'nome': 'Adaga Simples', 'bonus': bonus, 'dano': max(1, bonus)}
        elif n.startswith('Adaga Envenenada'):
            self.arma = {'nome': 'Adaga Envenenada', 'bonus': bonus + 1, 'dano': max(1, bonus)}
        elif n.startswith('Manoplas do Trovão'):
            self.arma = {'nome': 'Manoplas do Trovão', 'bonus': bonus + 1, 'dano': bonus + 2}
        elif n.startswith('Orbe Mental de Vecna'):
            self.arma = {'nome': 'Orbe Mental de Vecna', 'bonus': bonus + 2, 'dano': bonus + 1}
        elif n.startswith('Cajado de Osso'):
            self.arma = {'nome': 'Cajado de Osso', 'bonus': bonus, 'dano': 1}
        elif n.startswith('Lâmina Drenante'):
            self.arma = {'nome': 'Lâmina Drenante', 'bonus': bonus, 'dano': bonus, 'especial': 'roubo_vida'}
        elif n.startswith('Machado do Sangramento'):
            self.arma = {'nome': 'Machado do Sangramento', 'bonus': bonus, 'dano': bonus + 1, 'especial': 'sangramento'}
        elif n.startswith('Espada Fantasma'):
            self.arma = {'nome': 'Espada Fantasma', 'bonus': bonus, 'dano': bonus, 'especial': 'ignora_ca'}
        elif n.startswith('Machado de Guerra'):
            atk = bonus + 3
            self.arma = {'nome': 'Machado de Guerra', 'bonus': atk, 'dano': 12}
        elif n.startswith('Espada dos Mártires'):
            self.arma = {'nome': 'Espada dos Mártires', 'bonus': bonus, 'dano': bonus + 1}
        elif n.startswith('Lâmina Especular'):
            self.arma = {'nome': 'Lâmina Especular', 'bonus': bonus, 'dano': bonus}
        else:
            return False
        self.atualizar_atributos_equipamento()
        return True

    def gerenciar_equipamento(self, item_nome):
        """Equipa um item. Limite de 6 slots. Se cheio, oferece substituição."""
        if len(self.equipados) < 6:
            self.equipados.append(item_nome)
            self.atualizar_atributos_equipamento()
            return

        # Slots cheios — oferecer substituição
        print(f"\n⚠️  Slots de equipamento cheios! (6/6)")
        print("   Deseja substituir um item já equipado?\n")
        for i, eq in enumerate(self.equipados):
            p = peso_item(eq)
            print(f"   {i+1}. {eq}  ({p:.1f}kg)")
        print(f"   0. Cancelar — manter '{item_nome}' na bolsa")

        escolha = input("\n   Qual slot substituir? >> ").strip()
        try:
            idx = int(escolha) - 1
            if idx < 0 or idx >= len(self.equipados):
                print("   Operação cancelada.")
                self.inventario.append(item_nome)
                return
        except ValueError:
            print("   Operação cancelada.")
            self.inventario.append(item_nome)
            return

        item_substituido = self.equipados[idx]
        print(f"\n   '{item_substituido}' será removido dos equipados.")
        print("   O que deseja fazer com ele?")
        print("   1. Guardar na bolsa")
        print("   2. Largar no chão")
        print("   0. Cancelar")
        destino = input("   >> ").strip()

        if destino == '1':
            # Verificar se cabe na bolsa (peso)
            if self.peso_atual + peso_item(item_substituido) - peso_item(item_nome) <= self.capacidade_peso or True:
                self.equipados[idx] = item_nome
                self.inventario.append(item_substituido)
                # Limpar arma se o substituído era a arma ativa
                if self.arma and self.arma.get('nome', '') in item_substituido:
                    self.arma = None
                self.atualizar_atributos_equipamento()
                print(f"   ✅ '{item_nome}' equipado. '{item_substituido}' devolvido à bolsa.")
        elif destino == '2':
            self.equipados[idx] = item_nome
            if self.arma and self.arma.get('nome', '') in item_substituido:
                self.arma = None
            self.atualizar_atributos_equipamento()
            # Retornar o item_substituido para ser largado (o chamador trata)
            # Colocamos flag especial no atributo temporário
            self._item_para_largar_no_chao = item_substituido
            print(f"   ✅ '{item_nome}' equipado. '{item_substituido}' será largado no chão.")
        else:
            print("   Operação cancelada.")
            self.inventario.append(item_nome)

    def atualizar_efeitos(self):
        efeitos_para_remover = []

        for efeito, duracao in list(self.efeitos_ativos.items()):
            if isinstance(duracao, int):
                if duracao > 1:
                    self.efeitos_ativos[efeito] -= 1
                else:
                    efeitos_para_remover.append(efeito)

        for efeito in efeitos_para_remover:
            if efeito in self.efeitos_ativos:
                del self.efeitos_ativos[efeito]

            if efeito == 'berserker':
                print("💢 O efeito do Elixir do Berserker acabou!")
                self.bonus_temporario = 0
            elif efeito == 'forca':
                print("💪 O efeito da Poção de Força acabou!")
                self.bonus_temporario = 0
            elif efeito == 'protecao':
                bonus = self.efeitos_ativos.pop('valor_protecao', None)
                if bonus:
                    self.ac -= bonus
                    print(f"🛡️ Proteção acabou (-{bonus} CA).")
            elif efeito == 'invisibilidade':
                self.invisivel = False
                print("👁️ Sua invisibilidade desvaneceu.")
            else:
                print(f"⚠️ O efeito '{efeito}' acabou.")

    def atualizar_atributos_equipamento(self):
        self.ac = self.base_ac
        self.hp_max = self.base_hp_max
        self.ataque_bonus = self.base_ataque_bonus
        self.dano_lados = self.base_dano_lados

        hp_bonus = 0
        ca_bonus = 0
        ataque_bonus = 0
        dano_bonus = 0

        for item in self.equipados:
            try:
                bonus = int(item.split('+')[1]) if '+' in item else 0
            except:
                bonus = 0

            if 'Armadura de Mithril' in item:
                ca_bonus += bonus + 2   # base +2 + scaled
            elif 'Amuleto de Resistência' in item:
                ca_bonus += 1
                hp_bonus += 5 + bonus   # +5 base + bonus escalável
            elif 'Anel da Vitalidade' in item:
                hp_bonus += bonus
            # Escudo dos Condenados
            elif 'Escudo dos Condenados' in item:
                ca_bonus += bonus + 2
            # Itens simples de CA
            elif 'Escudo de Madeira' in item:
                ca_bonus += 2
            elif 'Capa de Couro' in item:
                ca_bonus += 1
            elif 'Amuleto de Osso' in item:
                ataque_bonus += 1
            # Coroa dos Condenados
            elif 'Coroa dos Condenados' in item:
                ca_bonus += 4
            # ── Armas de base fixa (dano e ataque já embutidos no arma dict) ──
            elif 'Machado de Guerra' in item:
                ataque_bonus += bonus    # bônus escalável extra (já há +3 fixo no arma dict)
            elif 'Espada Longa' in item:
                ataque_bonus += bonus    # bônus escalável extra (já há +2 fixo no arma dict)
            elif any(palavra in item for palavra in [
                'Espada Curta', 'Lâmina Sombria', 'Arco Élfico', 'Machado Anão Flamejante',
                'Manoplas do Trovão', 'Elmo da Fúria', 'Cajado de Gelo',
                'Orbe Mental de Vecna', 'Adaga Envenenada', 'Grimório das Almas',
                'Lâmina Drenante', 'Machado do Sangramento', 'Espada Fantasma',
                'Adaga Simples', 'Cajado de Osso',
            ]):
                ataque_bonus += bonus
                dano_bonus += max(1, bonus)
            # Grimório Portal — sem bônus de atributo, só habilidade
            elif 'Grimório Portal' in item:
                pass
            # Comuns v2
            elif 'Armadura de Couro' in item:
                ca_bonus += 3
            elif 'Escudo de Madeira' in item:
                ca_bonus += 2
            elif 'Armadura do Veterano' in item:
                ca_bonus += 4
            elif 'Luvas de Combate' in item:
                ataque_bonus += 1
            elif 'Capa Encantada' in item:
                ca_bonus += 2
            elif 'Amuleto de Deflexão' in item:
                ca_bonus += 1
            elif 'Amuleto Arcano' in item:
                pass   # passivo — tratado no turno_magia
            elif 'Talismã Protetor' in item:
                pass   # passivo — tratado no combate
            # Raros v2 equipáveis
            elif 'Espada dos Mártires' in item:
                ataque_bonus += bonus
                dano_bonus += bonus // 2 if bonus > 1 else 1
            elif 'Corrente do Espectro' in item:
                pass   # passivo — tratado no combate
            elif 'Grimório do Colapso' in item:
                pass   # habilidade — tratado no usar_magia
            elif 'Olho Necromântico' in item:
                pass   # passivo — acumula via flag
            elif 'Lâmina Especular' in item:
                ataque_bonus += bonus
                dano_bonus += bonus // 2 if bonus > 1 else 1
            elif 'Coroa de Espinhos de Ferro' in item:
                ataque_bonus += 3
                ca_bonus -= 2
            elif 'Rede de Caça' in item:
                pass   # combate: ativado como item
            elif 'Tomo da Entropia' in item:
                pass   # passivo aleatório por turno
            elif 'Tocha Suja' in item:
                pass   # visão: tratada em Mapa.mostrar via equipados
            elif 'Grimório da Maldição' in item:
                ataque_bonus += bonus // 2

        self.ac += ca_bonus
        self.hp_max = self.base_hp_max + hp_bonus
        self.ataque_bonus = self.base_ataque_bonus + ataque_bonus
        self.dano_lados = self.base_dano_lados + dano_bonus

        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def turno_magia(self):
        # Cristal de Mana: reduz cooldown 2x mais rápido
        reducao = 2 if self.cristal_mana_ativo and any('Cristal de Mana' in eq for eq in self.equipados) else 1
        # Amuleto Arcano: +1 redução adicional para Mago
        if self.classe == 'Mago' and any('Amuleto Arcano' in eq for eq in self.equipados):
            reducao += 1
        if self.cooldown_magia > 0:
            self.cooldown_magia = max(0, self.cooldown_magia - reducao)
        # Habilidade especial (não-magos)
        if self.cooldown_habilidade > 0:
            self.cooldown_habilidade -= 1
        # Coroa de Espinhos de Ferro — drena 1 HP por turno
        if any('Coroa de Espinhos de Ferro' in eq for eq in self.equipados):
            if self.hp > 1:
                self.hp -= 1
                print("👑 A Coroa de Espinhos drena 1 HP...")

        # Anel de Regeneração
        regeneracao = sum(1 for eq in self.equipados if 'Anel de Regeneração' in eq)
        if regeneracao > 0 and self.hp < self.hp_max:
            cura = min(regeneracao, self.hp_max - self.hp)
            self.hp += cura
            print(f"💖 {regeneracao}x Anel de Regeneração restauram {cura} HP.")

    def esta_vivo(self):
        return self.hp > 0

    def exibir_equipamentos(self):
        return " | Equipados:\n\t" + (', \n\t'.join(self.equipados) if self.equipados else "nenhum")

    def status(self):
        # Mostrar veneno especialmente
        veneno_str = ""
        if 'veneno' in self.efeitos_ativos:
            d = self.efeitos_ativos['veneno']
            veneno_str = f" 🐍VENENO({d['dano']}dmg/{d['turnos']}t)"
        if 'veneno_duplo' in self.efeitos_ativos:
            d = self.efeitos_ativos['veneno_duplo']
            veneno_str += f" ☠️VENENO FORTE({d['dano']}dmg/{d['turnos']}t)"

        classe_str = f"{self.classe}/{self.subclasse}" if self.subclasse else self.classe
        flechas_str = f" | 🏹 {self.flechas} flechas" if getattr(self, 'flechas', 0) > 0 else ""
        status = (f"{self.nome} ({classe_str}) - HP: {self.hp}/{self.hp_max} "
                  f"| CA: {self.ac}{veneno_str}{flechas_str}\n"
                  f"| Carga: {self.peso_atual:.1f}/{self.capacidade_peso}kg"
                  f"  (bolsa {self.peso_bolsa:.1f}kg + vestido {self.peso_vestido:.1f}kg)\n"
                  f"  Inventário: {', '.join(self.inventario) if self.inventario else 'vazio'}\n")
        status += self.exibir_equipamentos()
        if self.invisivel:
            status += " | 👻 Invisível"
        efeitos_visiveis = [f"{k}({v})" for k, v in self.efeitos_ativos.items()
                            if not k.startswith('valor_') and not isinstance(v, dict)]
        if efeitos_visiveis:
            status += "\n | Efeitos: " + ', '.join(efeitos_visiveis)
        return status

    def calcular_poder_magico_total(self):
        poder = self.ataque_bonus
        poder += self.bonus_temporario

        for item in self.equipados:
            if 'Cajado' in item:
                try:
                    poder += int(item.split('+')[1]) + 2
                except:
                    pass
            elif 'Orbe Mental de Vecna' in item:
                try:
                    poder += int(item.split('+')[1]) + 1
                except:
                    pass
            elif 'Grimório das Almas' in item:
                try:
                    poder += int(item.split('+')[1]) + 3
                except:
                    pass

        if any('Orbe Mental de Vecna' in eq for eq in self.equipados):
            amplificado = int(poder * 1.15)
            print(f"👁️ O Orbe de Vecna amplifica: {poder} ➜ {amplificado}")
            poder = amplificado
        # Olho Necromântico — bônus acumulado por kills
        poder += self.efeitos_ativos.get('olho_kills', 0)
        return poder


# =====================================================================
# INIMIGOS
# =====================================================================

class Inimigo:
    # ── Imunidades por nome ───────────────────────────────────────────
    IMUNES_VENENO = {
        "Esqueleto Guardião", "Arqueiro das Trevas",
        "Carniçal Profano", "Arauto do Vazio", "Dracolich",
        "Espectro das Profundezas",
    }
    IMUNES_CEGUEIRA = {
        "Dracolich", "Espectro das Profundezas", "Arauto do Vazio",
    }
    IMUNES_SANGRAMENTO = {
        "Gárgula de Pedra", "Esqueleto Guardião",
        "Dracolich", "Espectro das Profundezas",
    }
    IMUNES_PARALISADO = {
        "Orc Berserker",   # ignora 50% das vezes — tratado no atacar
    }

    def __init__(self, nome, hp, ac, ataque_bonus, dano_lados, pos):
        self.nome = nome
        self.hp = self.hp_max = hp
        self.ac = ac
        self.ataque_bonus = ataque_bonus
        self.dano_lados = dano_lados
        self.pos = pos
        self.efeitos_ativos = {}
        self.imune_veneno      = nome in Inimigo.IMUNES_VENENO
        self.imune_cegueira    = nome in Inimigo.IMUNES_CEGUEIRA
        self.imune_sangramento = nome in Inimigo.IMUNES_SANGRAMENTO
        self.alertado = False  # True quando atacado à distância — move-se direto ao jogador
        self.flechas_cravadas = 0  # flechas recebidas — usadas para recuperação ao morrer

    def processar_efeitos(self):
        remover = []
        for efeito, dados in list(self.efeitos_ativos.items()):
            if isinstance(dados, dict) and 'dano' in dados:
                # Imunidades
                if self.imune_veneno and efeito in ('veneno', 'veneno_duplo'):
                    remover.append(efeito)
                    print(f"💀 {self.nome} é imune a veneno! Efeito dissipado.")
                    continue
                if self.imune_sangramento and efeito == 'sangramento':
                    remover.append(efeito)
                    print(f"🪨 {self.nome} é imune a sangramento!")
                    continue
                dano = dados['dano']
                self.hp -= dano
                if efeito == 'sangramento':
                    print(f"🩸 {self.nome} sangra {dano} — a ferida não fecha!")
                elif efeito == 'fogo':
                    print(f"🔥 {self.nome} queima vivo: {dano} de dano!")
                else:
                    print(f"☠️  {self.nome} sofre {dano} de dano por {efeito}!")
                dados['turnos'] -= 1
                if dados['turnos'] <= 0:
                    remover.append(efeito)

        # Cegueira — decrementa (com imunidade)
        if 'cegueira' in self.efeitos_ativos and isinstance(self.efeitos_ativos['cegueira'], int):
            if self.imune_cegueira:
                remover.append('cegueira')
                print(f"👁️  {self.nome} dispela a cegueira — é imune!")
            else:
                self.efeitos_ativos['cegueira'] -= 1
                if self.efeitos_ativos['cegueira'] <= 0:
                    remover.append('cegueira')
                    print(f"👁️  A cegueira de {self.nome} passa.")

        # Maldição — decrementa
        if 'maldicao' in self.efeitos_ativos and isinstance(self.efeitos_ativos['maldicao'], int):
            self.efeitos_ativos['maldicao'] -= 1
            if self.efeitos_ativos['maldicao'] <= 0:
                remover.append('maldicao')
                print(f"💀 A maldição de {self.nome} se dissolve.")

        for efeito in remover:
            if efeito in self.efeitos_ativos:
                del self.efeitos_ativos[efeito]
            if efeito == 'cegueira':
                pen = self.efeitos_ativos.pop('cegueira_ca_pen', 0)
                if pen:
                    self.ac += pen

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            if getattr(self, 'bloqueia_fuga', False) or self.nome == "Olho de Vecna":
                print(vecna_meets), time.sleep(1)
                print(f"👁️ {self.nome} ignora sua invisibilidade!")
            else:
                print(f"🕵️‍♂️ {alvo.nome} está invisível! {self.nome} não ataca.")
                return

        if self.efeitos_ativos.get('cegueira', 0) > 0:
            if random.random() < 0.50:
                print(f"🕶️  {self.nome} está CEGO! O golpe passa pelo lado.")
                return

        if 'paralisado' in self.efeitos_ativos:
            print(f"🔒 {self.nome} está PARALISADO — não pode agir!")
            return

        if getattr(alvo, 'efeitos_ativos', {}).get('absorver_ataque', 0) > 0:
            dano_guardado = rolar_dado(self.dano_lados)
            alvo.efeitos_ativos['dano_guardado_vazio'] = dano_guardado
            del alvo.efeitos_ativos['absorver_ataque']
            print(f"📕 O TOMO DO VAZIO absorve o ataque de {self.nome}! ({dano_guardado} armazenados)")
            time.sleep(1)
            self.hp -= dano_guardado
            print(f"   ⚡ O vazio devolve {dano_guardado} de dano diretamente em {self.nome}!")
            return

        rolagem = rolar_dado(20)
        total   = rolagem + self.ataque_bonus
        if rolagem == 20:
            dano = rolar_dado(self.dano_lados) * 2
        elif total >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
        else:
            print(f"{self.nome} erra o ataque.")
            return

        if getattr(alvo, 'efeitos_ativos', {}).get('maldicao', 0) > 0:
            dano = dano * 2
            print(f"💀 MALDIÇÃO! O dano é dobrado sobre {alvo.nome}!")

        if getattr(alvo, 'efeitos_ativos', {}).get('ressurreicao', 0) > 0 and alvo.hp - dano <= 0:
            dano = alvo.hp - 1
            del alvo.efeitos_ativos['ressurreicao']
            print(f"✨ A RUNA DE RESSURREIÇÃO brilha! {alvo.nome} permanece com 1 HP!")

        if (dano > 10 and getattr(alvo, 'efeitos_ativos', {}).get('talisma_protetor', 0) > 0):
            print(f"🔮 TALISMÃ PROTETOR! Crítico absorvido — dano reduzido a 3!")
            dano = 3
            del alvo.efeitos_ativos['talisma_protetor']

        # Espectro: resistência física 40%
        if getattr(self, '_resistencia_fisica', False) and random.random() < 0.40:
            dano_red = max(1, dano // 2)
            print(f"👻 {self.nome} resiste ao dano físico! ({dano} → {dano_red})")
            dano = dano_red

        alvo.hp -= dano
        if rolagem == 20:
            print(f"💫 ACERTO CRÍTICO de {self.nome}: {dano} de dano!")
        else:
            print(f"💫 {self.nome} causa {dano} de dano!")

        if dano > 0 and any('Amuleto de Deflexão' in eq for eq in getattr(alvo, 'equipados', [])):
            if random.random() < 0.25:
                print(f"🛡️ AMULETO DE DEFLEXÃO! O golpe de {self.nome} é desviado!")
                alvo.hp += dano
                dano = 0

        if dano > 0 and any('Lâmina Especular' in eq for eq in getattr(alvo, 'equipados', [])):
            refletido = max(1, int(dano * 0.30))
            self.hp = max(0, self.hp - refletido)
            print(f"🪞 LÂMINA ESPECULAR reflete {refletido} de dano em {self.nome}!")

    def esta_vivo(self):
        return self.hp > 0


class InimigoEspecial(Inimigo):
    def __init__(self, nome, hp, ac, ataque_bonus, dano_lados, pos, tipo="comum", magia=False):
        super().__init__(nome, hp, ac, ataque_bonus, dano_lados, pos)
        self.tipo  = tipo
        self.magia = magia
        self.efeitos_ativos = {}
        if nome == "Dracolich":
            self.imune_veneno      = True
            self.imune_cegueira    = True
            self.imune_sangramento = True

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🕵️‍♂️ {alvo.nome} está invisível! {self.nome} não ataca.")
            return
        if self.magia and random.random() < 0.3:
            dano = rolar_dado(10) + 5
            alvo.hp -= dano
            print(f"🔥 {self.nome} lança uma rajada sombria: {dano} de dano!")
        else:
            super().atacar(alvo)


# =====================================================================
# INIMIGOS — TIER 1  ·  Área inicial  ·  dif 1–9
# =====================================================================

class RatoCarniceiro(InimigoEspecial):
    """Verme roedor das masmorras rasas. Fraco sozinho, perigoso em bando.
    MECÂNICA: duplo ataque rápido; crit causa sangramento 1 turno."""
    def __init__(self, pos, dificuldade=1):
        super().__init__(
            nome="Rato Carniceiro",
            hp=4 + dificuldade,
            ac=10 + dificuldade // 4,
            ataque_bonus=2 + dificuldade // 3,
            dano_lados=4,
            pos=pos, tipo='comum')

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🐀 O Rato não te vê nas sombras.")
            return
        for i in range(2):
            r = rolar_dado(20); t = r + self.ataque_bonus
            if r == 20:
                dano = rolar_dado(self.dano_lados) * 2
                alvo.hp -= dano
                print(f"💫 CRÍTICO! Rato rasga: {dano} dano!")
                alvo.efeitos_ativos['sangramento'] = {'dano': 1, 'turnos': 2}
                print(f"🩸 Garra arranha fundo — sangramento por 2 turnos!")
            elif t >= alvo.ac:
                dano = rolar_dado(self.dano_lados)
                alvo.hp -= dano
                print(f"🐀 Mordida #{i+1} do Rato Carniceiro: {dano} dano!")
            else:
                print(f"🐀 Mordida #{i+1} raspa no ar.")
            if not alvo.esta_vivo():
                break


class GoblinFurtivo(InimigoEspecial):
    """Oportunista das ruínas. Pode tentar fugir; às vezes rouba itens.
    MECÂNICA: 25% de escape quando HP < 35%; acerto 15% de roubar 1 item.
    FRAQUEZA: CA baixa — fácil de acertar."""
    def __init__(self, pos, dificuldade=1):
        super().__init__(
            nome="Goblin Furtivo",
            hp=7 + dificuldade,
            ac=11 + dificuldade // 4,
            ataque_bonus=3 + dificuldade // 3,
            dano_lados=5,
            pos=pos, tipo='comum')
        self._fugiu = False

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🕵️‍♂️ Goblin não te encontra na escuridão.")
            return
        # Tenta fugir quando quase morto
        if self.hp < self.hp_max * 0.35 and not self._fugiu:
            if random.random() < 0.25:
                self._fugiu = True
                self.hp = 0   # foge da sala — considerado derrotado sem loot
                print(f"🏃 O Goblin Furtivo FOGE para as sombras antes que você possa agir!")
                return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💫 CRÍTICO! Goblin apunhala pelas costas: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"🗡️ Goblin Furtivo corta: {dano} dano!")
            if random.random() < 0.15 and getattr(alvo, 'inventario', []):
                roubado = random.choice(alvo.inventario)
                alvo.inventario.remove(roubado)
                print(f"   💰 Goblin ROUBA {roubado} no meio do golpe!")
        else:
            print(f"🗡️ Goblin erra — tropeça no próprio pé.")


class EsqueletoGuardiao(InimigoEspecial):
    """Ossos animados de antigos sentinelas. Imune a veneno e sangramento.
    MECÂNICA: ao chegar em 0 HP pela 1ª vez, 30% de se remontar com 4 HP.
    FRAQUEZA: dano mágico recebido +50%."""
    def __init__(self, pos, dificuldade=1):
        super().__init__(
            nome="Esqueleto Guardião",
            hp=12 + dificuldade,
            ac=14 + dificuldade // 3,
            ataque_bonus=4 + dificuldade // 3,
            dano_lados=5,
            pos=pos, tipo='morto-vivo')
        self._remontou = False

    def esta_vivo(self):
        if self.hp <= 0 and not self._remontou:
            if random.random() < 0.30:
                self._remontou = True
                self.hp = 4
                print(f"💀 O ESQUELETO se remonta dos fragmentos! (4 HP restantes)")
                time.sleep(1)
                return True
        return self.hp > 0

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"💀 Esqueleto varre o ar sem te achar.")
            return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💫 CRÍTICO! Esqueleto golpeia com osso afiado: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"💀 Esqueleto Guardião ataca: {dano} dano!")
        else:
            print(f"💀 Esqueleto acerta pedra — farelos de osso.")


# =====================================================================
# INIMIGOS — TIER 2  ·  Área intermediária  ·  dif 10–17
# =====================================================================

class OrcBerserker(InimigoEspecial):
    """Orc de pele grossa. Resistente mas previsível.
    MECÂNICA: Fúria a <50% HP (+4 atk). 50% ignora paralisação.
    FRAQUEZA: CA média, sem defesas mágicas."""
    def __init__(self, pos, dificuldade=10):
        super().__init__(
            nome="Orc Berserker",
            hp=18 + dificuldade * 2,
            ac=13 + dificuldade // 4,
            ataque_bonus=5 + dificuldade // 3,
            dano_lados=8,
            pos=pos, tipo='guerreiro')
        self._furia_ativa = False

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"💪 Orc fareja o ar — não te encontra.")
            return
        # Ignora paralisação 50% das vezes
        if 'paralisado' in self.efeitos_ativos:
            if random.random() < 0.50:
                print(f"💢 O Orc QUEBRA a paralisação pela força bruta!")
                del self.efeitos_ativos['paralisado']
            else:
                print(f"🔒 {self.nome} está paralisado e não age.")
                return
        # Fúria
        if self.hp < self.hp_max * 0.5 and not self._furia_ativa:
            self._furia_ativa = True
            self.ataque_bonus += 4
            print(f"💢 {self.nome} entra em FÚRIA BERSERKER! +4 ataque!")
            time.sleep(0.8)
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💥 CRÍTICO BRUTAL! Orc esmaga: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"💪 Orc Berserker golpeia: {dano} dano!")
        else:
            print(f"💪 Orc erra — mas arranca um pedaço do chão.")


class ArqueiroDasTrevas(InimigoEspecial):
    """Morto-vivo arqueiro. Ataque duplo a distância. Imune a veneno.
    MECÂNICA: 2 flechas por turno (1d6 cada). Em corpo a corpo perde 2 CA.
    FRAQUEZA: HP baixo, frágil se alcançado."""
    def __init__(self, pos, dificuldade=10):
        super().__init__(
            nome="Arqueiro das Trevas",
            hp=13 + dificuldade,
            ac=12 + dificuldade // 4,
            ataque_bonus=6 + dificuldade // 3,
            dano_lados=6,
            pos=pos, tipo='morto-vivo')
        self.arma_loot = f'Arco da Ruína +{1 + dificuldade // 4}'

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🏹 Flechas passam longe — alvo invisível.")
            return
        print(f"🏹 Arqueiro das Trevas dispara flechas!")
        for i in range(2):
            r = rolar_dado(20); t = r + self.ataque_bonus
            if r == 20:
                dano = rolar_dado(4) * 2
                alvo.hp -= dano
                print(f"  💫 CRÍTICO! Flecha certeira: {dano} dano!")
            elif t >= alvo.ac:
                dano = rolar_dado(4)
                alvo.hp -= dano
                print(f"  🏹 Flecha #{i+1}: {dano} dano!")
            else:
                print(f"  🏹 Flecha #{i+1} desvia.")
            if not alvo.esta_vivo():
                break


class VermedaEntranhas(InimigoEspecial):
    """Criatura viscosa das profundezas. Veneno persistente e alto.
    MECÂNICA: 65% veneno (1d3+1) por 3 turnos.
    FRAQUEZA: CA baixa, sem resistências."""
    def __init__(self, pos, dificuldade=10):
        super().__init__(
            nome="Verme das Entranhas",
            hp=10 + dificuldade * 2,
            ac=11 + dificuldade // 3,
            ataque_bonus=4 + dificuldade // 2,
            dano_lados=5,
            pos=pos, tipo='venenoso')

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🐛 Verme rasteja às cegas.")
            return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💫 CRÍTICO! Verme morde ferozmente: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"🐛 Verme das Entranhas morde: {dano} dano!")
        else:
            print(f"🐛 Verme erra.")
            return
        if random.random() < 0.65:
            dano_v = rolar_dado(3) + 1
            alvo.efeitos_ativos['veneno'] = {'dano': dano_v, 'turnos': 3}
            print(f"🐍 Veneno inoculado! {dano_v} HP por 3 turnos!")


class CarnicaldaProfundeza(InimigoEspecial):
    """Morto-vivo com lâmina profana. Veneno DOBRADO. Imune a veneno.
    MECÂNICA: 50% veneno duplo (1d4×2) por 4 turnos.
    FRAQUEZA: sem resistência mágica, velocidade baixa."""
    def __init__(self, pos, dificuldade=10):
        super().__init__(
            nome="Carniçal Profano",
            hp=15 + dificuldade * 2,
            ac=13 + dificuldade // 3,
            ataque_bonus=5 + dificuldade // 2,
            dano_lados=7,
            pos=pos, tipo='venenoso_duplo')
        self.arma_loot = f'Lâmina Sombria +{1 + dificuldade // 4}'

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"⚔️ Carniçal fareja o ar.")
            return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💫 CRÍTICO! Carniçal rasga com lâmina profana: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"⚔️ Carniçal Profano corta com lâmina negra: {dano} dano!")
        else:
            print(f"⚔️ Carniçal erra.")
            return
        if random.random() < 0.50:
            dano_v = rolar_dado(4) * 2
            alvo.efeitos_ativos['veneno_duplo'] = {'dano': dano_v, 'turnos': 4}
            print(f"☠️  VENENO DOBRADO! Toxina profana: {dano_v} HP por 4 turnos!")


# =====================================================================
# INIMIGOS — TIER 3  ·  Área profunda  ·  dif 18–27
# =====================================================================

class SacerdoteDevedor(InimigoEspecial):
    """Servo corrompido. Magia sombria, veneno ritual e auto-cura.
    MECÂNICA: 40% ataque mágico + 55% veneno; 20% se cura 5 HP.
    FRAQUEZA: CA moderada, frágil sem magia ativa."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Sacerdote Devorador",
            hp=20 + dificuldade * 2,
            ac=15 + dificuldade // 4,
            ataque_bonus=7 + dificuldade // 3,
            dano_lados=9,
            pos=pos, tipo='elite_magico', magia=True)

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"✝️ Sacerdote murmura um encanto sem alvo.")
            return
        roll = random.random()
        if roll < 0.20:
            # Auto-cura
            cura = rolar_dado(6) + 2
            self.hp = min(self.hp + cura, self.hp_max)
            print(f"✝️ Sacerdote canaliza energia sombria em si mesmo — cura {cura} HP! ({self.hp}/{self.hp_max})")
        elif roll < 0.55:
            dano = rolar_dado(12) + 6
            alvo.hp -= dano
            print(f"✝️ Sacerdote canaliza necrose: {dano} dano mágico!")
            if random.random() < 0.55:
                dano_v = rolar_dado(3) + 2
                alvo.efeitos_ativos['veneno'] = {'dano': dano_v, 'turnos': 3}
                print(f"🐍 Veneno ritual! {dano_v} HP por 3 turnos!")
        else:
            r = rolar_dado(20); t = r + self.ataque_bonus
            if r == 20:
                dano = rolar_dado(self.dano_lados) * 2
                alvo.hp -= dano
                print(f"💫 CRÍTICO! Cajado profano: {dano} dano!")
            elif t >= alvo.ac:
                dano = rolar_dado(self.dano_lados)
                alvo.hp -= dano
                print(f"✝️ Cajado profano: {dano} dano!")
            else:
                print(f"✝️ Sacerdote erra.")


class ArautodoVazio(InimigoEspecial):
    """Entidade espectral que drena vitalidade. Imune veneno e cegueira.
    MECÂNICA: drena HP para si em cada acerto; 40% drenagem persistente.
    FRAQUEZA: dano físico em área (explosivo) ignora resistência espectral."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Arauto do Vazio",
            hp=24 + dificuldade * 2,
            ac=16 + dificuldade // 4,
            ataque_bonus=8 + dificuldade // 3,
            dano_lados=8,
            pos=pos, tipo='elite_espectral')

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🌑 Arauto sente sua essência... mas não consegue te alcançar.")
            return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            self.hp = min(self.hp + dano // 2, self.hp_max)
            print(f"💫 CRÍTICO DRENAGEM! Arauto suga {dano} HP, recupera {dano//2}!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            cura = dano // 2
            self.hp = min(self.hp + cura, self.hp_max)
            print(f"🌑 Arauto do Vazio drena {dano} HP e recupera {cura}.")
            if random.random() < 0.40:
                dano_v = rolar_dado(3)
                alvo.efeitos_ativos['drenagem'] = {'dano': dano_v, 'turnos': 2}
                print(f"🌑 Drenagem persistente: {dano_v} HP por 2 turnos!")
        else:
            print(f"🌑 Arauto do Vazio não encontra abertura.")


class GargulaDePedra(InimigoEspecial):
    """Estátua animada. Imune sangramento. Contraataque físico 30%.
    MECÂNICA: magia tem 25% de falhar (resistência pétrea); contraataque
              passivo — ao receber dano físico, 30% devolve metade.
    FRAQUEZA: lenta (sem ataque duplo), vulnerável a gelo/fogo DoT."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Gárgula de Pedra",
            hp=28 + dificuldade * 2,
            ac=18 + dificuldade // 4,
            ataque_bonus=6 + dificuldade // 3,
            dano_lados=9,
            pos=pos, tipo='elite_pétrea')
        self.resistencia_magica = 0.25   # verificado em usar_magia

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🗿 Gárgula permanece imóvel... por ora.")
            return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💫 CRÍTICO! Gárgula esmaga com peso de pedra: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"🗿 Gárgula de Pedra golpeia: {dano} dano!")
        else:
            print(f"🗿 Gárgula acerta o chão de pedra.")

    def receber_dano_fisico(self, dano, atacante):
        """Chamado pelo combate quando o jogador acerta. Contraataque 30%."""
        if random.random() < 0.30:
            contra = max(1, dano // 2)
            atacante.hp -= contra
            print(f"🗿 CONTRAATAQUE DA GÁRGULA! Fragmentos de pedra causam {contra} dano!")


class CampeaoDaMorte(InimigoEspecial):
    """Elite necromante-guerreiro. Magia e físico. Aplica maldição.
    MECÂNICA: 40% de aplicar maldição por 2 turnos no acerto.
    FRAQUEZA: CA relativamente baixa para um elite — aposta tudo no dano."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Campeão da Morte",
            hp=30 + dificuldade * 3,
            ac=17 + dificuldade // 4,
            ataque_bonus=9 + dificuldade // 3,
            dano_lados=12,
            pos=pos, tipo="elite", magia=True)

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"💀 Campeão sente o cheiro de mortal... mas não vê.")
            return
        if self.magia and random.random() < 0.30:
            dano = rolar_dado(10) + 5
            alvo.hp -= dano
            print(f"💀 Campeão da Morte invoca necrose: {dano} dano mágico!")
            if random.random() < 0.40:
                turnos = alvo.efeitos_ativos.get('maldicao', 0) + 2
                alvo.efeitos_ativos['maldicao'] = turnos
                print(f"☠️  MALDIÇÃO! Dano dobrado por 2 turnos!")
            return
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💥 CRÍTICO MORTAL! Campeão decepa: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"⚔️ Campeão da Morte golpeia: {dano} dano!")
            if random.random() < 0.40:
                turnos = alvo.efeitos_ativos.get('maldicao', 0) + 2
                alvo.efeitos_ativos['maldicao'] = turnos
                print(f"☠️  MALDIÇÃO aplicada por 2 turnos!")
        else:
            print(f"⚔️ Campeão erra — mas sente sua fraqueza.")


# =====================================================================
# INIMIGOS — TIER 4  ·  Área extrema  ·  modo extremo / dif 18+
# =====================================================================

class CavaleiroSemNome(InimigoEspecial):
    """Guerreiro amaldiçoado do abismo. Fúria letal. 50% ignora invis.
    MECÂNICA: fúria a <40% HP (+5 atk); 50% chance de dissipar invis.
    FRAQUEZA: CA alta mas previsível — padrão de ataque único."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Cavaleiro Sem Nome",
            hp=38 + dificuldade * 3,
            ac=20 + dificuldade // 4,
            ataque_bonus=12 + dificuldade // 3,
            dano_lados=14,
            pos=pos, tipo='extremo_guerreiro')
        self.furia_ativa = False
        self.arma_loot   = f'Elmo da Fúria +{3 + dificuldade // 6}'

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            if random.random() < 0.50:
                alvo.invisivel = False
                print(f"⚔️ O Cavaleiro sente a presença — INVISIBILIDADE DISSIPADA!")
            else:
                return
        if self.hp < self.hp_max * 0.4 and not self.furia_ativa:
            self.furia_ativa = True
            self.ataque_bonus += 5
            print(f"🔥 FÚRIA AMALDIÇOADA do Cavaleiro! +5 ataque!")
            time.sleep(0.8)
        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💥 CRÍTICO BRUTAL! Cavaleiro esmaga: {dano} dano!")
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"⚔️ Cavaleiro Sem Nome golpeia com força colossal: {dano} dano!")
        else:
            print(f"⚔️ Cavaleiro erra — mas mal por pouco.")


class SerpenteAbissal(InimigoEspecial):
    """Serpente das profundezas. Fareija invis. Ataque duplo + veneno.
    MECÂNICA: anula invisibilidade; 2 mordidas por turno; 75% veneno duplo forte.
    FRAQUEZA: nenhuma resistência física, CA média."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Serpente Abissal",
            hp=30 + dificuldade * 2,
            ac=17 + dificuldade // 4,
            ataque_bonus=10 + dificuldade // 3,
            dano_lados=12,
            pos=pos, tipo='extremo_venenoso')

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            alvo.invisivel = False
            print(f"🐍 A Serpente fareija sua essência vital — INVISIBILIDADE DISSIPADA!")
        for i in range(2):
            r = rolar_dado(20); t = r + self.ataque_bonus
            print(f"🐍 Mordida #{i+1}:")
            if r == 20:
                dano = rolar_dado(self.dano_lados) * 2
                alvo.hp -= dano
                print(f"  💥 CRÍTICO! Presas perfuram: {dano} dano!")
            elif t >= alvo.ac:
                dano = rolar_dado(self.dano_lados)
                alvo.hp -= dano
                print(f"  🐍 Mordida: {dano} dano!")
            else:
                print(f"  ❌ Mordida erra.")
                continue
            if random.random() < 0.75:
                dano_v = rolar_dado(5) * 2
                alvo.efeitos_ativos['veneno_duplo'] = {'dano': dano_v, 'turnos': 5}
                print(f"  ☠️  VENENO ABISSAL! {dano_v} HP por 5 turnos!")
            if not alvo.esta_vivo():
                break


class Dracolich(InimigoEspecial):
    """Dragão-morto-vivo. Imune veneno, cegueira, sangramento.
    MECÂNICA: 35% ataque de fogo com DoT (1d4 por 3 turnos); resistência
              mágica 30% (magia falha); crítico paralisa 1 turno.
    FRAQUEZA: lento — ataca só 1x por round."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Dracolich",
            hp=40 + dificuldade * 3,
            ac=19 + dificuldade // 3,
            ataque_bonus=13 + dificuldade // 3,
            dano_lados=14,
            pos=pos, tipo='lendário', magia=True)
        self.resistencia_magica = 0.30

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            print(f"🐉 Olhos do Dracolich brilham — te vê através de qualquer ilusão!")
            alvo.invisivel = False

        roll = random.random()
        if roll < 0.35:
            # Bafo de fogo com DoT
            dano = rolar_dado(12) + 8
            alvo.hp -= dano
            print(f"🔥 BAFO DE FOGO! Dracolich exala chamas necróticas: {dano} dano!")
            dano_fogo = rolar_dado(4)
            alvo.efeitos_ativos['fogo'] = {'dano': dano_fogo, 'turnos': 3}
            print(f"   🔥 Queimadura! {dano_fogo} HP por 3 turnos!")
        else:
            r = rolar_dado(20); t = r + self.ataque_bonus
            if r == 20:
                dano = rolar_dado(self.dano_lados) * 2
                alvo.hp -= dano
                print(f"💫 CRÍTICO MORTAL do Dracolich: {dano} dano!")
                alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 1}
                print(f"   🔒 O terror do crítico PARALISA {alvo.nome} por 1 turno!")
            elif t >= alvo.ac:
                dano = rolar_dado(self.dano_lados)
                alvo.hp -= dano
                print(f"🐉 Dracolich arranha com garras profanas: {dano} dano!")
            else:
                print(f"🐉 Dracolich erra — mas a arrogância é palpável.")


class EspectrodasProfundezas(InimigoEspecial):
    """Espírito profano das masmorras mais fundas. Resistência física.
    MECÂNICA: 40% resistência física (dano reduzido); imune veneno, cegueira,
              sangramento; por acerto: reduz HP máximo do jogador em 1.
              Dissipa invisibilidade (fareija almas vivas).
    FRAQUEZA: dano mágico recebido integral sem resistência."""
    def __init__(self, pos, dificuldade=18):
        super().__init__(
            nome="Espectro das Profundezas",
            hp=32 + dificuldade * 3,
            ac=17 + dificuldade // 4,
            ataque_bonus=11 + dificuldade // 3,
            dano_lados=10,
            pos=pos, tipo='extremo_espectral')
        self._resistencia_fisica = True   # flag verificada em Inimigo.atacar

    def atacar(self, alvo):
        if getattr(alvo, 'invisivel', False):
            alvo.invisivel = False
            print(f"👻 Espectro fareija sua alma — INVISIBILIDADE DISSIPADA!")

        r = rolar_dado(20); t = r + self.ataque_bonus
        if r == 20:
            dano = rolar_dado(self.dano_lados) * 2
            alvo.hp -= dano
            print(f"💫 CRÍTICO ESPECTRAL! Espectro atravessa você: {dano} dano!")
            _drenar_hp_max(alvo, 2)
        elif t >= alvo.ac:
            dano = rolar_dado(self.dano_lados)
            alvo.hp -= dano
            print(f"👻 Espectro toca sua alma: {dano} dano!")
            _drenar_hp_max(alvo, 1)
        else:
            print(f"👻 Espectro atravessa o ar sem te alcançar.")


def _drenar_hp_max(alvo, quantidade):
    """Reduz o HP máximo do alvo permanentemente."""
    alvo.base_hp_max = max(1, alvo.base_hp_max - quantidade)
    alvo.hp_max      = max(1, alvo.hp_max - quantidade)
    if alvo.hp > alvo.hp_max:
        alvo.hp = alvo.hp_max
    print(f"   💔 DRENAGEM DE ALMA! HP máximo reduzido em {quantidade}. ({alvo.hp}/{alvo.hp_max})")


# =====================================================================
# OlhoDeVecna — Chefe final escalável
# =====================================================================

class OlhoDeVecna(InimigoEspecial):
    def __init__(self, pos, dificuldade=1):
        # Escala progressiva: cada ponto de dificuldade aumenta HP, AC e poder de ataque
        hp_base       = 80  + dificuldade * 12
        ac_base       = 16  + dificuldade // 2
        atk_base      = 8   + dificuldade // 3
        dano_base     = 10  + dificuldade // 2
        super().__init__(
            nome="Olho de Vecna",
            hp=hp_base,
            ac=ac_base,
            ataque_bonus=atk_base,
            dano_lados=dano_base,
            pos=pos,
            tipo="lendário",
            magia=True
        )
        self.dificuldade = dificuldade
        self.bloqueia_fuga = True
        self.efeitos_ativos = {}
        self.fase2_ativada = False  # Ativa quando HP < 50%
        self._hp_max = hp_base

    def processar_efeitos(self):
        remover = []
        for efeito, dados in list(self.efeitos_ativos.items()):
            if isinstance(dados, dict) and 'dano' in dados:
                dano = dados['dano']
                if dano > 0:
                    self.hp -= dano
                    print(f"☠️  {self.nome} sofre {dano} de dano por {efeito}!")
                dados['turnos'] -= 1
                if dados['turnos'] <= 0:
                    remover.append(efeito)
        for efeito in remover:
            del self.efeitos_ativos[efeito]

        # Fase 2 — quando HP cai abaixo de 50%
        if not self.fase2_ativada and self.hp <= self._hp_max // 2:
            self.fase2_ativada = True
            print("\n🧿 O OLHO DE VECNA ENTRA EM FRENESI!")
            print("   Sua CA sobe, e seus ataques se tornam mais erráticos e devastadores!")
            time.sleep(2)
            self.ac += 4
            self.ataque_bonus += 3

    def atacar(self, alvo):
        limpar_tela()
        print(vecnas_eye)

        # Fase 2: ataques com efeitos especiais escalados
        if self.fase2_ativada:
            self._atacar_fase2(alvo)
        else:
            self._atacar_fase1(alvo)

    def _atacar_fase1(self, alvo):
        """Ataques da fase 1 — escalonados pela dificuldade."""
        roll = random.random()

        if self.dificuldade >= 20 and roll < 0.20:
            # Raio de desintegração (dif alta)
            dano = rolar_dado(self.dano_lados) + self.ataque_bonus
            dano = int(dano * 1.5)
            alvo.hp -= dano
            print(f"👁️ RAIO DE DESINTEGRAÇÃO! O Olho dissolve parte de você: {dano} de dano!")
        elif self.dificuldade >= 10 and roll < 0.35:
            # Maldição — enfraquece o jogador
            dano = max(0, rolar_dado(self.dano_lados) + self.ataque_bonus - alvo.ac)
            alvo.hp -= dano
            alvo.efeitos_ativos['maldicao'] = alvo.efeitos_ativos.get('maldicao', 0) + 2
            print(f"👁️ O Olho de Vecna amaldiçoa {alvo.nome}! {dano} de dano + Maldição (2t)!")
        else:
            # Ataque base
            dano = max(0, rolar_dado(self.dano_lados) + self.ataque_bonus - alvo.ac)
            alvo.hp -= dano
            print(f"👁️ {self.nome} vê através de qualquer ilusão. {dano} de dano a {alvo.nome}!")

    def _atacar_fase2(self, alvo):
        """Fase 2 — ataques múltiplos/caóticos."""
        roll = random.random()
        print("🔥 FASE 2 — O OLho pulsa com energia profana!")
        time.sleep(1)

        if roll < 0.25:
            # Ataque duplo
            d1 = max(0, rolar_dado(self.dano_lados) + self.ataque_bonus - alvo.ac)
            d2 = max(0, rolar_dado(self.dano_lados // 2 + 1) + self.ataque_bonus // 2 - alvo.ac)
            alvo.hp -= (d1 + d2)
            print(f"💢 GOLPE DUPLO! {d1} + {d2} = {d1 + d2} de dano!")
        elif roll < 0.45:
            # Drenagem de vida
            dano = max(0, rolar_dado(self.dano_lados) + self.ataque_bonus - alvo.ac)
            alvo.hp -= dano
            cura = dano // 3
            self.hp = min(self.hp + cura, self._hp_max)
            print(f"🩸 DRENAGEM DE VIDA! {dano} de dano. O Olho se cura em {cura} HP!")
        elif roll < 0.60 and self.dificuldade >= 8:
            # Paralisação mental
            dano = max(0, rolar_dado(self.dano_lados) + self.ataque_bonus - alvo.ac)
            alvo.hp -= dano
            alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 1}
            print(f"🧠 PARALISAÇÃO MENTAL! {dano} de dano. {alvo.nome} congela por 1 turno!")
        else:
            # Ataque base potenciado
            dano = max(0, rolar_dado(self.dano_lados) + self.ataque_bonus - alvo.ac)
            dano = int(dano * 1.25)
            alvo.hp -= dano
            print(f"👁️ Ataque potenciado: {dano} de dano!")


# =====================================================================
# HABILIDADES ESPECIAIS (Guerreiro / Ladino — botão 2 no combate)
# =====================================================================

def _usar_habilidade_especial(jogador, inimigo):
    """
    Executa a habilidade especial do Guerreiro ou Ladino.
    Retorna True se turno foi consumido, False se cancelado.
    """
    hab = jogador.habilidade_especial
    arma_dano = jogador.arma['dano'] if jogador.arma else 0

    if jogador.cooldown_habilidade > 0:
        print(f"⏳ Habilidade em recarga! ({jogador.cooldown_habilidade} turno(s))")
        time.sleep(1.5)
        return False

    # ── GUERREIRO ────────────────────────────────────────────────────
    if hab == 'investida':
        # Dano: (2d_lados + 2×arma_dano) com +3 de acerto. Penalidade: -2 CA
        print("⚔️  INVESTIDA FEROZ!")
        time.sleep(0.5)
        print("   Você avança com toda a força, arma à frente...")
        time.sleep(1)
        rolagem = rolar_dado(20) + jogador.ataque_bonus + 5
        if rolagem >= inimigo.ac or rolagem == 20:
            dano = (rolar_dado(jogador.dano_lados) + rolar_dado(jogador.dano_lados)
                    + arma_dano * 2)
            inimigo.hp -= dano
            print(f"   💥 Investida conecta! {dano} de dano massivo!")
        else:
            print("   ❌ Investida errou — o inimigo se desvia no último instante!")
        print("   ⚠️  Você ficou exposto! CA reduzida até o próximo turno.")
        jogador.ac = max(1, jogador.ac - 2)
        jogador.efeitos_ativos['exposto'] = 2
        jogador.cooldown_habilidade = 4
        time.sleep(1.5)
        return True

    elif hab == 'contra-ataque':
        if jogador.contra_ataque_ativo:
            # Desativação manual — cooldown começa agora
            jogador.contra_ataque_ativo = False
            jogador.cooldown_habilidade = 3
            print("🛡️  Modo Contra-Ataque DESATIVADO manualmente.")
            print("   ⏳ Recarga: 4 turnos.")
            time.sleep(1.5)
            return True
        else:
            jogador.contra_ataque_ativo = True
            # Não armazenar em efeitos_ativos — atualizar_efeitos() remove int=1 no mesmo turno
            print("🛡️  CONTRA-ATAQUE PREPARADO!")
            print("   Aguardando o próximo ataque do inimigo para revidar com força total.")
            print("   Dispara automaticamente e entra em recarga de 4 turnos.")
            time.sleep(1.5)
            return True

    elif hab == 'sequencial':
        # 3 golpes: cada um rola dano_lados + arma_dano (sem redução)
        print("⚡ GOLPES SEQUENCIAIS!")
        time.sleep(0.5)
        print("   Três golpes rápidos em sequência...")
        time.sleep(0.8)
        acertos = 0
        dano_total = 0
        for i in range(3):
            rolagem = rolar_dado(20) + jogador.ataque_bonus
            if rolagem >= inimigo.ac:
                dano = rolar_dado(jogador.dano_lados) + arma_dano
                inimigo.hp -= dano
                dano_total += dano
                acertos += 1
                print(f"   ⚔️  Golpe {i+1}: acerto! {dano} de dano.")
            else:
                print(f"   ❌ Golpe {i+1}: errou.")
            time.sleep(0.6)
        print(f"   📊 Total: {acertos}/3 acertos, {dano_total} de dano.")
        jogador.cooldown_habilidade = 3
        time.sleep(1)
        return True

    # ── LADINO ───────────────────────────────────────────────────────
    elif hab == 'sorrateiro':
        # Dano: 2d_lados + arma_dano + 1d8 + bônus invisibilidade
        print("🗡️  GOLPE SORRATEIRO!")
        time.sleep(0.5)
        bonus_invis = 6 if jogador.invisivel else 0
        dano = (rolar_dado(jogador.dano_lados) + rolar_dado(jogador.dano_lados)
                + arma_dano + rolar_dado(8) + bonus_invis)
        inimigo.hp -= dano
        if random.random() < 0.70:   # 70% de envenenar
            veneno_dano = rolar_dado(4) + 2
            inimigo.efeitos_ativos['veneno'] = {'dano': veneno_dano, 'turnos': 3}
            print(f"   ☠️  Golpe nas costas + veneno! {dano} dano. Veneno: {veneno_dano}/turno×3.")
        else:
            print(f"   🗡️  Golpe preciso e profundo! {dano} de dano.")
        jogador.cooldown_habilidade = 3
        time.sleep(1.5)
        return True

    elif hab == 'evasao':
        print("💨 EVASÃO!")
        time.sleep(0.5)
        print("   Você recua, abaixa e desaparece entre as sombras...")
        time.sleep(1)
        jogador.efeitos_ativos['evasao_ativa'] = 3
        jogador.cooldown_habilidade = 3
        print("   ✅ Evasão ativa por 2 turnos. 60% de desviar cada ataque.")
        time.sleep(1.5)
        return True

    elif hab == 'veneno_lamina':
        # Golpe imediato + aplica veneno potente nos próximos 3 ataques
        print("🐍 VENENO NA LÂMINA!")
        time.sleep(0.5)
        print("   Você aplica toxina concentrada na lâmina...")
        time.sleep(1)
        # Golpe imediato com a lâmina envenenada
        rolagem = rolar_dado(20) + jogador.ataque_bonus
        if rolagem >= inimigo.ac:
            dano_golpe = rolar_dado(jogador.dano_lados) + arma_dano
            inimigo.hp -= dano_golpe
            veneno_dano = rolar_dado(6) + 3
            inimigo.efeitos_ativos['veneno_duplo'] = {'dano': veneno_dano, 'turnos': 4}
            print(f"   🐍 Lâmina envenena! {dano_golpe} dano imediato.")
            print(f"   ☠️  Veneno potente: {veneno_dano} HP/turno por 4 turnos!")
        else:
            # Errou o golpe mas aplica o efeito nos próximos ataques mesmo assim
            print("   ❌ Golpe inicial errou — mas a lâmina está envenenada!")
        jogador.efeitos_ativos['lamina_envenenada'] = 3  # 3 ataques seguintes envenenam
        jogador.cooldown_habilidade = 4
        print("   ✅ Próximos 3 ataques aplicam veneno automático.")
        time.sleep(1.5)
        return True

    print("❓ Habilidade desconhecida.")
    time.sleep(1)
    return False


def _combate_explosivo(jogador, inimigo):
    """Usa explosivo arremessável como arma em combate."""
    if 'explosivo arremessável' not in jogador.inventario:
        print("❌ Sem explosivo!")
        time.sleep(1)
        return False

    jogador.inventario.remove('explosivo arremessável')
    print("💣 Você arremessa o explosivo em direção ao inimigo!")
    time.sleep(1)

    resultado = random.random()
    if resultado < 0.55:
        # Boa explosão — alto dano no inimigo
        dano_ini = rolar_dado(10) + rolar_dado(8) + 3
        dano_self = rolar_dado(4)
        inimigo.hp -= dano_ini
        jogador.hp = max(1, jogador.hp - dano_self)
        print(f"   💥 KABOOM! Explosão perfeita! {dano_ini} de dano em {inimigo.nome}!")
        print(f"   🪨 A onda de choque te atinge levemente: -{dano_self} HP.")
    elif resultado < 0.80:
        # Pouco dano no inimigo, muito no personagem — acidente
        dano_ini = rolar_dado(4)
        dano_self = rolar_dado(8) + 3
        inimigo.hp -= dano_ini
        jogador.hp = max(1, jogador.hp - dano_self)
        print(f"   💥 O explosivo detona perto demais!")
        print(f"   🔥 {inimigo.nome} recebe apenas {dano_ini} de dano...")
        print(f"   🪨 Mas você é jogado pelo impacto: -{dano_self} HP! ACIDENTE!")
    else:
        # Explosão falha ou ricochete completo
        dano_self = rolar_dado(6) + 2
        jogador.hp = max(1, jogador.hp - dano_self)
        print("   💥 O explosivo quica e explode em VOCÊ!")
        print(f"   🪨 -{dano_self} HP! {inimigo.nome} assiste incrédulo.")

    time.sleep(2)
    return True


# =====================================================================
# FUNÇÕES DE COMBATE
# =====================================================================

def consumir_turno_jogador(jogador):
    jogador.turno_magia()
    jogador.atualizar_efeitos()
    # ── Tomo da Entropia — efeito aleatório por turno ──────────────
    if any('Tomo da Entropia' in eq for eq in jogador.equipados):
        _tomo_entropia(jogador)


def _tomo_entropia(jogador):
    """Efeito aleatório por turno do Tomo da Entropia."""
    roll = random.random()
    if roll < 0.15:
        cura = rolar_dado(8) + 2
        jogador.hp = min(jogador.hp + cura, jogador.hp_max)
        print(f"📖 Tomo da Entropia: energia caótica te restaura +{cura} HP!")
    elif roll < 0.30:
        bônus = rolar_dado(4)
        jogador.bonus_temporario += bônus
        print(f"📖 Tomo da Entropia: fúria cósmica! +{bônus} ataque neste turno.")
    elif roll < 0.45:
        dano_caos = rolar_dado(6)
        jogador.hp = max(1, jogador.hp - dano_caos)
        print(f"📖 Tomo da Entropia: o caos se volta! -{dano_caos} HP.")
    elif roll < 0.55:
        jogador.ac += 2
        jogador.efeitos_ativos['entropia_ca'] = 1
        print("📖 Tomo da Entropia: escudo etéreo! +2 CA por 1 turno.")
    elif roll < 0.65:
        jogador.invisivel = True
        jogador.efeitos_ativos['invisibilidade'] = 1
        print("📖 Tomo da Entropia: dissolve-se no caos! Invisível por 1 turno.")
    elif roll < 0.75:
        jogador.cooldown_magia = max(0, jogador.cooldown_magia - 2)
        print("📖 Tomo da Entropia: o tempo enrola-se! -2 cooldown de magia.")
    else:
        print("📖 Tomo da Entropia: sussurros incompreensíveis... nada acontece.")


def mostrar_inimigo_art(inimigo):
    """Exibe o ASCII art do inimigo correspondente."""
    arte = {
        'Rato Carniceiro':         scavenger_rat,
        'Goblin Furtivo':          goblin,
        'Esqueleto Guardião':      guardian_skeleton,
        'Arqueiro das Trevas':     skull_archer,
        'Orc Berserker':           warrior_orc,
        'Gárgula de Pedra':        gargula,
        'Campeão da Morte':        death_champion,
        'Dracolich':               dracolich,
        'Verme das Entranhas':     verme_das_entranhas,
        'Carniçal Profano':        carniçal_profano,
        'Sacerdote Devorador':     sacerdote_devorador,
        'Arauto do Vazio':         arauto_do_vazio,
        'Cavaleiro Sem Nome':      cavaleiro_sem_nome,
        'Serpente Abissal':        serpente_abissal,
        'Espectro das Profundezas':reaper,
    }
    if inimigo.nome in arte:
        print(arte[inimigo.nome])


def combate(jogador, inimigo, inimigo_iniciou=False):
    print(f"\n⚔️  Combate iniciado contra {inimigo.nome}!")
    mostrar_inimigo_art(inimigo)
    time.sleep(2)

    def barra_vida(atual, maximo, tamanho=20):
        proporcao = max(atual, 0) / maximo
        cheios = int(proporcao * tamanho)
        vazios = tamanho - cheios
        return f"[{'█' * cheios}{'-' * vazios}] {max(0, atual)}/{maximo}"

    while jogador.esta_vivo() and inimigo.esta_vivo():

        # =====================================================
        # DoTs no início do round
        # =====================================================
        if hasattr(jogador, "processar_efeitos"):
            jogador.processar_efeitos()
            time.sleep(1)

        if hasattr(inimigo, "processar_efeitos"):
            inimigo.processar_efeitos()
            time.sleep(1)

        if not jogador.esta_vivo():
            print(f"☠️  {jogador.nome} sucumbiu aos efeitos!")
            return

        if not inimigo.esta_vivo():
            print(f"🔥 {inimigo.nome} foi derrotado pelos efeitos!")
            _loot_inimigo(jogador, inimigo)
            return

        # =====================================================
        # Inimigo inicia (emboscada)
        # =====================================================
        if inimigo_iniciou:
            limpar_tela()
            mostrar_inimigo_art(inimigo)
            print(f"🛡️  {inimigo.nome}: {barra_vida(inimigo.hp, inimigo.hp_max)}")
            print(f"\n❤️  {jogador.nome}: {barra_vida(jogador.hp, jogador.hp_max)}")
            print(f"\n⚠️  {inimigo.nome} te ataca de surpresa antes que você reaja!\n")
            time.sleep(1.5)
            inimigo.atacar(jogador)
            inimigo_iniciou = False
            time.sleep(1.5)
            if not jogador.esta_vivo():
                print("☠️  Você foi derrotado antes de agir!")
                time.sleep(2)
                return
            print(f"\n❤️  {jogador.nome}: {barra_vida(jogador.hp, jogador.hp_max)}")
            print("\n  [ ENTER para reagir ]")
            input()

        # =====================================================
        # Turno do jogador
        # =====================================================
        limpar_tela()
        mostrar_inimigo_art(inimigo)
        print(f"🛡️  {inimigo.nome}: {barra_vida(inimigo.hp, inimigo.hp_max)}")

        # Mostrar veneno ativo do jogador
        veneno_aviso = ""
        if 'veneno' in jogador.efeitos_ativos or 'veneno_duplo' in jogador.efeitos_ativos:
            veneno_aviso = " 🐍[ENVENENADO]"

        print(f"\n❤️  {jogador.nome}: {barra_vida(jogador.hp, jogador.hp_max)}{veneno_aviso}")
        print(f"🎽 {jogador.exibir_equipamentos()}")

        print("\nAções disponíveis:")
        tem_arco_combate = (jogador.arma and jogador.arma['nome'] in ('Arco Élfico', 'Arco da Ruína')
                            and getattr(jogador, 'flechas', 0) > 0)
        if tem_arco_combate:
            print(f"  1 - Atacar 🏹 (flechas restantes: {jogador.flechas})")
        else:
            print("  1 - Atacar")
        if jogador.classe == "Mago":
            cooldown_info = f" (recarga: {jogador.cooldown_magia})" if jogador.cooldown_magia > 0 else ""
            print(f"  2 - Usar Magia{cooldown_info}")
        elif jogador.habilidade_especial:
            nomes_hab = {
                'investida':     "Investida Feroz",
                'contra-ataque': "Contra-ataque",
                'sequencial':    "Golpes Sequenciais",
                'sorrateiro':    "Golpe Sorrateiro",
                'evasao':        "Evasão",
                'veneno_lamina': "Veneno na Lâmina",
            }
            nome_hab = nomes_hab.get(jogador.habilidade_especial, jogador.habilidade_especial)
            if jogador.cooldown_habilidade > 0:
                print(f"  2 - {nome_hab} [recarga: {jogador.cooldown_habilidade}t]")
            elif jogador.habilidade_especial == 'contra-ataque' and jogador.contra_ataque_ativo:
                print(f"  2 - {nome_hab} [AGUARDANDO — desativar]")
            else:
                print(f"  2 - {nome_hab}")
        tem_explosivo = 'explosivo arremessável' in jogador.inventario
        print(f"  3 - Usar Item{' (💣 explosivo disponível)' if tem_explosivo else ''}")
        print("  4 - Tentar Fugir")

        turno_valido = False
        acao = input("Escolha sua ação: ").strip()

        if acao == '1':
            hp_antes_inimigo = inimigo.hp
            if tem_arco_combate:
                # ── Ataque com arco (arma ativa = Arco Élfico) ────────
                mapa_ref = getattr(jogador, '_mapa_ref', None)
                if mapa_ref and hasattr(mapa_ref, 'tem_linha_de_visao'):
                    jx, jy = jogador.pos
                    ix, iy = inimigo.pos
                    if not mapa_ref.tem_linha_de_visao(jx, jy, ix, iy):
                        print("🏹 Uma parede bloqueia o disparo! Sem linha de visão.")
                        time.sleep(1.5)
                        print("⚠️  O inimigo não tem piedade.")
                        if inimigo.esta_vivo():
                            inimigo.atacar(jogador)
                        continue
                bonus = jogador.arma.get('bonus', 1)
                rolagem = rolar_dado(20) + jogador.ataque_bonus
                dano_base = rolar_dado(4) + bonus   # arco: d4 (menor alcance = menos força de impacto)
                if rolagem >= inimigo.ac or rolagem == 20:
                    critico = (rolagem == 20)
                    dano = dano_base * 2 if critico else dano_base
                    inimigo.hp -= dano
                    jogador.flechas = max(0, jogador.flechas - 1)
                    inimigo.flechas_cravadas = getattr(inimigo, 'flechas_cravadas', 0) + 1
                    if critico:
                        print(f"🏹 CRÍTICO! Flecha certeira em {inimigo.nome}: {dano} dano!")
                    else:
                        print(f"🏹 Flecha acerta {inimigo.nome}: {dano} dano!")
                    if jogador.flechas > 0 and random.random() < 0.25:
                        dano2 = rolar_dado(4) + bonus
                        inimigo.hp -= dano2
                        jogador.flechas = max(0, jogador.flechas - 1)
                        inimigo.flechas_cravadas = getattr(inimigo, 'flechas_cravadas', 0) + 1
                        print(f"🏹 DISPARO DUPLO! Segunda flecha: {dano2} dano!")
                else:
                    print(f"🏹 Flecha desvia! (rolagem {rolagem} vs CA {inimigo.ac})")
                    jogador.flechas = max(0, jogador.flechas - 1)
                dano_causado = max(0, hp_antes_inimigo - inimigo.hp)
                if dano_causado > 0 and hasattr(inimigo, 'receber_dano_fisico'):
                    inimigo.receber_dano_fisico(dano_causado, jogador)
                if jogador.flechas == 0:
                    print("   ⚠️  Flechas esgotadas! Arco desequipado.")
                    nome_arco = next((eq for eq in jogador.equipados if 'Arco Élfico' in eq or 'Arco da Ruína' in eq), None)
                    if nome_arco:
                        jogador.equipados.remove(nome_arco)
                        jogador.inventario.append(nome_arco)
                    jogador.arma = None
                    jogador.atualizar_atributos_equipamento()
                else:
                    print(f"   🏹 Flechas restantes: {jogador.flechas}")
            elif jogador.efeitos_ativos.pop('sacrificio', None):
                # ── Golpe do Sacrifício (arma corpo a corpo) ──────────
                dano_base = rolar_dado(jogador.dano_lados) + (jogador.arma['dano'] if jogador.arma else 0)
                dano_trip = dano_base * 3
                inimigo.hp -= dano_trip
                print(f"🏆 GOLPE DO SACRIFÍCIO! {dano_trip} de dano devastador!")
                time.sleep(1)
                dano_causado = max(0, hp_antes_inimigo - inimigo.hp)
                if dano_causado > 0 and hasattr(inimigo, 'receber_dano_fisico'):
                    inimigo.receber_dano_fisico(dano_causado, jogador)
            else:
                # ── Ataque corpo a corpo normal ───────────────────────
                jogador.atacar(inimigo)
                dano_causado = max(0, hp_antes_inimigo - inimigo.hp)
                if dano_causado > 0 and hasattr(inimigo, 'receber_dano_fisico'):
                    inimigo.receber_dano_fisico(dano_causado, jogador)
            turno_valido = True

        elif acao == '2' and jogador.classe == "Mago":
            if jogador.usar_magia(inimigo, mapa_atual=getattr(jogador, '_mapa_ref', None)):
                turno_valido = True

        elif acao == '2' and jogador.habilidade_especial and jogador.classe != "Mago":
            turno_valido = _usar_habilidade_especial(jogador, inimigo)

        elif acao == '3':
            turno_valido = jogador.usar_item_em_combate(inimigo)


        elif acao == '4':
            turno_valido = True

            if getattr(inimigo, 'bloqueia_fuga', False):
                print("🧿 Fugir é impossível!")
                time.sleep(2)
                inimigo.atacar(jogador)
                time.sleep(2)
                continue

            # ── Chance de fuga — acumula bônus de múltiplas fontes ────────
            if jogador.classe == "Ladino":
                chance_base = 0.45
            elif jogador.classe == "Guerreiro":
                chance_base = 0.18
            else:
                chance_base = 0.28

            bonus_fuga = 0.0
            fontes_fuga = []

            if 'Manto das Sombras' in jogador.equipados:
                bonus_fuga += 0.30
                fontes_fuga.append("Manto das Sombras (+30%)")
            if 'Botas do Silêncio' in jogador.equipados:
                bonus_fuga += 0.15
                fontes_fuga.append("Botas do Silêncio (+15%)")
            if jogador.invisivel:
                bonus_fuga += 0.25
                fontes_fuga.append("Invisibilidade (+25%)")
            if 'evasao_ativa' in jogador.efeitos_ativos:
                bonus_fuga += 0.10
                fontes_fuga.append("Evasão ativa (+10%)")

            chance_final = min(0.95, chance_base + bonus_fuga)

            if fontes_fuga:
                print(f"   Bônus de fuga: {', '.join(fontes_fuga)}")
            print(f"🏃 Tentando fugir... (chance total: {int(chance_final * 100)}%)")
            time.sleep(1)
            if random.random() < chance_final:
                print("✅ Você fugiu!")
                time.sleep(1)
                if random.random() < 0.33:
                    item = random.choice(['poção de cura', 'poção de força', 'poção de invisibilidade'])
                    if jogador.pode_carregar(item):
                        jogador.inventario.append(item)
                        print(f"🎁 Ao fugir, você encontra: {item}!")
                    else:
                        print(f"🎁 {item} estava no chão, mas sua mochila está cheia!")
                    time.sleep(2)
                if jogador.inventario and random.random() < 0.33:
                    perdido = random.choice(jogador.inventario)
                    jogador.inventario.remove(perdido)
                    print(f"💨 Na pressa, você perde: {perdido}!")
                return
            else:
                print("❌ Falha na fuga! Você perde o turno.")

        else:
            print("❌ Você hesita... o momento se perde.")
            time.sleep(1)
            turno_valido = True   # turno perdido, mas cooldowns avançam

        if turno_valido:
            consumir_turno_jogador(jogador)
        else:
            print("⚠️  O inimigo não tem piedade.")

        time.sleep(1)

        # ── Remover CA de exposição (investida) ───────────────────
        if 'exposto' in jogador.efeitos_ativos:
            jogador.ac = min(jogador.base_ac + sum(
                [2 if 'Armadura de Mithril' in eq else
                 2 if 'Escudo dos Condenados' in eq else
                 1 if 'Amuleto de Resistência' in eq else 0
                 for eq in jogador.equipados]
            ), jogador.ac + 2)
            del jogador.efeitos_ativos['exposto']

        if inimigo.esta_vivo():
            # ── Corrente do Espectro (Ladino) — 50% negar dano físico ──
            if (jogador.classe == 'Ladino' and
                    any('Corrente do Espectro' in eq for eq in jogador.equipados) and
                    random.random() < 0.50):
                print(f"👻 CORRENTE DO ESPECTRO! Você se dissolve entre os planos — {inimigo.nome} não atinge.")
                time.sleep(1)
            # ── Evasão passiva ────────────────────────────────────
            elif 'evasao_ativa' in jogador.efeitos_ativos and jogador.efeitos_ativos['evasao_ativa'] > 0:
                if random.random() < 0.60:
                    print(f"💨 Evasão! Você desvia do ataque de {inimigo.nome}!")
                    time.sleep(1)
                    jogador.efeitos_ativos['evasao_ativa'] -= 1
                    if jogador.efeitos_ativos['evasao_ativa'] <= 0:
                        del jogador.efeitos_ativos['evasao_ativa']
                        print("   (Evasão esgotada.)")
                    # Contra-ataque de oportunidade em evasão
                    if jogador.contra_ataque_ativo:
                        dano_ca = rolar_dado(jogador.dano_lados) + (jogador.arma['dano'] if jogador.arma else 0)
                        inimigo.hp -= dano_ca
                        print(f"   ⚔️  Contra-ataque de oportunidade! {dano_ca} de dano.")
                else:
                    inimigo.atacar(jogador)
            else:
                # ── Contra-ataque passivo ─────────────────────────
                if jogador.contra_ataque_ativo:
                    inimigo.atacar(jogador)
                    # Revida sempre — independente de o inimigo ter acertado ou errado
                    dano_ca = rolar_dado(jogador.dano_lados) + (jogador.arma['dano'] if jogador.arma else 0)
                    inimigo.hp -= dano_ca
                    print(f"   ⚔️  CONTRA-ATAQUE! {dano_ca} de dano em {inimigo.nome}!")
                    # Auto-desativar após 1 uso
                    jogador.contra_ataque_ativo = False
                    jogador.cooldown_habilidade = 4
                    print("   🛡️  Contra-ataque disparado. Recarga: 4 turnos.")
                else:
                    inimigo.atacar(jogador)

            # ── Lâmina envenenada aplica veneno no próximo ataque jogador ──
            # (já aplicado no atacar() do jogador via flag — reduz cargas aqui)
            if 'lamina_envenenada' in jogador.efeitos_ativos:
                jogador.efeitos_ativos['lamina_envenenada'] -= 1
                if jogador.efeitos_ativos['lamina_envenenada'] <= 0:
                    del jogador.efeitos_ativos['lamina_envenenada']
                    print("   (Veneno na lâmina esgotado.)")

            time.sleep(1)
        else:
            print(f"💀 {inimigo.nome} foi derrotado!")
            _loot_inimigo(jogador, inimigo)
            time.sleep(2)


def _coletar_flechas(jogador, disponivel):
    """Permite escolher quantas flechas coletar (0 a disponivel). Peso: 0.05kg/unidade."""
    peso_unit = 0.05
    espaco_livre = jogador.capacidade_peso - jogador.peso_atual
    max_pelo_peso = int(espaco_livre / peso_unit)
    max_coletavel = min(disponivel, max_pelo_peso)

    if max_coletavel <= 0:
        print(f"   ⚠️  Carga máxima atingida — sem espaço para flechas.")
        time.sleep(1)
        return

    print(f"   Coletar quantas? (1–{max_coletavel}, 0=nenhuma, ENTER=todas): ", end='', flush=True)
    entrada = input().strip()
    if entrada == '' or entrada.lower() == 'a':
        qtd = max_coletavel
    else:
        try:
            qtd = max(0, min(int(entrada), max_coletavel))
        except ValueError:
            qtd = 0

    if qtd > 0:
        jogador.flechas = getattr(jogador, 'flechas', 0) + qtd
        peso_ganho = round(qtd * peso_unit, 2)
        print(f"   ✅ +{qtd} flechas coletadas ({peso_ganho}kg). Total: {jogador.flechas} ({round(jogador.flechas * peso_unit, 2)}kg).")
    else:
        print(f"   ↩️  Flechas deixadas.")
    time.sleep(1)


def _loot_inimigo(jogador, inimigo):
    """Checa se inimigo derrubou loot especial (arma portada)."""
    # ── Drop de flechas ────────────────────────────────────────────────
    # Caso 1: Arqueiro das Trevas — sempre dropa flechas (6–12), escolha de qtd
    if inimigo.nome == 'Arqueiro das Trevas':
        qtd_total = random.randint(6, 12)
        print(f"🏹 O Arqueiro das Trevas carregava {qtd_total} flechas.")
        _coletar_flechas(jogador, qtd_total)
    # Caso 2: Inimigo foi atingido por flechas — recupera até 50% delas
    elif getattr(inimigo, 'flechas_cravadas', 0) > 0:
        cravadas = inimigo.flechas_cravadas
        recuperaveis = max(1, cravadas // 2)
        if recuperaveis > 0:
            print(f"🏹 {cravadas} flechas cravadas em {inimigo.nome}. Até {recuperaveis} recuperáveis.")
            _coletar_flechas(jogador, recuperaveis)
    # Olho Necromântico — ganha dano de magia por kill (máx +6)
    if any('Olho Necromântico' in eq for eq in jogador.equipados):
        kills_olho = jogador.efeitos_ativos.get('olho_kills', 0)
        if kills_olho < 6:
            kills_olho += 1
            jogador.efeitos_ativos['olho_kills'] = kills_olho
            print(f"👁️ Olho Necromântico absorve a morte de {inimigo.nome}! +1 dano mágico permanente (total +{kills_olho})")
    if hasattr(inimigo, 'arma_loot') and random.random() < 0.35:
        item = inimigo.arma_loot
        print(f"\n💀 {inimigo.nome} deixou cair: {item} ({peso_item(item)}kg)")
        time.sleep(1)
        if jogador.pode_carregar(item):
            r = input("   Pegar? (s/n): ").lower()
            if r == 's':
                jogador.inventario.append(item)
                print(f"   ✅ {item} adicionado ao inventário.")
            else:
                print(f"   ↩️  Você deixou o item no chão.")
        else:
            print(f"   ⚠️  Mochila pesada demais! ({jogador.peso_atual}/{jogador.capacidade_peso}kg). Item perdido.")
        time.sleep(1)


# =====================================================================
# REGIÃO — Conjunto de salas 4x4 conectadas
# =====================================================================

class Regiao:
    """
    Cada região possui entre 4 e 12 salas 4x4 conectadas aleatoriamente.
    A topologia muda a cada sessão de jogo.
    """

    def __init__(self, dificuldade_base=1, extrema=False):
        self.extrema = extrema
        self.dificuldade_base = dificuldade_base
        self.nome = random.choice(NOMES_REGIOES_EXTREMAS if extrema else NOMES_REGIOES_NORMAIS)
        self.salas = {}        # {(rx, ry): Mapa}
        self.conexoes = {}     # {(rx, ry): set((rx2,ry2))}
        self._gerar()

    def _gerar(self):
        num_salas = random.randint(4, 12)
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pos_inicial = (0, 0)
        self.salas[pos_inicial] = None   # placeholder
        self.conexoes[pos_inicial] = set()
        fila = [pos_inicial]

        while len(self.salas) < num_salas:
            random.shuffle(fila)
            expandiu = False
            for pos in fila:
                dirs_copia = direcoes.copy()
                random.shuffle(dirs_copia)
                for dx, dy in dirs_copia:
                    nova = (pos[0] + dx, pos[1] + dy)
                    if nova not in self.salas:
                        self.salas[nova] = None
                        self.conexoes.setdefault(pos, set()).add(nova)
                        self.conexoes.setdefault(nova, set()).add(pos)
                        fila.append(nova)
                        expandiu = True
                        break
                if expandiu:
                    break
            if not expandiu:
                break  # Não é possível expandir mais

        # Instanciar mapas
        for pos in self.salas:
            self.salas[pos] = Mapa(dificuldade=self.dificuldade_base, extrema=self.extrema)

    def tem_sala(self, pos):
        return pos in self.salas and self.salas[pos] is not None

    def sala(self, pos):
        m = self.salas.get(pos)
        if m is None and pos in self.salas:
            m = Mapa(dificuldade=self.dificuldade_base, extrema=self.extrema)
            self.salas[pos] = m
        return m

    def direcoes_livres(self, pos):
        """Retorna as direções (dx,dy) que possuem sala conectada a partir de pos."""
        vizinhos = self.conexoes.get(pos, set())
        result = []
        for v in vizinhos:
            if self.tem_sala(v):
                dx = v[0] - pos[0]
                dy = v[1] - pos[1]
                result.append((dx, dy))
        return result

    def num_salas(self):
        return len(self.salas)


# =====================================================================
# ANDAR LABIRINTO — Um nível completo e independente do subsolo
# =====================================================================

NOMES_ANDARES_PROFUNDOS = [
    "Cavernas dos Condenados",
    "Entranhas do Labirinto",
    "Profundezas Sem Nome",
    "Câmara do Esquecimento",
    "Corredor da Agonia Perpétua",
    "Passagens da Escuridão Eterna",
    "Abismo da Masmorra",
    "Galeria dos Mortos Antigos",
    "Túneis da Podridão",
    "Câmaras do Caos Primordial",
    "Veios da Pedra Amaldiçoada",
    "Labirinto das Almas Perdidas",
    "Salão da Danação",
    "Cripta dos Sem Retorno",
    "Fosso da Agonia",
]

DESCRICOES_ESCADAS_DESCIDA = [
    "Uma escadaria torta rasga o chão de pedra bruta, descendo para onde a luz não existe.",
    "Degraus gastos pela passagem de pés que nunca voltaram se perdem na escuridão abaixo.",
    "A escada range ao menor peso. Ela vai fundo — mais fundo do que deveria.",
    "Pedras encastradas na rocha formam uma descida abrupta. O frio aumenta visivelmente.",
    "Uma abertura no chão revela uma escadaria primitiva. O ar abaixo cheira a pedra velha e morte.",
]

DESCRICOES_ESCADAS_SUBIDA = [
    "Uma escada de volta à superfície — ou ao menos para o andar de cima.",
    "Degraus que sobem. Onde há luz há esperança. Onde há esperança há perigo.",
    "A escada range de alívio ao ser usada para subir. Ou talvez de decepção.",
]

DESCRICOES_ALTARES = {
    'altar antigo':    "Um altar de pedra coberto de musgo. Símbolos antigos gravados no topo ainda pulsam com uma luz suave. Parece um lugar de descanso — ou de súplica.",
    'altar de sangue': "Um altar escarlate, úmido. Veias de pedra vermelha irradiam calor. Algo aqui quer um tributo. E parece paciente o suficiente para esperar.",
    'círculo mágico':  "Runas concêntricas brilham no chão de pedra, formando um círculo perfeito. O ar ao redor vibra com energia arcana concentrada.",
    'estátua enigmática': "Uma estátua de pedra negra, sem rosto definido. Os olhos — de alguma forma — seguem você. Emanam uma presença silenciosa e antiga.",
    'portal do vazio': "Um rasgo no espaço, oscilando entre negro e violeta. O vento ao redor dele não existe fisicamente — ele puxa de dentro.",
}


class AndarLabirinto:
    """
    Um nível completo e independente do labirinto profundo.
    3–6 salas conectadas por corredores. Sem hub obrigatório.
    Entrada sempre tem escada de subida. 1–2 salas têm escada de descida.
    Salas sem escada = becos sem saída. Pelo menos 1 caminho leva adiante.
    """

    def __init__(self, numero_andar, dificuldade, extrema=False, entradas=None):
        self.numero = numero_andar
        self.dificuldade = dificuldade
        self.extrema = extrema
        self.nome = random.choice(NOMES_ANDARES_PROFUNDOS)
        self.salas = {}       # {(rx,ry): Mapa}
        self.conexoes = {}    # {(rx,ry): set[(rx2,ry2)]}
        # Coordenadas que DEVEM existir como salas com escada de subida
        # (cada coord corresponde a uma escada de descida no andar acima)
        self.entradas = set(entradas) if entradas else {(0, 0)}
        self.pos_entrada = min(self.entradas)   # entrada canônica (menor coord)
        self._gerar()

    # ── geração ──────────────────────────────────────────────────────

    def _gerar(self):
        from collections import deque
        num_salas = random.randint(3, 6)
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Garantir que todas as coordenadas de entrada existam como salas
        for coord in self.entradas:
            self.salas[coord] = None
            self.conexoes.setdefault(coord, set())

        # Expandir a partir de pos_entrada até atingir num_salas
        pos_inicial = self.pos_entrada
        fila = list(self.salas.keys())

        while len(self.salas) < num_salas:
            random.shuffle(fila)
            expandiu = False
            for pos in fila:
                dirs = direcoes.copy()
                random.shuffle(dirs)
                for dx, dy in dirs:
                    nova = (pos[0] + dx, pos[1] + dy)
                    if nova not in self.salas:
                        self.salas[nova] = None
                        self.conexoes.setdefault(pos, set()).add(nova)
                        self.conexoes.setdefault(nova, set()).add(pos)
                        fila.append(nova)
                        expandiu = True
                        break
                if expandiu:
                    break
            if not expandiu:
                break

        # Garantir conexão entre salas de entrada se houver mais de uma
        # (conectar cada entrada à mais próxima se ainda não estiver conectada)
        entradas_lista = sorted(self.entradas)
        for i, ea in enumerate(entradas_lista):
            for eb in entradas_lista[i+1:]:
                if eb not in self.conexoes.get(ea, set()):
                    # Adicionar conexão direta entre as entradas
                    self.conexoes.setdefault(ea, set()).add(eb)
                    self.conexoes.setdefault(eb, set()).add(ea)

        # Instanciar Mapas — sem escadas (colocamos manualmente abaixo)
        for pos in self.salas:
            m = Mapa(dificuldade=self.dificuldade, extrema=self.extrema)
            m.escadas = set()
            m.escada_subir = None
            m.escada_final = None
            self.salas[pos] = m

        # Escada de SUBIDA em cada sala de entrada (uma por coordenada)
        for coord_entrada in self.entradas:
            m_ent = self.salas[coord_entrada]
            sx, sy = self._celula_livre(m_ent)
            m_ent.escada_subir = (sx, sy)
            m_ent.matriz[sy][sx] = '.'

        outras = [p for p in self.salas if p not in self.entradas]

        # ── Calcular distâncias a partir da entrada ───────────────────
        from collections import deque as _deque
        dist_de_entrada = {pos_inicial: 0}
        fila_bfs = _deque([pos_inicial])
        while fila_bfs:
            cur = fila_bfs.popleft()
            for viz in self.conexoes.get(cur, set()):
                if viz not in dist_de_entrada:
                    dist_de_entrada[viz] = dist_de_entrada[cur] + 1
                    fila_bfs.append(viz)

        # ── Forçar elites em salas mais distantes ─────────────────────
        # Salas com distância >= 2 têm 70% de chance de ganhar um elite/rare adicional
        salas_distantes = [p for p, d in dist_de_entrada.items()
                           if d >= 2 and p != pos_inicial]
        for sp in salas_distantes:
            if random.random() < 0.70:
                m_sp = self.salas[sp]
                pos_lista = [(x2, y2)
                             for y2 in range(m_sp.altura)
                             for x2 in range(m_sp.largura)
                             if m_sp.matriz[y2][x2] == '.']
                if pos_lista:
                    ex2, ey2 = random.choice(pos_lista)
                    m_sp._spawn_inimigo_elite(ex2, ey2, self.dificuldade,
                                              distancia_hub=dist_de_entrada[sp])

        if self.numero >= 14:
            # Boss no andar final — sala mais distante
            pos_boss = self._pos_mais_distante(pos_inicial)
            m_boss = self.salas[pos_boss]
            bx, by = self._celula_livre(m_boss)
            m_boss.escada_final = (bx, by)
            m_boss.matriz[by][bx] = '.'
        else:
            # Escadas de descida: 0–2 por andar, só em salas não-entrada
            # Becos sem saída são válidos — o jogador pode sempre subir de volta
            candidatas = [p for p in self.salas
                          if p not in self.entradas and self.salas[p] is not None]
            if candidatas:
                nd = random.randint(1 if len(candidatas) >= 1 else 0,
                                    min(2, len(candidatas)))
                for p in random.sample(candidatas, nd):
                    m = self.salas[p]
                    ex, ey = self._celula_livre(m)
                    m.escadas.add((ex, ey))
                    m.matriz[ey][ex] = '.'

    def _celula_livre(self, mapa):
        livres = [(x, y) for y in range(mapa.altura) for x in range(mapa.largura)
                  if mapa.matriz[y][x] == '.'
                  and (x, y) != mapa.escada_subir
                  and (x, y) not in mapa.escadas
                  and (x, y) != mapa.escada_final]
        if livres:
            return random.choice(livres)
        # Nenhuma célula 'normal' livre — forçar uma
        for y in range(mapa.altura):
            for x in range(mapa.largura):
                if mapa.matriz[y][x] != '#':
                    mapa.matriz[y][x] = '.'
                    return x, y
        mapa.matriz[1][1] = '.'
        return 1, 1

    def _pos_mais_distante(self, origem):
        from collections import deque
        visitados = {origem: 0}
        fila = deque([origem])
        mais_distante = origem
        max_dist = 0
        while fila:
            pos = fila.popleft()
            for viz in self.conexoes.get(pos, set()):
                if viz not in visitados:
                    visitados[viz] = visitados[pos] + 1
                    if visitados[viz] > max_dist:
                        max_dist = visitados[viz]
                        mais_distante = viz
                    fila.append(viz)
        return mais_distante

    # ── interface ─────────────────────────────────────────────────────

    def tem_sala(self, pos):
        return pos in self.salas and self.salas[pos] is not None

    def sala(self, pos):
        m = self.salas.get(pos)
        if m is None and pos in self.salas:
            # Sala existe na topologia mas sem mapa — gerar agora
            m = Mapa(dificuldade=self.dificuldade, extrema=self.extrema)
            m.escadas = set()
            m.escada_final = None
            m.escada_subir = None
            self.salas[pos] = m
        # Invariante crítico: salas de entrada SEMPRE têm escada de subida
        if m is not None and pos in self.entradas and not m.escada_subir:
            sx, sy = self._celula_livre(m)
            m.escada_subir = (sx, sy)
            m.matriz[sy][sx] = '.'
        return m

    def direcoes_livres(self, pos):
        vizinhos = self.conexoes.get(pos, set())
        return [(v[0] - pos[0], v[1] - pos[1]) for v in vizinhos if self.tem_sala(v)]

    def num_salas(self):
        return len(self.salas)


# =====================================================================
# MAPA — Grade 4x4 com inimigos, itens, estruturas
# =====================================================================

class Mapa:
    def __init__(self, largura=4, altura=4, dificuldade=1, extrema=False):
        self.largura = largura
        self.altura = altura
        self.extrema = extrema
        self.matriz = [['#' for _ in range(largura)] for _ in range(altura)]
        self.inimigos = []
        self.itens = {}
        self.portas = {}
        self.escadas = set()
        self.escada_subir = None    # escada de subida (volta um andar)
        self.escada_final = None
        self.estruturas = {}
        self.contagem_parede = {}   # {(x,y): int} — vezes que o jogador tentou entrar nesta parede
        self.tochas_parede = []     # [(x,y)] — tochas fixadas em paredes, iluminam range 2
        self.gerar_labirinto(dificuldade)

    def gerar_labirinto(self, dificuldade):
        # Geração de terreno
        for y in range(self.altura):
            for x in range(self.largura):
                borda = x in [0, self.largura - 1] or y in [0, self.altura - 1]
                if random.random() < (0.20 if borda else 0.07):
                    self.matriz[y][x] = '#'
                else:
                    self.matriz[y][x] = '.'

        # Garantir pelo menos UMA célula livre no meio de cada borda (entrada/saída direcional)
        # Norte (y=0): coluna do meio
        mx, my = self.largura // 2, self.altura // 2
        self.matriz[0][mx] = '.'
        self.matriz[self.altura - 1][mx] = '.'   # Sul
        self.matriz[my][0] = '.'                  # Oeste
        self.matriz[my][self.largura - 1] = '.'  # Leste

        # Garantir pelo menos uma célula livre
        livres = [(x, y) for y in range(self.altura) for x in range(self.largura) if self.matriz[y][x] == '.']
        if not livres:
            self.matriz[1][1] = '.'
            livres = [(1, 1)]

        tipo_andar = random.choices(
            population=["normal", "vazio", "armadilhas", "elite", "tesouro"],
            weights=[0.55, 0.10, 0.12, 0.13, 0.10],
            k=1
        )[0]

        if tipo_andar == "vazio":
            print("🌫️  ..."), time.sleep(2)
            return

        elif tipo_andar == "armadilhas":
            armadilhas_possiveis = ['espinhos', 'flechas', 'bomba mágica', 'gás venenoso']
            for _ in range(random.randint(3, 6)):
                x, y = random.randint(1, self.largura - 2), random.randint(1, self.altura - 2)
                if self.matriz[y][x] == '.':
                    tipo = random.choice(armadilhas_possiveis)
                    self.estruturas[(x, y)] = f"armadilha_{tipo}"
            return

        elif tipo_andar == "elite":
            print("👹 Uma presença poderosa domina esta sala...")
            pos_lista = [(x, y) for y in range(1, self.altura - 1)
                         for x in range(1, self.largura - 1) if self.matriz[y][x] == '.']
            if pos_lista:
                x, y = random.choice(pos_lista)
                self._spawn_inimigo_elite(x, y, dificuldade)
            return

        elif tipo_andar == "tesouro":
            self._popular_itens(dificuldade, minimo=6, maximo=10)
            return

        # --- Andar normal ---
        if random.random() < 0.65:
            self._popular_inimigos(dificuldade)

        self._popular_itens(dificuldade, minimo=2, maximo=5 + dificuldade)

        # Portas
        if random.random() < 0.6:
            for _ in range(random.randint(1, 2)):
                x, y = random.randint(1, self.largura - 2), random.randint(1, self.altura - 2)
                if self.matriz[y][x] == '.':
                    self.portas[(x, y)] = random.random() < 0.5

        # Escadas (dentro da região — avançam no subsolo)
        if dificuldade >= 33:
            if random.random() < 0.4:
                pos_lista = [(x, y) for y in range(1, self.altura - 1)
                             for x in range(1, self.largura - 1) if self.matriz[y][x] == '.']
                if pos_lista:
                    x, y = random.choice(pos_lista)
                    self.escada_final = (x, y)
            else:
                print("⚠️  Nenhuma saída ativa neste andar...")
        else:
            pos_lista = [(x, y) for y in range(1, self.altura - 1)
                         for x in range(1, self.largura - 1) if self.matriz[y][x] == '.']
            if pos_lista:
                x, y = random.choice(pos_lista)
                self.escadas.add((x, y))

        # Estruturas especiais
        estruturas_possiveis = ['altar antigo', 'círculo mágico', 'estátua enigmática']
        if self.extrema:
            estruturas_possiveis += ['altar de sangue', 'portal do vazio']
        for _ in range(random.randint(1, 2)):
            x, y = random.randint(1, self.largura - 2), random.randint(1, self.altura - 2)
            if self.matriz[y][x] == '.':
                self.estruturas[(x, y)] = random.choice(estruturas_possiveis)

        # ── Tochas de parede (0-2 por sala) ──────────────────────────
        # Apenas paredes internas (não bordas extremas) adjacentes a pelo menos
        # uma célula livre — simula tochas cravadas na pedra.
        candidatos_tocha = []
        for cy in range(1, self.altura - 1):
            for cx in range(1, self.largura - 1):
                if self.matriz[cy][cx] == '#':
                    tem_livre = any(
                        0 <= cx + ddx < self.largura and 0 <= cy + ddy < self.altura
                        and self.matriz[cy + ddy][cx + ddx] == '.'
                        for ddx, ddy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    )
                    if tem_livre:
                        candidatos_tocha.append((cx, cy))
        random.shuffle(candidatos_tocha)
        self.tochas_parede = candidatos_tocha[:random.randint(0, 2)]

    def _lista_itens(self, dificuldade):
        # ── Itens comuns (early-game, sempre disponíveis) ──────────────
        comuns = [
            # Consumíveis base
            'poção de cura', 'poção de força', 'poção de invisibilidade', 'antídoto',
            'chave', 'antídoto',   # peso extra
            # Comuns v1
            'Bandagem', 'Pedra de Afiar', 'Erva Medicinal',
            'Erva do Sono', 'Pó de Revelação',
            'Tocha Suja',
            'Flechas (20)',
            'Flechas (10)',
            'Pergaminho da Lanterna Espiritual',
            f'Adaga Simples +1',
            'Escudo de Madeira',
            f'Cajado de Osso +1',
            'Capa de Couro',
            'Amuleto de Osso',
            # Comuns v2
            'Vela Votiva',
            'Poção de Sangue',
            'Garrafa de Ácido',
            'Armadura de Couro',
            'Luvas de Combate',
            'Talismã Protetor',
            'Pó de Gelo',
            'Amuleto Arcano',
            'Amuleto de Deflexão',
            'Capa Encantada',
            # Escaláveis early
            f'Elixir do Berserker +{1 + dificuldade // 2}',
            f'Pergaminho de Proteção +{1 + dificuldade // 2}',
            f'Anel da Vitalidade +{1 + dificuldade // 2}',
            f'Espada Curta +{1 + dificuldade //4}',
            f'Lâmina Sombria +{1 + dificuldade // 2}',
            f'Arco Élfico +{1 + dificuldade // 2}',
            f'Arco da Ruína +{1 + dificuldade // 2}',
            f'Armadura de Mithril +{1 + dificuldade // 2}',
            f'Machado Anão Flamejante +{1 + dificuldade // 2}',
            f'Elmo da Fúria +{1 + dificuldade // 2}',
            'Botas do Silêncio',
            f'Cajado de Gelo +{1 + dificuldade // 2}',
            'Tomo de Sabedoria Antiga',
            f'Amuleto de Resistência +{1 + dificuldade // 2}',
            'Anel de Regeneração',
            f'Manoplas do Trovão +{1 + dificuldade // 2}',
            f'Escudo dos Condenados +{2 + dificuldade // 3}',
            f'Colar da Fúria Ancestral +{2 + dificuldade // 3}',
            'Cristal de Mana',
            f'Adaga Envenenada +{1 + dificuldade // 2}',
            'Manto das Sombras',
            'explosivo arremessável',
        ]

        # ── Itens raros / lendários (dificuldade 10+) ─────────────────
        raros = []
        if dificuldade >= 10:
            raros += [
                f'Orbe Mental de Vecna +{1 + dificuldade // 2}',
                f'Grimório das Almas +{2 + dificuldade // 3}',
                'Grimório Portal',
                f'Lâmina Drenante +{2 + dificuldade // 3}',
                f'Machado do Sangramento +{2 + dificuldade // 3}',
                f'Orbe da Cegueira +{1 + dificuldade // 3}',
                # Raros v2 — nível médio
                f'Espada dos Mártires +{2 + dificuldade // 4}',
                'Corrente do Espectro',
                f'Grimório do Colapso +{2 + dificuldade // 4}',
                'Runa do Limiar',
                'Olho Necromântico',
                f'Lâmina Especular +{2 + dificuldade // 4}',
            ]
        if dificuldade >= 18:
            raros += [
                f'Grimório da Maldição +{2 + dificuldade // 4}',
                'Coroa dos Condenados',
                'Runa de Ressurreição',
                f'Espada Fantasma +{3 + dificuldade // 4}',
                'Cálice do Sacrifício',
                'Anel da Putrefação',
                f'Tomo do Vazio +{2 + dificuldade // 4}',
                # Lendários v2 — profundezas
                'Coroa de Espinhos de Ferro',
                'Rede de Caça',
                f'Tomo da Entropia +{2 + dificuldade // 4}',
                'Cálice de Sangue Antigo',
            ]

        # ── Diário Perdido: pool especial — uma única entrada (raríssimo) ──
        # A distribuição por sessão é controlada em DungeonGame._colocar_diarios()
        # Não entra no pool aleatório normal.

        # Profundezas: itens raros têm 35% de peso na pool
        if dificuldade >= 10 and raros:
            pool_ponderada = comuns * 2 + raros
            return pool_ponderada
        return comuns

    def _popular_itens(self, dificuldade, minimo=2, maximo=6):
        itens_possiveis = self._lista_itens(dificuldade)
        if random.random() < 0.75:
            quantidade = random.randint(minimo, maximo)
            for _ in range(quantidade):
                x, y = random.randint(1, self.largura - 2), random.randint(1, self.altura - 2)
                if self.matriz[y][x] == '.' and (x, y) not in self.itens:
                    self.itens[(x, y)] = random.choice(itens_possiveis)

    def _spawn_inimigo_elite(self, x, y, dificuldade, distancia_hub=0):
        """Spawna inimigo elite. Quanto maior distancia_hub, mais pesado."""
        # Tier 4 — modo extremo (dif 30+) ou muito profundo (dif 48+)
        if (self.extrema and dificuldade >= 30) or dificuldade >= 48:
            pool = [CavaleiroSemNome, SerpenteAbissal, Dracolich, EspectrodasProfundezas]
            cls = random.choice(pool)
            self.inimigos.append(cls((x, y), dificuldade))

        # Tier 3 elite — andares profundos (dif 30+)
        elif dificuldade >= 30:
            pool = [CampeaoDaMorte, GargulaDePedra, SacerdoteDevedor, ArautodoVazio]
            cls = random.choice(pool)
            self.inimigos.append(cls((x, y), dificuldade))

        # Tier 2 elite — andares médios (dif 18+)
        elif dificuldade >= 18:
            pool = [OrcBerserker, ArqueiroDasTrevas,
                    VermedaEntranhas, CarnicaldaProfundeza]
            cls = random.choice(pool)
            self.inimigos.append(cls((x, y), dificuldade))

        # Tier 1 elite — andares rasos
        else:
            pool = [EsqueletoGuardiao, CarnicaldaProfundeza, GoblinFurtivo]
            cls = random.choice(pool)
            self.inimigos.append(cls((x, y), dificuldade))

    def _popular_inimigos(self, dificuldade):
        qtd_inimigos = random.randint(1, 2 + dificuldade // 5)

        for _ in range(qtd_inimigos):
            pos_lista = [(x, y) for y in range(self.altura) for x in range(self.largura)
                         if self.matriz[y][x] == '.']
            if not pos_lista:
                break
            x, y = random.choice(pos_lista)
            roll  = random.random()

            # ── TIER 4: Modo extremo (dif >= 42 = andar 7+) ou extrema pura ──
            # CavaleiroSemNome, Dracolich, SerpenteAbissal, EspectrodasProfundezas
            if self.extrema and dificuldade >= 30:
                if roll < 0.28:
                    self.inimigos.append(CavaleiroSemNome((x, y), dificuldade))
                elif roll < 0.50:
                    self.inimigos.append(SerpenteAbissal((x, y), dificuldade))
                elif roll < 0.68:
                    self.inimigos.append(Dracolich((x, y), dificuldade))
                elif roll < 0.82:
                    self.inimigos.append(EspectrodasProfundezas((x, y), dificuldade))
                elif roll < 0.91:
                    cls = random.choice([CampeaoDaMorte, GargulaDePedra])
                    self.inimigos.append(cls((x, y), dificuldade))
                else:
                    self.inimigos.append(ArautodoVazio((x, y), dificuldade))

            # Tier 4 sem extremo: só em dif >= 48 (andar 8+)
            elif dificuldade >= 48:
                if roll < 0.28:
                    self.inimigos.append(CavaleiroSemNome((x, y), dificuldade))
                elif roll < 0.50:
                    self.inimigos.append(SerpenteAbissal((x, y), dificuldade))
                elif roll < 0.68:
                    self.inimigos.append(Dracolich((x, y), dificuldade))
                elif roll < 0.82:
                    self.inimigos.append(EspectrodasProfundezas((x, y), dificuldade))
                else:
                    cls = random.choice([CampeaoDaMorte, GargulaDePedra])
                    self.inimigos.append(cls((x, y), dificuldade))

            # ── TIER 3: Andares profundos (dif 30–47 = andar 5–7) ─────────
            # GargulaDePedra, CampeaoDaMorte, SacerdoteDevedor, ArautodoVazio
            elif dificuldade >= 30:
                if roll < 0.22:
                    cls = random.choice([SacerdoteDevedor, ArautodoVazio])
                    self.inimigos.append(cls((x, y), dificuldade))
                elif roll < 0.42:
                    cls = random.choice([GargulaDePedra, CampeaoDaMorte])
                    self.inimigos.append(cls((x, y), dificuldade))
                elif roll < 0.60:
                    cls = random.choice([VermedaEntranhas, CarnicaldaProfundeza])
                    self.inimigos.append(cls((x, y), dificuldade))
                elif roll < 0.75:
                    self.inimigos.append(OrcBerserker((x, y), dificuldade))
                elif roll < 0.88:
                    self.inimigos.append(ArqueiroDasTrevas((x, y), dificuldade))
                else:
                    self.inimigos.append(EsqueletoGuardiao((x, y), dificuldade))

            # ── TIER 2: Andares médios (dif 18–29 = andar 3–4) ────────────
            # OrcBerserker, ArqueiroDasTrevas, VermedaEntranhas, CarnicaldaProfundeza
            elif dificuldade >= 18:
                if roll < 0.25:
                    cls = random.choice([VermedaEntranhas, CarnicaldaProfundeza])
                    self.inimigos.append(cls((x, y), dificuldade))
                elif roll < 0.48:
                    self.inimigos.append(OrcBerserker((x, y), dificuldade))
                elif roll < 0.68:
                    self.inimigos.append(ArqueiroDasTrevas((x, y), dificuldade))
                elif roll < 0.84:
                    self.inimigos.append(EsqueletoGuardiao((x, y), dificuldade))
                else:
                    self.inimigos.append(GoblinFurtivo((x, y), dificuldade))

            # ── TIER 1: Andares rasos (dif 1–17 = andar 1–2) ──────────────
            else:
                if roll < 0.30:
                    cls = random.choice([RatoCarniceiro, GoblinFurtivo])
                    self.inimigos.append(cls((x, y), dificuldade))
                elif roll < 0.52:
                    self.inimigos.append(EsqueletoGuardiao((x, y), dificuldade))
                elif roll < 0.68:
                    self.inimigos.append(VermedaEntranhas((x, y), dificuldade))
                elif roll < 0.82:
                    self.inimigos.append(CarnicaldaProfundeza((x, y), dificuldade))
                else:
                    for _ in range(random.randint(2, 3)):
                        pos2 = random.choice(pos_lista)
                        self.inimigos.append(RatoCarniceiro(pos2, dificuldade))

    def tem_linha_de_visao(self, x0, y0, x1, y1):
        """
        Retorna True se há linha de visão direta entre (x0,y0) e (x1,y1).
        Usa Bresenham. Paredes (#) bloqueiam. A célula de destino pode ser parede.
        """
        dx = abs(x1 - x0); dy = abs(y1 - y0)
        sx = 1 if x1 > x0 else -1
        sy = 1 if y1 > y0 else -1
        err = dx - dy
        cx, cy = x0, y0
        while True:
            if cx == x1 and cy == y1:
                return True
            if (cx != x0 or cy != y0):   # não bloqueia na origem
                if 0 <= cx < self.largura and 0 <= cy < self.altura:
                    if self.matriz[cy][cx] == '#':
                        return False
            e2 = 2 * err
            if e2 > -dy:
                err -= dy; cx += sx
            if e2 < dx:
                err += dx; cy += sy

    def _calc_visivel(self, jogador_pos, vision_range):
        """Retorna células visíveis usando LOS (Bresenham) a partir do jogador
        e das tochas de parede. Paredes bloqueiam luz entre fontes diferentes."""
        jx, jy = jogador_pos
        visivel = set()

        # ── Visão do jogador ──────────────────────────────────────────
        for dy in range(-vision_range, vision_range + 1):
            for dx in range(-vision_range, vision_range + 1):
                nx, ny = jx + dx, jy + dy
                if 0 <= nx < self.largura and 0 <= ny < self.altura:
                    if self.tem_linha_de_visao(jx, jy, nx, ny):
                        visivel.add((nx, ny))

        # ── Tochas de parede — range 2, mas bloqueadas por paredes ───
        for tx, ty in self.tochas_parede:
            # Tocha só ilumina se o jogador consegue ver a tocha
            if (tx, ty) not in visivel:
                continue
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    nx, ny = tx + dx, ty + dy
                    if 0 <= nx < self.largura and 0 <= ny < self.altura:
                        if self.tem_linha_de_visao(tx, ty, nx, ny):
                            visivel.add((nx, ny))
        return visivel

    def mostrar(self, jogador_pos, jogador=None, full_vis=False):
        """Renderiza o mapa com borda gótica e sistema de iluminação."""
        CW = 3   # largura de cada célula em caracteres

        # ── Calcular visibilidade ─────────────────────────────────────
        if full_vis:
            visivel = {(x, y) for y in range(self.altura) for x in range(self.largura)}
        else:
            vision_range = 1
            if jogador is not None:
                if 'Tocha Suja' in getattr(jogador, 'equipados', []):
                    vision_range = 2
                lanterna = getattr(jogador, 'lanterna_espiritual', 0)
                if lanterna and lanterna > 0:
                    vision_range = 2
            visivel = self._calc_visivel(jogador_pos, vision_range)

        # ── Símbolo de cada célula ────────────────────────────────────
        def celula(x, y):
            pos = (x, y)
            oculto = pos not in visivel
            if oculto:
                return '   ' #'▓▓▓'
            if pos == jogador_pos:
                return '[●]'
            if any(i.pos == pos and i.esta_vivo() for i in self.inimigos):
                return '(!)'
            if pos in self.itens:
                return '[?]'
            if pos in self.portas:
                return '▐█▌' if self.portas[pos] else '▐░▌'
            if pos == self.escada_final:
                return '[X]'
            if pos in self.escadas:
                return '[>]'
            if pos == self.escada_subir:
                return '[<]'
            if pos in self.tochas_parede:
                return '▐f▌'   # tocha cravada na parede
            if pos in self.estruturas:
                return '[+]'
            if self.matriz[y][x] == '#':
                return '███'
            return ' ▒ ' # futuramente variar conforme áreas. Exemplo: [~] solo alagado

        # ── Borda gótica ──────────────────────────────────────────────
        inner_w = self.largura * CW + 2   # +2 = 1 espaço de padding em cada lado
        title   = '─── MASMORRA ───'
        tlen    = len(title)
        if tlen < inner_w - 2:
            lp = (inner_w - 2 - tlen) // 2
            rp = inner_w - 2 - tlen - lp
            top = f" ╔{'═'*lp}{title}{'═'*rp}╗"
        else:
            top = f"  ╔{'═'*inner_w}╗"
        bot = f"  ╚{'═'*inner_w}╝"

        # Indicador de visão na borda inferior
        if not full_vis:
            if vision_range >= 2:
                luz_str = '🔦' if 'Tocha Suja' in getattr(jogador, 'equipados', []) else '🕯️'
                vis_tag = f" {luz_str} visão:2"
            else:
                vis_tag = '⚫ escuridão '
            vlen = len(vis_tag) + 4   # +4 for "  ╚" and "╝"
            if vlen < inner_w + 4:
                fill = inner_w - len(vis_tag)
                bot = f"  ╚{' '*(fill//2)}{vis_tag}{''*(fill - fill//2)}╝"

        # ── Renderizar ────────────────────────────────────────────────
        print(top)
        for y in range(self.altura):
            row = ' '
            for x in range(self.largura):
                row += celula(x, y)
            row += ' '
            print(f"  ║{row}║")
        print(bot)

    def mover_inimigos(self, jogador_pos, jogador):
        inimigos_que_agiram = set()
        tem_botas = 'Botas do Silêncio' in getattr(jogador, 'equipados', [])
        # Botas do Silêncio reduzem o range de detecção de infinito para 2 tiles (Manhattan)
        range_deteccao = 2 if tem_botas else 999

        for inimigo in self.inimigos:
            if not inimigo.esta_vivo() or id(inimigo) in inimigos_que_agiram:
                continue

            ix, iy = inimigo.pos
            jx, jy = jogador_pos
            dist = abs(jx - ix) + abs(jy - iy)

            # Alertado por ataque à distância — ignora furtividade e se move sempre
            if getattr(inimigo, 'alertado', False):
                pass  # continua — não verifica range_deteccao
            elif dist > range_deteccao:
                continue   # inimigo fica parado — não percebe

            dx = 1 if jx > ix else -1 if jx < ix else 0
            dy = 1 if jy > iy else -1 if jy < iy else 0

            if abs(jx - ix) > abs(jy - iy):
                novo_x, novo_y = ix + dx, iy
            else:
                novo_x, novo_y = ix, iy + dy

            if (0 <= novo_x < self.largura and 0 <= novo_y < self.altura and
                    self.matriz[novo_y][novo_x] == '.' and (novo_x, novo_y) != jogador_pos):
                inimigo.pos = (novo_x, novo_y)
                inimigos_que_agiram.add(id(inimigo))

            elif (novo_x, novo_y) == jogador_pos:
                if jogador.invisivel:
                    print(f"👻 {inimigo.nome} não percebe sua presença.")
                    continue
                # Botas: chance de o inimigo ignorar mesmo ao alcançar
                if tem_botas and random.random() < 0.40:
                    print(f"👟 {inimigo.nome} está bem perto mas seus passos não fizeram barulho — passa despercebido.")
                    continue
                print(f"\n⚠️  {inimigo.nome} alcança você!")
                time.sleep(1)
                combate(jogador, inimigo, inimigo_iniciou=True)
                inimigos_que_agiram.add(id(inimigo))
                if not jogador.esta_vivo():
                    return


# =====================================================================
# SISTEMA DE JOGO — Regiões, Progresso, Navegação
# =====================================================================

# Mapeamento de direções
DIR_MAP = {
    'w': (0, -1),  # Norte
    's': (0, 1),   # Sul
    'a': (-1, 0),  # Oeste
    'd': (1, 0),   # Leste
}

DIR_OPOSTA = {
    (0, -1): (0, 1),
    (0, 1): (0, -1),
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
}

NOME_DIRECAO = {
    (0, -1): "Norte",
    (0, 1): "Sul",
    (-1, 0): "Oeste",
    (1, 0): "Leste",
}


class DungeonGame:
    def __init__(self):
        self.jogador = self.criar_personagem()

        # Contadores
        self.nivel = 0          # Salas únicas visitadas (progresso real)
        self.andar = 1          # Profundidade atual

        # Modo extremo
        self.modo_extremo = False

        # Regiões do nível 1 (hub + 4 direções)
        self.regioes = {}
        for dir_key in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            self.regioes[dir_key] = Regiao(dificuldade_base=1, extrema=False)

        # Estado atual de navegação — superfície (andar 1)
        self.regiao_atual_key = None    # None = hub central
        self.sala_pos = (0, 0)          # posição da sala dentro da região
        self._mapa_hub = self._criar_mapa_hub()
        self.mapa = self._mapa_hub

        # ── Sistema de andares profundos ──────────────────────────────
        # Cada andar > 1 é um AndarLabirinto independente
        self.andares = {}           # {num_andar: AndarLabirinto}
        self.sala_no_andar = (0, 0) # posição dentro do AndarLabirinto atual
        self.em_andar_profundo = False  # True quando andar > 1

        # Coordenadas de entrada por andar — {num_andar: set of (rx,ry)}
        # Cada coord é uma escada de descida no andar acima que leva a esse andar
        self.entradas_andares = {}

        # Contexto de retorno por escada:
        # {andar_destino: {'profundo': bool, 'regiao': key, 'sala': pos, 'andar_sala': pos, 'xy': (x,y)}}
        self.spawn_retorno = {}

        # Controle de progresso
        self.salas_visitadas = set()
        self._registrar_visita('hub', (0, 0))

        # Diário Perdido — 5 por sessão, distribuídos aleatoriamente
        pool = list(DIARIO_ENTRADAS)
        random.shuffle(pool)
        self._diarios_por_sessao = pool[:5]
        self._diarios_lidos = 0
        self._diarios_colocados = 0

        # Direção usada para entrar na região atual (para voltar ao hub)
        self.dir_entrada = None

        # Posição do jogador no mapa 4x4
        self.x, self.y = self.spawn_jogador()
        self.jogador.pos = (self.x, self.y)
        self.jogador._mapa_ref = self.mapa   # para portal mago
        self.jogador._game_ref = self         # para Diário Perdido

    def _criar_mapa_hub(self):
        """Hub central — sala de conexão entre regiões."""
        m = Mapa(dificuldade=1)
        m.inimigos = []
        m.escadas = set()
        # Garantir entradas abertas em todas as bordas do hub
        mx, my = m.largura // 2, m.altura // 2
        m.matriz[0][mx] = '.'          # Norte
        m.matriz[m.altura - 1][mx] = '.'  # Sul
        m.matriz[my][0] = '.'          # Oeste
        m.matriz[my][m.largura - 1] = '.'  # Leste
        return m

    def _registrar_visita(self, regiao_key, sala_pos):
        """Registra visita e incrementa contador se for sala nova."""
        chave = (str(regiao_key), sala_pos)
        if chave not in self.salas_visitadas:
            self.salas_visitadas.add(chave)
            if regiao_key != 'hub':
                self.nivel += 1
                # Modo extremo — somente ao atingir profundidade >= 11 em andar profundo
                # Nunca ativa por exploração do andar 1
                if (self.em_andar_profundo and self.andar >= 7
                        and not self.modo_extremo):
                    self._ativar_modo_extremo()

    def _ativar_modo_extremo(self):
        """Ativa o modo extremo da dungeon a partir do nível 28."""
        self.modo_extremo = True
        limpar_tela()
        print("\n" + "█" * 50)
        print("  ☠️   A DUNGEON ENTRA EM MODO EXTREMO   ☠️")
        print("█" * 50)
        time.sleep(1)
        print(random.choice(DESCRICOES_EXTREMAS))
        time.sleep(3)
        print("💀 As regiões restantes se corrompem com energia profana...")
        time.sleep(2)
        # Regenerar regiões ainda não visitadas como extremas
        dif_extrema = self._dificuldade_atual()
        for dir_key, regiao in self.regioes.items():
            chave = (str(dir_key), (0, 0))
            if chave not in self.salas_visitadas:
                self.regioes[dir_key] = Regiao(
                    dificuldade_base=dif_extrema,
                    extrema=True
                )

    def spawn_jogador(self):
        """Encontra posição livre no mapa atual."""
        return self._spawn_em_mapa(self.mapa)

    def _spawn_em_mapa(self, mapa):
        """Encontra posição livre em qualquer mapa dado. Nunca retorna None."""
        if mapa is None:
            return 1, 1
        tentativas = 0
        while tentativas < 100:
            x, y = random.randint(0, mapa.largura - 1), random.randint(0, mapa.altura - 1)
            if mapa.matriz[y][x] == '.':
                return x, y
            tentativas += 1
        # Busca exaustiva
        for y in range(mapa.altura):
            for x in range(mapa.largura):
                if mapa.matriz[y][x] == '.':
                    return x, y
        # Último recurso: forçar célula livre em (1,1)
        mapa.matriz[1][1] = '.'
        return 1, 1

    def _spawn_junto_a(self, mapa, escada_pos):
        """
        Retorna (x, y) junto à escada: prefere a célula exata, depois as 8 adjacentes
        em ordem de proximidade, por fim qualquer célula livre do mapa.
        Nunca retorna a própria célula da escada (para não re-disparar a escada).
        """
        ex, ey = escada_pos
        adjacentes = [
            (ex + dx, ey + dy)
            for dx in (-1, 0, 1) for dy in (-1, 0, 1)
            if (dx, dy) != (0, 0)
        ]
        # Ordenar: ortogonais primeiro, depois diagonais
        adjacentes.sort(key=lambda p: abs(p[0]-ex) + abs(p[1]-ey))
        for ax, ay in adjacentes:
            if 0 <= ax < mapa.largura and 0 <= ay < mapa.altura:
                if mapa.matriz[ay][ax] == '.':
                    # Não pousar em cima de outra escada
                    if ((ax, ay) not in mapa.escadas
                            and (ax, ay) != mapa.escada_subir
                            and (ax, ay) != mapa.escada_final):
                        return ax, ay
        return self._spawn_em_mapa(mapa)

    def criar_personagem(self):
        limpar_tela()
        print("""
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║          L I M I A R   D O   M U N D O                       ║
  ║                                                              ║
  ║   Onde as cordilheiras negras cercam o que não deve ser      ║
  ║   encontrado. Onde os desertos e os oceanos separam o        ║
  ║   possível do proibido. Onde o material e o imaterial        ║
  ║   partilham o mesmo chão de pedra e escuridão.               ║
  ║                                                              ║
  ║        "Nenhum mapa chega até aqui por acidente."            ║
  ║                                                              ║
  ╚══════════════════════════════════════════════════════════════╝
""")
        time.sleep(3)

        # ── Mestre se apresenta ──────────────────────────────────────
        def n(txt, p=1.4):
            print(txt); time.sleep(p)

        n("A névoa se abre.", 1.2)
        n("À sua frente, um portão de pedra negra lavrada com inscrições", 1.2)
        n("em língua que nenhuma academia reconhece.", 1.8)
        n("", 0.3)
        n("Diante do portão, uma figura.", 1.5)
        n("Não velha. Não jovem. Algo anterior a essas categorias.", 2)
        n("Veste um manto que absorve a luz ao redor. Não escuro — ausente.", 2)
        n("", 0.3)
        n("Ela vos olha sem surpresa.", 1.2)
        n("Como quem aguarda há séculos e encontrou, no aguardar,", 1.2)
        n("uma forma perversa de serenidade.", 2.5)
        n("", 0.5)
        n("A voz, quando vem, ressoa mais dentro do peito que pelos ouvidos:", 2)
        n("", 0.3)
        print("  ╔═══════════════════════════════════════════════════════════╗")
        print("  ║  PORTEIRO — Ah. Mais um que chegou até aqui.              ║")
        print("  ║                                                           ║")
        print("  ║  Raros o fazem. Raro não significa merecido —             ║")
        print("  ║  significa apenas que as cordilheiras vos deixaram        ║")
        print("  ║  passar. Por razão própria delas.                         ║")
        print("  ║                                                           ║")
        print("  ║  Sou o Porteiro do Limiar. Registro os que entram.        ║")
        print("  ║  Não os que saem...                                       ║")
        print("  ║                                                           ║")
        print("  ║  Antes que as portas se abram: tenho perguntas.           ║")
        print("  ║  O Limiar exige que eu saiba com quem trato.              ║")
        print("  ╚═══════════════════════════════════════════════════════════╝")
        time.sleep(3)
        input("\n  [ pressione ENTER para responder ao Porteiro ]")

        # ── Escolha de classe — através do Mestre ───────────────────
        limpar_tela()
        n("", 0.3)
        n("O Porteiro inclina levemente a cabeça.", 1.5)
        n("Os olhos — se os tem — percorrem vós com atenção metódica.", 2)
        n("", 0.3)
        print("  PORTEIRO — Pelo porte, pelo olhar, pela forma como chegastes...")
        time.sleep(2)
        print("             Posso ver o que sois. Mas prefiro que o digais.")
        time.sleep(2.5)
        print()
        print("  ┌─────────────────────────────────────────────────────────┐")
        print("  │  1 — GUERREIRO                                          │")
        print("  │      Forjado em aço e sangue perdido. Carrega o peso    │")
        print("  │      do passado e da armadura com igual estoicismo.     │")
        print("  │      Os muros do Limiar reconhecem as marcas de batalha.│")
        print("  │                                                         │")
        print("  │  2 — MAGO                                               │")
        print("  │      Conhecedor de palavras que rasgam o véu do mundo.  │")
        print("  │      O Limiar foi construído para guardar o que magos   │")
        print("  │      buscam. A ironia não escapa ao Porteiro.           │")
        print("  │                                                         │")
        print("  │  3 — LADINO                                             │")
        print("  │      A sombra que caminha à frente de si mesma.         │")
        print("  │      Chegastes sem convite — o que significa que        │")
        print("  │      o Limiar vos deixou entrar de propósito.           │")
        print("  └─────────────────────────────────────────────────────────┘")
        print()

        personagem = None
        classe_escolhida = None
        while personagem is None:
            c = input("  O que sois? >> ").strip()
            if c == '1':
                classe_escolhida = "Guerreiro"
                limpar_tela()
                time.sleep(2)
                personagem = Personagem("Guerreiro", 25, 16, 6, 8, "Guerreiro", 6, 8)
            elif c == '2':
                classe_escolhida = "Mago"
                limpar_tela()
                print(escolhe_mago(wizard))
                time.sleep(2)
                personagem = Personagem("Mago", 19, 12, 3, 10, "Mago", 3, 10)
            elif c == '3':
                classe_escolhida = "Ladino"
                limpar_tela()
                print(escolhe_ladino(rogue))
                time.sleep(2)
                personagem = Personagem("Ladino", 21, 14, 9, 6, "Ladino", 9, 6)

        self._sessao_zero(personagem, classe_escolhida)
        return personagem

    # ─────────────────────────────────────────────────────
    # SESSÃO ZERO — O PORTEIRO DO LIMIAR CONHECE O AVENTUREIRO
    # ─────────────────────────────────────────────────────
    def _sessao_zero(self, personagem, classe):
        """
        Entrevista narrativa conduzida pelo Porteiro do Limiar.
        Perguntas dissertivas detectam palavras-chave e concedem bônus.
        Perguntas objetivas definem build inicial, habilidades e afinidade espiritual.
        """

        # ── Utilitários de narração ───────────────────────────────────
        def n(txt, p=1.4):
            print(txt); time.sleep(p)

        def porteiro(txt, pausa=2.0):
            """Fala do Porteiro em caixa."""
            linhas = []
            palavras = txt.split()
            linha = ""
            for w in palavras:
                if len(linha) + len(w) + 1 > 55:
                    linhas.append(linha)
                    linha = w
                else:
                    linha = (linha + " " + w).strip()
            if linha:
                linhas.append(linha)
            print()
            print("  ╔═════════════════════════════════════════════════════════════════════════════════╗")
            for l in linhas:
                print(f"  ║  PORTEIRO — {l:<65}║")
            print("  ╚═════════════════════════════════════════════════════════════════════════════════╝")
            time.sleep(pausa)

        def porteiro_curto(linhas_lista, pausa=2.0):
            """Bloco de fala multi-linha do Porteiro."""
            print()
            print("  ╔═════════════════════════════════════════════════════════════════════════════════╗")
            primeira = True
            for l in linhas_lista:
                prefixo = "  PORTEIRO — " if primeira else "             "
                print(f"  ║  {prefixo} {l:<65}║")
                primeira = False
            print("  ╚═════════════════════════════════════════════════════════════════════════════════╝")
            time.sleep(pausa)

        def perguntar(texto, pausa_antes=1.0):
            time.sleep(pausa_antes)
            print(f"\n  >> {texto}")
            r = input("     Você: ").strip()
            return r.lower() if r else ""

        def escolha_numerada(titulo, opcoes, pausa=0.5):
            """Menu de múltipla escolha. Retorna índice 0-based ou 0 por padrão."""
            time.sleep(pausa)
            print(f"\n  {titulo}")
            for i, op in enumerate(opcoes):
                print(f"     {i+1}. {op}")
            while True:
                c = input("     >> ").strip()
                try:
                    idx = int(c) - 1
                    if 0 <= idx < len(opcoes):
                        return idx
                except ValueError:
                    pass
                print("     (escolha um número válido)")

        def bonus_narrativo(texto, pausa=2.0):
            """Exibe bônus recebido com pausa dramática."""
            print(f"\n  ✦ {texto}")
            time.sleep(pausa)

        # ── Detecção de palavras-chave ────────────────────────────────
        # Cada categoria tem raízes de palavras para capturar flexões
        KWDS_OURO      = {'ouro', 'rique', 'rico', 'tesour', 'moeda', 'dinh', 'fortu', 'lucr', 'ganho', 'riqueza', 'espóli', 'espolios', 'comerci', 'negóc', 'contrato', 'joia', 'gemas', 'recompensa'}
        KWDS_VINGANCA  = {'vingan', 'vingar', 'ódio', 'odio', 'raiva', 'ira', 'punir', 'puni', 'matar', 'assassi', 'traido', 'traição', 'rancor', 'fúria', 'furia', 'revide', 'retaliar', 'retali', 'sangue por sangue', 'não perdoo', 'nao perdoo', 'ele merece', 'ela merece', 'destruir', 'acerto'}
        KWDS_SABER     = {'conhec', 'saber', 'segred', 'mistér', 'mister', 'verda', 'revela', 'sabedo', 'aprend', 'estud', 'pesqui', 'descob', 'arcano', 'antigo', 'proibid', 'livro', 'grimório', 'magia', 'comprend', 'entend', 'decifr', 'manuscrit', 'tábua', 'necrono', 'mythos', 'verdade'}
        KWDS_SONHO     = {'sonho', 'sonhei', 'visão', 'visao', 'chamad', 'convit', 'pressági', 'presság', 'voz', 'manda', 'guiad', 'profecia', 'oráculo', 'oracul', 'augúrio', 'auguri', 'sinal', 'presság', 'revelação', 'quando dormia', 'sonhava que', 'nas trevas eu ouvi', 'algo me chama'}
        KWDS_AMOR      = {'famíl', 'famil', 'amor', 'saudad', 'esposa', 'marido', 'filh', 'pai', 'mãe', 'mae', 'irmã', 'irmao', 'irmão', 'amad', 'perdi', 'buscand', 'salvar', 'rescue', 'resgate', 'luto', 'chorei', 'levaram', 'desaparec',}
        KWDS_GLORIA    = {'glória', 'gloria', 'fama', 'honra', 'héroi', 'heroi', 'lend', 'imortal', 'nome', 'histór', 'épico', 'epico', 'proeza', 'bardo', 'canto', 'memór', 'reconhec', 'prová', 'provar', 'rei', 'rainha'}
        KWDS_MEDO      = {'medo', 'pavor', 'terror', 'assust', 'corage', 'enfrent', 'desafi', 'prova', 'superar', 'supero', 'vencer o medo', 'fobia', 'apavorad', 'tremir', 'tremo', 'não consigo parar', 'nao consigo parar', 'pesadelo', 'acordei e vim'}
        KWDS_NIHIL     = {'nada', 'nihil', 'vazio', 'absurd', 'sem sentido', 'não importa', 'nao importa', 'indiferença', 'indiferenc', 'camus', 'nietzsch', 'além do bem', 'alem do bem', 'vontade de poder', 'morte de deus', 'eterno retorno', 'revolta'}
        KWDS_EXILIO    = {'exílio', 'exilio', 'banid', 'expuls', 'desterra', 'fugitiv', 'fugindo', 'perseguido', 'foragid', 'procurado', 'escond', 'escap', 'não posso voltar', 'nao posso voltar', 'eles me querem', 'não tenho lar', 'nao tenho lar'}
        KWDS_CULPA     = {'culpa', 'arrepen', 'pecado', 'redemp', 'redenção', 'redencao', 'perdão', 'perdao', 'expiação', 'expiacao', 'pagar', 'merec', 'castigo', 'puniç', 'punição', 'fiz algo', 'algo que fiz', 'não mereço', 'nao mereço', 'dívida'}
        KWDS_LOUCURA   = {'loucura', 'insania', 'insanidade', 'loucur', 'delirio', 'delírio', 'alucinação', 'alucinac', 'vozes', 'não sou mais', 'nao sou mais', 'mente quebr', 'desmor', 'rasgar', 'vejo coisas', 'ouço algo', 'não estou bem', 'nao estou bem', 'fragmentad'}
        KWDS_DESTINO   = {'destino', 'fatali', 'fado', 'inevitável', 'inevitavel', 'predestinado', 'profet', 'não tenho escolha', 'nao tenho escolha', 'foi escrito', 'marcado', 'estava escrito', 'não há outra via', 'nao ha outra via', 'as estrelas disseram'}
        KWDS_PODER     = {'poder', 'dominar', 'domínio', 'dominio', 'controlar', 'controle', 'governa', 'soberan', 'rei', 'rainha', 'trono', 'conquist', 'subjugar', 'subjug', 'quero comandar', 'ninguém me para', 'nao me param', 'não me param'}
        KWDS_MORTE     = {'morrer', 'morto', 'moribund', 'já estou', 'ja estou morto', 'acabou', 'fim', 'última coisa', 'ultima coisa', 'não tenho mais', 'nao tenho mais', 'suicid', 'imolação', 'imolaç', 'sacrifíc', 'sacrific', 'entregar minha vida', 'morte', 'morro de qualquer forma'}
        KWDS_FILOSOFIA = {'heidegger', 'sartre', 'camus', 'kafka', 'poe', 'lovecraft', 'borges', 'schopenhau', 'shopenhau', 'pessimis', 'absurdo', 'contingência', 'contingencia', 'ser-para-morte', 'ser para morte', 'angústia', 'angustia existencial', 'shopenhauer', 'niilismo', 'dasein', 'fenomenolog', 'kierkeg', 'stirner'}
        # ── NOVAS MOTIVAÇÕES ────────────────────────────────────────────
        KWDS_SEGREDO   = {'segredo que', 'guardar', 'ninguém pode saber', 'nao pode saber', 'não pode saber', 'escondi', 'escondem', 'querem calar', 'silenciar', 'enterrar', 'sumir com', 'verdade oculta', 'conspiraç', 'conspiracao', 'eles sabem', 'senhor deste mundo'}
        KWDS_CRIACAO   = {'criar', 'construir', 'forjar', 'esculpir', 'obra', 'minha obra', 'arte', 'artefato', 'inventar', 'descobrir método', 'alcançar maestria', 'alcancar maestria', 'legado que deixo', 'transformar', 'mudar o mundo', 'nova era', 'fórmula', 'formula'}
        KWDS_SANGUE    = {'matar porque gosto', 'prazer em matar', 'sangue', 'cheiro de sangue', 'violência me chama', 'guerra chama', 'só sinto algo', 'so sinto algo', 'quando mato', 'quando há luta', 'quando ha luta', 'berserker', 'berserk', 'fúria de batalha', 'furia de batalha', 'adrenalina'}
        KWDS_ABISMO    = {'abismo', 'as profundezas me chamam', 'coisa nas profundezas', 'entidade', 'grande antigo', 'cthulhu', 'dagon', 'nyarlathotep', 'azathoth', 'yog', 'deep one', 'cosmico', 'cósmico', 'fora do tempo', 'infinito fria', 'estrelas certas', 'quando as estrelas'}
        KWDS_MAGIA_VELHA = {'magia antiga', 'feiticeiro', 'runa', 'pacto', 'fiz um pacto', 'assinei', 'vendi', 'alma por', 'preço da magia', 'dom que cobrou', 'custo do dom', 'maldição que trouxe', 'grimório que encontrei', 'livro proibido que li', 'livro antigo',}
        KWDS_RESISTENCIA = {'resistir', 'resistência', 'resistencia', 'não se curvar', 'nao se curvar', 'recusar', 'recuso', 'me recuso', 'não aceito', 'nao aceito', 'luta sem fim', 'nunca capitulo', 'nunca me rendo', 'prefiro morrer lutando', 'até o fim'}

        # ── SUBCLASSES — palavras-chave de detecção ──────────────────────
        KWDS_BARBARO    = {'fúria', 'furia', 'berserk', 'selvagem', 'raiva', 'barbaro', 'bárbaro',
                           'instinto', 'destruir', 'raiva', 'só força', 'so força',
                           'esqueço de mim', 'sem pensar', 'combate é vida',
                           'machado', 'rasgar', 'massacrar', 'sangue e ferro'}
        KWDS_CAVALEIRO  = {'honra', 'cavaleiro', 'juramento', 'juro', 'código', 'codigo', 'nobre',
                           'nobreza', 'proteger', 'servir', 'dever', 'lealdade', 'vassalo',
                           'espada e escudo', 'disciplina', 'promessa', 'ordem', 'cavalaria',
                           'arte marcial', 'tática', 'formação', 'estudei'}
        KWDS_MAGO_AZUL  = {'luz', 'curar', 'cura', 'proteção', 'protecao', 'elemento', 'elementar',
                           'agua', 'fogo', 'ar', 'terra', 'bondade', 'ajudar', 'iluminar',
                           'claridade', 'benevolente', 'harmonia', 'equilíbrio', 'equilibrio',
                           'natureza arcana', 'magia da vida', 'poder mágico puro', 'alma de luz', 'alma de luz'}
        KWDS_MAGO_NEGRO = {'necro', 'maldição', 'maldicao', 'sombras', 'escuridão', 'escuridao',
                           'poder ilimitado', 'poderoso', 'almas', 'drain', 'drenar', 'morte é poder', 'poder mágico mortal',
                           'morte e poder', 'necromancia', 'poder', 'poder absoluto', 'tudo tem preço',
                           'tudo tem preco', 'não me importo', 'nao me importo com o custo',
                           'dark magic', 'magia sombria', 'magia negra', 'feitiço proibido', 'feitico proibido', 'rituais'}
        KWDS_LADRAO     = {'roubar', 'espólio', 'tomar', 'furtar', 'recompensa', 'bolso', 'mercado negro', 'sobreviver', 'esgueirar',
                           'fugir sempre', 'não confrontar', 'nao confrontar', 'ladrão', 'ladrao',
                           'pickpocket', 'armadilha', 'armadilhas', 'ouro',
                           'tesouros', 'abrir fechaduras', 'deslizar nas sombras', 'sombras e lucro'}
        KWDS_ASSASSINO  = {'matar', 'eliminar', 'eliminacao', 'eliminação', 'assassinar', 'assassinato', 'contrato', 'alvo', 'silencioso',
                           'execução', 'execucao', 'executar', 'veneno', 'perfeição', 'perfeicao', 'sem rastro',
                           'um golpe', 'golpe certeiro', 'ofício do assassino', 'ninguém viu',
                           'ninguem viu', 'sigilo e morte', 'lâmina', 'veneno', 'alvo', 'caça',}

        def detectar(resposta, kwds):
            return any(k in resposta for k in kwds)

        # ── 1. NOME ────────────────────────────────────────────────────
        limpar_tela()
        time.sleep(0.8)

        porteiro_curto([
            "Bem-vindo ao Limiar do Mundo.",
            "",
            "Sou o Porteiro. Registro os que entram.",
            "Perguntas breves. O tempo aqui é... peculiar.",
        ], pausa=3)
        time.sleep(0.5)

        resp_nome = perguntar("Como vos chamais?", pausa_antes=0.5)
        nome = resp_nome.strip().title() if resp_nome.strip() else classe
        personagem.nome = nome
        limpar_tela()

        # ── 2. POR QUE VIESTES? (dissertiva + keyword) ────────────────
        porteiro_curto([
            f"{nome}.",
            "",
            "O Limiar fica além de toda cordilheira, deserto",
            "e oceano que o mundo conhece. Nenhum acidente",
            "traz alguém até aqui.",
            "",
            "Por que viestes?",
        ], pausa=3)

        resp_motivo = perguntar("Por que viestes ao Limiar?")
        limpar_tela()

        # Reações e bônus por motivo
        if detectar(resp_motivo, KWDS_OURO):
            porteiro_curto([
                f"Ouro.",
                "",
                "Os caçadores de fortuna chegam mais que os outros.",
                "Nenhum voltou para gastar o que encontrou.",
                "",
                "O Limiar, contudo, respeita o pragmatismo.",
                "Deixa aqui uma chave. Portas trancadas guardam",
                "o que vale a pena guardar.",
            ], pausa=3)
            personagem.inventario.append('chave')
            bonus_narrativo(f"O Porteiro concede: +1 Chave ao inventário.")

        elif detectar(resp_motivo, KWDS_VINGANCA):
            porteiro_curto([
                "Vingança.",
                "",
                "A mais honesta das razões. A mais perigosa.",
                "O ódio afia — até que o fio vira contra quem segura.",
                "",
                "O Limiar reconhece a lâmina da raiva.",
                "Que vos sirva bem, enquanto durar.",
            ], pausa=3)
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            bonus_narrativo(f"+1 Bônus de ataque permanente. A raiva tem custo próprio.")

        elif detectar(resp_motivo, KWDS_SABER):
            porteiro_curto([
                "Conhecimento.",
                "",
                "O Olho de Vecna guarda o que nenhuma biblioteca",
                "ousou catalogar. Verdades que são armas. Segredos",
                "que são venenos de ação lenta.",
                "",
                "O Limiar abre caminho para os que buscam saber.",
                "Raramente os deixa voltar com ele.",
            ], pausa=3)
            personagem.ac += 1
            personagem.base_ac += 1
            bonus_narrativo("+1 CA permanente. A mente afiada é armadura.")

        elif detectar(resp_motivo, KWDS_SONHO):
            porteiro_curto([
                "Um sonho.",
                "",
                "Então viestes pelo maior dos tesouros.",
                "O segredo das masmorras que transitam entre",
                "o material e o imaterial...",
            ], pausa=2.5)
            print()
            resp_mestre = perguntar("Mestre? Dissestes Mestre?", pausa_antes=0.5)
            porteiro_curto([
                "Sim.",
                "",
                "Não dissestes que fostes convidado em sonho?",
                "Quem convida, conhece. Quem conhece, governa.",
                "",
                "O Olho de Vecna aguarda. Ele também vos aguardava.",
            ], pausa=3)
            personagem.afinidade_espiritual = True
            bonus_narrativo("Afinidade espiritual concedida. Os altares vos reconhecerão.")

        elif detectar(resp_motivo, KWDS_AMOR):
            porteiro_curto([
                "Alguém. Ou a memória de alguém.",
                "",
                "Os que entram por amor raramente encontram",
                "o que buscam. Mas são os que chegam mais fundo.",
                "",
                "Há força estranha em carregar alguém por dentro.",
            ], pausa=3)
            personagem.hp += 4
            personagem.hp_max += 4
            personagem.base_hp_max += 4
            bonus_narrativo("+4 HP permanente. O que carregamos nos sustenta.")

        elif detectar(resp_motivo, KWDS_GLORIA):
            porteiro_curto([
                "Glória.",
                "",
                "Nenhum cântico menciona os que chegaram ao Limiar",
                "e voltaram. Apenas os que não voltaram viram",
                "seus nomes gravados em mito.",
                "",
                "O Porteiro não desencoraja. Apenas registra.",
            ], pausa=3)
            personagem.ac += 1
            personagem.base_ac += 1
            bonus_narrativo("+1 CA. Quem busca glória carrega o escudo mais alto.")

        elif detectar(resp_motivo, KWDS_MEDO):
            porteiro_curto([
                "Medo.",
                "",
                "Poucos admitem. Menos ainda o enfrentam.",
                "Há coragem específica em descer ao que vos aterroriza.",
                "",
                "'A coragem não é ausência de medo,",
                "mas o julgamento de que outra coisa é mais importante.'",
                "O Limiar reserva seus tesouros para os que tremem e continuam.",
            ], pausa=3)
            personagem.hp += 2
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            bonus_narrativo("+2 HP + +1 ataque. A coragem tem peso e fio.")

        elif detectar(resp_motivo, KWDS_NIHIL):
            porteiro_curto([
                "O nada.",
                "",
                "O único problema filosófico",
                "sério é o suicídio. Mas vós descestes — logo,",
                "decidistes algo. Ainda que seja apenas isso:",
                "'Ao menos isto. Ao menos agora.'",
                "",
                "O Limiar aprecia os que chegam sem ilusões.",
            ], pausa=3.5)
            personagem.ac += 2
            personagem.base_ac += 2
            personagem.hp += 3
            personagem.hp_max += 3
            personagem.base_hp_max += 3
            bonus_narrativo("+2 CA + +3 HP. A lucidez sem ilusões é armadura rara.")

        elif detectar(resp_motivo, KWDS_EXILIO):
            porteiro_curto([
                "O exílio.",
                "",
                "Os banidos chegam ao Limiar com mais frequência",
                "do que os convidados. O mundo vos expulsou —",
                "o Limiar vos recebe. Por razão própria, claro.",
                "",
                "Os foragidos aprendem a mover-se sem ser vistos.",
                "Aqui, esse talento vale ouro.",
            ], pausa=3.5)
            personagem.ac += 1
            personagem.base_ac += 1
            personagem.inventario.append('poção de invisibilidade')
            bonus_narrativo("+1 CA + Poção de Invisibilidade. O exilado conhece o valor de desaparecer.")

        elif detectar(resp_motivo, KWDS_CULPA):
            porteiro_curto([
                "Culpa.",
                "",
                "A mais pesada das cargas. Não o crime em si —",
                "mas o saber que o cometeu.",
                "",
                "O homem que desce ao subsolo não foge da culpa —",
                "a carrega como estandarte, esperando o castigo ou a redenção.",
                "",
                "O Limiar guarda ambos.",
            ], pausa=4)
            personagem.hp += 5
            personagem.hp_max += 5
            personagem.base_hp_max += 5
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            bonus_narrativo("+5 HP + +1 ataque. A culpa sustenta mais que a fé.")

        elif detectar(resp_motivo, KWDS_LOUCURA):
            porteiro_curto([
                "A loucura.",
                "",
                "O conhecimento que ultrapassa o",
                "suportável não destrói — transforma.",
                "'O mais misericordioso do mundo é a incapacidade",
                "da mente humana de correlacionar seu conteúdo.'",
                "",
                "Mas os que já quebraram chegam aqui inteiros de",
                "outra forma. O Limiar os reconhece.",
            ], pausa=4)
            personagem.ataque_bonus += 2
            personagem.base_ataque_bonus += 2
            personagem.afinidade_espiritual = True
            bonus_narrativo("+2 ataque + Afinidade espiritual. A mente quebrada vê mais.")

        elif detectar(resp_motivo, KWDS_DESTINO):
            porteiro_curto([
                "O destino.",
                "",
                "Os fatalistas são os mais perigosos dos aventureiros.",
                "Não porque sejam invencíveis — mas porque não recuam.",
                "",
                "O Limiar não tem nome para o fado — mas o reconhece",
                "quando o carrega alguém que atravessa o portão.",
            ], pausa=4)
            personagem.ac += 1
            personagem.base_ac += 1
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            personagem.inventario.append('Runa de Ressurreição')
            bonus_narrativo("+1 CA + +1 ataque + Runa de Ressurreição. O destino protege os seus.")

        elif detectar(resp_motivo, KWDS_PODER):
            porteiro_curto([
                "Poder.",
                "",
                "Força criadora — não a dominação baixa de tiranos,",
                "mas o impulso de superar-se a si mesmo.",
                "",
                "O Limiar conhece os dois tipos. E os dois chegam",
                "ao mesmo fim. A questão é: que poder buscais?",
            ], pausa=4)
            personagem.ataque_bonus += 2
            personagem.base_ataque_bonus += 2
            personagem.dano_lados += 1
            personagem.base_dano_lados += 1
            bonus_narrativo("+2 ataque + +1 dado de dano. A vontade de poder tem peso.")

        elif detectar(resp_motivo, KWDS_MORTE):
            porteiro_curto([
                "A morte.",
                "",
                "A consciência da finitude é o que torna",
                "a existência autêntica.",
                "",
                "Mas há diferença entre quem a busca e quem",
                "a contempla. O Porteiro anota: qual sois vós?",
            ], pausa=4)
            # Bonus especial: Cálice do Sacrifício — o tema da morte tem peso próprio
            personagem.hp_max += 8
            personagem.hp += 8
            personagem.base_hp_max += 8
            personagem.inventario.append('Cálice do Sacrifício')
            bonus_narrativo("+8 HP máx + Cálice do Sacrifício. Quem não teme a morte é formidável.")

        elif detectar(resp_motivo, KWDS_FILOSOFIA):
            porteiro_curto([
                "Uma referência filosófica no limiar do abismo.",
                "",
                "A esperança aqui não é infinita. É escassa mas existe.",
                "Apenas não assume as formas que se espera.",
                "",
                "O Porteiro aprecia os que chegam com vocabulário.",
            ], pausa=4)
            personagem.ac += 2
            personagem.base_ac += 2
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            bonus_narrativo("+2 CA + +1 ataque. A erudição tem sua própria dureza.")

        elif detectar(resp_motivo, KWDS_SEGREDO):
            porteiro_curto([
                "Um segredo.",
                "",
                "... em algum lugar existe o livro que contém",
                "tudo — incluindo sua destruição.",
                "",
                "O Limiar guarda muitos segredos. Talvez o vosso",
                "já esteja aqui, esperando ser encontrado.",
                "Ou enterrado ainda mais fundo.",
            ], pausa=4)
            personagem.ac += 1
            personagem.base_ac += 1
            personagem.inventario.append('chave')
            personagem.inventario.append('Vela Votiva')
            bonus_narrativo("+1 CA + Chave + Vela Votiva. Segredos exigem luz e entrada forçada.")

        elif detectar(resp_motivo, KWDS_CRIACAO):
            porteiro_curto([
                "Criação. Obra.",
                "",
                "Há grandeza nisso — e há perigo.",
                "A criação que ultrapassa o permitido",
                "sempre cobra a mesma fatura.",
                "",
                "Que vossa obra valha o preço que ainda virá.",
            ], pausa=4.5)
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            personagem.hp += 3
            personagem.hp_max += 3
            personagem.base_hp_max += 3
            if personagem.classe == 'Mago':
                personagem.inventario.append('Amuleto Arcano')
                bonus_narrativo("+1 ataque + +3 HP + Amuleto Arcano. O criador precisa de ferramentas.")
            else:
                personagem.inventario.append('Pedra de Afiar')
                bonus_narrativo("+1 ataque + +3 HP + Pedra de Afiar. Toda obra começa com a ferramenta certa.")

        elif detectar(resp_motivo, KWDS_SANGUE):
            porteiro_curto([
                "O prazer da batalha.",
                "",
                "O Porteiro conhece esse olhar. Não é raro.",
                "Os que chegam aqui com sede de violência",
                "encontram o Limiar hospitaleiro.",
                "",
                "Berserkers, campeões caídos, gladiadores sem arena.",
                "A masmorra os absorve como solo absorve sangue.",
                "",
                "'Não há mais nobre espetáculo', dizia o romano,",
                "'do que o homem que defronta sua morte com sorriso.'",
                "O Limiar concorda. Mas suspeita de vós.",
            ], pausa=5)
            personagem.ataque_bonus += 2
            personagem.base_ataque_bonus += 2
            personagem.dano_lados += 2
            personagem.base_dano_lados += 2
            personagem.hp -= 5
            if personagem.hp < 1:
                personagem.hp = 1
            bonus_narrativo("+2 ataque + +2 dado de dano, -5 HP. O sangue alimenta o que consome.")

        elif detectar(resp_motivo, KWDS_ABISMO):
            porteiro_curto([
                "Você as sentiu.",
                "",
                "As entidades mais antigas que o tempo.",
                "não são deuses. São indiferentes como o cosmos.",
                "",
                "O Limiar existe porque algo abaixo dele",
                "precisa de uma porta. E de portadores.",
                "",
                "O Porteiro registra com cuidado incomum:",
                "vós viestes por vós mesmos — ou fordes trazidos?",
            ], pausa=5)
            personagem.afinidade_espiritual = True
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            personagem.ac += 1
            personagem.base_ac += 1
            personagem.inventario.append('Tomo de Sabedoria Antiga')
            bonus_narrativo("+1 ataque + +1 CA + Tomo de Sabedoria Antiga + Afinidade espiritual. O abismo reconhece os seus.")

        elif detectar(resp_motivo, KWDS_MAGIA_VELHA):
            porteiro_curto([
                "Um pacto.",
                "",
                "O Porteiro não julga pactos. Ele os registra.",
                "E observa com interesse quem chega ao Limiar",
                "carregando uma dívida arcana nas costas.",
                "",
                "O credor, seja lá quem for, vive mais fundo.",
            ], pausa=5)
            personagem.ataque_bonus += 1
            personagem.base_ataque_bonus += 1
            if personagem.classe == 'Mago':
                personagem.cooldown_magia = 0
                personagem.inventario.append('Grimório das Almas +1')
                bonus_narrativo("+1 ataque + Grimório das Almas + magia desbloqueada. O pacto tem suas regalias.")
            else:
                personagem.inventario.append('Amuleto de Osso')
                personagem.hp += 4
                personagem.hp_max += 4
                personagem.base_hp_max += 4
                bonus_narrativo("+1 ataque + +4 HP + Amuleto de Osso. O preço do pacto, pago em carne.")

        elif detectar(resp_motivo, KWDS_RESISTENCIA):
            porteiro_curto([
                "Resistência. Recusa.",
                "",
                "Não porque a rocha não esmaga.",
                "Mas porque o empurrar se torna o próprio ser.",
                "",
                "O Limiar quebrou muitos que resistiram.",
                "O Porteiro anota com interesse genuíno:",
                "ele não conhece mais nenhum que nunca cedeu.",
                "",
                "Mas há sempre o primeiro.",
            ], pausa=5)
            personagem.hp += 6
            personagem.hp_max += 6
            personagem.base_hp_max += 6
            personagem.ac += 1
            personagem.base_ac += 1
            personagem.inventario.append('Runa de Ressurreição')
            bonus_narrativo("+6 HP + +1 CA + Runa de Ressurreição. Os que não cedem pagam em resistência.")

        elif resp_motivo:
            porteiro_curto([
                f"'{resp_motivo[:40]}'.",
                "",
                "O Porteiro anota. Mais do que devia.",
                "Há razões que não cabem nas categorias conhecidas.",
                "O Limiar aprecia a originalidade.",
            ], pausa=2.5)
            personagem.hp += 2
            personagem.hp_max += 2
            personagem.base_hp_max += 2
            bonus_narrativo("+2 HP. O Limiar recompensa o que não classifica.")

        else:
            porteiro_curto([
                "Silêncio.",
                "",
                "Respeitável. Há quem carregue o motivo tão fundo",
                "que nem a pergunta o alcança.",
                "",
                "O Porteiro não insiste. Registra o silêncio como resposta.",
            ], pausa=3)

        input("\n  [ ENTER ]")
        limpar_tela()

        # MOVER AQUI A DETECÇÃO DE SUBCLASSE
        # ── DETECÇÃO DE SUBCLASSE ─────────────────────────────────────
        # Tenta inferir a subclasse a partir da resposta à origem.
        # Se não detectar, apresenta uma pergunta discreta de múltipla escolha.
        def _detectar_subclasse(resp):
            if classe == "Guerreiro":
                if detectar(resp, KWDS_BARBARO):
                    return 'Bárbaro'
                if detectar(resp, KWDS_CAVALEIRO):
                    return 'Cavaleiro'
            elif classe == "Mago":
                if detectar(resp, KWDS_MAGO_NEGRO):
                    return 'Mago Negro'
                if detectar(resp, KWDS_MAGO_AZUL):
                    return 'Mago Azul'
            elif classe == "Ladino":
                if detectar(resp, KWDS_ASSASSINO):
                    return 'Assassino'
                if detectar(resp, KWDS_LADRAO):
                    return 'Ladrão'
            return None

        subclasse_detectada = _detectar_subclasse(resp_motivo)

        if subclasse_detectada is None:
            # Fallback — pergunta discreta por classe
            porteiro_curto([
                "Posso entrever vossas intenções, mas ainda assim deveis me dizer:",
            ], pausa=2)
            if classe == "Guerreiro":
                porteiro_curto([
                    "Quando encontrais um inimigo mais forte,",
                    "qual é a vossa resposta instintiva?",
                ], pausa=2)
                idx_sc = escolha_numerada("Vossa resposta:", [
                    "Lançar-me à frente com tudo — minha raiva é minha força",
                    "Avaliar, posicionar, proteger o que precisa ser defendido",
                ])
                subclasse_detectada = 'Bárbaro' if idx_sc == 0 else 'Cavaleiro'
            elif classe == "Mago":
                porteiro_curto([
                    "Como vedes o conhecimento arcano?",
                ], pausa=2)
                idx_sc = escolha_numerada("Vossa visão:", [
                    "Como ferramenta de criação e proteção — luz que ordena o caos",
                    "Como poder que precisa ser tomado — mesmo que o preço seja alto",
                ])
                subclasse_detectada = 'Mago Azul' if idx_sc == 0 else 'Mago Negro'
            elif classe == "Ladino":
                porteiro_curto([
                    "O que vos move nas sombras?",
                ], pausa=2)
                idx_sc = escolha_numerada("Vosso motor:", [
                    "Sobrevivência — roubo o que preciso, fujo quando posso",
                    "Propósito — há um alvo. Sempre há um alvo",
                ])
                subclasse_detectada = 'Ladrão' if idx_sc == 0 else 'Assassino'

        personagem.subclasse = subclasse_detectada

        # ── Reação do Porteiro + aplicar stats da subclasse ──────────
        _SUBCLASSE_INFO = {
            'Bárbaro':    ("O Porteiro inclina a cabeça. \"Fúria. O mais primitivo dos dons.\"",
                          "A raiva não precisa de estratégia para ser letal."),
            'Cavaleiro':  ("\"Disciplina e código.\"", "O Limiar respeita os que seguem uma ética de batalha."),
            'Mago Azul':  ("\"Luz arcana. A magia como cura e ordem.\"", "Rara a benevolência aqui embaixo."),
            'Mago Negro': ("\"Sombras e necromantica.\"", "O preço do poder sombrio é cobrado cedo ou tarde."),
            'Ladrão':     ("\"Sobrevivência. O mais pragmático dos motores.\"", "O Limiar conhece quem sabe fugir. E o desafia."),
            'Assassino':  ("\"Um alvo. Sempre há um alvo.\"", "O Porteiro anota: perigoso e focado."),
        }

        # GAMBIARRA - Ajustar Futuramente?
        if subclasse_detectada == 'Bárbaro':
            limpar_tela()
            print(escolhe_guerreiro(warrior))
            time.sleep(2)
            limpar_tela()
        elif subclasse_detectada == 'Cavaleiro':
            limpar_tela()
            print(escolhe_cavaleiro(knight))
            time.sleep(2)
            limpar_tela()

        linha1, linha2 = _SUBCLASSE_INFO.get(subclasse_detectada, ("Registrado.", ""))
        porteiro_curto([linha1, "", linha2, "", f"Subclasse: {subclasse_detectada}."], pausa=2.5)
        bonus_narrativo(f"Subclasse definida: {subclasse_detectada}.")

        # ── Aplicar stats base da subclasse ────────────────────────
        def _aplicar_stats_subclasse(p, sc):
            if sc == 'Bárbaro':
                p.hp += 7;      p.hp_max += 7;    p.base_hp_max += 7
                p.ataque_bonus += 2; p.base_ataque_bonus += 2
                p.dano_lados   += 2; p.base_dano_lados   += 2
            elif sc == 'Cavaleiro':
                p.hp += 2;      p.hp_max += 2;    p.base_hp_max += 2
                p.ac += 3;      p.base_ac += 3
            elif sc == 'Mago Azul':
                p.ac += 1;      p.base_ac += 1
                p.hp += 2;      p.hp_max += 2;    p.base_hp_max += 2
                p.efeitos_ativos['canal_vital'] = 999
            elif sc == 'Mago Negro':
                p.ataque_bonus += 2; p.base_ataque_bonus += 2
                p.dano_lados   += 2; p.base_dano_lados   += 2
                p.hp = max(1, p.hp - 2); p.hp_max = max(1, p.hp_max - 2); p.base_hp_max = max(1, p.base_hp_max - 2)
            elif sc == 'Ladrão':
                p.hp += 2;      p.hp_max += 2;    p.base_hp_max += 2
                p.ac += 1;      p.base_ac += 1
                p.efeitos_ativos['evasao_passiva'] = 999
            elif sc == 'Assassino':
                p.ataque_bonus += 3; p.base_ataque_bonus += 3
                p.hp = max(1, p.hp - 2); p.hp_max = max(1, p.hp_max - 2); p.base_hp_max = max(1, p.base_hp_max - 2)

        _aplicar_stats_subclasse(personagem, subclasse_detectada)

        # ── 3. PERGUNTA DISSERTIVA — ESPECÍFICA DA CLASSE ─────────────
        if classe == "Guerreiro":
            porteiro_curto([
                f"Guerreiro. As mãos dizem o que a boca cala.",
                "",
                "Calosidades. Uma cicatriz antiga no ângulo errado.",
                "Já perdestes algo por causa dessa mão. Não a dor —",
                "o que não conseguistes mais fazer depois.",
                "",
                "De onde vindes, Guerreiro?",
            ], pausa=3)
            resp_origem = perguntar("De onde vindes?")
            limpar_tela()

            if detectar(resp_origem, KWDS_VINGANCA) or detectar(resp_origem, {'guerra', 'batalha', 'conflito', 'exérc'}):
                porteiro_curto([
                    "O campo de batalha. Claro.",
                    "",
                    "Os que sobrevivem à guerra chegam ao Limiar",
                    "com algo diferente dos outros: a certeza de que",
                    "sobreviver não é necessariamente a melhor opção.",
                    "",
                    "Essa perspectiva vos tornará perigosos aqui dentro.",
                ], pausa=3)
                personagem.dano_lados += 2
                personagem.base_dano_lados += 2
                bonus_narrativo(f"+2 dado de dano. Sangue velho nos músculos.")
            elif detectar(resp_origem, KWDS_AMOR | {'família', 'aldeia', 'vilag', 'cidad'}):
                porteiro_curto([
                    "Uma vida antes desta.",
                    "",
                    "Guardiões são os mais duros guerreiros.",
                    "Não porque nasceram assim — porque aprenderam",
                    "o que vale proteger.",
                ], pausa=3)
                personagem.ac += 1
                personagem.hp += 3
                personagem.hp_max += 3
                personagem.base_hp_max += 3
                bonus_narrativo("+1 CA + +3 HP. O escudo do guardião.")
            elif resp_origem:
                porteiro_curto([
                    "Cada guerreiro traz sua cicatriz de origem.",
                    "",
                    "A vossa marca vos tornará mais resistente",
                    "do que a maioria que pisou nestas pedras.",
                ], pausa=2.5)
                personagem.hp += 2
                personagem.hp_max += 2
                personagem.base_hp_max += 2
                bonus_narrativo("+2 HP.")
            else:
                porteiro_curto([
                    "Silêncio sobre a origem. Compreensível.",
                    "O passado pesa mais que a armadura.",
                ], pausa=2)

        elif classe == "Mago":
            porteiro_curto([
                f"Mago. Há um brilho nos olhos que só vem",
                "de noites demais lendo o que não devia ser lido.",
                "",
                "O Limiar foi construído, em parte, para guardar",
                "respostas que magos nunca param de buscar.",
                "",
                "Que segredo vos trouxe até aqui?",
            ], pausa=3)
            resp_segredo = perguntar("Que segredo buscais?")
            limpar_tela()

            if detectar(resp_segredo, {'morte', 'imortal', 'vida etern', 'ressurr', 'nécro', 'necro'}):
                porteiro_curto([
                    "A imortalidade. Ou seu reverso.",
                    "",
                    "O Olho de Vecna é a resposta mais completa",
                    "que existe para essa pergunta.",
                    "",
                    "Também é a mais perigosa de se receber.",
                    "O conhecimento necrótico afia vossa magia.",
                ], pausa=3)
                personagem.ataque_bonus += 2
                personagem.base_ataque_bonus += 2
                bonus_narrativo("+2 bônus de ataque mágico. A necromantica afia o feitiço.")
            elif detectar(resp_segredo, {'origem', 'criação', 'começo', 'princ', 'deus', 'divino', 'cosmic'}):
                porteiro_curto([
                    "A origem de tudo.",
                    "",
                    "A pergunta mais antiga. O Limiar guarda",
                    "fragmentos de respostas que as civilizações",
                    "afogaram antes que destruíssem o mundo.",
                    "",
                    "Vossa mente expande ao contemplar o abismo.",
                ], pausa=3)
                personagem.ac += 2
                personagem.base_ac += 2
                bonus_narrativo("+2 CA. A contemplação do cosmos endurece a mente.")
            elif resp_segredo:
                porteiro_curto([
                    "Segredos têm peso próprio.",
                    "",
                    "O Porteiro anota. Vossa busca vos tornará",
                    "mais perspicaz do que a média que desce.",
                ], pausa=2.5)
                personagem.ataque_bonus += 1
                personagem.base_ataque_bonus += 1
                bonus_narrativo("+1 bônus mágico. O desejo afia o feitiço.")
            else:
                porteiro_curto([
                    "O segredo que não pode ser nomeado.",
                    "O Porteiro respeita os que sabem o que não se diz.",
                ], pausa=2)

        elif classe == "Ladino":
            porteiro_curto([
                "Ladino.",
                "",
                "Chegastes sem convite formal. O que significa",
                "que o Limiar vos percebeu e decidiu não fechar",
                "as portas. Isso raramente é acidente.",
                "",
                "O que sabeis que não deveis saber?",
            ], pausa=3)
            resp_segredo = perguntar("O que sabeis que não deveis?")
            limpar_tela()

            if detectar(resp_segredo, {'rota', 'caminho', 'mapa', 'passagem', 'atalho', 'entrada', 'saída', 'saida'}):
                porteiro_curto([
                    "Rotas proibidas. Passagens sem registro.",
                    "",
                    "A habilidade mais útil que alguém pode trazer",
                    "ao Limiar. Os labirintos aqui não têm mapa",
                    "— mas os que conhecem rotas sentem as saídas.",
                ], pausa=3)
                personagem.ataque_bonus += 1
                personagem.base_ataque_bonus += 1
                personagem.ac += 1
                personagem.base_ac += 1
                bonus_narrativo("+1 ataque + +1 CA. A intuição geográfica protege.")
            elif detectar(resp_segredo, {'pessoa', 'nomes', 'ident', 'rosto', 'quem', 'poder'}):
                porteiro_curto([
                    "Nomes que não devem ser ditos em voz alta.",
                    "",
                    "Conhecimento de pessoas é a moeda mais",
                    "perigosa que existe. E vós a carregais.",
                    "",
                    "O Limiar aprecia quem sabe com quem lida.",
                ], pausa=3)
                personagem.hp += 3
                personagem.hp_max += 3
                personagem.base_hp_max += 3
                bonus_narrativo("+3 HP. Saber quem é o inimigo antecipa o golpe.")
            elif resp_segredo:
                porteiro_curto([
                    "Hm.",
                    "",
                    "O Porteiro anota com cuidado.",
                    "Os que sabem demais sobrevivem exatamente",
                    "porque sabem demais.",
                ], pausa=2.5)
                personagem.ataque_bonus += 1
                personagem.base_ataque_bonus += 1
                bonus_narrativo("+1 ataque. O conhecimento proibido é uma faca.")
            else:
                porteiro_curto([
                    "Sabiamente, guardais o segredo do segredo.",
                    "O Porteiro anota: disciplinado. Perigoso.",
                ], pausa=2)

        input("\n  [ ENTER ]")
        limpar_tela()

        # ── 4. O QUE CARREGAIS? (múltipla escolha → item inicial extra) ──
        porteiro_curto([
            "Antes de entrar, devo pedir para que prepareis vosso equipamento.",
            "",
            "Além do óbvio que carregais —",
            "há algo específico que escolhestes trazer?",
        ], pausa=2.5)

        if classe == "Guerreiro":
            op_itens = [
                "Uma poção de cura",
                "Uma chave mestra",
                "Um antídoto de veneno",
                "Nada além do necessário",
            ]
        elif classe == "Mago":
            op_itens = [
                "Anel de Regeneração",
                "Um antídoto",
                "Um Tomo de Sabedoria Antiga (+3 CA ao ler)",
                "Apenas o cajado da mente",
            ]
        else:  # Ladino
            op_itens = [
                "Uma chave",
                "Uma poção de invisibilidade",
                "Um antídoto",
                "Nada",
            ]

        idx_item = escolha_numerada("O que carregais além?", op_itens)

        if classe == "Guerreiro":
            extras = ['poção de cura', 'chave', 'antídoto', None]
        elif classe == "Mago":
            extras = ['Anel de Regeneração', 'antídoto', 'Tomo de Sabedoria Antiga', None]
        else:
            extras = ['chave', 'poção de invisibilidade', 'antídoto', None]

        item_extra = extras[idx_item]
        if item_extra:
            personagem.inventario.append(item_extra)
            porteiro_curto([f"Registrado: {item_extra}."], pausa=1.5)
            bonus_narrativo(f"{item_extra} adicionado ao inventário.")
        else:
            porteiro_curto(["Viajar leve. A escolha dos que confiam no corpo."], pausa=1.5)
            personagem.hp += 2
            personagem.hp_max += 2
            personagem.base_hp_max += 2
            bonus_narrativo("+2 HP. A leveza fortalece a resistência.")

        input("\n  [ ENTER ]")
        limpar_tela()

        # ── 4b. EQUIPAMENTO BASE (itens de partida por subclasse) ─────────
        porteiro_curto([
            "Então preparastes vosso equipamento?",
            "",
            "Todo aventureiro parte com o básico do ofício.",
            "Nada mais. Nada menos.",
        ], pausa=2)

        sc = personagem.subclasse

        if sc == 'Bárbaro':
            itens_base = ['poção de cura', 'Espada Curta +1', 'Escudo de Madeira', 'Runa do Limiar']
            porteiro_curto([
                "Bárbaro. Força bruta e instinto afiado.",
                "Tomos são papel. Ferro é real.",
            ], pausa=2)
            op_extra = [
                "Elmo da Fúria +2 — fúria e poder às custas da defesa",
                "Espada Curta +1 — lâmina de reserva",
                "Poção de Sangue — HP imediato, com custo",
                "Explosivo Arremessável — quando o machado não alcança",
            ]
            extras = ['Elmo da Fúria +2', 'Espada Curta +1', 'Poção de Sangue', 'explosivo arremessável']

        elif sc == 'Cavaleiro':
            itens_base = ['poção de cura', 'Espada Longa +1', 'Armadura do Veterano', 'Runa do Limiar']
            porteiro_curto([
                "Cavaleiro. Disciplina, código e aço refinado.",
                "Podeis ler tomos — o conhecimento também é armadura.",
            ], pausa=2)
            op_extra = [
                "Espada Curta +1 — lâmina de reserva",
                "Amuleto de Resistência +1 — HP e CA passivos",
                "Escudo de Madeira — +2 CA adicional",
                "Explosivo Arremessável — para quando o código permite",
            ]
            extras = ['Espada Curta +1', 'Amuleto de Resistência +1', 'Escudo de Madeira', 'explosivo arremessável']

        elif sc == 'Mago Azul':
            itens_base = ['poção de cura', 'Cristal de Mana', 'antídoto', 'Runa do Limiar']
            porteiro_curto([
                "Mago da Luz. A magia que protege e restaura.",
                "Toque de Cura já está em vosso arsenal.",
            ], pausa=2)
            op_extra = [
                "Cajado de Gelo +1 — amplificador elemental frio",
                "Tomo de Sabedoria Antiga — +3 CA imediato",
                "Grimório Portal — atravessa paredes com arcana",
                "Amuleto de Deflexão — deflexão passiva +1 CA",
            ]
            extras = ['Cajado de Gelo +1', 'Tomo de Sabedoria Antiga', 'Grimório Portal', 'Amuleto de Deflexão']

        elif sc == 'Mago Negro':
            itens_base = ['poção de cura', 'Grimório das Almas +2', 'Orbe Mental de Vecna +1', 'Runa do Limiar']
            porteiro_curto([
                "Mago das Sombras. Necromancia e maldição.",
                "Drenar Vida já está em vosso arsenal.",
            ], pausa=2)
            op_extra = [
                "Grimório do Colapso — paralisa inimigo 2 turnos",
                "Tomo de Sabedoria Antiga — +3 CA ao ler",
                "Explosivo Arremessável — caos tem muitas formas",
                "Poção de Sangue — HP imediato",
            ]
            extras = ['Grimório do Colapso', 'Tomo de Sabedoria Antiga', 'explosivo arremessável', 'Poção de Sangue']

        elif sc == 'Ladrão':
            itens_base = ['Botas do Silêncio', 'Adaga Simples +1', 'chave', 'Runa do Limiar']
            porteiro_curto([
                "Ladrão. Furtividade, sobrevivência e oportunismo.",
                "Armadilhas raramente vos surpreendem.",
            ], pausa=2)
            op_extra = [
                "Capa de Couro — leve proteção",
                "Poção de Invisibilidade — desaparecer quando necessário",
                "Adaga Simples +1 adicional — corte duplo",
                "Explosivo Arremessável — saída de emergência",
            ]
            extras = ['Capa de Couro', 'poção de invisibilidade', 'Adaga Simples +1', 'explosivo arremessável']

        else:  # Assassino
            itens_base = ['Adaga Envenenada +1', 'Botas do Silêncio', 'antídoto', 'Runa do Limiar']
            porteiro_curto([
                "Assassino. Silêncio, veneno e um único golpe.",
                "Crít em 19 ou 20. Veneno automático no golpe letal.",
            ], pausa=2)
            op_extra = [
                "Capa de Couro - leve proteção",
                "Espada Curta +1 — mais mordida no golpe inicial",
                "Pedra de Afiar — mantenha o fio cortante",
                "Explosivo Arremessável — quando a situação pedir algo menos sutil",
            ]
            extras = ['Capa de Couro', 'Espada Curta +1', 'Pedra de Afiar', 'explosivo arremessável']

        rotulo_pergunta = {
            'Bárbaro': "E vosso equipamento de reserva?",
            'Cavaleiro': "E vosso recurso complementar?",
            'Mago Azul': "E vossa ferramenta de escolha?",
            'Mago Negro': "E vossa arma secreta?",
            'Ladrão': "E vosso recurso de emergência?",
            'Assassino': "E vosso trunfo final?",
        }.get(sc, "E vossa escolha extra?")

        idx_ex = escolha_numerada(rotulo_pergunta, op_extra)
        itens_base.append(extras[idx_ex])

        # ── Distribuir itens base e AUTO-EQUIPAR ──────────────────────
        # Consumíveis ficam no inventário; armas/armaduras/acessórios são equipados. [por enquanto não liberar arco inicial]
        CONSUMIVEIS = {
            'poção de cura', 'poção de invisibilidade', 'antídoto',
            'chave', 'explosivo arremessável', 'Poção de Sangue',
            'Bandagem', 'Pó de Revelação', 'Garrafa de Ácido',
            'Erva do Sono', 'Pedra de Afiar', 'Pó de Gelo',
            'Pergaminho da Lanterna Espiritual',  # consumível mago
            'Flechas (20)', 'Flechas (10)',   # munição — consomem-se ao equipar
            'Pergaminho de Proteção',         # consumível mago
            'Diário Perdido',                # consumível — salva o jogo
        }
        for item_b in itens_base:
            personagem.inventario.append(item_b)
            if item_b not in CONSUMIVEIS:
                # Remove do inventário temporariamente para chamar _usar_item_direto
                # (que o re-equipará via gerenciar_equipamento ou aplicará efeito de tomo)
                try:
                    personagem.inventario.remove(item_b)
                    personagem._usar_item_direto(item_b)
                except Exception:
                    personagem.inventario.append(item_b)   # fallback: volta ao inventário

        bonus_narrativo(f"Equipamento base registrado e equipado: {', '.join(itens_base)}.")

        """
        # ── Flechas iniciais para quem tem Arco Élfico ────────────────
        if personagem.arma and personagem.arma.get('nome') in ('Arco Élfico', 'Arco da Ruína'):
            personagem.flechas = 20
            print("   🏹 20 flechas concedidas — munição inicial do Arco Élfico.")

        input("\n  [ ENTER ]")
        limpar_tela()
        """
        # ── 5. DOM ESPECIAL — bônus de atributo (múltipla escolha) ────
        porteiro_curto([
            "Cada um que chega ao Limiar traz um dom.",
            "",
            "Não habilidade aprendida. Dom. A coisa que sois",
            "mesmo quando tudo mais falha.",
            "",
            "Qual o vosso?",
        ], pausa=2.5)

        if classe == "Guerreiro":
            op_dom = [
                "Resistência — o corpo nega o que a mente aceitou (+6 HP)",
                "Fúria — cada golpe recebido acende o próximo (+2 ataque)",
                "Armadura viva — a pele aprende com as cicatrizes (+2 CA)",
                "Golpe pesado — os dados de dano têm lados a mais (+2 dano)",
            ]
            idx_dom = escolha_numerada("Vosso dom:", op_dom)
            if idx_dom == 0:
                personagem.hp += 6; personagem.hp_max += 6; personagem.base_hp_max += 6
                bonus_narrativo("+6 HP permanente.")
            elif idx_dom == 1:
                personagem.ataque_bonus += 2; personagem.base_ataque_bonus += 2
                bonus_narrativo("+2 bônus de ataque permanente.")
            elif idx_dom == 2:
                personagem.ac += 2; personagem.base_ac += 2
                bonus_narrativo("+2 CA permanente.")
            else:
                personagem.dano_lados += 2; personagem.base_dano_lados += 2
                bonus_narrativo("+2 lados de dado de dano.")

        elif classe == "Mago":
            op_dom = [
                "Mente de cristal — a magia voa mais longe (+3 bônus mágico)",
                "Véu arcano — a aura protege o corpo frágil (+3 CA)",
                "Canal vital — a magia drena os inimigos (+2 HP máx por feitiço)",
                "Corpus etéreo — a carne desaparece sob pressão (+5 HP)",
            ]
            idx_dom = escolha_numerada("Vosso dom:", op_dom)
            if idx_dom == 0:
                personagem.ataque_bonus += 3; personagem.base_ataque_bonus += 3
                bonus_narrativo("+3 bônus mágico permanente.")
            elif idx_dom == 1:
                personagem.ac += 3; personagem.base_ac += 3
                bonus_narrativo("+3 CA permanente.")
            elif idx_dom == 2:
                # Efeito especial: cada magia regenera 2 HP (implementado via flag)
                personagem.efeitos_ativos['canal_vital'] = 999  # permanente
                bonus_narrativo("+2 HP a cada feitiço lançado. Canal vital ativo.")
            else:
                personagem.hp += 5; personagem.hp_max += 5; personagem.base_hp_max += 5
                bonus_narrativo("+5 HP permanente.")

        else:  # Ladino
            op_dom = [
                "Reflexo de sombra — o golpe vem antes do alvo perceber (+2 ataque)",
                "Pele de névoa — sumis um instante antes do golpe (+2 CA)",
                "Passos sem eco — a chance de fuga e evasão aumenta (+3 HP + evasão)",
                "Leitura de ambiente — encontrais rotas onde não existem (+1 ataque e +1 CA)",
            ]
            idx_dom = escolha_numerada("Vosso dom:", op_dom)
            if idx_dom == 0:
                personagem.ataque_bonus += 2; personagem.base_ataque_bonus += 2
                bonus_narrativo("+2 bônus de ataque.")
            elif idx_dom == 1:
                personagem.ac += 2; personagem.base_ac += 2
                bonus_narrativo("+2 CA.")
            elif idx_dom == 2:
                personagem.hp += 3; personagem.hp_max += 3; personagem.base_hp_max += 3
                # evasão: menor chance de ser atacado (implementado no combate via flag)
                personagem.efeitos_ativos['evasao_passiva'] = 999
                bonus_narrativo("+3 HP + evasão passiva: 20% de desviar golpes.")
            else:
                personagem.ataque_bonus += 1; personagem.base_ataque_bonus += 1
                personagem.ac += 1; personagem.base_ac += 1
                bonus_narrativo("+1 ataque + +1 CA. Leitura do campo de batalha.")

        input("\n  [ ENTER ]")
        limpar_tela()

        # ── 5b. HABILIDADE ESPECIAL (Guerreiro / Ladino) ───────────────
        if classe == "Guerreiro":
            porteiro_curto([
                "E o dom que vos define em batalha.",
                "",
                "Todo guerreiro tem uma técnica que aprendeu",
                "não em treino, mas em desespero.",
                "",
                "Qual a vossa?",
            ], pausa=2.5)
            op_hab_g = [
                "Investida Feroz — avançar com tudo, dano duplo (recarga 4t)",
                "Contra-ataque — postura passiva; responde quando inimigo erra (recarga 3t)",
                "Golpes Sequenciais — três ataques rápidos, dano base reduzido (recarga 3t)",
                "Nenhuma — apenas força e vontade",
            ]
            idx_hab_g = escolha_numerada("Vossa técnica:", op_hab_g)
            habs_g = ['investida', 'contra-ataque', 'sequencial', None]
            personagem.habilidade_especial = habs_g[idx_hab_g]
            if personagem.habilidade_especial:
                bonus_narrativo(f"Habilidade especial: {op_hab_g[idx_hab_g].split(' — ')[0]}. Use botão 2 no combate.")
            else:
                bonus_narrativo("Sem habilidade especial. A simplicidade tem sua própria força.")

        elif classe == "Ladino":
            porteiro_curto([
                "Ladinos não lutam — resolvem problemas.",
                "",
                "Qual o vosso método preferido quando",
                "a furtividade não é mais suficiente?",
            ], pausa=2.5)
            op_hab_l = [
                "Golpe Sorrateiro — golpe alto garantido + veneno (recarga 3t)",
                "Evasão — 60% de desviar próximos 2 ataques (recarga 3t)", # Verificar e confirmar [evasão test], antes eram 3 ataques inimigos
                "Veneno na Lâmina — 3 ataques automáticos com veneno (recarga 4t)",
                "Nenhuma — fuga e improviso são suficientes",
            ]
            idx_hab_l = escolha_numerada("Vosso método:", op_hab_l)
            habs_l = ['sorrateiro', 'evasao', 'veneno_lamina', None]
            personagem.habilidade_especial = habs_l[idx_hab_l]
            if personagem.habilidade_especial:
                bonus_narrativo(f"Habilidade especial: {op_hab_l[idx_hab_l].split(' — ')[0]}. Use botão 2 no combate.")
            else:
                bonus_narrativo("Sem habilidade especial. Agilidade pura vale mais que qualquer técnica.")

        if classe != "Mago":
            input("\n  [ ENTER ]")
            limpar_tela()

        # ── 6. AFINIDADE ESPIRITUAL ────────────────────────────────────
        # (só pergunta se ainda não concedida pelo KWDS_SONHO)
        if not personagem.afinidade_espiritual:
            porteiro_curto([
                "Uma última coisa.",
                "",
                "O Limiar está repleto de altares e estatuas",
                "de deuses cuja memória as civilizações perderam.",
                "",
                "Ainda credes em algo além do que os olhos veem?",
            ], pausa=2.5)

            op_fe = [
                "Sim — há forças além da compreensão humana",
                "Depende — algumas coisas têm aparência divina",
                "Não — apenas o que posso tocar existe",
                "Não sei — vim ao Limiar para descobrir",
            ]
            idx_fe = escolha_numerada("Vossa fé:", op_fe)

            if idx_fe == 0:
                porteiro_curto([
                    "Fé genuína. Rara aqui embaixo.",
                    "",
                    "Os altares do Limiar reconhecem os que acreditam.",
                    "Orai com frequência — o retorno será proporcional.",
                ], pausa=2.5)
                personagem.afinidade_espiritual = True
                bonus_narrativo("Afinidade espiritual plena. Altares sempre respondem.")

            elif idx_fe == 1:
                porteiro_curto([
                    "Fé pragmática.",
                    "",
                    "Os altares vos ouvirão. Nem sempre responderão.",
                    "Mas quanto mais orardes, mais a probabilidade aumenta.",
                    "O Limiar é um lugar de conversões graduais.",
                ], pausa=2.5)
                bonus_narrativo("Afinidade parcial. Orai muito — os altares ouvirão.")

            elif idx_fe == 2:
                porteiro_curto([
                    "Ceticismo absoluto.",
                    "",
                    "Respeitável. Os altares existem independente",
                    "de vossa crença. Se algum dia mudardes de ideia,",
                    "eles ainda estarão lá.",
                ], pausa=2.5)
                bonus_narrativo("Sem afinidade. Altares podem ser convertidos com oração constante.")

            else:
                porteiro_curto([
                    "Vim ao Limiar para descobrir.",
                    "",
                    "A melhor razão de todas.",
                    "O Limiar responde a perguntas. Raramente",
                    "com respostas confortáveis.",
                    "",
                    "Os altares vos testerão. Continuai orando.",
                ], pausa=2.5)
                bonus_narrativo("Sem afinidade inicial. Orai nos altares para converter.")

            input("\n  [ ENTER ]")
            limpar_tela()

        # ── 7. FECHAMENTO — O PORTEIRO ABRE O PORTÃO ──────────────────
        porteiro_curto([
            f"Registro completo. {nome}. {classe}.",
            "",
            f"HP: {personagem.hp}  CA: {personagem.ac}  Ataque: +{personagem.ataque_bonus}",
            f"Carga: {personagem.capacidade_peso}kg  Inventário: {len(personagem.inventario)} item(ns)",
            f"Afinidade espiritual: {'Sim' if personagem.afinidade_espiritual else 'Não (ou parcial)'}",
        ], pausa=3)

        n("", 0.3)
        porteiro_curto([
            "O Limiar do Mundo vos aguardava.",
            "",
            "As masmorras têm quatro corredores a partir do centro.",
            "Norte, Sul, Leste, Oeste — cada região é distinta,",
            "gerada a cada sessão, impossível de mapear com antecedência.",
            "",
            "Escadas '>': aprofundam o abismo.",
            "Escadas '<': permitem recuar. Use-as.",
            "",
            "O Olho de Vecna dorme nos andares mais profundos.",
            "Alguns dizem que é um artefato. Outros, que é um Feiticeiro",
            "que descobriu os segredos do mundo e os guardou para si.",
            "",
            "Nenhum dos que desceram voltou para confirmar.",
        ], pausa=4)

        n("", 0.5)
        n("O portão de pedra negra se abre.", 1.5)
        n("O ar que sai é mais velho que qualquer civilização.", 2)
        n("O Porteiro se afasta. Não deseja boa sorte.", 1.5)
        n("Não aqui.", 2.5)
        n("", 0.5)
        print("  [ ENTER para adentrar as Masmorras Liminares ]")
        input()

    def _dificuldade_atual(self):
        """
        Dificuldade unificada:
          - Andar é o motor principal (×6 por andar).
          - Salas exploradas no total contribuem como sub-progressão (÷3).
          Assim descer andares é muito mais impactante que apenas explorar.
        """
        return max(1, self.andar * 6 + self.nivel // 3)

    def _mostrar_hud(self):
        limpar_tela()

        if self.modo_extremo:
            print("🔥💀 [ REGIÃO EXTREMA — ALÉM DO ABISMO ] 💀🔥")

        if self.em_andar_profundo and self.andar in self.andares:
            # ── HUD: Andar profundo ──────────────────────────────────
            andar_obj = self.andares[self.andar]
            salas_visitadas_andar = sum(
                1 for k in self.salas_visitadas
                if isinstance(k, tuple) and len(k) == 3 and k[0] == 'andar' and k[1] == self.andar
            )
            livres = andar_obj.direcoes_livres(self.sala_no_andar)
            dir_str = [NOME_DIRECAO.get(d, '?') for d in livres]
            print(f"🕳️  {andar_obj.nome}")
            print(f"   Profundidade: Andar {self.andar}  |  Sala: {self.sala_no_andar}")
            print(f"   Passagens: {', '.join(dir_str) if dir_str else 'Nenhuma (beco sem saída!)'}")
        elif self.regiao_atual_key is not None:
            # ── HUD: Região do nível 1 ───────────────────────────────
            regiao = self.regioes[self.regiao_atual_key]
            dir_nome = NOME_DIRECAO.get(self.regiao_atual_key, "?")
            regiao_nome = f"Região {dir_nome}: {regiao.nome}"
            salas_total = regiao.num_salas()
            visitadas_regiao = sum(1 for s in self.salas_visitadas
                                   if isinstance(s, tuple) and s[0] == str(self.regiao_atual_key))
            print(f"🗺️  {regiao_nome}")
            print(f"   Salas exploradas: {visitadas_regiao}/{salas_total} | "
                  f"Sala atual: {self.sala_pos}")
            livres = self.regioes[self.regiao_atual_key].direcoes_livres(self.sala_pos)
            dir_str = [NOME_DIRECAO.get(d, '?') for d in livres]
            print(f"   Passagens: {', '.join(dir_str) if dir_str else 'Nenhuma (beco sem saída!)'}")
        else:
            # ── HUD: Hub central ────────────────────────────────────
            print(f"🗺️  Hub Central — escolha uma direção para explorar")
            print("   Norte(W) | Sul(S) | Oeste(A) | Leste(D)")

        print()
        # Hub = sempre visibilidade total; dungeons usam o sistema de iluminação
        em_hub = (self.regiao_atual_key is None and not self.em_andar_profundo)
        self.mapa.mostrar((self.x, self.y), jogador=self.jogador, full_vis=em_hub)
        print()
        diarios_rest = len(self._diarios_por_sessao) - self._diarios_lidos
        diario_str = f"  |  📓 Diários: {self._diarios_lidos}/{len(self._diarios_por_sessao)}" if diarios_rest >= 0 else ""
        j = self.jogador
        extras = []
        if j.flechas > 0 and j.arma and j.arma.get('nome') in ('Arco Élfico', 'Arco da Ruína'):
            extras.append(f"🏹 {j.flechas} flechas")
        elif j.flechas > 0:
            extras.append(f"🏹 {j.flechas} flechas (arco não equipado)")
        if j.classe == 'Mago' and j.cooldown_magia > 0:
            extras.append(f"✨ magia: {j.cooldown_magia}t recarga")
        elif j.classe == 'Mago':
            extras.append("✨ magia pronta [m]")
        extras_str = "  |  " + "  |  ".join(extras) if extras else ""
        print(self.jogador.status() + f"\n| Andar: {self.andar}  |  Progressão: {self.nivel} salas  |  Dificuldade: {self._dificuldade_atual()}{diario_str}{extras_str}")
        print()

    def jogar(self):
        limpar_tela()
        print(f"\n  A porta atrás de {self.jogador.nome} fecha com um eco que demora demais.\n")
        time.sleep(2)
        print("  O cheiro de pedra úmida e algo mais antigo toma conta do ar.")
        time.sleep(2.5)
        print("  A tocha tremula. Mas não apaga.\n")
        time.sleep(2.5)

        while self.jogador.esta_vivo():
            self.jogador.turno_magia()
            self.jogador.atualizar_efeitos()

            # ── Processar veneno e DoTs FORA do combate também ──
            self.jogador.processar_efeitos()
            if not self.jogador.esta_vivo():
                break

            self._mostrar_hud()

            cmd = input("Comando (wasd=mover | e=inv | m=magia | b=arco | x=explosivo | p=portal | r=runa | ?=ajuda | sair): ").lower().strip()

            if cmd == '?':
                self._mostrar_ajuda()
                continue

            elif cmd in DIR_MAP:
                self._processar_movimento(cmd)

            elif cmd == 'e':
                self._abrir_inventario()

            elif cmd == 'm':
                self._usar_magia_explorar()

            elif cmd == 'b':
                self._usar_arco_explorar()

            elif cmd == 'x':
                self._usar_explosivo_explorar()

            elif cmd == 'r':
                self._usar_runa_limiar()

            elif cmd == 'p':
                self._usar_portal_explorar()

            elif cmd == 'sair':
                print("🛑 Fim da aventura.")
                break

            else:
                print("❓ Comando desconhecido.")

            # Inimigos se movem após cada ação do jogador
            self.mapa.mover_inimigos((self.x, self.y), self.jogador)

        if not self.jogador.esta_vivo():
            limpar_tela()
            print(f"\n  {self.jogador.nome} não voltou.\n")
            time.sleep(2)
            msgs_morte = [
                "A masmorra não distingue os corajosos dos imprudentes.",
                "As tochas se apagam uma a uma até o silêncio ser completo.",
                "Algo nas profundezas se move em direção ao que sobrou.",
                "O Olho de Vecna permanece sem testemunhas.",
            ]
            print(f"  {random.choice(msgs_morte)}\n")
            time.sleep(2)
            print(f"  Profundidade máxima: Andar {self.andar}  |  Salas exploradas: {self.nivel}  |  Dificuldade final: {self._dificuldade_atual()}")
            time.sleep(1.5)
            print()
            print(f"  {random.choice(DICAS_MORTE)}")
            print()
            time.sleep(3)
            print("  As Masmorras Liminares seguem esperando o próximo.\n")
            time.sleep(2.5)

    # ─────────────────────────────────────────────────────
    # INVENTÁRIO NAVEGÁVEL  (w/s, números + ENTER, seção bolsa e equipados)
    # ─────────────────────────────────────────────────────
    def _abrir_inventario(self):
        """
        Inventário em duas seções: BOLSA e EQUIPADOS.
        - w/s navega dentro da seção ativa
        - Tab (t) alterna seção
        - 1..N pula direto e abre menu
        - ENTER abre menu do item selecionado
        - q fecha
        """
        jogador = self.jogador
        secao = 'bolsa'
        cursor_b = 0
        cursor_e = 0

        while True:
            limpar_tela()
            bolsa = jogador.inventario
            equip = jogador.equipados
            nb = len(bolsa)
            ne = len(equip)

            # ── HUD de status completo ────────────────────────────────
            print("╔══════════════════════════════════════════════════╗")
            print("║               🎒  INVENTÁRIO                     ║")
            print("╠══════════════════════════════════════════════════╣")
            # HP bar
            hp_ratio = max(jogador.hp, 0) / max(jogador.hp_max, 1)
            hp_cheios = int(hp_ratio * 20)
            hp_bar = f"[{'█'*hp_cheios}{'-'*(20-hp_cheios)}]"
            print(f"║  ❤️  HP  {hp_bar} {jogador.hp}/{jogador.hp_max}")
            print(f"║  🛡️  CA: {jogador.ac}   ⚔️  Atq: {jogador.ataque_bonus}   🎲 d{jogador.dano_lados}")
            # Efeitos ativos
            efeitos_vis = []
            if 'veneno' in jogador.efeitos_ativos:
                d = jogador.efeitos_ativos['veneno']
                efeitos_vis.append(f"🐍Veneno({d['dano']}dmg/{d['turnos']}t)")
            if 'veneno_duplo' in jogador.efeitos_ativos:
                d = jogador.efeitos_ativos['veneno_duplo']
                efeitos_vis.append(f"☠️Veneno+({d['dano']}dmg/{d['turnos']}t)")
            for ef, v in jogador.efeitos_ativos.items():
                if ef not in ('veneno', 'veneno_duplo', 'valor_protecao') and isinstance(v, int):
                    efeitos_vis.append(f"{ef}({v}t)")
            if efeitos_vis:
                ef_str = '  '.join(efeitos_vis)[:46]
                print(f"║  {ef_str}")
            if jogador.invisivel:
                print("║  👻 Invisível")
            if jogador.cooldown_magia > 0 and jogador.classe == "Mago":
                print(f"║  🔮 Magia: recarga em {jogador.cooldown_magia} turnos")
            # Peso
            livre = round(jogador.capacidade_peso - jogador.peso_atual, 2)
            print(f"║  ⚖️  Carga: {jogador.peso_atual:.1f}/{jogador.capacidade_peso}kg"
                  f"  (bolsa {jogador.peso_bolsa:.1f} + vest. {jogador.peso_vestido:.1f})\n"
                  f"  livre: {livre:.1f}kg")
            print("╠══════════════════════════════════════════════════╣")

            # ── BOLSA ──
            hdr_b = "► BOLSA" if secao == 'bolsa' else "  BOLSA"
            slots_equip = f"({ne}/6 equipados)"
            # Flechas aparecem como entrada virtual no fim da bolsa
            flechas_qtd = getattr(jogador, 'flechas', 0)
            n_virtual = 1 if flechas_qtd > 0 else 0   # 1 slot virtual para flechas
            nb_total = nb + n_virtual
            print(f"║  {hdr_b}                        {slots_equip:>16} ║")
            if not bolsa and flechas_qtd == 0:
                print("║  ( bolsa vazia )                                 ║")
            else:
                for i, item in enumerate(bolsa):
                    ativo = secao == 'bolsa' and i == cursor_b
                    seta = " ▶ " if ativo else "   "
                    p = peso_item(item)
                    nome_c = item[:28] if len(item) > 28 else item
                    print(f"║{seta}{i+1:>2}. {nome_c:<28}  {p:.1f}kg        ║")
                if flechas_qtd > 0:
                    idx_f = nb   # índice virtual = depois dos reais
                    ativo = secao == 'bolsa' and cursor_b == idx_f
                    seta = " ▶ " if ativo else "   "
                    peso_f = round(flechas_qtd * 0.05, 2)
                    label = f"🏹 Flechas ({flechas_qtd})"
                    print(f"║{seta}{idx_f+1:>2}. {label:<28}  {peso_f:.1f}kg ║")

            print("╠══════════════════════════════════════════════════╣")

            # ── EQUIPADOS ──
            hdr_e = "► EQUIPADOS ⚔️" if secao == 'equipados' else "  EQUIPADOS ⚔️"
            print(f"║  {hdr_e}  (pesam na carga, max 6)         ║")
            if not equip:
                print("║  ( nenhum equipado )                           ║")
            else:
                for i, eq in enumerate(equip):
                    ativo = secao == 'equipados' and i == cursor_e
                    seta = " ▶ " if ativo else "   "
                    eq_c = eq[:28] if len(eq) > 28 else eq
                    p = peso_item(eq)
                    print(f"║{seta}{i+1:>2}. {eq_c:<28}  {p:.1f}kg        ║")

            print("╠══════════════════════════════════════════════════╣")
            n_ativo = nb_total if secao == 'bolsa' else ne
            if n_ativo > 0:
                print(f"║  w/s=navegar  1-{n_ativo}=ir direto  ENTER=agir          ║")
            print("║  t = alternar seção  |  q = fechar               ║")
            print("╚══════════════════════════════════════════════════╝")

            tecla = input("> ").lower().strip()

            if tecla == 'q':
                break
            elif tecla == 't':
                secao = 'equipados' if secao == 'bolsa' else 'bolsa'
            elif tecla == 'w':
                if secao == 'bolsa' and nb_total > 0:
                    cursor_b = (cursor_b - 1) % nb_total
                elif secao == 'equipados' and ne > 0:
                    cursor_e = (cursor_e - 1) % ne
            elif tecla == 's':
                if secao == 'bolsa' and nb_total > 0:
                    cursor_b = (cursor_b + 1) % nb_total
                elif secao == 'equipados' and ne > 0:
                    cursor_e = (cursor_e + 1) % ne
            elif tecla.isdigit():
                idx = int(tecla) - 1
                if secao == 'bolsa' and 0 <= idx < nb_total:
                    cursor_b = idx
                    if cursor_b == nb and flechas_qtd > 0:
                        self._menu_flechas()
                    else:
                        acao = self._menu_item(bolsa[cursor_b], cursor_b)
                        self._lancar_item_no_chao_se_necessario()
                        cursor_b, fechar = self._aplicar_acao_inv(acao, cursor_b)
                        if fechar:
                            break
                elif secao == 'equipados' and 0 <= idx < ne:
                    cursor_e = idx
                    fechar = self._menu_item_equipado(cursor_e)
                    if fechar:
                        break
            elif tecla in ('', 'enter'):
                if secao == 'bolsa' and nb_total > 0:
                    if cursor_b == nb and flechas_qtd > 0:
                        self._menu_flechas()
                    else:
                        acao = self._menu_item(bolsa[cursor_b], cursor_b)
                        self._lancar_item_no_chao_se_necessario()
                        cursor_b, fechar = self._aplicar_acao_inv(acao, cursor_b)
                        if fechar:
                            break
                elif secao == 'equipados' and ne > 0:
                    fechar = self._menu_item_equipado(cursor_e)
                    if fechar:
                        break

    def _menu_flechas(self):
        """Menu de gerenciamento de flechas: descartar quantidade específica."""
        j = self.jogador
        while True:
            limpar_tela()
            qtd = getattr(j, 'flechas', 0)
            peso_total = round(qtd * 0.05, 2)
            print(f"╔══════════════════════════════════════════════════╗")
            print(f"║  🏹 Flechas ({qtd})                              ║")
            print(f"║  ⚖️  {peso_total:.1f}kg  ({qtd} × 0.05kg/unidade) ║")
            print(f"╠══════════════════════════════════════════════════╣")
            print(f"║  Usada automaticamente pelo arco.                ║")
            print(f"╠══════════════════════════════════════════════════╣")
            print(f"║  1 — Descartar algumas flechas                   ║")
            print(f"║  0 — Voltar                                      ║")
            print(f"╚══════════════════════════════════════════════════╝")
            op = input("> ").strip()
            if op == '1':
                print(f"   Descartar quantas? (1–{qtd}, ENTER=cancelar): ", end='', flush=True)
                entrada = input().strip()
                if entrada == '':
                    continue
                try:
                    n = max(0, min(int(entrada), qtd))
                except ValueError:
                    continue
                if n > 0:
                    j.flechas = qtd - n
                    print(f"   ↩️  {n} flechas descartadas. Restantes: {j.flechas}.")
                    time.sleep(1.2)
                if j.flechas == 0:
                    return
            elif op == '0':
                return

    def _lancar_item_no_chao_se_necessario(self):
        """Verifica se gerenciar_equipamento marcou um item para largar no chão."""
        item = getattr(self.jogador, '_item_para_largar_no_chao', None)
        if item:
            self.jogador._item_para_largar_no_chao = None
            pos_drop = (self.x, self.y)
            for _ in range(8):
                if pos_drop not in self.mapa.itens:
                    break
                nx = self.x + random.choice([-1, 0, 1])
                ny = self.y + random.choice([-1, 0, 1])
                if (0 <= nx < self.mapa.largura and 0 <= ny < self.mapa.altura
                        and self.mapa.matriz[ny][nx] == '.'):
                    pos_drop = (nx, ny)
            self.mapa.itens[pos_drop] = item
            print(f"   📍 '{item}' largado no chão em ({pos_drop[0]},{pos_drop[1]}).")
            time.sleep(1)

    def _aplicar_acao_inv(self, acao, cursor):
        """Trata resultado de _menu_item. Retorna (novo_cursor, deve_fechar)."""
        jogador = self.jogador
        if acao == 'usado_ou_equipado':
            if not jogador.inventario:
                return 0, True
            return min(cursor, len(jogador.inventario) - 1), False
        elif acao == 'deixar':
            item_removido = jogador.inventario.pop(cursor)
            pos_drop = (self.x, self.y)
            tentativas = 0
            while pos_drop in self.mapa.itens and tentativas < 8:
                nx = self.x + random.choice([-1, 0, 1])
                ny = self.y + random.choice([-1, 0, 1])
                if (0 <= nx < self.mapa.largura and 0 <= ny < self.mapa.altura
                        and self.mapa.matriz[ny][nx] == '.'):
                    pos_drop = (nx, ny)
                tentativas += 1
            self.mapa.itens[pos_drop] = item_removido
            limpar_tela()
            print(f"↩️  Você largou '{item_removido}' no chão.")
            time.sleep(1.5)
            if not jogador.inventario:
                return 0, True
            return min(cursor, len(jogador.inventario) - 1), False
        return cursor, False

    def _menu_item(self, item, cursor_idx):
        """Sub-menu de ação para um item selecionado. Retorna o que aconteceu."""
        jogador = self.jogador
        while True:
            limpar_tela()
            nome_c = item[:44] if len(item) > 44 else item
            print(f"╔══════════════════════════════════════════════════╗")
            print(f"║  {nome_c:<48}║")
            print(f"║  ⚖️  {peso_item(item):.1f}kg"
                  f"{'   [EQUIPADO]' if item in jogador.equipados else '':>38} ║")
            print(f"╠══════════════════════════════════════════════════╣")
            desc = descricao_item(item)
            palavras = desc.split()
            linha_desc = ""
            for w in palavras:
                if len(linha_desc) + len(w) + 1 > 46:
                    print(f"║  {linha_desc:<48}║")
                    linha_desc = w
                else:
                    linha_desc = (linha_desc + " " + w).strip()
            if linha_desc:
                print(f"║  {linha_desc:<48}║")
            print(f"╠══════════════════════════════════════════════════╣")
            print(f"║  1 — Usar / Equipar                              ║")
            print(f"║  2 — Examinar (desc. completa)                   ║")
            print(f"║  3 — Deixar no chão                              ║")
            print(f"║  0 — Voltar                                      ║")
            print(f"╚══════════════════════════════════════════════════╝")

            op = input("> ").strip()
            if op == '1':
                jogador.inventario.pop(cursor_idx)
                jogador._usar_item_direto(item)
                return 'usado_ou_equipado'
            elif op == '2':
                input("\n  Pressione ENTER para continuar...")
            elif op == '3':
                return 'deixar'
            elif op == '0':
                return 'cancelar'

    def _menu_item_equipado(self, cursor_e):
        """Sub-menu para item equipado: desequipar, largar, comparar. Retorna True=fechar."""
        jogador = self.jogador
        while True:
            if cursor_e >= len(jogador.equipados):
                return False
            item = jogador.equipados[cursor_e]
            limpar_tela()
            nome_c = item[:44] if len(item) > 44 else item
            print(f"╔══════════════════════════════════════════════════╗")
            print(f"║  ⚔️  {nome_c:<45}║")
            print(f"║  ⚖️  {peso_item(item):.1f}kg   [EQUIPADO — slot {cursor_e+1}/6]              ║")
            print(f"╠══════════════════════════════════════════════════╣")
            # descrição
            desc = descricao_item(item)
            palavras = desc.split()
            linha_desc = ""
            for w in palavras:
                if len(linha_desc) + len(w) + 1 > 46:
                    print(f"║  {linha_desc:<48}║")
                    linha_desc = w
                else:
                    linha_desc = (linha_desc + " " + w).strip()
            if linha_desc:
                print(f"║  {linha_desc:<48}║")
            print(f"╠══════════════════════════════════════════════════╣")
            # comparar com item na bolsa de mesmo tipo
            tipo_item = item.split('+')[0].strip() if '+' in item else item
            similar_bolsa = next((b for b in jogador.inventario if tipo_item in b), None)
            if similar_bolsa:
                p2 = peso_item(similar_bolsa)
                try:
                    bonus_eq  = int(item.split('+')[1]) if '+' in item else 0
                    bonus_b   = int(similar_bolsa.split('+')[1]) if '+' in similar_bolsa else 0
                    delta = bonus_b - bonus_eq
                    sinal = f"+{delta}" if delta > 0 else str(delta)
                    comp = f"Na bolsa: {similar_bolsa[:20]} ({p2:.1f}kg) Δ{sinal}"
                except:
                    comp = f"Na bolsa: {similar_bolsa[:30]} ({p2:.1f}kg)"
                print(f"║  🔄 {comp:<46}║")
                print(f"╠══════════════════════════════════════════════════╣")
            # Verificar se é arma alternável
            _ARMA_PREFIXOS = (
                'Espada Curta','Espada Longa','Lâmina Sombria','Arco Élfico','Arco da Ruína',
                'Machado Anão Flamejante','Cajado de Gelo','Adaga Simples',
                'Adaga Envenenada','Manoplas do Trovão','Orbe Mental de Vecna',
                'Cajado de Osso','Lâmina Drenante','Machado do Sangramento',
                'Espada Fantasma','Machado de Guerra','Espada dos Mártires',
                'Lâmina Especular',
            )
            arma_ativa_nome = jogador.arma.get('nome', '') if jogador.arma else ''
            _eh_arma_reconhecida = any(item.startswith(p) for p in _ARMA_PREFIXOS)
            ja_ativa = bool(arma_ativa_nome and arma_ativa_nome in item)
            if _eh_arma_reconhecida and not ja_ativa:
                print(f"║  1 — Ativar como arma principal ⚔️               ║")
                print(f"║  2 — Desequipar (volta à bolsa)                  ║")
                print(f"║  3 — Largar no chão                              ║")
                print(f"║  0 — Voltar                                      ║")
            elif _eh_arma_reconhecida and ja_ativa:
                print(f"║  ✅ Esta é sua arma principal ativa              ║")
                print(f"║  1 — Desequipar (volta à bolsa)                  ║")
                print(f"║  2 — Largar no chão                              ║")
                print(f"║  0 — Voltar                                      ║")
            else:
                print(f"║  1 — Desequipar (volta à bolsa)                  ║")
                print(f"║  2 — Largar no chão                              ║")
                print(f"║  0 — Voltar                                      ║")
            print(f"╚══════════════════════════════════════════════════╝")

            op = input("> ").strip()
            if _eh_arma_reconhecida and not ja_ativa:
                # Mapa de opções: 1=ativar, 2=desequipar, 3=largar
                if op == '1':
                    jogador._ativar_arma_por_nome(item)
                    limpar_tela()
                    print(f"⚔️  {item} ativado como arma principal!")
                    time.sleep(1.5)
                    return False
                elif op == '2':
                    jogador.equipados.pop(cursor_e)
                    jogador.inventario.append(item)
                    jogador.atualizar_atributos_equipamento()
                    if jogador.arma and jogador.arma.get('nome', '') in item:
                        jogador.arma = None
                    limpar_tela()
                    print(f"🔓 {item} desequipado. Devolvido à bolsa.")
                    time.sleep(1.5)
                    return False
                elif op == '3':
                    jogador.equipados.pop(cursor_e)
                    if jogador.arma and jogador.arma.get('nome', '') in item:
                        jogador.arma = None
                    jogador.atualizar_atributos_equipamento()
                    jogador._item_para_largar_no_chao = item
                    print(f"↩️  {item} será largado no chão.")
                    time.sleep(1)
                    return False
                elif op == '0':
                    return False
            elif _eh_arma_reconhecida and ja_ativa:
                # Mapa: 1=desequipar, 2=largar
                if op == '1':
                    jogador.equipados.pop(cursor_e)
                    jogador.inventario.append(item)
                    jogador.arma = None
                    jogador.atualizar_atributos_equipamento()
                    limpar_tela()
                    print(f"🔓 {item} desequipado. Devolvido à bolsa.")
                    time.sleep(1.5)
                    return False
                elif op == '2':
                    jogador.equipados.pop(cursor_e)
                    jogador.arma = None
                    jogador.atualizar_atributos_equipamento()
                    jogador._item_para_largar_no_chao = item
                    print(f"↩️  {item} será largado no chão.")
                    time.sleep(1)
                    return False
                elif op == '0':
                    return False
            else:
                # Não é arma — menu normal: desequipar ou largar
                if op == '1':
                    jogador.equipados.pop(cursor_e)
                    jogador.inventario.append(item)
                    jogador.atualizar_atributos_equipamento()
                    if jogador.arma and jogador.arma.get('nome', '') in item:
                        jogador.arma = None
                    limpar_tela()
                    print(f"🔓 {item} desequipado. Devolvido à bolsa.")
                    time.sleep(1.5)
                    return False
                elif op == '2':
                    jogador.equipados.pop(cursor_e)
                    jogador.atualizar_atributos_equipamento()
                    if jogador.arma and jogador.arma.get('nome', '') in item:
                        jogador.arma = None
                    jogador._item_para_largar_no_chao = item
                    limpar_tela()
                    print(f"↩️  '{item}' será largado no chão.")
                    time.sleep(1.5)
                    return False
                elif op == '0':
                    return False

    def _mostrar_ajuda(self):
        print("""
╔══════════════════════════════════════════════════╗
║                   CONTROLES                      ║
║  w/a/s/d  — mover / mudar sala / região          ║
║  e        — abrir inventário navegável           ║
║  m        — Magia (Mago): míssil, área ou cura   ║
║             em qualquer inimigo visível          ║
║  b        — Arco: disparo à distância (range 3)  ║
║             requer flechas equipadas             ║
║  x        — explosivo arremessável (destrói      ║
║             paredes, portas e acerta inimigos)   ║
║  p        — Grimório Portal (Mago): atravessa    ║
║             uma parede adjacente                 ║
║  r        — Runa do Limiar: volta ao hub         ║
║  ?        — esta tela de ajuda                   ║
║  sair     — encerrar sessão                      ║
╠══════════════════════════════════════════════════╣
║  NO INVENTÁRIO:                                  ║
║  w / s    — navegar item acima / abaixo          ║
║  1, 2, 3… — pular direto para o item             ║
║  ENTER    — agir (usar/equipar/examinar/largar)  ║
║  q        — fechar inventário                    ║
║                                                  ║
║  obs: Múltiplos itens acumulam status mas só um  ║
║       efeito pode ser ativado por vez.           ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║  ESCADAS:                                        ║
║  >  desce um andar (mais fundo, mais difícil)    ║
║  <  sobe um andar  (retorno — mesmo spawn)       ║
╠══════════════════════════════════════════════════╣
║  PESO:                                           ║
║  Bolsa + equipamentos = carga total              ║
║  Equipar NÃO alivia o peso — você veste, não     ║
║  abandona. Largar no chão alivia.                ║
╠══════════════════════════════════════════════════╣
║  NO COMBATE:                                     ║
║  1 — Atacar  2 — Magia/Hab  3 — Item  4 — Fugir  ║
╠══════════════════════════════════════════════════╣
║  MAPA:  ● você  ! inimigo  ? item  > desce       ║
║         < sobe  ▓ porta trancada  + estrutura    ║
╚══════════════════════════════════════════════════╝
""")
        input("  [ ENTER para continuar ]")

    # ─────────────────────────────────────────────────────
    # MAGIA NA EXPLORAÇÃO [m] — Mago usa spells sem combate
    # ─────────────────────────────────────────────────────
    def _usar_magia_explorar(self):
        """
        O Mago pode lançar magias durante a exploração:
        - Míssil Mágico: atinge inimigo em range 3 (distância Manhattan)
        - Explosão Arcana (AoE): atinge todos os inimigos visíveis em range 2
        - Toque de Cura (Mago Azul): cura HP sem alvo
        - Drenar Vida (Mago Negro): em inimigo visível
        Inimigos atingidos ficam ALERTADOS e avançam imediatamente.
        """
        j = self.jogador
        if j.classe != 'Mago':
            print("✨ Apenas Magos podem lançar magias na exploração.")
            time.sleep(1)
            return

        if j.cooldown_magia > 0:
            print(f"❌ Magia em recarga! ({j.cooldown_magia} turnos restantes)")
            time.sleep(1)
            return

        subclasse = getattr(j, 'subclasse', None)
        tem_almas  = any('Grimório das Almas' in eq for eq in j.equipados)
        tem_colaps = any('Grimório do Colapso' in eq for eq in j.equipados)

        # ── Lista inimigos VISÍVEIS no mapa atual ─────────────────────
        vision_range = 1
        if 'Tocha Suja' in getattr(j, 'equipados', []):
            vision_range = 2
        if getattr(j, 'lanterna_espiritual', 0) > 0:
            vision_range = 2
        celulas_visiveis = self.mapa._calc_visivel((self.x, self.y), vision_range)
        inimigos_vivos = [
            i for i in self.mapa.inimigos
            if i.esta_vivo() and i.pos in celulas_visiveis
        ]
        if not inimigos_vivos and subclasse != 'Mago Azul':
            print("✨ Não há inimigos visíveis para atacar.")
            time.sleep(1)
            return

        # ── Montar menu de opções ──────────────────────────────────────
        limpar_tela()
        self._mostrar_hud()
        print("\n✨ MAGIA — EXPLORAÇÃO")
        print("  1 — Míssil Mágico      (range 3, 1 alvo)")
        if tem_almas:
            print("  2 — Onda de Almas      (range 3, 1 alvo, +dano)")
        print("  3 — Explosão Arcana    (range 2, TODOS os inimigos visíveis)")
        if subclasse == 'Mago Azul':
            print("  4 — Toque de Cura      (cura própria HP, cooldown 3t)")
        if subclasse == 'Mago Negro' and inimigos_vivos:
            print("  4 — Drenar Vida        (range 3, 1 alvo, rouba HP)")
        if tem_colaps and inimigos_vivos:
            print("  5 — Colapso            (range 3, paralisa 2 turnos)")
        print("  0 — Cancelar")

        sub = input(">> ").strip()
        if sub == '0' or sub == '':
            return

        poder = j.calcular_poder_magico_total()

        # ── 1 / 2 — Míssil Mágico ou Onda de Almas (1 alvo) ─────────
        if sub in ('1', '2'):
            if not inimigos_vivos:
                print("Sem alvo."); time.sleep(1); return
            print("\n  Inimigos detectados:")
            alvos_magia = []
            for idx, ini in enumerate(inimigos_vivos, 1):
                ix, iy = ini.pos
                dist = abs(self.x - ix) + abs(self.y - iy)
                tem_los = self.mapa.tem_linha_de_visao(self.x, self.y, ix, iy)
                bloq = "  ▓ parede bloqueia" if not tem_los else ""
                fora = "  ✗ fora do alcance" if dist > 3 else ""
                print(f"  {idx}. {ini.nome}  (dist {dist}{bloq}{fora})")
                if dist <= 3 and tem_los:
                    alvos_magia.append(ini)
            sel = input("  Escolha o alvo (0=cancelar): ").strip()
            try:
                alvo = inimigos_vivos[int(sel) - 1]
            except (ValueError, IndexError):
                return
            dist_alvo = abs(self.x - alvo.pos[0]) + abs(self.y - alvo.pos[1])
            if dist_alvo > 3:
                print(f"❌ {alvo.nome} está fora do alcance! (dist {dist_alvo}, max 3)")
                time.sleep(1.5); return
            if not self.mapa.tem_linha_de_visao(self.x, self.y, alvo.pos[0], alvo.pos[1]):
                print(f"❌ Uma parede bloqueia a magia em direção a {alvo.nome}!")
                time.sleep(1.5); return

            if sub == '2' and tem_almas:
                dano = poder + rolar_dado(6) + 4
                alvo.hp -= dano
                print(f"\n👻 Onda de Almas atinge {alvo.nome}: {dano} dano necrótico!")
                j.cooldown_magia = 4
            else:
                # Míssil Mágico — resistência mágica
                rolagem = rolar_dado(4) + 3
                dano = poder + rolagem
                res = getattr(alvo, 'resistencia_magica', 0.0)
                if res > 0 and random.random() < res:
                    revert = max(1, dano // 2)
                    alvo.hp -= (dano - revert)
                    print(f"\n✨ Míssil Mágico! {alvo.nome} resiste parcialmente: {dano - revert} dano.")
                else:
                    alvo.hp -= dano
                    print(f"\n✨ Míssil Mágico atinge {alvo.nome}: {dano} dano mágico!")
                j.cooldown_magia = 5

            alvo.alertado = True
            time.sleep(1)
            if alvo.esta_vivo():
                print(f"   ⚠️  {alvo.nome} foi atingido e avança furioso!")
                time.sleep(1)
                combate(j, alvo, inimigo_iniciou=False)
            else:
                print(f"   💀 {alvo.nome} foi destruído à distância!")
                _loot_inimigo(j, alvo)
                self.mapa.inimigos.remove(alvo)
            time.sleep(1)

        # ── 3 — Explosão Arcana AoE ───────────────────────────────────
        elif sub == '3':
            alvos_area = [
                i for i in inimigos_vivos
                if abs(self.x - i.pos[0]) + abs(self.y - i.pos[1]) <= 2
                and self.mapa.tem_linha_de_visao(self.x, self.y, i.pos[0], i.pos[1])
            ]
            if not alvos_area:
                print("Nenhum inimigo em range 2 para Explosão Arcana.")
                time.sleep(1); return
            dano_base = poder + rolar_dado(8) + 2
            print(f"\n💥 EXPLOSÃO ARCANA — atinge {len(alvos_area)} inimigo(s)!")
            time.sleep(0.5)
            sobreviventes = []
            for alvo in alvos_area:
                dano = max(1, dano_base - random.randint(0, 3))
                res = getattr(alvo, 'resistencia_magica', 0.0)
                if res > 0 and random.random() < res:
                    dano = max(1, dano // 2)
                    print(f"   🛡️ {alvo.nome} resiste: {dano} dano.")
                else:
                    print(f"   🔥 {alvo.nome}: {dano} dano!")
                alvo.hp -= dano
                alvo.alertado = True
                if alvo.esta_vivo():
                    sobreviventes.append(alvo)
                else:
                    print(f"   💀 {alvo.nome} destruído!")
                    _loot_inimigo(j, alvo)
            self.mapa.inimigos = [i for i in self.mapa.inimigos if i.esta_vivo()]
            j.cooldown_magia = 6
            time.sleep(1)
            if sobreviventes:
                print(f"\n   ⚠️  {len(sobreviventes)} inimigo(s) sobreviveram e avançam!")
                time.sleep(1)
                for alvo in sobreviventes:
                    if alvo.esta_vivo() and j.esta_vivo():
                        combate(j, alvo, inimigo_iniciou=True)

        # ── 4 — Cura (Mago Azul) ou Drenar Vida (Mago Negro) ─────────
        elif sub == '4':
            if subclasse == 'Mago Azul':
                cura = 10 + poder // 2 + rolar_dado(6)
                j.hp = min(j.hp + cura, j.hp_max)
                print(f"\n💙 TOQUE DE CURA! +{cura} HP recuperados.")
                j.cooldown_magia = 3
                time.sleep(1.5)
            elif subclasse == 'Mago Negro' and inimigos_vivos:
                print("\n  Escolha o alvo para Drenar Vida:")
                for idx, ini in enumerate(inimigos_vivos, 1):
                    dist = abs(self.x - ini.pos[0]) + abs(self.y - ini.pos[1])
                    tem_los = self.mapa.tem_linha_de_visao(self.x, self.y, ini.pos[0], ini.pos[1])
                    bloq = "  ▓ bloqueado" if not tem_los else ""
                    print(f"  {idx}. {ini.nome} (dist {dist}{bloq})")
                sel = input("  Alvo (0=cancelar): ").strip()
                try:
                    alvo = inimigos_vivos[int(sel) - 1]
                except (ValueError, IndexError):
                    return
                if abs(self.x - alvo.pos[0]) + abs(self.y - alvo.pos[1]) > 3:
                    print("❌ Fora do alcance!"); time.sleep(1); return
                if not self.mapa.tem_linha_de_visao(self.x, self.y, alvo.pos[0], alvo.pos[1]):
                    print("❌ Uma parede bloqueia o fluxo vital!"); time.sleep(1.5); return
                dano = poder + rolar_dado(8) + 2
                alvo.hp -= dano
                roubado = dano // 2
                j.hp = min(j.hp + roubado, j.hp_max)
                alvo.alertado = True
                print(f"\n💀 DRENAR VIDA! {dano} dano em {alvo.nome}, +{roubado} HP para você!")
                j.cooldown_magia = 4
                time.sleep(1)
                if alvo.esta_vivo():
                    combate(j, alvo, inimigo_iniciou=False)
                else:
                    print(f"   💀 {alvo.nome} sucumbiu!")
                    _loot_inimigo(j, alvo)
                    self.mapa.inimigos.remove(alvo)

        # ── 5 — Colapso (paralisa) ────────────────────────────────────
        elif sub == '5' and tem_colaps and inimigos_vivos:
            print("\n  Inimigos para Colapso:")
            for idx, ini in enumerate(inimigos_vivos, 1):
                dist = abs(self.x - ini.pos[0]) + abs(self.y - ini.pos[1])
                tem_los = self.mapa.tem_linha_de_visao(self.x, self.y, ini.pos[0], ini.pos[1])
                bloq = "  ▓ bloqueado" if not tem_los else ""
                print(f"  {idx}. {ini.nome} (dist {dist}{bloq})")
            sel = input("  Alvo (0=cancelar): ").strip()
            try:
                alvo = inimigos_vivos[int(sel) - 1]
            except (ValueError, IndexError):
                return
            if abs(self.x - alvo.pos[0]) + abs(self.y - alvo.pos[1]) > 3:
                print("❌ Fora do alcance!"); time.sleep(1); return
            if not self.mapa.tem_linha_de_visao(self.x, self.y, alvo.pos[0], alvo.pos[1]):
                print("❌ Uma parede fragmenta o colapso antes de atingir o alvo!"); time.sleep(1.5); return
            alvo.efeitos_ativos['paralisado'] = {'dano': 0, 'turnos': 2}
            alvo.alertado = True
            print(f"\n🌀 COLAPSO! {alvo.nome} está paralisado por 2 turnos!")
            j.cooldown_magia = 5
            time.sleep(2)

    # ─────────────────────────────────────────────────────
    # ARCO NA EXPLORAÇÃO [b] — disparo à distância range 3
    # ─────────────────────────────────────────────────────
    def _usar_arco_explorar(self):
        """
        Disparo de arco fora do combate.
        - Auto-equipa Arco Élfico do inventário se não estiver equipado.
        - Requer flechas disponíveis.
        - Range 3 (Manhattan) com linha de visão livre (sem parede entre jogador e alvo).
        - Inimigo atingido fica ALERTADO; se sobreviver entra em combate.
        - Arco Élfico: 25% disparo duplo (gasta 2 flechas).
        - Ao acabar flechas o arco é desequipado automaticamente.
        """
        j = self.jogador
        tem_arco = j.arma and j.arma['nome'] in ('Arco Élfico', 'Arco da Ruína')

        # ── Reequipar arco já em equipados (mas arma ativa é outra) ──
        if not tem_arco:
            arco_eq = next((eq for eq in j.equipados if eq.startswith('Arco Élfico') or eq.startswith('Arco da Ruína')), None)
            if arco_eq:
                bonus = int(arco_eq.split('+')[1]) if '+' in arco_eq else 1
                nome_arco_real = 'Arco da Ruína' if arco_eq.startswith('Arco da Ruína') else 'Arco Élfico'
                b = max(1, bonus - 1) if nome_arco_real == 'Arco da Ruína' else bonus
                j.arma = {'nome': nome_arco_real, 'bonus': b, 'dano': b}
                j.atualizar_atributos_equipamento()
                tem_arco = True
                print(f"🏹 {nome_arco_real} reativado como arma principal.")
                time.sleep(0.8)

        # ── Equip se arco está na bolsa mas não foi equipado ainda ───
        if not tem_arco:
            arco_inv = next((it for it in j.inventario if it.startswith('Arco Élfico') or it.startswith('Arco da Ruína')), None)
            if arco_inv:
                bonus = int(arco_inv.split('+')[1]) if '+' in arco_inv else 1
                nome_arco_real = 'Arco da Ruína' if arco_inv.startswith('Arco da Ruína') else 'Arco Élfico'
                b = max(1, bonus - 1) if nome_arco_real == 'Arco da Ruína' else bonus
                j.arma = {'nome': nome_arco_real, 'bonus': b, 'dano': b}
                j.inventario.remove(arco_inv)
                j.equipados.append(arco_inv)
                j.atualizar_atributos_equipamento()
                tem_arco = True
                print(f"🏹 {nome_arco_real} equipado automaticamente.")
                time.sleep(0.8)
            else:
                print("🏹 Você não tem nenhum Arco equipado.")
                time.sleep(1); return

        flechas = getattr(j, 'flechas', 0)
        if flechas <= 0:
            print("🏹 Sem flechas! O Arco é desequipado.")
            nome_arco = next((eq for eq in j.equipados if 'Arco Élfico' in eq or 'Arco da Ruína' in eq), None)
            if nome_arco:
                j.equipados.remove(nome_arco)
                j.inventario.append(nome_arco)
            j.arma = None
            j.atualizar_atributos_equipamento()
            time.sleep(1.5); return

        inimigos_vivos = [i for i in self.mapa.inimigos if i.esta_vivo()]
        if not inimigos_vivos:
            print("🏹 Nenhum inimigo para mirar.")
            time.sleep(1); return

        # ── Calcular células visíveis para filtrar alvos ───────────────
        vision_range = 1
        if 'Tocha Suja' in getattr(j, 'equipados', []):
            vision_range = 2
        if getattr(j, 'lanterna_espiritual', 0) > 0:
            vision_range = 2
        celulas_visiveis = self.mapa._calc_visivel((self.x, self.y), vision_range)

        limpar_tela()
        self._mostrar_hud()
        print(f"\n🏹 ARCO ÉLFICO — {flechas} flechas disponíveis")
        print("   Inimigos detectados:")

        alvos_validos = []
        for ini in inimigos_vivos:
            ix, iy = ini.pos
            dist = abs(self.x - ix) + abs(self.y - iy)
            visivel = ini.pos in celulas_visiveis
            tem_los = visivel and self.mapa.tem_linha_de_visao(self.x, self.y, ix, iy)
            if dist <= 3 and tem_los:
                marcador = "✓"
                alvos_validos.append(ini)
            elif not visivel:
                continue   # fora da luz — não revela posição
            elif dist <= 3 and not tem_los:
                marcador = "▓"
            else:
                marcador = "✗"
            bloqueio = "  — parede bloqueia" if dist <= 3 and not tem_los else ""
            fora = "  — fora do alcance" if dist > 3 else ""
            print(f"  {marcador} {ini.nome}  HP:{ini.hp}  (dist {dist}{bloqueio}{fora})")

        if not alvos_validos:
            print("   Nenhum inimigo em range 3 com linha de visão livre.")
            time.sleep(1.5); return

        print()
        for idx, ini in enumerate(alvos_validos, 1):
            print(f"  {idx}. {ini.nome}")
        print("  0. Cancelar")
        sel = input("  Alvo: ").strip()

        if sel == '0' or sel == '':
            return
        try:
            idx_sel = int(sel) - 1
            if idx_sel < 0 or idx_sel >= len(alvos_validos):
                return
            alvo = alvos_validos[idx_sel]
        except (ValueError, IndexError):
            return

        # ── Resolução do disparo ──────────────────────────────────────
        bonus = j.arma.get('bonus', 1)
        dano_base = rolar_dado(4) + bonus   # arco: d4 (projétil, não impacto direto)
        rolagem = rolar_dado(20) + j.ataque_bonus
        flechas_usadas = 0
        print()
        if rolagem >= alvo.ac or rolagem == 20:
            critico = (rolagem == 20)
            dano = dano_base * 2 if critico else dano_base
            alvo.hp -= dano
            j.flechas = max(0, j.flechas - 1)
            flechas_usadas += 1
            alvo.flechas_cravadas = getattr(alvo, 'flechas_cravadas', 0) + 1
            if critico:
                print(f"🏹 ACERTO CRÍTICO! Flecha crava em {alvo.nome}: {dano} dano!")
            else:
                print(f"🏹 Flecha acerta {alvo.nome}: {dano} dano!")

            # Disparo duplo — 25% Arco Élfico, 15% Arco da Ruína
            chance_duplo = 0.15 if j.arma['nome'] == 'Arco da Ruína' else 0.25
            if j.flechas > 0 and random.random() < chance_duplo:
                dano2 = rolar_dado(4) + bonus
                alvo.hp -= dano2
                j.flechas = max(0, j.flechas - 1)
                flechas_usadas += 1
                alvo.flechas_cravadas = getattr(alvo, 'flechas_cravadas', 0) + 1
                label = "💀 DISPARO DUPLO (Ruína)!" if j.arma['nome'] == 'Arco da Ruína' else "🏹 DISPARO DUPLO!"
                print(f"{label} Segunda flecha: {dano2} dano adicional!")
        else:
            print(f"🏹 Flecha passa longe de {alvo.nome}! (rolagem {rolagem} vs CA {alvo.ac})")
            j.flechas = max(0, j.flechas - 1)
            flechas_usadas += 1
            # Flecha perdida — não cravar

        # ── Reação do inimigo ─────────────────────────────────────────
        alvo.alertado = True
        time.sleep(1.2)

        if j.flechas == 0:
            print("   ⚠️  Flechas esgotadas! Arco desequipado automaticamente.")
            nome_arco = next((eq for eq in j.equipados if 'Arco Élfico' in eq or 'Arco da Ruína' in eq), None)
            if nome_arco:
                j.equipados.remove(nome_arco)
                j.inventario.append(nome_arco)
            j.arma = None
            j.atualizar_atributos_equipamento()
            time.sleep(1)
        else:
            print(f"   🏹 Flechas restantes: {j.flechas}")

        if alvo.esta_vivo():
            reacoes = [
                f"⚠️  {alvo.nome} ruge de dor e avança em fúria!",
                f"⚠️  {alvo.nome} detecta a origem da flecha e carga!",
                f"⚠️  {alvo.nome} é atingido — e não parece satisfeito.",
                f"⚠️  O grito de {alvo.nome} ecoa pelo corredor — ele vem!",
            ]
            print(random.choice(reacoes))
            time.sleep(1.5)
            combate(j, alvo, inimigo_iniciou=False)
        else:
            print(f"   💀 {alvo.nome} foi abatido à distância!")
            _loot_inimigo(j, alvo)
            self.mapa.inimigos.remove(alvo)
            time.sleep(1)

    def _processar_movimento(self, cmd):
        # ── Decrementar Lanterna Espiritual por movimento ────────────
        j = self.jogador
        if getattr(j, 'lanterna_espiritual', 0) > 0:
            j.lanterna_espiritual -= 1
            if j.lanterna_espiritual == 0:
                print("🕯️  A Lanterna Espiritual se apaga. A escuridão retorna.")
                import time as _t; _t.sleep(1.5)
            elif j.lanterna_espiritual <= 3:
                print(f"🕯️  A luz arcana vacila... ({j.lanterna_espiritual} movimentos restantes)")

        dx, dy = DIR_MAP[cmd]
        nx, ny = self.x + dx, self.y + dy

        # Movimento dentro da grade 4x4 atual
        if 0 <= nx < self.mapa.largura and 0 <= ny < self.mapa.altura:
            self._mover_dentro_sala(nx, ny)
        else:
            # Saiu da borda do mapa 4x4 — tenta mudar de sala ou região
            self._mover_entre_salas(dx, dy)

    def _mover_dentro_sala(self, nx, ny):
        """Movimento dentro da sala 4x4 atual."""

        # Porta
        if (nx, ny) in self.mapa.portas:
            if self.mapa.portas[(nx, ny)]:
                if 'chave' in self.jogador.inventario:
                    usar = input("🔐 Porta trancada! Usar chave? (s/n) ").lower()
                    if usar == 's':
                        self.jogador.inventario.remove('chave')
                        self.mapa.portas[(nx, ny)] = False
                        print("✅ Porta destrancada.")
                        time.sleep(1)
                        self.x, self.y = nx, ny
                        self.jogador.pos = (self.x, self.y)
                else:
                    print("🔒 Porta trancada! Você precisa de uma chave para abri-la.")
                    time.sleep(1.5)
            else:
                print("🚪 Você atravessa a porta.")
                self.x, self.y = nx, ny
                self.jogador.pos = (self.x, self.y)
            return

        # Parede
        if self.mapa.matriz[ny][nx] == '#':
            # Sistema de passagem secreta: 3 tentativas → 5% de abrir
            chave_parede = (nx, ny)
            self.mapa.contagem_parede[chave_parede] = self.mapa.contagem_parede.get(chave_parede, 0) + 1
            count = self.mapa.contagem_parede[chave_parede]
            if count >= 3 and random.random() < 0.05:
                self.mapa.matriz[ny][nx] = '.'
                print(wall)
                print("🌑 A pedra range... cede... DESMORONA silenciosamente.")
                time.sleep(1)
                print("   Uma passagem secreta se abre diante de você.")
                time.sleep(1.5)
                self.x, self.y = nx, ny
                self.jogador.pos = (self.x, self.y)
                self._verificar_celula()
                return
            print(wall)
            if count == 2:
                print("🚫 Parede sólida. Mas ela parece... levemente instável.")
            elif count >= 3:
                print("🚫 Parede sólida. Cada batida ressoa de forma estranha.")
            else:
                print("🚫 Parede! Procure outra rota.")
            time.sleep(1)
            return

        # Movimento livre
        self.x, self.y = nx, ny
        self.jogador.pos = (self.x, self.y)
        self._verificar_celula()

    def _mover_entre_salas(self, dx, dy):
        """Tenta mover para sala adjacente — em região (andar 1) ou AndarLabirinto (andar 2+)."""
        dir_key = (dx, dy)

        # ── Andar profundo (AndarLabirinto) ───────────────────────────
        if self.em_andar_profundo:
            andar_obj = self.andares.get(self.andar)
            if andar_obj is None:
                return
            nova_sala = (self.sala_no_andar[0] + dx, self.sala_no_andar[1] + dy)
            if andar_obj.tem_sala(nova_sala):
                dir_nome = NOME_DIRECAO.get(dir_key, '?')
                chave_v = ('andar', self.andar, nova_sala)
                ja_visitada = chave_v in self.salas_visitadas
                if ja_visitada:
                    msgs = [
                        "🌫️  Estas pedras parecem as mesmas. Mas o labirinto nunca é o mesmo.",
                        "👁️  Você já esteve aqui — ou algo muito parecido.",
                        "🕯️  A sombra da tocha projeta figuras diferentes desta vez.",
                    ]
                    print(f"🚶 Você retorna para {dir_nome}...")
                    time.sleep(0.6)
                    if random.random() < 0.45:
                        print(random.choice(msgs))
                        time.sleep(1.2)
                else:
                    print(f"🚶 Você avança para {dir_nome}...")
                    time.sleep(1)
                novo_mapa = andar_obj.sala(nova_sala)
                if novo_mapa is None:
                    print("🚫 O corredor desmorona — passage bloqueada.")
                    time.sleep(1)
                    return
                self.sala_no_andar = nova_sala
                self.salas_visitadas.add(chave_v)
                self.mapa = novo_mapa
                self.x, self.y = self._spawn_borda_oposta(dx, dy)
                self.jogador.pos = (self.x, self.y)
            else:
                print(wall)
                print("🚫 Pedra sólida. Este corredor não existe.")
                time.sleep(1)
            return

        # ── Nível superficial (andar 1) ───────────────────────────────

        # Caso 1: No hub — entra em uma região
        if self.regiao_atual_key is None:
            if dir_key in self.regioes:
                regiao = self.regioes[dir_key]
                dir_nome = NOME_DIRECAO[dir_key]
                print(avanca_dungeon(dungeon, dungeon2, dungeon3, lost_garden))
                print(f"🧭 Você adentra a Região {dir_nome}: {regiao.nome}")
                time.sleep(2)
                self.regiao_atual_key = dir_key
                self.sala_pos = (0, 0)
                self.dir_entrada = dir_key
                self.mapa = regiao.sala((0, 0))
                self._registrar_visita(dir_key, (0, 0))
                self._atualizar_dificuldade_regiao()
                self.x, self.y = self._spawn_borda_oposta(dx, dy)
                self.jogador.pos = (self.x, self.y)
            else:
                print(wall)
                print("🚫 Parede! Não há passagem nesta direção.")
            return

        # Caso 2: Em uma região
        regiao = self.regioes[self.regiao_atual_key]
        nova_sala = (self.sala_pos[0] + dx, self.sala_pos[1] + dy)

        # Voltar para o hub
        if self.sala_pos == (0, 0) and dir_key == DIR_OPOSTA.get(self.dir_entrada):
            msgs_hub = [
                "🏠 Você retorna ao Hub Central. As marcas que deixou nas paredes ainda estão lá.",
                "🏠 O Hub Central. Familiar, estático — um ponto fixo num labirinto que respira.",
                "🏠 De volta ao centro. A tocha do hub queima como você a deixou.",
            ]
            print(random.choice(msgs_hub))
            time.sleep(1)
            self.regiao_atual_key = None
            self.dir_entrada = None
            self.sala_pos = (0, 0)
            self.mapa = self._mapa_hub
            self.x, self.y = self._spawn_borda_oposta(dx, dy)
            self.jogador.pos = (self.x, self.y)
            return

        # Ir para sala adjacente na região
        if regiao.tem_sala(nova_sala):
            dir_nome = NOME_DIRECAO.get(dir_key, '?')
            chave_nova_sala = (str(self.regiao_atual_key), nova_sala)
            ja_visitada = chave_nova_sala in self.salas_visitadas
            if ja_visitada:
                msgs_labirinto_vivo = [
                    "🌫️  O corredor parece diferente. Mas as marcas que você deixou ainda estão lá.",
                    "👁️  As paredes parecem ter se movido. Ou talvez seja sua imaginação.",
                    "🕯️  A tocha projeta sombras diferentes. O labirinto respira enquanto você não olha.",
                    "🩸 Você reconhece este lugar — mas algo foi deslocado. A masmorra tem memória própria.",
                    "🌀 A sala parece a mesma. Parece.",
                ]
                print(f"🚶 Você retorna para {dir_nome}...")
                time.sleep(0.6)
                if random.random() < 0.45:
                    print(random.choice(msgs_labirinto_vivo))
                    time.sleep(1.5)
            else:
                print(f"🚶 Você segue para {dir_nome}...")
                time.sleep(1)
            self.sala_pos = nova_sala
            self.mapa = regiao.sala(nova_sala)
            self._registrar_visita(self.regiao_atual_key, nova_sala)
            self._atualizar_dificuldade_regiao()
            self.x, self.y = self._spawn_borda_oposta(dx, dy)
            self.jogador.pos = (self.x, self.y)
        else:
            print(wall)
            print("🚫 Sem passagem! Este caminho está bloqueado. Procure outra rota ou escadaria.")
            time.sleep(1)

    def _spawn_borda_oposta(self, dx, dy):
        """
        Spawn na borda OPOSTA à direção de movimento.
        Escaneia da borda para o centro, linha por linha, até achar célula livre.
        """
        if self.mapa is None:
            return 1, 1
        W, H = self.mapa.largura, self.mapa.altura
        m = self.mapa.matriz

        if dx == 1:       # moveu Leste → entra pelo Oeste
            for x in range(W):
                cands = [(x, y) for y in range(H) if m[y][x] == '.']
                if cands:
                    return random.choice(cands)
        elif dx == -1:    # moveu Oeste → entra pelo Leste
            for x in range(W - 1, -1, -1):
                cands = [(x, y) for y in range(H) if m[y][x] == '.']
                if cands:
                    return random.choice(cands)
        elif dy == 1:     # moveu Sul → entra pelo Norte
            for y in range(H):
                cands = [(x, y) for x in range(W) if m[y][x] == '.']
                if cands:
                    return random.choice(cands)
        elif dy == -1:    # moveu Norte → entra pelo Sul
            for y in range(H - 1, -1, -1):
                cands = [(x, y) for x in range(W) if m[y][x] == '.']
                if cands:
                    return random.choice(cands)

        # Fallback completo — qualquer célula livre
        return self._spawn_em_mapa(self.mapa)

    def _atualizar_dificuldade_regiao(self):
        """Regenera o mapa da sala com dificuldade atualizada se necessário."""
        dif = self._dificuldade_atual()
        # Atualiza o mapa atual da sala com nova dificuldade
        regiao = self.regioes.get(self.regiao_atual_key)
        if regiao and self.sala_pos in regiao.salas:
            sala_atual = regiao.salas[self.sala_pos]
            # Apenas regenera se não foi visitada antes (mantém estado se já explorada)
            chave = (str(self.regiao_atual_key), self.sala_pos)
            if sala_atual is None:
                novo_mapa = Mapa(dificuldade=dif, extrema=self.modo_extremo)
                regiao.salas[self.sala_pos] = novo_mapa
                self.mapa = novo_mapa
                self._tentar_colocar_diario(novo_mapa)

    def _tentar_colocar_diario(self, mapa):
        """Coloca um Diário Perdido aleatoriamente em mapa se ainda há exemplares não colocados."""
        diarios_restantes = len(self._diarios_por_sessao) - getattr(self, '_diarios_colocados', 0)
        if diarios_restantes <= 0:
            return
        # Probabilidade decresce conforme menos restam; garante que todos sejam colocados
        # Colocamos sempre com 40% de chance por sala, mas após certas salas força colocação
        salas_exploradas = self.nivel
        diarios_colocados = getattr(self, '_diarios_colocados', 0)
        # Forçar colocação se ficaram poucos (evitar perder diários por não aparecerem)
        forcar = (salas_exploradas >= 8 + diarios_colocados * 5 and diarios_restantes > 0)
        if forcar or random.random() < 0.40:
            livres = [(x, y)
                      for y in range(1, mapa.altura - 1)
                      for x in range(1, mapa.largura - 1)
                      if mapa.matriz[y][x] == '.' and (x, y) not in mapa.itens]
            if livres:
                px, py = random.choice(livres)
                mapa.itens[(px, py)] = 'Diário Perdido'
                self._diarios_colocados = getattr(self, '_diarios_colocados', 0) + 1

    def _usar_runa_limiar(self):
        """Runa do Limiar: teletransporta de volta ao hub central."""
        j = self.jogador
        if 'Runa do Limiar' not in j.inventario:
            print("❌ Você não possui a Runa do Limiar.")
            time.sleep(1)
            return
        print("\n🌀 RUNA DO LIMIAR")
        print("   Uma fissura no espaço abre diante de vós...")
        time.sleep(1)
        print("   O Limiar chama. Desejais retornar ao hub central?")
        r = input("   (s/n): ").lower().strip()
        if r != 's':
            print("   Cancelado. A runa permanece intacta.")
            time.sleep(0.8)
            return
        j.inventario.remove('Runa do Limiar')
        # Teleporta para hub
        self.em_andar_profundo = False
        self.regiao_atual_key = None
        self.mapa = self._mapa_hub
        self.x, self.y = self.spawn_jogador()
        self.andar = 1
        print("   ✨ A fissura vos engole. Em um instante, o hub central.")
        time.sleep(1.5)
        print("   Vós retornastes. A runa se desintegrou em pó cósmico.")
        time.sleep(1.5)

    def _usar_explosivo_explorar(self):
        """
        Uso do explosivo arremessável FORA do combate.
        O jogador aponta para uma célula adjacente; se for parede ou porta, detona.
        Se já for livre, pode acertar inimigo adjacente ou causar auto-dano.
        """
        j = self.jogador
        if 'explosivo arremessável' not in j.inventario:
            print("❌ Você não tem explosivo arremessável.")
            time.sleep(1)
            return

        print("\n💣 EXPLOSIVO ARREMESSÁVEL")
        print("   Para onde deseja arremessá-lo?")
        print("   w = Norte | s = Sul | a = Oeste | d = Leste | c = cancelar")
        dir_cmd = input("   >> ").lower().strip()

        if dir_cmd == 'c' or dir_cmd not in DIR_MAP:
            print("   ↩️  Cancelado. O explosivo permanece na bolsa.")
            time.sleep(0.8)
            return

        dx, dy = DIR_MAP[dir_cmd]
        tx, ty = self.x + dx, self.y + dy

        # Fora dos limites
        if not (0 <= tx < self.mapa.largura and 0 <= ty < self.mapa.altura):
            print("   💨 O explosivo voa para além dos limites da sala e explode longe.")
            time.sleep(1)
            j.inventario.remove('explosivo arremessável')
            return

        j.inventario.remove('explosivo arremessável')

        if self.mapa.matriz[ty][tx] == '#':
            # Detonação bem-sucedida de parede
            print("   💥 KABOOM!")
            time.sleep(0.5)
            print("   A parede range, racha e desmorona em poeira e pedregulhos.")
            time.sleep(1.5)
            self.mapa.matriz[ty][tx] = '.'
            self.mapa.contagem_parede.pop((tx, ty), None)
            # Chance de auto-dano por estilhaços (25%)
            if random.random() < 0.25:
                dano = rolar_dado(4)
                j.hp = max(1, j.hp - dano)
                print(f"   🪨 Estilhaços te atingem! -{dano} HP.")
            else:
                print("   ✅ Passagem aberta. Você se abriga a tempo dos estilhaços.")
            time.sleep(1.5)

        elif (tx, ty) in self.mapa.portas:
            # Detonação de porta (trancada ou não)
            estava_trancada = self.mapa.portas[(tx, ty)]
            del self.mapa.portas[(tx, ty)]
            print("   💥 KABOOM!")
            time.sleep(0.5)
            if estava_trancada:
                print("   A porta trancada voa pelos ares em mil lascas fumegantes.")
            else:
                print("   A porta range, despedaça-se e o corredor se abre à força.")
            time.sleep(1.5)
            # Sempre algum auto-dano por estilhaços de madeira/ferro
            dano = rolar_dado(3)
            j.hp = max(1, j.hp - dano)
            print(f"   🪚 Estilhaços de madeira e metal te arranham: -{dano} HP.")
            time.sleep(1.5)
        else:
            # Já era livre ou tem inimigo — acidente parcial
            inimigo_no_local = next((i for i in self.mapa.inimigos if i.pos == (tx, ty) and i.esta_vivo()), None)
            if inimigo_no_local:
                print("   💥 KABOOM! O explosivo acerta um inimigo diretamente!")
                time.sleep(1)
                dano_ini = rolar_dado(12) + 4
                dano_self = rolar_dado(6)
                inimigo_no_local.hp -= dano_ini
                j.hp = max(1, j.hp - dano_self)
                print(f"   🔥 {inimigo_no_local.nome} recebe {dano_ini} de dano!")
                print(f"   🪨 A explosão também te atinge: -{dano_self} HP.")
                if not inimigo_no_local.esta_vivo():
                    print(f"   💀 {inimigo_no_local.nome} foi destruído pela explosão!")
                time.sleep(2)
            else:
                print("   💥 O explosivo estoura no ar vazio...")
                dano_self = rolar_dado(4)
                j.hp = max(1, j.hp - dano_self)
                print(f"   🪨 Você ainda leva {dano_self} HP de dano por descuido.")
                time.sleep(1.5)

    def _usar_portal_explorar(self):
        """
        Grimório Portal fora do combate.
        O Mago escolhe uma parede adjacente e se teletransporta para o outro lado.
        Mesma lógica de Personagem._usar_portal, mas usando posição real do jogo.
        """
        j = self.jogador
        if j.classe != 'Mago':
            print("❌ Apenas magos dominam o Grimório Portal.")
            time.sleep(1)
            return
        if not any('Grimório Portal' in eq for eq in j.equipados):
            print("❌ Você não tem o Grimório Portal equipado.")
            time.sleep(1)
            return
        if j.cooldown_magia > 0:
            print(f"❌ Portal em recarga! ({j.cooldown_magia} turnos restantes)")
            time.sleep(1)
            return

        print("\n🌀 GRIMÓRIO PORTAL — Exploração")
        print("   Escolha a direção da parede a atravessar:")
        print("   w = Norte | s = Sul | a = Oeste | d = Leste | c = cancelar")
        dir_cmd = input("   >> ").lower().strip()

        if dir_cmd == 'c' or dir_cmd not in DIR_MAP:
            print("   ↩️  Cancelado.")
            time.sleep(0.8)
            return

        dx, dy = DIR_MAP[dir_cmd]
        tx, ty = self.x + dx, self.y + dy   # parede alvo
        bx, by = tx + dx, ty + dy           # célula do outro lado
        W, H = self.mapa.largura, self.mapa.altura

        if not (0 <= tx < W and 0 <= ty < H):
            print("   Não há parede nessa direção — apenas o vazio além dos limites.")
            time.sleep(1)
            return

        if self.mapa.matriz[ty][tx] != '#':
            print("   Não há parede nessa direção para o portal atravessar.")
            j.cooldown_magia = 2
            time.sleep(1)
            return

        if not (0 <= bx < W and 0 <= by < H) or self.mapa.matriz[by][bx] != '.':
            print("   O outro lado da parede está bloqueado. O portal colapsa sem efeito.")
            j.cooldown_magia = 2
            time.sleep(1)
            return

        print("   ✨ Uma fenda violeta rasga a pedra...")
        time.sleep(1)
        print("   Você atravessa a parede em um lampejo de luz arcana.")
        time.sleep(1.2)
        self.x, self.y = bx, by
        j.pos = (bx, by)
        j.cooldown_magia = 6
        print(f"   🌀 Portal bem-sucedido! Nova posição: ({bx}, {by}).")
        time.sleep(1)
        self._verificar_celula()

    def _verificar_celula(self):
        """Verifica eventos na célula atual (itens, inimigos, escadas, estruturas)."""
        x, y = self.x, self.y

        # ── Item no chão ──
        if (x, y) in self.mapa.itens:
            item = self.mapa.itens[(x, y)]

            # Flechas avulsas — converter direto ao estoque com escolha de qtd
            if item.startswith('Flechas'):
                qtd_item = 20 if '20' in item else 10
                print(f"\n🎁 Você vê no chão: {item}")
                time.sleep(0.5)
                print(f"   {descricao_item(item)}")
                peso_unit = 0.05
                espaco = self.jogador.capacidade_peso - self.jogador.peso_atual
                max_peso = int(espaco / peso_unit)
                max_col = min(qtd_item, max_peso)
                if max_col <= 0:
                    print(f"   ⚠️  Sem espaço para mais flechas (carga cheia).")
                    time.sleep(1.5)
                else:
                    print(f"   Coletar quantas? (1–{max_col}, ENTER=todas, 0=nenhuma): ", end='', flush=True)
                    entrada = input().strip()
                    if entrada == '0':
                        print("   ↩️  Flechas deixadas.")
                        time.sleep(0.8)
                    else:
                        try:
                            qtd = max(0, min(int(entrada), max_col)) if entrada else max_col
                        except ValueError:
                            qtd = max_col
                        if qtd > 0:
                            self.mapa.itens.pop((x, y))
                            self.jogador.flechas = getattr(self.jogador, 'flechas', 0) + qtd
                            sobra = qtd_item - qtd
                            if sobra > 0:
                                # Deixar o restante no chão como novo item
                                nome_resto = f'Flechas ({sobra})' if sobra not in (10, 20) else f'Flechas ({sobra})'
                                self.mapa.itens[(x, y)] = nome_resto
                            peso_ganho = round(qtd * peso_unit, 2)
                            print(f"   ✅ +{qtd} flechas ({peso_ganho}kg). Total: {self.jogador.flechas}.")
                            time.sleep(1)
                        else:
                            print("   ↩️  Flechas deixadas.")
                            time.sleep(0.8)
                return  # não processa como item normal

            peso = peso_item(item)
            print(f"\n🎁 Você vê no chão: {item}")
            time.sleep(0.5)
            print(f"   📖 {descricao_item(item)}")
            print(f"   ⚖️  Peso: {peso:.1f}kg  |  Carga atual: {self.jogador.peso_atual:.1f}/{self.jogador.capacidade_peso}kg")
            time.sleep(1)
            if not self.jogador.pode_carregar(item):
                print(f"   ⚠️  Mochila pesada demais! Não há espaço para mais {peso:.1f}kg.")
                print(f"      Abra [e] inventário e descarte algo primeiro.")
                time.sleep(2)
            else:
                r = input("   Pegar? (s/n): ").lower()
                if r == 's':
                    self.mapa.itens.pop((x, y))
                    self.jogador.inventario.append(item)
                    print(f"   ✅ {item} adicionado ao inventário.")
                    time.sleep(1)
                else:
                    print("   ↩️  Você deixou o item no chão.")
                    time.sleep(0.8)

        # Inimigo
        for inimigo in self.mapa.inimigos:
            if inimigo.pos == (x, y):
                if self.jogador.invisivel:
                    if isinstance(inimigo, OlhoDeVecna):
                        print("🧿 O Olho de Vecna dissipa sua invisibilidade!")
                        self.jogador.invisivel = False
                    else:
                        print("👻 Você passa despercebido graças à invisibilidade.")
                        continue

                # Botas do Silêncio
                chance_combate = 1.0
                bonus_evitar = 0.0
                if 'Botas do Silêncio' in self.jogador.equipados:
                    bonus_evitar += 0.60   # 60% de evitar combate ao pisar na célula
                if self.jogador.invisivel:
                    # invisível já tratado acima — não duplica
                    pass

                if bonus_evitar > 0 and random.random() < bonus_evitar:
                    print("👟 Seus passos não fazem barulho — você passa despercebido!")
                    break

                combate(self.jogador, inimigo)
                self.jogador._mapa_ref = self.mapa    # referência para portal mago
                self.mapa.inimigos = [i for i in self.mapa.inimigos if i.esta_vivo()]
                break

        # Escada final (chefe)
        if (x, y) == self.mapa.escada_final:
            limpar_tela()
            print(stairway)
            time.sleep(1)
            print("\n💀 Uma escadaria ancestral... impregnada com energia profana além da compreensão.")
            time.sleep(2)
            print("   A pedra vibra sob seus pés. Algo colossal respira lá embaixo.")
            time.sleep(2)
            resp = input("\n   Deseja descer e enfrentar o que aguarda? (s/n): ").lower().strip()
            if resp != 's':
                print("   Você hesita. A masmorra não te pressa — ela espera.")
                time.sleep(1.5)
                return
            print(vecna_sees_everything), time.sleep(4)
            print(vecna_meets), time.sleep(4)
            print(vecnas_eye), time.sleep(2)
            print("💀 O Olho de Vecna flutua no centro da sala, em sua forma mais pura!")
            dif_boss = self._dificuldade_atual()
            print(f"   [Dificuldade do chefe: {dif_boss}]")
            time.sleep(1)
            chefe_final = OlhoDeVecna((x, y), dificuldade=dif_boss)
            combate(self.jogador, chefe_final)
            if self.jogador.esta_vivo():
                print("\n🌟 Você derrotou o Olho de Vecna!"), time.sleep(3)
                print("🏆 A maldição se dissipa..."), time.sleep(3)
                print("🎉 Parabéns! Você venceu as Masmorras Liminares!"), time.sleep(3)
            else:
                print("\n💀 O Olho de Vecna consome sua alma..."), time.sleep(3)
            exit()

        # Escada normal — DESCIDA para AndarLabirinto
        elif (x, y) in self.mapa.escadas:
            if self.andar >= 43:
                print("🔒 Os degraus desmoronaram. Não há como descer mais.")
                time.sleep(2)
                return
            # Descreve e confirma
            limpar_tela()
            print(stairway)
            time.sleep(0.8)
            print(f"\n🕳️  {random.choice(DESCRICOES_ESCADAS_DESCIDA)}")
            time.sleep(2)
            print(f"   Profundidade atual: Andar {self.andar}  →  Andar {self.andar + 1}")
            time.sleep(1)
            resp = input("\n   Deseja descer? (s/n): ").lower().strip()
            if resp != 's':
                print("   Você recua. Pode ser uma boa decisão.")
                time.sleep(1.5)
                return

            msgs_descida = [
                "Os degraus desaparecem no escuro abaixo...",
                "O frio aumenta a cada degrau. Algo mais fundo aguarda.",
                "Suas botas ecoam pedra após pedra, descendo para onde a luz não alcança.",
                "A escada range sob seu peso, como se protestasse contra a descida.",
            ]
            print(f"\n🌀 {random.choice(msgs_descida)}")
            time.sleep(1.5)

            # Salvar contexto de retorno
            # Chave: (andar_destino, coord_origem) — única por escada específica
            # coord_origem inclui posição da escada para evitar colisão quando duas
            # escadas saem da mesma sala
            if self.em_andar_profundo:
                base = self.sala_no_andar
            elif self.regiao_atual_key is None:
                base = (0, 0)
            else:
                rx, ry = self.regiao_atual_key
                sx, sy = self.sala_pos
                base = (rx * 20 + sx, ry * 20 + sy)
            # Tornar coord única incorporando posição da escada no mapa
            coord_origem = (base[0] * 100 + x, base[1] * 100 + y)

            self.spawn_retorno[(self.andar + 1, coord_origem)] = {
                'profundo': self.em_andar_profundo,
                'regiao': self.regiao_atual_key,
                'sala': self.sala_pos,
                'andar_sala': self.sala_no_andar,
                'xy': (x, y),
            }

            self.andar += 1
            dif = self._dificuldade_atual()

            # Registrar coord como entrada do próximo andar
            if self.andar not in self.entradas_andares:
                self.entradas_andares[self.andar] = set()
            self.entradas_andares[self.andar].add(coord_origem)

            # Criar AndarLabirinto se ainda não existe
            if self.andar not in self.andares:
                entradas = self.entradas_andares[self.andar]
                self.andares[self.andar] = AndarLabirinto(
                    self.andar, dif, extrema=self.modo_extremo, entradas=entradas
                )
                print(f"   Você chega ao Andar {self.andar}: {self.andares[self.andar].nome}")
                time.sleep(1.5)
            else:
                # Andar já existe — garantir que a sala de entrada existe
                andar_existente = self.andares[self.andar]
                if coord_origem not in andar_existente.salas:
                    m_nova = Mapa(dificuldade=dif, extrema=self.modo_extremo)
                    m_nova.escadas = set()
                    m_nova.escada_final = None
                    sx2, sy2 = andar_existente._celula_livre(m_nova)
                    m_nova.escada_subir = (sx2, sy2)
                    m_nova.matriz[sy2][sx2] = '.'
                    andar_existente.salas[coord_origem] = m_nova
                    andar_existente.entradas.add(coord_origem)
                    mais_prox = min(
                        (p for p in andar_existente.salas if p != coord_origem),
                        key=lambda p: abs(p[0]-coord_origem[0]) + abs(p[1]-coord_origem[1]),
                        default=None
                    )
                    if mais_prox:
                        andar_existente.conexoes.setdefault(coord_origem, set()).add(mais_prox)
                        andar_existente.conexoes.setdefault(mais_prox, set()).add(coord_origem)
                print(f"   Você retorna ao Andar {self.andar}: {self.andares[self.andar].nome}")
                time.sleep(1.5)

            andar_obj = self.andares[self.andar]
            self.em_andar_profundo = True
            self.sala_no_andar = coord_origem
            self.mapa = andar_obj.sala(self.sala_no_andar)
            self.salas_visitadas.add(('andar', self.andar, self.sala_no_andar))
            # Pousar junto à escada de subida (para poder voltar facilmente)
            if self.mapa.escada_subir:
                self.x, self.y = self._spawn_junto_a(self.mapa, self.mapa.escada_subir)
            else:
                self.x, self.y = self._spawn_em_mapa(self.mapa)
            self.jogador.pos = (self.x, self.y)

        # Escada de SUBIDA — volta um nível
        elif (x, y) == self.mapa.escada_subir:
            if self.andar <= 1:
                print("🔒 Não há para onde subir. Você está no nível mais alto.")
                time.sleep(2)
                return
            # Descreve e confirma
            limpar_tela()
            print(stairway)
            time.sleep(0.8)
            print(f"\n🔼 {random.choice(DESCRICOES_ESCADAS_SUBIDA)}")
            time.sleep(1.5)
            print(f"   Você está no Andar {self.andar}  →  subindo para Andar {self.andar - 1}")
            time.sleep(1)
            resp = input("\n   Deseja subir? (s/n): ").lower().strip()
            if resp != 's':
                print("   Você permanece. O andar de cima pode esperar.")
                time.sleep(1.5)
                return

            msgs_subida = [
                "Seus músculos ardem subindo cada degrau. A luz acima parece menos hostil.",
                "O ar muda conforme você sobe — menos pesado, menos antigo.",
                "Os passos sobem pelo corredor de pedra. Você reconhece as marcas que deixou na parede.",
                "A escada range diferente subindo. Menos ameaçadora. Quase familiar.",
            ]
            print(f"\n{random.choice(msgs_subida)}")
            time.sleep(1.5)

            self.andar -= 1
            # A chave do retorno é (andar_de_onde_estamos, sala_atual)
            # antes do decremento o andar era self.andar+1
            retorno = self.spawn_retorno.get((self.andar + 1, self.sala_no_andar))

            if retorno and not retorno['profundo']:
                # Voltar à superfície (regiões do andar 1)
                self.em_andar_profundo = False
                self.regiao_atual_key = retorno['regiao']
                self.sala_pos = retorno['sala']
                if self.regiao_atual_key is not None:
                    self.mapa = self.regioes[self.regiao_atual_key].salas[self.sala_pos]
                else:
                    self.mapa = self._mapa_hub
                # Pousar junto à escada de descida original
                escada_orig = retorno['xy']
                self.x, self.y = self._spawn_junto_a(self.mapa, escada_orig)
            elif retorno and retorno['profundo']:
                # Voltar a um AndarLabirinto anterior
                andar_anterior = self.andares.get(self.andar)
                if andar_anterior:
                    self.sala_no_andar = retorno['andar_sala']
                    self.mapa = andar_anterior.sala(self.sala_no_andar)
                    escada_orig = retorno['xy']
                    if self.mapa:
                        self.x, self.y = self._spawn_junto_a(self.mapa, escada_orig)
                    else:
                        self.x, self.y = self._spawn_em_mapa(self.mapa)
                else:
                    self.em_andar_profundo = False
                    self.mapa = self._mapa_hub
                    self.x, self.y = self._spawn_em_mapa(self.mapa)
            else:
                # Fallback
                self.em_andar_profundo = self.andar > 1
                if self.em_andar_profundo and self.andar in self.andares:
                    andar_obj = self.andares[self.andar]
                    self.sala_no_andar = andar_obj.pos_entrada
                    self.mapa = andar_obj.sala(self.sala_no_andar)
                else:
                    self.em_andar_profundo = False
                    self.mapa = self._mapa_hub
                self.x, self.y = self._spawn_em_mapa(self.mapa)

            print(f"   Você está de volta ao Andar {self.andar}.")
            time.sleep(1.5)
            self.jogador.pos = (self.x, self.y)

        # Estruturas especiais
        elif (x, y) in self.mapa.estruturas:
            estrutura = self.mapa.estruturas[(x, y)]

            if estrutura.startswith("armadilha_"):
                # Armadilhas disparam sem confirmação
                tipo = estrutura.split('_')[1]
                dano = random.randint(1, 2)
                if tipo == 'gás venenoso':
                    print("☠️  Você ouve um chiado... Gás venenoso invade sua garganta!")
                    time.sleep(1.5)
                    dano_v = rolar_dado(3)
                    self.jogador.efeitos_ativos['veneno'] = {'dano': dano_v, 'turnos': 3}
                    print(f"   🐍 Envenenado! -{dano_v} HP por 3 turnos. Use um antídoto!")
                    time.sleep(2)
                elif tipo == 'espinhos':
                    print("⚠️  Espinhos emergem do chão com um estalo metálico!")
                    time.sleep(1)
                    self.jogador.hp = max(0, self.jogador.hp - dano)
                    print(f"   🩸 -{dano} HP! (HP restante: {self.jogador.hp}/{self.jogador.hp_max})")
                    time.sleep(1.5)
                elif tipo == 'flechas':
                    print("⚠️  Um mecanismo clica — flechas disparam das paredes!")
                    time.sleep(1)
                    self.jogador.hp = max(0, self.jogador.hp - dano)
                    print(f"   🏹 -{dano} HP! (HP restante: {self.jogador.hp}/{self.jogador.hp_max})")
                    time.sleep(1.5)
                else:
                    print(f"⚠️  Armadilha de {tipo} ativada!")
                    time.sleep(1)
                    self.jogador.hp = max(0, self.jogador.hp - dano)
                    print(f"   💥 -{dano} HP! (HP restante: {self.jogador.hp}/{self.jogador.hp_max})")
                    time.sleep(1.5)
                del self.mapa.estruturas[(x, y)]
                if not self.jogador.esta_vivo():
                    print("☠️  Você foi morto por uma armadilha!")
                    time.sleep(2)
            else:
                # ── Estrutura interativa: descrever + perguntar ──────
                limpar_tela()
                desc_est = DESCRICOES_ALTARES.get(estrutura, f"Uma {estrutura} estranha e imponente.")
                print(f"\n🔮 Você se depara com: {estrutura.upper()}")
                time.sleep(0.5)
                print(f"\n   {desc_est}")
                time.sleep(2)
                resp = input("\n   Deseja interagir? (s/n): ").lower().strip()
                if resp != 's':
                    print("   Você observa de longe e segue em frente.")
                    time.sleep(1.5)
                    # Estrutura permanece para futuras interações
                    return

                # ── Efeitos das estruturas ───────────────────────────
                if estrutura == 'altar antigo':
                    print(altar)
                    time.sleep(2)
                    print("🧎 Você ajoelha diante do altar e murmura uma oração esquecida...")
                    time.sleep(2)
                    self.jogador.altar_oracoes += 1
                    # Afinidade plena: sempre cura. Sem afinidade: chance crescente com orações
                    if self.jogador.afinidade_espiritual:
                        chance_cura = 1.0
                    else:
                        chance_cura = min(0.9, 0.25 + self.jogador.altar_oracoes * 0.15)
                    if random.random() < chance_cura:
                        cura = rolar_dado(6) + 4
                        self.jogador.hp = min(self.jogador.hp + cura, self.jogador.hp_max)
                        print(f"   ✨ Uma luz suave emana do altar. +{cura} HP recuperados!")
                        # Conversão gradual
                        if not self.jogador.afinidade_espiritual and self.jogador.altar_oracoes >= 5:
                            self.jogador.afinidade_espiritual = True
                            print("   🕯️  Algo muda em você. Os altares vos reconhecem agora.")
                    else:
                        restantes = max(0, 5 - self.jogador.altar_oracoes)
                        print(f"   🕯️  O altar ouve, mas não responde. ({self.jogador.altar_oracoes} oração/ões)")
                        if restantes > 0:
                            print(f"      Continue orando — {restantes} mais e algo pode mudar.")
                    time.sleep(2)

                elif estrutura == 'altar de sangue':
                    print("🩸 Você se aproxima. O altar pulsa mais forte.")
                    time.sleep(1.5)
                    if random.random() < 0.5:
                        cura = rolar_dado(8) + 6
                        self.jogador.hp = min(self.jogador.hp + cura, self.jogador.hp_max)
                        print(f"   🩸 O altar aceita sua devoção! +{cura} HP restaurados.")
                    else:
                        dano_ritual = rolar_dado(6)
                        self.jogador.hp = max(1, self.jogador.hp - dano_ritual)
                        print(f"   🩸 O altar drena sua força vital! -{dano_ritual} HP arrancados.")
                    time.sleep(2)

                elif estrutura == 'portal do vazio':
                    print("🌌 Você estende a mão. O portal te puxa com força súbita...")
                    time.sleep(1.5)
                    if self.em_andar_profundo and self.andar in self.andares:
                        andar_obj = self.andares[self.andar]
                        nova_sala = random.choice(list(andar_obj.salas.keys()))
                        self.sala_no_andar = nova_sala
                        self.salas_visitadas.add(('andar', self.andar, nova_sala))
                        self.mapa = andar_obj.sala(nova_sala)
                        self.x, self.y = self._spawn_em_mapa(self.mapa)
                        self.jogador.pos = (self.x, self.y)
                        print("   🌌 O portal te engole! Você emerge em outra câmara do andar.")
                    elif self.regiao_atual_key and len(self.regioes[self.regiao_atual_key].salas) > 1:
                        nova_sala = random.choice(list(self.regioes[self.regiao_atual_key].salas.keys()))
                        self.sala_pos = nova_sala
                        self.mapa = self.regioes[self.regiao_atual_key].sala(nova_sala)
                        self._registrar_visita(self.regiao_atual_key, nova_sala)
                        self.x, self.y = self.spawn_jogador()
                        self.jogador.pos = (self.x, self.y)
                        print("   🌌 O portal te engole! Você emerge em outra parte da região.")
                    else:
                        print("   🌌 O portal falha. Um cheiro de enxofre permanece no ar.")
                    time.sleep(2)

                elif estrutura == 'círculo mágico':
                    if self.jogador.classe == "Mago":
                        limpar_tela()
                        print(magic_circle), time.sleep(1)
                        limpar_tela()
                        print(magic_circle_blink), time.sleep(1)
                        limpar_tela()
                        print(magic_circle), time.sleep(1)
                        print("✨ As runas pulsam! Seus poderes arcanos são restaurados...")
                        time.sleep(1.5)
                        self.jogador.cooldown_magia = 0
                        self.jogador.ataque_bonus += 3
                        print("   🔮 Magia recarregada! +3 INT permanente.")
                        time.sleep(2)
                    else:
                        print(magic_circle)
                        print("❓ As runas pulsam estranhamente, mas você não compreende.")
                        time.sleep(2)

                elif estrutura == 'estátua enigmática':
                    print(statue)
                    time.sleep(1.5)
                    # Afinidade espiritual aumenta chance de drop
                    chance_drop = 0.7 if self.jogador.afinidade_espiritual else 0.35
                    if random.random() < chance_drop:
                        print("   A estátua dissolve-se em névoa. Um item materializa-se!")
                        time.sleep(2)
                        itens_estatua = ['poção de cura', 'chave', 'antídoto',
                                         'Escudo dos Condenados +2',
                                         'Adaga Envenenada +2',
                                         'Grimório das Almas +2']
                        item = random.choice(itens_estatua)
                        p = peso_item(item)
                        print(f"   🎁 {item} ({p:.1f}kg) aparece diante de você!")
                        time.sleep(1)
                        if self.jogador.pode_carregar(item):
                            r = input("   Pegar? (s/n): ").lower()
                            if r == 's':
                                self.jogador.inventario.append(item)
                                print(f"   ✅ {item} adicionado.")
                            else:
                                self.mapa.itens[(x, y)] = item
                                print("   ↩️  Deixado no chão.")
                        else:
                            self.mapa.itens[(x, y)] = item
                            print(f"   ⚠️  Pesado demais! Item deixado no chão.")
                        time.sleep(1.5)
                    else:
                        print("   A estátua observa em silêncio... e some.")
                        time.sleep(2)

                del self.mapa.estruturas[(x, y)]



# =====================================================================
# DIÁRIO PERDIDO — textos de lore (3 por sessão, distribuição aleatória)
# =====================================================================

DIARIO_ENTRADAS = [
    # Entrada 0
    (
        "⬛ DIÁRIO PERDIDO — Entrada I",
        """\
  O tinteiro está quase seco. Escrevo à luz de um fragmento de cristal
  que encontrei no segundo corredor — azul, pulsante, como se respirasse.

  Meu nome é Orvyn Tess. Cartógrafo. Cheguei ao Limiar seguindo mapas
  que ninguém deveria ter feito. Alguém mapeou este lugar antes de mim.
  A caligrafia nos corredores inferiores é velha demais para ser humana
  no tempo que imagino — e estranha o suficiente para me preocupar.

  Desci três andares. O quarto cheira a algo que não consigo nomear.
  Não é podridão. É anterior à podridão. É o cheiro do que existia
  antes das coisas começarem a apodrecer.

  Se alguém encontrar isto: sigam as marcas de giz azul. Elas levam
  ao lugar que chamei de Câmara do Eco. Não entrem de noite — embora
  "noite" aqui seja apenas uma questão de convenção interna.

                                          — O. Tess, Cartógrafo do Rei"""
    ),
    # Entrada 1
    (
        "⬛ DIÁRIO PERDIDO — Entrada II",
        """\
  Não sei quantos dias passaram. A pedra não envelhece aqui.

  Encontrei os restos de uma expedição anterior — seis pessoas, pelos
  pertences espalhados. Nenhum corpo. Apenas ossos que não pertencem
  a seis corpos. Mais. Muito mais.

  A criatura que chamo de Olho — ela os vê. Isso é o que mais assusta.
  Não é que ataque. É que vê. Completamente. Como se olhar já fosse
  uma forma de violência que apenas se torna física mais tarde.

  Aprendi que os altares aceitam sangue. Não muito — um corte no polegar
  basta. Em troca, às vezes concedem visões. Às vezes apenas consomem
  o sangue e ficam em silêncio. Isso também é uma forma de resposta.

  Estou no quinto andar. Abaixo, ouço algo que parece linguagem.
  Não é. Cheguei a essa conclusão por eliminação.

                                          — O. Tess, ainda em pé"""
    ),
    # Entrada 2
    (
        "⬛ DIÁRIO PERDIDO — Entrada III",
        """\
  Última entrada que consigo escrever com clareza.

  O Limiar não é uma masmorra. Compreendi isso tarde demais.
  É uma fronteira. Uma membrana entre o que pode ser pensado
  e o que não deve ser pensado. Quem a construiu sabia disso —
  construiu não para guardar tesouros, mas para guardar a ideia
  de que certas coisas existem.

  O Olho de Vecna está além do sétimo andar. Não como sentinela.
  Como habitante. Esteve sempre aqui. O Limiar foi erguido ao redor
  dele, não o contrário.

  Deixo este diário para quem vier depois. Se chegastes até aqui,
  sois mais que um aventureiro. Sois uma testemunha.

  Não derrotem o Olho. Não é possível derrotar algo que é parte
  da estrutura do lugar. Apenas... sobrevivam o suficiente para
  entender o que viram. Depois saiam.

  Se conseguirem sair.

                                          — O. Tess
                                          (Cartógrafo do Rei, suspeito)
                                          (Sobrevivente do Limiar, duvidoso)"""
    ),
    # Entrada 3 (extra — sorteio pode pegar esta também)
    (
        "⬛ DIÁRIO PERDIDO — Caderno de Rascunhos",
        """\
  [Escrito em letras pequenas, apertadas, com tinta que parece sangue diluído]

  Regras que aprendi. Para quem vier depois.

  1. Quando um corredor parecer idêntico a outro que você já percorreu —
     não é. O Limiar reformula-se. Não completamente. Apenas o suficiente
     para que você não perceba imediatamente.

  2. Os inimigos mortos-vivos não sentem dor. Isso é uma fraqueza deles,
     não uma força — porque dor existe para comunicar dano, e eles
     não sabem quando estão perdendo.

  3. Os altares de sangue pedem mais do que os altares antigos.
     Mas também dão mais. A questão é o que "mais" significa para você.

  4. Existe algo no andar mais profundo que não é o Olho de Vecna.
     O Olho também sabe que existe. Isso parece preocupá-lo.
     Essa é a coisa mais tranquilizadora que descobri aqui.

  5. Se encontrastes este diário: sois mais sortudos que eu.
     Eu não encontrei nenhum.

                                          — Autor desconhecido
                                          (A letra parece familiar)"""
    ),
    # Entrada 4
    (
        "⬛ DIÁRIO PERDIDO — Fragmento sem Capa",
        """\
  [As primeiras páginas estão carbonizadas. O texto começa abruptamente.]

  ...o fogo não funcionou da forma esperada. A criatura que chamamos
  de Arauto recuou, mas não por medo — por curiosidade. Como se
  o fogo fosse algo que ela não havia visto antes e quisesse entender
  antes de agir.

  Perdemos Maret na câmara com o círculo mágico.
  Não de forma violenta. Ela simplesmente entrou no círculo
  e quando saiu não era mais Maret. Andava como ela. Falava
  como ela. Mas os olhos estavam em lugares ligeiramente errados.

  Não em termos físicos. Em termos de onde ela olhava.

  Deixamos ela para trás no terceiro andar. Se encontrarem
  uma mulher com olhos que olham para lugares que não existem —
  não a ajudem. Não por maldade. Apenas porque não há o que ajudar.

  Continuamos descendo. Somos três agora.
  [O texto termina aqui. As páginas seguintes estão em branco,
  mas com marcas de dedos nas margens — como se alguém as tivesse
  folheado muitas vezes, procurando algo que não está lá.]"""
    ),
]

DICAS_MORTE = [
    "💡 Na masmorra é possível encontrar rotas alternativas e passagens secretas."
    "💡 Múltiplas armas e armaduras equipadas podem acumular atributos base, mas não efeitos específicos."
    "💡 Inimigos mortos-vivos são imunes a veneno — guarde seu antídoto.",
    "💡 A Gárgula de Pedra contra-ataca golpes físicos. Magia funciona melhor.",
    "💡 O Goblin Furtivo pode roubar itens do seu inventário durante o combate.",
    "💡 Tocha Suja equipada ou Lanterna Espiritual ampliam seu campo de visão para 2 células.",
    "💡 Tochas cravadas em paredes iluminam 2 células ao redor — observe o mapa.",
    "💡 O Espectro das Profundezas drena seu HP máximo permanentemente com cada acerto.",
    "💡 Fugir também é uma vitória. Especialmente contra o Dracolich.",
    "💡 O Esqueleto Guardião pode se remontar uma vez com 4 HP ao chegar a 0.",
    "💡 Diários Perdidos são raros — apenas 5 por sessão. Cada um salva o jogo e revela lore.",
    "💡 Altares antigos concedem efeitos variáveis. Altares de sangue pedem mais, mas dão mais.",
    "💡 Inimigos de elite aparecem mais frequentemente em salas distantes do hub.",
    "💡 O Orc Berserker tem 50% de chance de quebrar paralisação pela força bruta.",
    "💡 Veneno duplo causa 2x de dano por turno — antídoto imediato é prioridade.",
    "💡 A Serpente Abissal fareija sua alma — invisibilidade não funciona contra ela.",
    "💡 O modo extremo ativa-se ao andar 6 ou 18 salas exploradas.",
    "💡 Andares profundos têm elites nas salas mais distantes da entrada.",
    "💡 Explosivos arremessáveis destroem paredes e causam alta variância de dano.",
    "💡 O Arauto do Vazio drena vida e cura a si mesmo — priorize dano alto por turno.",
]

# =====================================================================
# SISTEMA DE SAVE/LOAD — JSON em ~/.masmorras_liminares/saves/
# =====================================================================

SAVE_DIR = os.path.join(os.path.expanduser("~"), ".masmorras_liminares", "saves")


def _garantir_dir_save():
    os.makedirs(SAVE_DIR, exist_ok=True)


def _listar_saves():
    """Retorna lista de dicts com info de cada save slot, ordenada por data."""
    _garantir_dir_save()
    saves = []
    for fname in os.listdir(SAVE_DIR):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(SAVE_DIR, fname)
        try:
            with open(path, "r", encoding="utf-8") as f:
                dados = json.load(f)
            saves.append({
                "arquivo":    fname,
                "nome":       dados.get("nome_personagem", "?"),
                "classe":     dados.get("classe", "?"),
                "subclasse":  dados.get("subclasse", ""),
                "andar":      dados.get("andar", 1),
                "nivel":      dados.get("nivel", 0),
                "hp":         dados.get("hp", 0),
                "hp_max":     dados.get("hp_max", 0),
                "data":       dados.get("data_save", ""),
                "diarios":    dados.get("diarios_lidos", 0),
            })
        except Exception:
            continue
    saves.sort(key=lambda s: s["data"], reverse=True)
    return saves


def _save_personagem(personagem):
    """Serializa Personagem para dict."""
    return {
        "nome":                personagem.nome,
        "hp":                  personagem.hp,
        "hp_max":              personagem.hp_max,
        "ac":                  personagem.ac,
        "base_ac":             personagem.base_ac,
        "base_hp_max":         personagem.base_hp_max,
        "ataque_bonus":        personagem.ataque_bonus,
        "dano_lados":          personagem.dano_lados,
        "classe":              personagem.classe,
        "base_ataque_bonus":   personagem.base_ataque_bonus,
        "base_dano_lados":     personagem.base_dano_lados,
        "inventario":          personagem.inventario,
        "equipados":           personagem.equipados,
        "arma":                personagem.arma,
        "armadura":            personagem.armadura,
        "cooldown_magia":      personagem.cooldown_magia,
        "bonus_temporario":    personagem.bonus_temporario,
        "invisivel":           personagem.invisivel,
        "pos":                 list(personagem.pos),
        "efeitos_ativos":      {k: v for k, v in personagem.efeitos_ativos.items()
                                if k not in ('absorver_ataque', 'talisma_protetor')},
        "capacidade_peso":     personagem.capacidade_peso,
        "afinidade_espiritual":personagem.afinidade_espiritual,
        "altar_oracoes":       personagem.altar_oracoes,
        "habilidade_especial": personagem.habilidade_especial,
        "cooldown_habilidade": personagem.cooldown_habilidade,
        "contra_ataque_ativo": personagem.contra_ataque_ativo,
        "subclasse":           personagem.subclasse,
        "lanterna_espiritual": getattr(personagem, 'lanterna_espiritual', 0),
        "flechas":             getattr(personagem, 'flechas', 0),
        "cristal_mana_ativo":  personagem.cristal_mana_ativo,
    }


def _load_personagem(d):
    """Reconstrói Personagem a partir de dict."""
    p = Personagem(
        d["nome"], d["hp_max"], d["base_ac"],
        d["base_ataque_bonus"], d["base_dano_lados"],
        d["classe"], d["base_ataque_bonus"], d["base_dano_lados"]
    )
    p.hp                  = d["hp"]
    p.hp_max              = d["hp_max"]
    p.ac                  = d["ac"]
    p.base_ac             = d["base_ac"]
    p.base_hp_max         = d["base_hp_max"]
    p.ataque_bonus        = d["ataque_bonus"]
    p.dano_lados          = d["dano_lados"]
    p.inventario          = d["inventario"]
    p.equipados           = d["equipados"]
    p.arma                = d["arma"]
    p.armadura            = d["armadura"]
    p.cooldown_magia      = d["cooldown_magia"]
    p.bonus_temporario    = d["bonus_temporario"]
    p.invisivel           = d["invisivel"]
    p.pos                 = tuple(d["pos"])
    p.efeitos_ativos      = d["efeitos_ativos"]
    p.capacidade_peso     = d["capacidade_peso"]
    p.afinidade_espiritual= d["afinidade_espiritual"]
    p.altar_oracoes       = d["altar_oracoes"]
    p.habilidade_especial = d["habilidade_especial"]
    p.cooldown_habilidade = d["cooldown_habilidade"]
    p.contra_ataque_ativo = d["contra_ataque_ativo"]
    p.subclasse           = d["subclasse"]
    p.lanterna_espiritual = d.get("lanterna_espiritual", 0)
    p.flechas             = d.get("flechas", 0)
    p.cristal_mana_ativo  = d.get("cristal_mana_ativo", False)
    p._mapa_ref           = None
    return p


def salvar_jogo(game, slot_nome=None):
    """Salva o estado do jogo em JSON. Retorna caminho do arquivo ou None."""
    _garantir_dir_save()
    agora = datetime.datetime.now()
    ts    = agora.strftime("%Y%m%d_%H%M%S")
    nome_arquivo = slot_nome if slot_nome else f"save_{ts}.json"
    path = os.path.join(SAVE_DIR, nome_arquivo)

    # ── Serializar entradas_andares {int: [[x,y],...]} ────────────────
    entradas_ser = {
        str(k): [list(c) for c in v]
        for k, v in getattr(game, 'entradas_andares', {}).items()
    }

    # ── Serializar spawn_retorno {[andar,cx,cy]: {...}} ───────────────
    retorno_ser = {}
    for (andar_dest, coord), ctx in getattr(game, 'spawn_retorno', {}).items():
        key = f"{andar_dest},{coord[0]},{coord[1]}"
        retorno_ser[key] = {
            'profundo':   ctx['profundo'],
            'regiao':     list(ctx['regiao']) if ctx['regiao'] else None,
            'sala':       list(ctx['sala']),
            'andar_sala': list(ctx['andar_sala']),
            'xy':         list(ctx['xy']),
        }

    dados = {
        "data_save":          agora.isoformat(),
        "nome_personagem":    game.jogador.nome,
        "classe":             game.jogador.classe,
        "subclasse":          game.jogador.subclasse,
        "hp":                 game.jogador.hp,
        "hp_max":             game.jogador.hp_max,
        "andar":              game.andar,
        "nivel":              game.nivel,
        "modo_extremo":       game.modo_extremo,
        "x":                  game.x,
        "y":                  game.y,
        "diarios_lidos":      getattr(game, '_diarios_lidos', 0),
        # ── Estado de navegação ───────────────────────────────────────
        "em_andar_profundo":  game.em_andar_profundo,
        "sala_no_andar":      list(game.sala_no_andar),
        "regiao_atual_key":   list(game.regiao_atual_key) if game.regiao_atual_key else None,
        "sala_pos":           list(game.sala_pos),
        "dir_entrada":        list(game.dir_entrada) if game.dir_entrada else None,
        "entradas_andares":   entradas_ser,
        "spawn_retorno":      retorno_ser,
        "personagem":         _save_personagem(game.jogador),
    }

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        return path
    except Exception as e:
        print(f"   ⚠️  Erro ao salvar: {e}")
        return None


def carregar_jogo(fname):
    """Carrega um save e retorna um DungeonGame reconstituído, ou None se erro."""
    path = os.path.join(SAVE_DIR, fname)
    try:
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except Exception as e:
        print(f"   ⚠️  Erro ao carregar: {e}")
        return None

    game = DungeonGame.__new__(DungeonGame)

    # ── Estado básico ─────────────────────────────────────────────────
    game.nivel        = dados.get("nivel", 0)
    game.andar        = dados.get("andar", 1)
    game.modo_extremo = dados.get("modo_extremo", False)
    game.x            = dados.get("x", 1)
    game.y            = dados.get("y", 1)
    game._diarios_lidos     = dados.get("diarios_lidos", 0)
    game._diarios_por_sessao = []

    # ── Personagem ────────────────────────────────────────────────────
    game.jogador = _load_personagem(dados["personagem"])

    # ── Estado de navegação ───────────────────────────────────────────
    game.em_andar_profundo = dados.get("em_andar_profundo", False)
    game.sala_no_andar     = tuple(dados.get("sala_no_andar", [0, 0]))
    rk = dados.get("regiao_atual_key")
    game.regiao_atual_key  = tuple(rk) if rk else None
    game.sala_pos          = tuple(dados.get("sala_pos", [0, 0]))
    dk = dados.get("dir_entrada")
    game.dir_entrada       = tuple(dk) if dk else None

    # ── Reconstruir entradas_andares ──────────────────────────────────
    game.entradas_andares = {}
    for k_str, coords in dados.get("entradas_andares", {}).items():
        game.entradas_andares[int(k_str)] = {tuple(c) for c in coords}

    # ── Reconstruir spawn_retorno ─────────────────────────────────────
    game.spawn_retorno = {}
    for key_str, ctx in dados.get("spawn_retorno", {}).items():
        parts = key_str.split(",")
        andar_dest = int(parts[0])
        coord = (int(parts[1]), int(parts[2]))
        game.spawn_retorno[(andar_dest, coord)] = {
            'profundo':   ctx['profundo'],
            'regiao':     tuple(ctx['regiao']) if ctx['regiao'] else None,
            'sala':       tuple(ctx['sala']),
            'andar_sala': tuple(ctx['andar_sala']),
            'xy':         tuple(ctx['xy']),
        }

    # ── Mundo: regiões de superfície (sempre regeneradas) ────────────
    dif = max(1, game.andar * 6 + game.nivel // 3)
    game.regioes = {}
    for dir_key in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        game.regioes[dir_key] = Regiao(
            dificuldade_base=dif,
            extrema=game.modo_extremo
        )

    game._mapa_hub = game._criar_mapa_hub()
    game.salas_visitadas = set()
    game._registrar_visita('hub', (0, 0))

    # ── Andares profundos: recriar o andar atual com entradas corretas ─
    game.andares = {}
    if game.em_andar_profundo and game.andar > 1:
        # Recriar todos os andares até o atual com as entradas salvas
        for num_andar in range(2, game.andar + 1):
            entradas = game.entradas_andares.get(num_andar, {game.sala_no_andar})
            game.andares[num_andar] = AndarLabirinto(
                num_andar, dif, extrema=game.modo_extremo, entradas=entradas
            )
        # Posicionar no andar e sala corretos
        andar_obj = game.andares[game.andar]
        game.mapa = andar_obj.sala(game.sala_no_andar)
        if game.mapa is None:
            # Fallback: sala de entrada
            game.sala_no_andar = andar_obj.pos_entrada
            game.mapa = andar_obj.sala(game.sala_no_andar)
        # Spawn junto à escada de subida (referência conhecida)
        if game.mapa and game.mapa.escada_subir:
            game.x, game.y = game._spawn_junto_a(game.mapa, game.mapa.escada_subir)
        else:
            game.x, game.y = game._spawn_em_mapa(game.mapa)
    else:
        # Superfície — posicionar no hub ou na região correta
        game.em_andar_profundo = False
        game.andar = 1
        if game.regiao_atual_key and game.regiao_atual_key in game.regioes:
            regiao = game.regioes[game.regiao_atual_key]
            if regiao.tem_sala(game.sala_pos):
                game.mapa = regiao.sala(game.sala_pos)
            else:
                game.sala_pos = (0, 0)
                game.mapa = regiao.sala((0, 0))
        else:
            game.regiao_atual_key = None
            game.sala_pos = (0, 0)
            game.mapa = game._mapa_hub
        game.x, game.y = game._spawn_em_mapa(game.mapa)

    game.jogador.pos       = (game.x, game.y)
    game.jogador._mapa_ref = game.mapa
    game.jogador._game_ref = game

    return game


# =====================================================================
# MENU PRINCIPAL
# =====================================================================

import sys
import random

def _fade_print(texto, delay=0.0005):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


def _nevoa_ascii(linhas=5, largura=70):
    chars = ["░", "▒", "▓", " "]
    for _ in range(linhas):
        linha = "".join(random.choice(chars) for _ in range(largura))
        print("   " + linha)
        time.sleep(0.03)



def _exibir_tela_titulo():
    limpar_tela()

    _nevoa_ascii()

    banner = r"""
   ⚜ ════════════════════════════════════════════════════════════════════ ⚜
   ║                                                                      ║
   ║        ██████╗     ██╗     ██╗███╗   ███╗██╗ █████╗ ██████╗          ║
   ║       ██╔═══██╗    ██║     ██║████╗ ████║██║██╔══██╗██╔══██╗         ║
   ║       ██║   ██║    ██║     ██║██╔████╔██║██║███████║██████╔╝         ║
   ║       ██║   ██║    ██║     ██║██║╚██╔╝██║██║██╔══██║██╔══██╗         ║
   ║       ╚██████╔╝    ███████╗██║██║ ╚═╝ ██║██║██║  ██║██║  ██║         ║
   ║        ╚═════╝     ╚══════╝╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝         ║
   ║                                                                      ║
   ║                    ✠   O   L I M I A R   ✠                           ║
   ║                                                                      ║
   ║                  ☩  Ninguém jamais retornou  ☩                       ║
   ║                                                                      ║
   ⚜ ════════════════════════════════════════════════════════════════════ ⚜
"""
    _fade_print(banner)

    _nevoa_ascii()


def _formatar_save(i, sv):
    sub = f" / {sv['subclasse']}" if sv['subclasse'] else ""
    hp_str  = f"HP {sv['hp']}/{sv['hp_max']}"
    data_str = sv['data'][:16].replace('T', ' ') if sv['data'] else ""
    diarios = f"📓×{sv['diarios']}" if sv['diarios'] else ""
    return (
        f"  [{i}] {sv['nome']}  •  {sv['classe']}{sub}\n"
        f"       Andar {sv['andar']} · {sv['nivel']} salas · {hp_str} "
        f"{diarios}\n"
        f"       {data_str}"
    )


def menu_principal():
    """Loop do menu principal. Retorna DungeonGame ou None para sair."""
    while True:
        _exibir_tela_titulo()
        saves = _listar_saves()

        print()
        print("        ╔══════════════════════════════════════╗")
        print("        ║                                      ║")
        print("        ║   ⚔  [1] INICIAR NOVA DESCIDA        ║")
        print(f"        ║  📜  [2] CONTINUAR DESCIDA ({len(saves)})       ║")
        print("        ║   ✠  [3] ABANDONAR LIMIAR            ║")
        print("        ║                                      ║")
        print("        ╚══════════════════════════════════════╝")
        print()

        escolha = input("  >> ").strip()

        if escolha == '1':
            return DungeonGame()

        elif escolha == '2':
            if not saves:
                print("\n  Nenhum registro de aventura encontrado.")
                time.sleep(2)
                continue

            while True:
                limpar_tela()
                saves = _listar_saves()   # atualizar após possível exclusão

                print("\n  ╔══════════════════════ GRIMÓRIO DE AVENTURAS ═══════════════════════╗\n")
                for i, sv in enumerate(saves, 1):
                    print(_formatar_save(i, sv))
                    print("  ─────────────────────────────────────────────────────────────────")
                print("\n  ╚══════════════════════════════════════════════════════════════════╝")
                print("\n  Digite o número para retornar à aventura.")
                print("  'del N' ou 'del N, M, ...' para apagar registros.")
                print("  0 para voltar.")

                sel = input("  >> ").strip().lower()

                if sel == '0' or sel == '':
                    break

                # ── Comando de exclusão ──────────────────────────────
                if sel.startswith('del'):
                    partes = sel[3:].replace(' ', '')
                    try:
                        indices = [int(p) - 1 for p in partes.split(',') if p]
                    except ValueError:
                        print("  ⚠️  Formato inválido. Use: del 2  ou  del 1, 3")
                        time.sleep(1.5)
                        continue

                    validos = [i for i in indices if 0 <= i < len(saves)]
                    if not validos:
                        print("  ⚠️  Número(s) inválido(s).")
                        time.sleep(1.5)
                        continue

                    print(f"\n  Registros a excluir:")
                    for i in sorted(validos):
                        sv = saves[i]
                        sub = f" / {sv['subclasse']}" if sv['subclasse'] else ""
                        print(f"    [{i+1}] {sv['nome']}  •  {sv['classe']}{sub}  — Andar {sv['andar']}")
                    conf = input("\n  Tem certeza? (s/n): ").strip().lower()
                    if conf == 's':
                        for i in sorted(validos, reverse=True):
                            path_del = os.path.join(SAVE_DIR, saves[i]["arquivo"])
                            try:
                                os.remove(path_del)
                            except Exception:
                                pass
                        excluidos = len(validos)
                        print(f"\n  ✅ {excluidos} registro(s) apagado(s). Slots renumerados.")
                        time.sleep(1.5)
                    else:
                        print("  Operação cancelada.")
                        time.sleep(1)
                    continue

                # ── Carregar save ────────────────────────────────────
                try:
                    idx = int(sel) - 1
                    if 0 <= idx < len(saves):
                        limpar_tela()
                        print("\n  Desvelando memórias da masmorra...")
                        time.sleep(1)
                        game = carregar_jogo(saves[idx]["arquivo"])
                        if game:
                            print(f"\n  Bem-vindo de volta, {game.jogador.nome}.")
                            print(f"  Andar {game.andar} — {game.nivel} salas exploradas.")
                            print(f"  O Limiar aguardava.\n")
                            time.sleep(2.5)
                            return game
                        else:
                            print("  ⚠️  Não foi possível carregar este save.")
                            time.sleep(2)
                    else:
                        print("  ⚠️  Número fora do intervalo.")
                        time.sleep(1)
                except ValueError:
                    print("  ⚠️  Entrada inválida.")
                    time.sleep(1)

        elif escolha == '3':
            limpar_tela()
            print("\n  O Limiar fecha suas portas.\n")
            time.sleep(1)
            return None


# =====================================================================
# HANDLER DO DIÁRIO PERDIDO (chamado via _usar_item_direto)
# =====================================================================

def _ler_diario(game, personagem):
    """Lê um Diário Perdido: exibe lore, salva o jogo, conta uso."""
    diarios_pool = getattr(game, '_diarios_por_sessao', DIARIO_ENTRADAS[:3])
    lidos        = getattr(game, '_diarios_lidos', 0)

    limpar_tela()
    if not diarios_pool:
        print("   📓 As páginas estão em branco. Este diário já revelou seus segredos.")
        time.sleep(2)
        return

    entrada = diarios_pool[lidos % len(diarios_pool)]
    titulo, texto = entrada

    print(f"\n  {titulo}")
    print("  " + "─" * 52)
    print()
    for linha in texto.strip().splitlines():
        print(f"  {linha}")
        time.sleep(0.07)
    print()
    print("  " + "─" * 52)
    time.sleep(2)
    print("\n  📓 As palavras de outro aventureiro ficam gravadas em sua memória.")
    time.sleep(1.5)

    # Salvar o jogo
    print("\n  🖋️  Você usa as últimas páginas em branco para registrar sua posição...")
    time.sleep(1)
    caminho = salvar_jogo(game)
    if caminho:
        game._diarios_lidos = lidos + 1
        print(f"  ✅ Progresso salvo.")
        input("\n  [ pressione ENTER para continuar ]")
    else:
        print(f"  ⚠️  Não foi possível salvar.")
        input("\n  [ pressione ENTER para continuar ]")
    time.sleep(2)


# ----------------------------- EXECUÇÃO ----------------------------------
if __name__ == "__main__":
    while True:
        game = menu_principal()
        if game is None:
            break
        game.jogar()
        # Após sair (morte ou quit manual), volta ao menu principal
