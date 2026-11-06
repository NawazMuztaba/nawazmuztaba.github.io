/* Motion without a Three.js/WebGL draw loop. Native SVG/CSS only. */
document.addEventListener("DOMContentLoaded",()=>{
 const scene=document.getElementById("scene");
 const svg=document.getElementById("signal-overlay");
 const button=document.getElementById("motion-toggle");
 const reduced=matchMedia("(prefers-reduced-motion: reduce)");
 if(!scene||!svg||!button)return;
 let userPaused=reduced.matches,visible=true;
 const sync=()=>{
   const paused=userPaused||document.hidden||!visible||reduced.matches;
   scene.classList.toggle("paused",paused);
   try{paused?svg.pauseAnimations():svg.unpauseAnimations()}catch{}
   button.textContent=paused?"Resume effects":"Pause effects";
   button.setAttribute("aria-pressed",String(!paused));
 };
 button.addEventListener("click",()=>{userPaused=!userPaused;sync()});
 document.addEventListener("visibilitychange",sync);
 reduced.addEventListener("change",sync);
 const io=new IntersectionObserver(entries=>{
   visible=Boolean(entries[0]?.isIntersecting);sync()
 },{threshold:.01});
 io.observe(scene);sync();
});
