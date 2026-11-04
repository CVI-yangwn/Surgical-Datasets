"""Theme CSS for the DeepPaperNote HTML reading report."""

CSS = r"""
:root{--bg:#f7f7fb;--bg2:#fff;--card:#fff;--bd:#e3e3ef;--tx:#1d1d2b;--tx2:#4a4a63;--mut:#7a7a93;
--ac:#5b5bd6;--ac2:#c04fa8;--ok:#1f9d63;--warn:#d98a00;--bad:#d64545;--hl:#eef0ff;--dt:#e9f7f1;
--grad:linear-gradient(135deg,#5b5bd6,#8b5cf6,#c04fa8);--r:14px}
[data-theme=dark]{--bg:#0b0b12;--bg2:#12121c;--card:#14141f;--bd:#262640;--tx:#f1f1fb;--tx2:#c4c4dc;--mut:#8a8aa8;
--ac:#8b93ff;--ac2:#f472b6;--ok:#34d399;--warn:#fbbf24;--bad:#ff7b7b;--hl:#1a1b3a;--dt:#102a22}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',Inter,system-ui,sans-serif;background:var(--bg);color:var(--tx);line-height:1.85}
.wrap{max-width:980px;margin:0 auto;padding:0 22px}
.nav{position:fixed;top:0;left:0;right:0;z-index:50;height:54px;display:flex;align-items:center;gap:20px;padding:0 22px;
background:color-mix(in srgb,var(--bg2) 90%,transparent);backdrop-filter:blur(14px);border-bottom:1px solid var(--bd);overflow-x:auto}
.nav b{background:var(--grad);-webkit-background-clip:text;color:transparent;white-space:nowrap}
.nav a{color:var(--mut);font-size:.85em;text-decoration:none;white-space:nowrap;padding:4px 0;border-bottom:2px solid transparent}
.nav a:hover,.nav a.on{color:var(--ac);border-color:var(--ac)}
.nav .sp{flex:1}
.nav button{border:1px solid var(--bd);background:var(--card);color:var(--tx2);border-radius:999px;padding:3px 12px;cursor:pointer;font-size:.8em}
section.blk{padding:84px 0 24px}
h2.sec{font-size:1.6em;font-weight:800;background:var(--grad);-webkit-background-clip:text;color:transparent;margin-bottom:6px}
.desc{color:var(--mut);font-size:.9em;margin-bottom:22px}
.hero h1{font-size:2.1em;line-height:1.3;font-weight:900;margin-bottom:6px}
.hero .sub{font-size:1.05em;color:var(--tx2);margin-bottom:14px}
.meta{color:var(--mut);font-size:.88em;margin-bottom:10px}
.chip{display:inline-block;background:var(--grad);color:#fff;border-radius:999px;padding:3px 14px;font-size:.8em;font-weight:600;margin-right:8px}
.tag{display:inline-block;border:1px solid var(--bd);background:var(--card);color:var(--tx2);border-radius:999px;padding:2px 11px;font-size:.78em;margin:3px 5px 3px 0}
.one{font-size:1.12em;margin:18px 0;padding:16px 20px;border-left:4px solid var(--ac);background:var(--hl);border-radius:0 var(--r) var(--r) 0}
.score{display:inline-flex;align-items:baseline;gap:8px;border:1px solid var(--bd);background:var(--card);border-radius:var(--r);padding:10px 18px;margin-top:6px}
.score .v{font-size:1.9em;font-weight:900;color:var(--ac)}.score .l{color:var(--mut);font-size:.82em}
a.src{color:var(--ac);text-decoration:none;font-size:.9em;margin-left:6px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:var(--r);padding:26px 28px;margin-bottom:24px}
.card h3{font-size:1.2em;margin-bottom:12px;display:flex;align-items:center;gap:10px}
.num{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:var(--grad);color:#fff;font-size:.85em;flex:none}
.card p{margin:10px 0;color:var(--tx2)}.card strong{color:var(--tx)}
.card ul,.card ol{margin:10px 0 10px 1.4em;color:var(--tx2)}.card li{margin:4px 0}
.card h4,.card h5{margin:16px 0 6px;font-size:1.02em}
.card blockquote{border-left:3px solid var(--bd);padding:4px 14px;color:var(--mut);margin:10px 0}
code{background:var(--hl);border-radius:5px;padding:1px 6px;font-size:.9em;font-family:ui-monospace,Menlo,Consolas,monospace}
pre{background:var(--hl);border-radius:10px;padding:12px 14px;overflow-x:auto;margin:10px 0}
.math{overflow-x:auto;margin:12px 0;text-align:center}
.tbl{overflow-x:auto;margin:14px 0}table{border-collapse:collapse;width:100%;font-size:.88em}
th,td{border:1px solid var(--bd);padding:6px 10px;text-align:left}th{background:var(--hl);color:var(--tx)}
.fig{margin:16px 0;text-align:center}.fig img{max-width:100%;border:1px solid var(--bd);border-radius:10px;cursor:zoom-in;background:#fff}
.fig figcaption{color:var(--mut);font-size:.82em;margin-top:6px}
.ph{border:1px dashed var(--bd);border-radius:10px;padding:10px 14px;color:var(--mut);font-size:.88em;margin:12px 0}
.strip{margin-top:14px;padding:10px 14px;border-radius:10px;font-size:.88em;line-height:1.7}
.strip.h{background:var(--hl)}.strip.d{background:var(--dt)}
.strip .t{font-weight:700;margin-right:6px}.strip .i{display:inline-block;margin:2px 10px 2px 0}
.strip.h .i::before{content:"\2022 ";color:var(--ac)}.strip.d .i::before{content:"\2022 ";color:var(--ok)}
.take{display:grid;gap:10px}.take div{background:var(--hl);border-radius:10px;padding:10px 16px;color:var(--tx2)}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
.box{border:1px solid var(--bd);border-radius:var(--r);padding:16px 18px;background:var(--card)}
.box h4{margin-bottom:8px}.box.ok h4{color:var(--ok)}.box.bad h4{color:var(--bad)}.box.q h4{color:var(--warn)}
.box ul{margin-left:1.2em;color:var(--tx2);font-size:.92em}.box li{margin:6px 0}
.round{border:1px solid var(--bd);border-radius:var(--r);padding:14px 18px;background:var(--card);margin-bottom:12px}
.round .h{display:flex;justify-content:space-between;font-weight:700}.round .s{color:var(--ac)}
.round p{color:var(--tx2);font-size:.9em;margin-top:6px}.gates{font-size:.8em;color:var(--mut);margin-top:6px}
.dims{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:6px;margin-top:8px;font-size:.8em;color:var(--mut)}
.dims b{color:var(--tx)}
.note{color:var(--mut);font-size:.82em;margin-top:8px}
footer{text-align:center;color:var(--mut);font-size:.82em;padding:40px 0 60px}
#lb{display:none;position:fixed;inset:0;background:rgba(0,0,0,.86);z-index:99;align-items:center;justify-content:center;cursor:zoom-out}
#lb img{max-width:94vw;max-height:92vh;background:#fff;border-radius:8px}
@media(max-width:640px){.hero h1{font-size:1.5em}.card{padding:18px}}
@media print{.nav,#lb{display:none}section.blk{padding-top:20px}}
"""
