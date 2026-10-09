# -*- coding: utf-8 -*-
HEADER = '''<div class="mainnav"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Upcoop"><img src="assets/logo-upcoop-slim.svg" alt="Upcoop"></a>
  <nav><a class="more" href="#">Nos produits</a><a href="#">Qui êtes-vous ?</a><a href="#">Pourquoi choisir Upcoop</a><a href="#">Blog</a></nav>
  <div class="right"><span><img src="assets/search.svg" alt="">Rechercher</span><span><img src="assets/account2.svg" alt="">Mon espace</span></div>
  <div class="contrast">CONTRASTE</div>
</div></div>'''

SUBNAV = '''<div class="subnav"><div class="wrap">
  <div class="tabs"><a class="on" href="#">Découvrir</a><a href="#">Utiliser</a></div>
  <div class="btns"><a class="btn btn-white" href="#">Faire une simulation</a><a class="btn btn-orange" href="#">Demander un devis</a></div>
</div></div>'''

def footer(page_desc):
    return f'''<footer><div class="wrap">
  <div class="cols">
    <div><img class="logo-f" src="assets/logo-upcoop-slim.svg" alt="Upcoop"><p style="font-weight:300;margin-top:16px">Coopérative de solutions de paiement et de services à utilité sociale.</p></div>
    <div><h5>Nos produits</h5><ul><li>Déjeuner</li><li>Cadhoc</li><li>UpOne</li><li>CESU Chèque Domicile</li><li>Chèque Culture</li><li>Chèque Lire</li></ul></div>
    <div><h5>Qui êtes-vous ?</h5><ul><li>Entreprise +50</li><li>Entreprise -50</li><li>CSE</li><li>Commerçants</li><li>Collectivité &amp; Organisme Social</li></ul></div>
    <div><h5>Upcoop</h5><ul><li>Pourquoi choisir Upcoop</li><li>Société à mission</li><li>Blog</li><li>Aide, déjà client</li><li>Contact</li></ul></div>
  </div>
  <div class="legal">Maquette de démonstration datashake, non affiliée à Upcoop : {page_desc} Ajouts GEO signalés par les pastilles, chiffres repris de up.coop, montants indicatifs. <a href="index.html">Voir les autres maquettes</a></div>
</div></footer>'''

HINT_SCRIPT = '''<div class="geo-hint" id="geo-hint"><span class="demo">1</span><span>Cliquez sur les pastilles pour voir le changement GEO</span><button type="button" aria-label="Fermer">&times;</button></div>
<script>
  const hint=document.getElementById('geo-hint');const dismissHint=()=>{if(hint)hint.classList.add('gone');};
  if(hint)hint.querySelector('button').addEventListener('click',e=>{e.stopPropagation();dismissHint();});
  if(location.search.includes('nohint')&&hint)hint.style.display='none';
  document.querySelectorAll('.geo-badge').forEach(btn=>{btn.setAttribute('title','Cliquez pour voir le changement GEO');
    btn.addEventListener('click',e=>{e.stopPropagation();document.body.classList.add('geo-seen');dismissHint();
      const tip=document.getElementById(btn.getAttribute('data-tooltip'));const was=tip.classList.contains('open');
      document.querySelectorAll('.geo-tooltip.open').forEach(t=>t.classList.remove('open'));
      document.querySelectorAll('.geo-badge').forEach(b=>b.setAttribute('aria-expanded','false'));
      if(!was){tip.classList.add('open');btn.setAttribute('aria-expanded','true');}});});
  document.querySelectorAll('.geo-tooltip').forEach(t=>t.addEventListener('click',e=>e.stopPropagation()));
  document.addEventListener('click',()=>{document.querySelectorAll('.geo-tooltip.open').forEach(t=>t.classList.remove('open'));document.querySelectorAll('.geo-badge').forEach(b=>b.setAttribute('aria-expanded','false'));});
</script>'''

def badge(n, kind, title, text):
    return (f'<button class="geo-badge" type="button" data-tooltip="t{n}" aria-expanded="false">{n}</button>'
            f'<div class="geo-tooltip" id="t{n}" role="tooltip"><span class="kind">{kind}</span><strong>{title}</strong><p>{text}</p></div>')

ORG = '''{"@context":"https://schema.org","@type":"Organization","@id":"https://up.coop/#organization","name":"Upcoop","legalName":"Upcoop","alternateName":["Groupe Up","Chèque Déjeuner","Groupe Chèque Déjeuner","Up"],"url":"https://up.coop/","logo":"https://up.coop/wp-content/themes/upcoop/images/logo-upcoop-slim.svg","description":"Coopérative (SCOP) de solutions de paiement et de services à utilité sociale : titre-restaurant UpDéjeuner, titre cadeau Cadhoc, carte multi-avantages UpOne, CESU Chèque Domicile, Chèque Culture, Chèque Lire.","address":{"@type":"PostalAddress","addressLocality":"Gennevilliers","addressCountry":"FR"},"sameAs":["https://www.wikidata.org/wiki/Q3117361","https://fr.wikipedia.org/wiki/Upcoop","https://groupe.up.coop/fr/"],"brand":[{"@type":"Brand","name":"UpDéjeuner"},{"@type":"Brand","name":"Cadhoc"},{"@type":"Brand","name":"UpOne"},{"@type":"Brand","name":"Chèque Domicile"}]}'''
