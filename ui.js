const toggle=document.getElementById("menu-toggle");
const nav=document.getElementById("primary-navigation");
if(toggle&&nav){
  const close=()=>{nav.classList.remove("open");toggle.setAttribute("aria-expanded","false")};
  toggle.addEventListener("click",()=>{const opening=!nav.classList.contains("open");nav.classList.toggle("open",opening);toggle.setAttribute("aria-expanded",String(opening));});
  nav.querySelectorAll("a").forEach(a=>a.addEventListener("click",close));
  document.addEventListener("keydown",e=>{if(e.key==="Escape"&&nav.classList.contains("open")){close();toggle.focus()}});
  document.addEventListener("pointerdown",e=>{if(!nav.contains(e.target)&&!toggle.contains(e.target))close()});
  window.addEventListener("resize",()=>{if(window.innerWidth>900)close()});
}
