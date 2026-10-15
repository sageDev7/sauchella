"""Agrega al styles.css los componentes de las páginas internas (correr una sola vez)."""
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(D)
c = open("styles.css", encoding="utf8").read()
assert "PÁGINAS INTERNAS" not in c

BASE = r'''/* =========================================================
   PÁGINAS INTERNAS (todo en tonos oscuros de la misma familia)
   ========================================================= */
.nav a[aria-current]::after{transform:scaleX(1)}
.mnav a[aria-current]{color:var(--bronze-l)}

/* ---------- cabecera ---------- */
.ph{position:relative;min-height:72vh;min-height:72svh;display:flex;align-items:flex-end;overflow:hidden;background:var(--ink);isolation:isolate;padding:calc(var(--hdr) + 4rem) 0 5rem}
.ph-short{min-height:0;padding:calc(var(--hdr) + 5rem) 0 4.2rem;background:linear-gradient(120deg,var(--deep) 0%,var(--umber) 100%)}
.ph-bg{position:absolute;inset:-8% 0 0;z-index:-2;background-size:cover;background-repeat:no-repeat;filter:sepia(.35) saturate(.8) brightness(.55);will-change:transform}
.ph:not(.ph-short)::after{content:"";position:absolute;inset:0;z-index:-1;background:
  linear-gradient(95deg,rgba(14,13,12,.95) 0%,rgba(14,13,12,.84) 45%,rgba(22,19,15,.4) 100%),
  linear-gradient(0deg,rgba(14,13,12,.92) 0%,transparent 55%)}
.ph-in{position:relative;z-index:1;width:100%}
.crumbs{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;margin-bottom:1.6rem;font-size:.7rem;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--muted-l)}
.crumbs li{display:flex;align-items:center;gap:.5rem}
.crumbs a{transition:color .3s}
.crumbs a:hover{color:var(--bronze-l)}
.crumbs i{font-size:.8rem;color:var(--bronze)}
.crumbs [aria-current]{color:var(--bronze-l)}
.ph-h1{font-size:clamp(2.4rem,4.8vw,4.2rem);line-height:1.08;max-width:min(100%,16em);letter-spacing:-.015em}
.ph-h1 em{display:block;font-style:italic;color:var(--bronze-l)}
.ph-h1 em .w{font-style:italic}
.ph .lead{margin-top:1.4rem;max-width:40rem}
.ph-ctas{display:flex;flex-wrap:wrap;gap:1rem;margin-top:2.2rem}

/* ---------- perfil ---------- */
.bio{padding:140px 0;background:var(--umber)}
.hitos-sec{padding:110px 0;background:var(--deep)}
.tl-h{position:relative;display:grid;grid-template-columns:repeat(4,1fr);gap:2rem}
.tl-h::before{content:"";position:absolute;left:0;right:0;top:2.55rem;height:1px;background:linear-gradient(90deg,var(--bronze-d),var(--bronze-l),var(--bronze-d))}
.tl-h li{position:relative;padding-top:3.6rem}
.tl-h li::before{content:"";position:absolute;left:0;top:2.55rem;width:11px;height:11px;margin-top:-5px;border-radius:50%;background:var(--deep);border:1px solid var(--bronze-l)}
.tl-h b{position:absolute;top:0;left:0;font-family:var(--head);font-weight:400;font-style:italic;font-size:1.5rem;color:var(--bronze-l);white-space:nowrap}
.tl-h h3{margin-bottom:.4rem;font-size:1.3rem}
.tl-h p{font-size:.95rem;color:var(--muted-l)}
.tl-h li.reveal:nth-child(2){transition-delay:.1s}.tl-h li.reveal:nth-child(3){transition-delay:.2s}.tl-h li.reveal:nth-child(4){transition-delay:.3s}
.principios{padding:140px 0;background:var(--umber-2)}
.princ-list{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
.princ-list li{padding:2.4rem 2.2rem;background:rgba(11,10,8,.3);border:1px solid var(--line-l);border-top:2px solid var(--bronze)}
.princ-list .m-n{display:block;margin-bottom:1.2rem;font-size:2rem}
.princ-list h3{margin-bottom:.6rem;font-size:1.5rem}
.princ-list p{color:var(--muted-l)}
.princ-list li.reveal:nth-child(2){transition-delay:.1s}.princ-list li.reveal:nth-child(3){transition-delay:.2s}
.cita-c{max-width:44rem;margin:4.5rem auto 0;padding:1.6rem 0 0;border-left:0;border-top:1px solid var(--bronze);text-align:center;font-size:1.35rem}

/* ---------- intervención en juicio ---------- */
.bloques{padding:130px 0;background:var(--deep)}
.bloque{display:grid;grid-template-columns:.85fr 1.15fr;gap:5rem;padding:4rem 0;border-top:1px solid var(--line-l)}
.bloque:last-child{border-bottom:1px solid var(--line-l)}
.bloque-head{display:flex;align-items:baseline;gap:1.4rem}
.bloque-head .m-n{font-size:3rem}
.bloque-head h2{font-size:clamp(1.8rem,3vw,2.5rem)}
.bloque-key{margin-bottom:1.1rem;font-family:var(--head);font-style:italic;font-size:1.35rem;line-height:1.45;color:var(--bronze-l)}
.bloque-body p:not(.bloque-key){margin-bottom:1rem;color:var(--muted-l)}
.instruccion{padding:130px 0;background:var(--umber-2)}
.instr-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:5rem;align-items:center}
.instruccion .lead{margin-bottom:2rem;color:var(--bone)}

/* ---------- cierre ---------- */
.cta-band{position:relative;padding:130px 0;background:var(--night);text-align:center}
.cta-band::before{content:"";position:absolute;left:50%;top:0;width:min(420px,60vw);height:1px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,var(--bronze),transparent)}
.cta-band .h2{max-width:44rem;margin:0 auto}
.cta-band .lead{max-width:36rem;margin:1.2rem auto 0}
.cta-ctas{display:flex;justify-content:center;flex-wrap:wrap;gap:1rem;margin-top:2.3rem}

/* ---------- preguntas (página) ---------- */
.faq-page{padding:110px 0 130px}
.faq-page-in{max-width:52rem}
.faq-page .faq-note{margin-top:2.6rem}

/* ---------- privacidad ---------- */
.legal{padding:100px 0 130px;background:var(--umber)}
.legal-in{max-width:46rem}
.legal-date{margin-bottom:2.4rem;font-size:.85rem;font-weight:600;color:var(--bronze-l)}
.legal h2{margin:2.6rem 0 .8rem;font-size:1.45rem}
.legal p,.legal li{color:var(--muted-l)}
.legal p+p{margin-top:.8rem}
.legal ul{display:grid;gap:.5rem;margin:.8rem 0}
.legal li{position:relative;padding-left:1.3rem}
.legal li::before{content:"";position:absolute;left:0;top:.8em;width:.55rem;height:1px;background:var(--bronze)}
.legal b{color:var(--bone)}

/* ---------- 404 ---------- */
.nf{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:center;overflow:hidden;background:var(--ink);isolation:isolate;padding:calc(var(--hdr) + 3rem) 0 4rem}
.nf-bg{position:absolute;inset:0;z-index:-2;background:url('./img/pasillo.jpg') center/cover no-repeat;filter:sepia(.35) brightness(.45)}
.nf::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(95deg,rgba(14,13,12,.97) 0%,rgba(14,13,12,.85) 55%,rgba(22,19,15,.55) 100%)}
.nf-num{display:block;margin-bottom:1rem;font-family:var(--head);font-style:italic;font-size:clamp(6rem,14vw,11rem);line-height:.85;color:var(--bronze)}
.nf .lead{margin-top:1.3rem;max-width:34rem}

'''
RESP = r'''
/* ---------- páginas internas: responsive ---------- */
@media (max-width:1024px){
  .tl-h{grid-template-columns:1fr 1fr;gap:2.4rem 2rem}
  .tl-h::before{display:none}
  .tl-h li::before{display:none}
  .tl-h li{padding-top:0;border-top:1px solid var(--bronze)}
  .tl-h b{position:static;display:block;margin:1.2rem 0 .7rem;line-height:1.2}
  .princ-list{grid-template-columns:1fr}
  .bloque,.instr-grid{grid-template-columns:1fr;gap:1.6rem}
}
@media (max-width:768px){
  .ph{min-height:0;padding:calc(var(--hdr) + 3.5rem) 0 4rem;text-align:center}
  .ph-short{padding:calc(var(--hdr) + 3rem) 0 3.2rem}
  .ph:not(.ph-short)::after{background:linear-gradient(180deg,rgba(14,13,12,.8) 0%,rgba(14,13,12,.86) 55%,rgba(14,13,12,.97) 100%)}
  .crumbs{justify-content:center;font-size:.62rem;letter-spacing:.14em}
  .ph-h1{font-size:clamp(1.75rem,8.2vw,2.5rem);max-width:none}
  .ph-h1 em{font-size:1.12em}
  .ph .lead{margin-left:auto;margin-right:auto;font-size:1rem}
  .ph-ctas{flex-direction:column;align-items:center}
  .ph-ctas .btn{width:100%;max-width:300px}
  .bio,.principios,.bloques,.instruccion,.cta-band,.legal{padding:84px 0}
  .hitos-sec{padding:70px 0}
  .faq-page{padding:70px 0 84px}
  .tl-h{grid-template-columns:1fr;text-align:center}
  .tl-h b{transform:none}
  .princ-list li{padding:2rem 1.4rem;text-align:center}
  .cita-c{font-size:1.15rem;margin-top:3rem}
  .bloque{padding:3rem 0;text-align:center}
  .bloque-head{flex-direction:column;align-items:center;gap:.4rem}
  .instr-grid>div{text-align:center}
  .cta-ctas{flex-direction:column;align-items:center}
  .cta-ctas .btn{width:100%;max-width:300px}
  .faq-page .faq-note{text-align:center}
  .nf{text-align:center}
  .nf .lead{margin-left:auto;margin-right:auto}
}
'''
i = c.index("/* =========================================================\n   RESPONSIVE")
c = c[:i] + BASE + c[i:] + RESP
open("styles.css", "w", encoding="utf8").write(c)
print("ok")
