# Design Library — SETUP

Personal design reference system. Links-primary (источник истины — URLs), style-profile-cached (основная рабочая зона — дистиллированные `.md` профили).

## Директории

```
design-library/
├── sources/                   ← ссылки + метаданные (что откуда брать)
│   ├── designers/             ← один .md на дизайнера (портфолио, ключевые работы)
│   ├── collections/           ← твои saved/favorited: Envato, Canva, Behance
│   └── principles/            ← универсальные приёмы (color/typo/grid)
├── style-profiles/            ← ДИСТИЛЛИРОВАННЫЕ профили (основная рабочая зона)
│                                palette hex, typography, signature moves, приёмы
├── analyses/                  ← разборы конкретных работ (по designer/project)
├── my-works/                  ← мои проекты + итерации
└── templates/                 ← шаблоны для новых entries
```

## Как это использовать

### 1. Добавить нового дизайнера
Скажи Claude: **"добавь [имя] в design-library"** или **"проанализируй [URL] как референс"**.

Claude:
1. Создаёт `sources/designers/<slug>.md` (портфолио + список ключевых работ)
2. Фетчит 3-5 репрезентативных работ (через WebFetch или Claude in Chrome)
3. Пишет `analyses/<slug>/*.md` по каждой работе
4. Синтезирует `style-profiles/<slug>.md`

### 2. Создать дизайн в чьём-то стиле
**"постер в стиле [designer] + [designer]"** или **"дизайн X на тему Y, комбинируй стили A и B"**

Claude читает `style-profiles/*.md` → синтезирует → создаёт → сохраняет в `my-works/<date>-<project>/`.

### 3. Обновить профиль
**"обнови [designer], посмотри что нового"** — Claude перечитывает портфолио, обновляет `style-profiles/<slug>.md`.

### 4. Добавить Envato/Canva favorites
**"добавь эту Canva [URL/ID] в collections"** или **"залогь Envato item [URL]"** — Claude добавит в `collections/envato-saved.md` / `collections/canva-favorites.md`.

## Какой инструмент для какого источника

| Источник | Инструмент Claude | Auth? |
|---|---|---|
| Designer personal sites | WebFetch | нет |
| Behance (public) | WebFetch → если не отдаёт картинки, Claude in Chrome | иногда |
| Behance (логин) | Claude in Chrome | да |
| **Canva** | Canva MCP (`search-designs`, `get-design`, `generate-design`) | да (через MCP) |
| **Envato Elements** | Claude in Chrome (твоя сессия) | да |
| Pinterest public board | WebFetch | нет |
| Pinterest private board | Claude in Chrome | да |
| Instagram (любое) | Claude in Chrome | да |
| Dribbble | WebFetch | нет (обычно) |
| Awwwards | WebFetch | нет |

## Принципы организации

1. **Slugs в snake-case** (пример: `ash-thorp`, `josan-gonzalez`, `james-white-signalnoise`)
2. **Каждая работа в `analyses/` именуется:** `YYYY-project-name.md` (примеры: `2019-ghost-in-shell-ui.md`)
3. **my-works датированы:** `YYYY-MM-short-name/` (пример: `2026-04-cyber-art-expo/`)
4. **Style profiles — авторитетный источник истины для работы.** Обновляй при изменении направления дизайнера.
5. **Last sync дата** в каждом профиле — если она старше полугода, надо обновить.

## Текущий inventory (v1)

**Designers seeded (9):**

| Designer | Genre | Use when... |
|---|---|---|
| Ash Thorp | Cinematic UI / minimalist sci-fi | Нужен cold serious tech-sublime (BR2049 vibe) |
| Josan Gonzalez | Dense cyberpunk editorial | Maximalist packed cyberpunk illustration |
| James White / Signalnoise | 80s retrofuturism / synthwave | Nostalgic optimism, sunset gradients |
| Syd Mead | Legacy industrial concept art | Painterly gravitas, atmospheric realism |
| Beeple | Digital 3D satirical daily-art | Absurd cultural commentary, bold 3D |
| **Kilian Eng** | Retrofuturism screen-print | Warm nostalgic sci-fi posters (Mondo tradition) |
| **Yoji Shinkawa** | Sumi-e ink on mecha | Traditional Japanese ink + futuristic subjects |
| **David Carson** | Chaos typography / grunge | Anti-grid rebellion, emotional layouts |
| **Stefan Sagmeister** | Concept-first brand | Big ideas через unusual materials/handwork |

**Collections:** envato-saved, canva-favorites, behance-cyberpunk (placeholders)
**Principles:** color-theory, typography-hierarchy, composition-grids
**Works:** 2026-04-cyber-art-expo (V1 + V2 Thorp)

## Расширение

Предложения для добавления (genre coverage):
- **Illustrators:** Drew Conklin, James Jirat Patradoon, Ilya Kuvshinov, Katsuhiro Otomo (Akira)
- **Type/poster:** Tom Whalen, Anthony Petrie, Swissted, Josef Müller-Brockmann (Swiss)
- **Motion/brand:** Pentagram, Collins, Bond, Paula Scher
- **Editorial:** The New York Times design, Wired visuals, Pentagram magazines
- **Architectural/industrial:** Dieter Rams (Braun), Massimo Vignelli
- **Modern digital:** Refik Anadol (generative AI art), Pak
- **Brutalist web:** Balenciaga.com-era, David Rudnick
- **Sound/music visuals:** Hipgnosis (Pink Floyd), Peter Saville (Joy Division/Factory)

Просто скажи Claude что добавить.

## Последнее обновление
Created: 2026-04-15
