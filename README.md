# Upcoop, maquettes GEO (datashake)

Maquettes de démonstration du pré-audit GEO Upcoop, non affiliées à Upcoop, `noindex`.

- `titre-restaurant.html` : page up.coop/updejeuner reproduite, 8 pastilles GEO
- `guide-meilleur-titre-restaurant-pme.html` : article de conseil sur la DA du blog up.coop, 8 pastilles GEO
- `mindmap-titre-restaurant.html` : mindmap D3 des 50 prompts du marché titre-restaurant (`?fit=1`, `?macro`, `?zoom=k`, `?bare`)

La mindmap lit deux fichiers optionnels à la racine : `volumes.json` (`{"mot-clé": volume Google mensuel}`, volume de prompt = 12 %) et `runs.json` (`{"id du prompt": {"gpt": "Upcoop 1er" | "Upcoop absent" | "Swile 1er, Upcoop 3e", "aio": "avec Upcoop" | "sans Upcoop" | "non"}}`). Sans eux, elle affiche « volume à venir ».

Les pages se régénèrent depuis `src/` (`python3 page_dejeuner.py`, `python3 page_article.py`).
