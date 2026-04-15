# Canva — Favorites & Designs

> Canva designs worth referencing / reusing. Accessible через Canva MCP напрямую.

## Access
- Platform: canva.com (user authenticated via Canva MCP)
- Tools available:
  - `search-designs` — найти existing designs
  - `get-design` / `get-design-content` — прочитать содержимое
  - `generate-design` — создать новый (via AI prompt)
  - `start-editing-transaction` → `perform-editing-operations` → `commit` — редактировать

## Personal designs
Track design IDs (format starts with "D" for finished designs, or `dg-` prefix for AI generation candidates).

### Example entry format
```
## Project: [Project Name] ([YYYY-MM-DD])
- Style direction: [brief description]
- Brand kit: [ID or "none"]
- Design ID: [D...]
- Canva URL: [link]
- Notes: [what works, what to iterate]
```

## Brand kits
_List brand kit IDs + names here for fast reference during generation tasks._

## Template bookmarks
_Canva templates worth reusing — note template ID + when to apply._

## Notes
- Canva MCP `generate-design` query param requires ~150-300 chars for good results
- Design type matters: 'flyer' = 8.5×11, 'poster' = larger formats, 'presentation' = 16:9
- For Illustrator workflow: create editable design → export SVG (via UI, not MCP) → open in AI

## Last sync
2026-04-15
