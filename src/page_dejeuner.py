# -*- coding: utf-8 -*-
import json
from common import HEADER, SUBNAV, footer, HINT_SCRIPT, badge, ORG

FAQ = [
    ("Upcoop, c'est l'ancien Chèque Déjeuner ?",
     "Oui. Upcoop est le nouveau nom du groupe coopératif connu sous les noms Chèque Déjeuner puis Groupe Up. La carte déjeuner Upcoop, appelée UpDéjeuner, est le nouveau Chèque Déjeuner : même émetteur, même réseau de commerçants, en carte ou en chèque."),
    ("Où la carte déjeuner Upcoop est-elle acceptée ?",
     "Dans plus de 253 500 restaurants et commerçants en France, y compris les supermarchés et les épiceries, et en ligne auprès de plus de 40 000 enseignes de livraison comme Uber Eats, Deliveroo ou Nestor. Elle se paie sans contact, avec Apple Pay et Google Pay."),
    ("Quel est le plafond d'utilisation du titre-restaurant Upcoop ?",
     "La carte déjeuner Upcoop se débite au centime près, dans la limite de 25 € par jour. Le solde non utilisé reste disponible pour un prochain repas, et un complément de paiement par carte personnelle évite de bloquer quand l'addition dépasse."),
    ("Combien coûte un titre-restaurant Upcoop à l'employeur ?",
     "L'employeur finance entre 50 et 60 % de la valeur du titre, exonérés de cotisations sociales jusqu'à 7,32 € par salarié et par jour en 2026. Pour 35 salariés, 20 jours par mois et un titre de 10 € financé à 60 %, la part employeur est de 4 200 € par mois. Les frais de gestion se chiffrent sur devis, sans frais de livraison mensuels pour la carte."),
    ("Une petite entreprise peut-elle proposer la carte déjeuner Upcoop ?",
     "Oui, dès un salarié, quel que soit le contrat : CDI, CDD à temps plein ou partiel, alternance et stage. Upcoop a un parcours dédié aux entreprises de moins de 50 salariés, avec commande et rechargement en ligne."),
    ("Upcoop ou Swile, Edenred et Pluxee, quelle différence ?",
     "Les quatre émetteurs proposent une carte titre-restaurant soumise aux mêmes règles d'exonération et de plafond. Upcoop se distingue par son statut de coopérative (SCOP) depuis plus de 60 ans, son réseau de 253 500 commerçants, une carte 100 % recyclée, la certification ISO 9001 et Origine France Garantie, et le programme Up+ qui reverse du cashback chez des commerçants partenaires."),
]

faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://up.coop/"},
    {"@type": "ListItem", "position": 2, "name": "Nos produits", "item": "https://up.coop/nos-produits/"},
    {"@type": "ListItem", "position": 3, "name": "Déjeuner, titre-restaurant", "item": "https://up.coop/updejeuner/"}]}
svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": "UpDéjeuner, titre-restaurant Upcoop en carte ou en chèque",
          "serviceType": "Titre-restaurant", "provider": {"@id": "https://up.coop/#organization"}, "areaServed": "FR",
          "audience": {"@type": "BusinessAudience", "name": "Entreprises, associations, collectivités"},
          "dateModified": "2026-10-01",
          "additionalProperty": [
              {"@type": "PropertyValue", "name": "Plafond journalier d'utilisation", "value": "25 €"},
              {"@type": "PropertyValue", "name": "Exonération de la part employeur 2026", "value": "7,32 € par jour et par salarié"},
              {"@type": "PropertyValue", "name": "Commerçants acceptant la carte", "value": "253 500"},
              {"@type": "PropertyValue", "name": "Enseignes de livraison en ligne", "value": "40 000"}]}

FAQ_HTML = "\n".join(
    f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ))

html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Titre-restaurant Upcoop (ex Chèque Déjeuner) : carte UpDéjeuner | maquette GEO datashake</title>
<meta name="description" content="Maquette datashake de la page up.coop/updejeuner : page d'origine reproduite, ajouts GEO en pastilles pour être lue et citée par ChatGPT, Gemini et les Aperçus IA de Google.">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="https://up.coop/updejeuner/">
<meta property="og:title" content="Titre-restaurant Upcoop, le nouveau Chèque Déjeuner">
<meta property="og:description" content="Carte déjeuner acceptée chez 253 500 commerçants, jusqu'à 25 € par jour, part employeur exonérée jusqu'à 7,32 € en 2026.">
<meta property="og:image" content="https://up.coop/wp-content/uploads/solution-dejeuner-decouvrir-header-desktop.jpg">
<link rel="stylesheet" href="assets/up-site.css">
<script type="application/ld+json">{ORG}</script>
<script type="application/ld+json">{json.dumps(bc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(svc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
<body>
{HEADER}
{SUBNAV}

<section class="hero"><div class="wrap">
  <div>
    <nav class="crumb geo-mark" aria-label="Fil d'Ariane">
      {badge(1, "Structure + code", "Fil d'Ariane complet et balisé", "La page d'origine affiche une maison puis « Déjeuner », et son <code>BreadcrumbList</code> Yoast s'arrête à ces deux niveaux. Le chemin complet Accueil, Nos produits, Déjeuner, titre-restaurant, dit aux moteurs génératifs que la page est la fiche produit du titre-restaurant d'Upcoop, et non un article.")}
      <span class="home"></span><a href="#">Accueil</a> » <a href="#">Nos produits</a> » <span>Déjeuner, titre-restaurant</span>
    </nav>
    <img class="brand" src="assets/Dejeuner-Upcoop.svg" alt="Déjeuner Upcoop">
    <h1>Le titre restaurant qui améliore le pouvoir d’achat et la qualité de vie au travail !</h1>
    <div class="updated geo-mark">
      {badge(2, "Autorité + fraîcheur", "Éditeur identifié et date de mise à jour", "La page ne montre aucune date, elle n'existe que dans les métadonnées Yoast. Or le plafond, l'exonération et l'usage en supermarché changent chaque année : une IA écarte une page dont elle ne peut pas dater les chiffres. La date est affichée, portée par <code>&lt;time&gt;</code> et reprise en <code>dateModified</code>, avec Upcoop en éditeur.")}
      <div class="av">U</div><div><b>L'équipe Déjeuner Upcoop</b>Mis à jour le <time datetime="2026-10-01">1er octobre 2026</time> · chiffres de l'exonération 2026</div>
    </div>
    <div class="ctas"><a class="btn btn-orange btn-lg" href="#">Je commande</a><a class="link-orange" href="#">Accéder à mon espace</a></div>
    <div class="tp">Qu'en pensent nos clients ?<div class="stars"><i></i><i></i><i></i><i></i><i></i></div><small>Basé sur 2157 avis · Trustpilot</small></div>
  </div>
  <div class="pic"><img src="assets/solution-dejeuner-decouvrir-header-desktop.jpg" alt="Collègues qui déjeunent ensemble au restaurant"></div>
</div></section>

<section class="sec"><div class="wrap narrow">
  <div class="geo-quick geo-mark">
    {badge(3, "Sémantique", "Réponse directe en tête de page", "Une IA lit les premiers paragraphes et repart. Ce bloc répond en cinq lignes aux prompts mesurés : ce qu'est la carte, où elle passe, combien elle coûte, ce qu'elle remplace. C'est le paragraphe que ChatGPT recopie quand on lui demande « quelle carte titre-restaurant pour une PME ».")}
    <strong>En bref.</strong> La carte déjeuner Upcoop, appelée UpDéjeuner, est le titre-restaurant de la coopérative Upcoop, <strong>anciennement Chèque Déjeuner</strong>.
    <ul>
      <li><strong>Acceptée chez plus de 253 500 restaurants et commerçants</strong>, supermarchés compris, et chez plus de 40 000 enseignes de livraison en ligne.</li>
      <li><strong>Jusqu'à 25 € par jour</strong>, débités au centime près, solde reporté automatiquement, Apple Pay et Google Pay.</li>
      <li><strong>Part employeur de 50 à 60 %</strong>, exonérée de cotisations jusqu'à <strong>7,32 € par salarié et par jour en 2026</strong>.</li>
      <li>Ouverte <strong>dès un salarié</strong>, en CDI, CDD, alternance ou stage, et choisie par près de <strong>40 000 entreprises</strong> pour <strong>1,2 million d'utilisateurs</strong>.</li>
    </ul>
  </div>
</div></section>

<section class="sec beige"><div class="wrap two">
  <div>
    <h2>La solution déjeuner Upcoop, bien plus qu’un titre restaurant</h2>
    <p>Vous cherchez à soutenir le pouvoir d’achat de vos collaborateurs sans que cela ne pèse sur vos charges ? Faites comme près de 40 000 entreprises clientes et plus d’1,2 million d’utilisateurs en France, choisissez le titre déjeuner Upcoop en carte ou chèque !</p>
    <p>Le titre restaurant Upcoop, c’est la garantie d’une vraie pause déjeuner quotidienne pour déconnecter et partager un moment de convivialité et cela, au service de la performance de votre entreprise.</p>
    <ul class="check">
      <li>Bénéficiez d’une exonération fiscale et sociale sur la part financée par l’employeur : jusqu’à 7,32 € / salarié / jour, en 2026.</li>
      <li>Proposez des titres déjeuner à partir d’un salarié, quel que soit son contrat de travail.</li>
      <li>Donnez à vos salariés la possibilité de régler leur repas jusqu’à 25 €/jour en carte déjeuner Upcoop ou chèque restaurant déjeuner Upcoop.</li>
    </ul>
  </div>
  <img src="assets/Application-carte-dejeuner-upcoop-1.webp" alt="Application et carte déjeuner Upcoop">
</div></section>

<section class="sec"><div class="wrap">
  <div class="geo-mark">
    {badge(4, "Entité de marque", "Upcoop, anciennement Chèque Déjeuner et Groupe Up", "Deux changements de nom en six ans : les modèles associent encore le titre-restaurant au « Chèque Déjeuner » et au « Groupe Up ». Le schéma <code>Organization</code> actuel ne porte que le nom et le logo. Ce bloc relie explicitement les trois noms, et le schéma gagne <code>alternateName</code> et <code>sameAs</code> vers Wikidata (Q3117361, qui connaît déjà les anciens noms), Wikipédia et groupe.up.coop. Sans ce lien, une IA cite l'ancien nom ou un concurrent.")}
    <div class="entity">
      <h2 style="margin:0">Upcoop, le nouveau nom du Chèque Déjeuner</h2>
      <dl>
        <dt>Nom actuel</dt><dd>Upcoop, coopérative (SCOP) de solutions de paiement et de services à utilité sociale</dd>
        <dt>Anciens noms</dt><dd>Chèque Déjeuner, puis Groupe Up. La carte UpDéjeuner est le nouveau Chèque Déjeuner.</dd>
        <dt>Depuis</dt><dd>Plus de 60 ans de coopération</dd>
        <dt>Produits</dt><dd>UpDéjeuner (titre-restaurant), Cadhoc (titre cadeau), UpOne (carte multi-avantages), CESU Chèque Domicile, Chèque Culture, Chèque Lire</dd>
        <dt>Certifications</dt><dd>Titre déjeuner certifié ISO 9001 et Origine France Garantie, carte 100 % recyclée</dd>
      </dl>
    </div>
  </div>
</div></section>

<section class="sec beige"><div class="wrap">
  <div class="geo-mark">
    {badge(5, "Sémantique + structure", "Le coût en euros, dans un vrai tableau", "La page d'origine renvoie au simulateur, que les IA ne peuvent pas exécuter. Un <code>&lt;table&gt;</code> chiffre la part employeur et la part salarié pour trois valeurs de titre, sur une PME de 35 salariés. C'est le format que les moteurs génératifs extraient pour répondre « combien coûtent des titres-restaurant pour 30 salariés ».")}
    <h2>Combien coûte le titre-restaurant Upcoop pour votre entreprise ?</h2>
    <p>Exemple pour une PME de 35 salariés, 20 jours travaillés par mois, part employeur fixée à 60 %, dans la limite d'exonération de 7,32 € par titre en 2026.</p>
    <div class="table-wrap"><table class="compare">
      <thead><tr><th>Valeur du titre</th><th>Part employeur par jour</th><th>Part salarié par jour</th><th>Part employeur par mois, 35 salariés</th><th>Part salarié par mois</th><th>Cotisations sur la part employeur</th></tr></thead>
      <tbody>
        <tr><th>9,00 €</th><td>5,40 €</td><td>3,60 €</td><td><b>3 780 €</b></td><td>2 520 €</td><td>0 €</td></tr>
        <tr class="hl"><th>10,00 €</th><td>6,00 €</td><td>4,00 €</td><td><b>4 200 €</b></td><td>2 800 €</td><td>0 €</td></tr>
        <tr><th>12,20 €</th><td>7,32 €, plafond exonéré</td><td>4,88 €</td><td><b>5 124 €</b></td><td>3 416 €</td><td>0 €</td></tr>
      </tbody></table></div>
    <p class="caption">Calcul indicatif sur la règle de financement de 50 à 60 % et l'exonération 2026 publiées sur up.coop. Frais de gestion sur devis, zéro frais de livraison mensuels pour la carte.</p>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="geo-mark">
    {badge(6, "Autorité", "Des faits vérifiables, pas des slogans", "« Bien plus qu'un titre restaurant » ne se cite pas. Un réseau de 253 500 commerçants, 40 000 enseignes en livraison, 40 000 entreprises clientes et 1,2 million d'utilisateurs se citent. Ces chiffres, déjà présents plus bas sur la page d'origine, remontent ici et sont repris en <code>additionalProperty</code> dans un schéma <code>Service</code>.")}
    <h2>Voici pourquoi choisir la carte déjeuner Upcoop !</h2>
    <div class="cards4">
      <div><img src="assets/Picto-simplicite.svg" alt=""><b>253 500</b><span>restaurants et commerçants qui acceptent la carte</span></div>
      <div><img src="assets/Picto-mobile-carte.svg" alt=""><b>40 000</b><span>enseignes de livraison en ligne, Uber Eats, Deliveroo, Nestor</span></div>
      <div><img src="assets/Picto-bourse-argent.svg" alt=""><b>40 000</b><span>entreprises clientes, 1,2 million d'utilisateurs</span></div>
      <div><img src="assets/Picto-securite.svg" alt=""><b>ISO 9001</b><span>et Origine France Garantie, carte 100 % recyclée</span></div>
    </div>
    <p class="geo-src" style="margin-top:14px">Source : up.coop, page Déjeuner et page Pourquoi choisir Upcoop.</p>
  </div>
</div></section>

<section class="sec beige"><div class="wrap">
  <div class="geo-mark">
    {badge(7, "Sémantique", "Une réponse par situation", "« Pour une TPE », « avec du télétravail », « pour une collectivité » : ces prompts reçoivent aujourd'hui des réponses tirées de comparateurs. Trois blocs courts, une recommandation nette par profil, c'est la forme exacte d'une réponse d'assistant, et les profils que up.coop sert déjà dans son menu Qui êtes-vous.")}
    <h2>Quelle formule déjeuner selon votre entreprise ?</h2>
    <div class="who">
      <div><h4>TPE de moins de 10 salariés</h4><p>Commande en ligne en autonomie, carte physique ou virtuelle, une seule distribution tous les quatre ans et rechargement à distance chaque mois.</p><span class="pick">Carte UpDéjeuner, parcours Entreprise -50</span></div>
      <div><h4>PME avec des salariés en télétravail</h4><p>Le titre reste dû chaque jour travaillé, même à domicile : la carte paie la livraison de repas chez plus de 40 000 enseignes en ligne.</p><span class="pick">Carte UpDéjeuner avec paiement en ligne</span></div>
      <div><h4>Collectivité ou association</h4><p>Financement de 50 à 60 % pour les agents, ouvert à tous les contrats, avec un parcours dédié aux collectivités et organismes sociaux sur up.coop.</p><span class="pick">Carte ou chèque déjeuner, parcours Collectivité</span></div>
    </div>
  </div>
</div></section>

<section class="sec"><div class="wrap narrow">
  <h2 class="geo-mark" style="display:table">Vos questions sur le titre-restaurant Upcoop
    {badge(8, "Sémantique + code", "FAQ sur les vrais prompts, balisée FAQPage", "Les questions d'origine sont génériques (« Pourquoi choisir le titre déjeuner Upcoop ? ») et rangées en accordéons fermés. Elle reprend ici mot pour mot les prompts mesurés dans ChatGPT, Gemini et les Aperçus IA, dont « Upcoop, c'est l'ancien Chèque Déjeuner ? » et la comparaison avec Swile, Edenred et Pluxee, avec des réponses de deux à trois phrases chiffrées, doublées d'un schéma <code>FAQPage</code>.")}
  </h2>
  <div class="faq">
{FAQ_HTML}
  </div>
  <div class="sources"><b>Sources</b><ul><li>up.coop, pages Déjeuner, Entreprise -50 et Pourquoi choisir Upcoop</li><li>URSSAF, limite d'exonération de la contribution patronale aux titres-restaurant pour 2026</li><li>Commission nationale des titres-restaurant (CNTR), conditions d'attribution et d'utilisation</li></ul></div>
</div></section>

{footer("page up.coop/updejeuner reproduite pour illustrer les ajouts GEO, textes d'origine conservés.")}
{HINT_SCRIPT}
</body>
</html>
'''
open('../titre-restaurant.html', 'w').write(html)
print('ok')
