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

## Текущий inventory (v1.2.0)

**Designers seeded (14):**

| Designer | Genre | Use when... | Last sync |
|---|---|---|---|
| Ash Thorp | Cinematic UI / atmospheric illustration | Cold serious tech-sublime (BR2049 vibe) | LIVE 2026-04-15 |
| Josan Gonzalez / Death Burger | Dense cyberpunk editorial | Maximalist packed cyberpunk illustration | LIVE 2026-04-15 |
| James White / Signalnoise | 80s retrofuturism / synthwave | Nostalgic optimism, sunset gradients | LIVE 2026-04-15 |
| Syd Mead (deceased 2019) | Legacy industrial concept art | Painterly gravitas, atmospheric realism | posthumous 2026-04-15 |
| Beeple | Digital 3D satirical daily-art | Absurd cultural commentary, bold 3D | LIVE 2026-04-15 |
| Kilian Eng | Retrofuturism + dark fantasy + engraving | Warm nostalgic sci-fi posters (Mondo tradition) | LIVE 2026-04-15 |
| Yoji Shinkawa | Sumi-e ink on mecha | Traditional Japanese ink + futuristic subjects | LIVE + WS 2026-04-15 |
| David Carson | Chaos typography / anti-design | Anti-grid rebellion, emotional layouts | LIVE 2026-04-15 |
| Stefan Sagmeister | Concept-first brand | Big ideas via unusual materials/handwork | LIVE 2026-04-15 |
| **Paula Scher** | Type-forward editorial maximalism | Loud but literate — cultural institutions | seed 2026-04-15 |
| **Kenya Hara** | Japanese modern minimalism (Muji) | Quiet premium, breathing-room design | seed 2026-04-15 |
| **Peter Saville** | Cerebral minimalism via appropriation | Record sleeves / thinking-object aesthetic | seed 2026-04-15 |
| **Massimo Vignelli** (d. 2014) | Swiss modernism systems | Wayfinding, institutional identity | seed 2026-04-15 |
| **Refik Anadol** | Generative / AI-collab art | Machine-imagination at architectural scale | seed 2026-04-15 |

**Analyses (deep-dive breakdowns):**
- analyses/ash-thorp/2017-ghost-in-shell-ui.md
- analyses/yoji-shinkawa/2015-mgs5-sahelanthropus.md
- analyses/david-carson/1994-ray-gun-bryan-ferry-spread.md

**Collections:** envato-saved, canva-favorites, behance-cyberpunk (placeholders)
**Principles:** color-theory, typography-hierarchy, composition-grids
**Works:** 2026-04-cyber-art-expo (Thorp NEO-GENESIS) + showcase-2026-04 (Shinkawa ink mecha) — two reference pieces setting the quality bar

**GitHub infrastructure (as of v1.2.0):**
- .github/ISSUE_TEMPLATE/ — 4 structured forms (new-designer, profile-refinement, new-principle, bug) + config
- .github/pull_request_template.md — full checklist from CONTRIBUTING quality bar
- .github/workflows/lint.yml — validates style profile + source sections + internal link integrity
- Discussions enabled with welcome post at /discussions/1
- docs/share-drafts.md — copy-paste-ready announcement text for Reddit / HN / PH / X / Telegram

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
