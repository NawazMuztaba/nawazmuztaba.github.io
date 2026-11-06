import * as THREE from "three";

const visual=document.querySelector("[data-globe]");
const canvas=document.getElementById("globe-canvas");
const pauseButton=document.getElementById("globe-pause");
const motionQuery=window.matchMedia("(prefers-reduced-motion: reduce)");
const desktopQuery=window.matchMedia("(min-width: 741px)");
const ACTIVE=()=>desktopQuery.matches && !motionQuery.matches;

if(visual && canvas && pauseButton && ACTIVE()){
  let renderer,scene,camera,earthGroup,ringGroup,earthMaterial,frameId=0,lastTime=0;
  let ready=false,visible=true,paused=false,drag=false,lastX=0,resizeObserver;
  let arcs=[],pulses=[],owned=[],texture=null,disposed=false;

  const spherical=(lat,lon,r=1.32)=>{
    const a=THREE.MathUtils.degToRad(lat),b=THREE.MathUtils.degToRad(lon);
    return new THREE.Vector3(Math.cos(a)*Math.sin(b)*r,Math.sin(a)*r,Math.cos(a)*Math.cos(b)*r);
  };
  function line(points,color,opacity){
    const g=new THREE.BufferGeometry().setFromPoints(points);
    const m=new THREE.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false});
    owned.push(g,m);
    return new THREE.Line(g,m);
  }
  function buildScene(map){
    scene=new THREE.Scene();
    camera=new THREE.PerspectiveCamera(39,1,.1,100);
    camera.position.set(0,.06,5.2);
    renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true,powerPreference:"low-power"});
    renderer.setClearColor(0x000000,0);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.5));
    map.colorSpace=THREE.SRGBColorSpace;
    map.anisotropy=Math.min(4,renderer.capabilities.getMaxAnisotropy());
    texture=map;

    earthGroup=new THREE.Group();
    earthGroup.rotation.set(.13,.45,.04);
    scene.add(earthGroup);
    const globeGeo=new THREE.SphereGeometry(1.32,68,48);
    earthMaterial=new THREE.MeshBasicMaterial({map,color:0xffffff});
    owned.push(globeGeo,earthMaterial);
    earthGroup.add(new THREE.Mesh(globeGeo,earthMaterial));

    const gridMat=new THREE.LineBasicMaterial({color:0x4f9daa,transparent:true,opacity:.13,depthWrite:false});
    owned.push(gridMat);
    for(let lat=-60;lat<=60;lat+=30){
      const pts=[];for(let lon=-180;lon<=180;lon+=3)pts.push(spherical(lat,lon,1.324));
      const g=new THREE.BufferGeometry().setFromPoints(pts);owned.push(g);
      earthGroup.add(new THREE.Line(g,gridMat));
    }
    for(let lon=0;lon<180;lon+=30){
      const pts=[];for(let lat=-90;lat<=90;lat+=3)pts.push(spherical(lat,lon,1.324));
      const g=new THREE.BufferGeometry().setFromPoints(pts);owned.push(g);
      earthGroup.add(new THREE.Line(g,gridMat));
    }

    const locations=[
      [28,77],[51,-.1],[40,-74],[1,104],[-34,18],[35,139],[25,55],
      [48,2],[37,-122],[-23,-46],[13,80],[31,121]
    ];
    const pairs=[[0,1],[0,5],[0,6],[1,2],[1,7],[2,8],[3,5],[4,6],[7,9],[8,10],[5,11]];
    const nodeGeo=new THREE.SphereGeometry(.024,8,6);
    const nodeMat=new THREE.MeshBasicMaterial({color:0x7effd2});
    owned.push(nodeGeo,nodeMat);
    for(const [lat,lon] of locations){
      const node=new THREE.Mesh(nodeGeo,nodeMat);
      node.position.copy(spherical(lat,lon,1.352));
      earthGroup.add(node);
    }
    for(let i=0;i<pairs.length;i++){
      const [a,b]=pairs[i],start=spherical(...locations[a],1.36),end=spherical(...locations[b],1.36);
      const mid=start.clone().add(end).normalize().multiplyScalar(1.67);
      if(start.clone().add(end).length()<.2)continue;
      const curve=new THREE.QuadraticBezierCurve3(start,mid,end);
      const points=curve.getPoints(46);
      const arc=line(points,i%3===0?0x2afad0:0x40c9ef,i%3===0?.47:.27);
      earthGroup.add(arc);
      arcs.push(curve);
    }
    const pulseGeo=new THREE.SphereGeometry(.033,8,8);
    const pulseMat=new THREE.MeshBasicMaterial({color:0x96ffcf});
    owned.push(pulseGeo,pulseMat);
    for(let i=0;i<Math.min(5,arcs.length);i++){
      const dot=new THREE.Mesh(pulseGeo,pulseMat);
      dot.userData={curve:arcs[i*2],phase:i/5};
      earthGroup.add(dot);pulses.push(dot);
    }

    ringGroup=new THREE.Group();scene.add(ringGroup);
    const ringDefs=[
      [1.68,.0038,.52,-.38,0x19d99a,.64],
      [1.83,.0030,-.32,.71,0x31e5e2,.46],
      [1.57,.0025,1.13,.21,0x45eddd,.29]
    ];
    for(const [radius,tube,rx,ry,color,opacity] of ringDefs){
      const g=new THREE.TorusGeometry(radius,tube,3,165);
      const m=new THREE.MeshBasicMaterial({color,transparent:true,opacity,depthWrite:false});
      const ring=new THREE.Mesh(g,m);ring.rotation.set(rx,ry,0);
      ringGroup.add(ring);owned.push(g,m);
    }
    const haloGeo=new THREE.SphereGeometry(1.385,40,28);
    const haloMat=new THREE.MeshBasicMaterial({color:0x1bdde2,transparent:true,opacity:.06,side:THREE.BackSide,depthWrite:false});
    owned.push(haloGeo,haloMat);
    scene.add(new THREE.Mesh(haloGeo,haloMat));
    resize();
  }
  function resize(){
    if(!renderer||!camera)return;
    const stage=visual.querySelector(".globe-stage");
    const w=Math.max(1,Math.round(stage.clientWidth));
    const h=Math.max(1,Math.round(stage.clientHeight));
    renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();
    if(ready&&!frameId)renderer.render(scene,camera);
  }
  function shouldRun(){return ready && !paused && visible && !document.hidden && ACTIVE() && !disposed}
  function tick(t){
    frameId=0;
    if(!shouldRun())return;
    const delta=Math.min(.05,(t-(lastTime||t))/1000);lastTime=t;
    if(!drag)earthGroup.rotation.y+=delta*.14;
    ringGroup.rotation.z+=delta*.032;
    ringGroup.rotation.y+=delta*.018;
    pulses.forEach((dot,i)=>dot.position.copy(dot.userData.curve.getPoint(((t*.00011)+(i*.21)+dot.userData.phase)%1)));
    renderer.render(scene,camera);
    frameId=requestAnimationFrame(tick);
  }
  function updateAnimation(){
    if(!shouldRun()){if(frameId)cancelAnimationFrame(frameId);frameId=0;lastTime=0;return}
    if(!frameId)frameId=requestAnimationFrame(tick);
  }
  function initialize(){
    if(disposed || ready || !ACTIVE())return;
    let gl;
    try{gl=canvas.getContext("webgl2",{alpha:true,antialias:true});}catch{}
    if(!gl)return; // Accessible static SVG remains visible.
    const loader=new THREE.TextureLoader();
    loader.load("./assets/earth-texture.svg",map=>{
      if(disposed){map.dispose();return}
      try{
        buildScene(map);ready=true;visual.classList.add("ready");
        pauseButton.hidden=false;
        renderer.render(scene,camera);
        resizeObserver=new ResizeObserver(resize);
        resizeObserver.observe(visual.querySelector(".globe-stage"));
        updateAnimation();
      }catch(err){console.warn("3D globe unavailable; static fallback retained.",err);destroy();}
    },undefined,()=>console.warn("Earth texture unavailable; static fallback retained."));
  }
  function destroy(){
    disposed=true;
    if(frameId)cancelAnimationFrame(frameId);
    resizeObserver?.disconnect();
    owned.forEach(x=>{try{x.dispose?.()}catch{}});
    texture?.dispose();
    renderer?.dispose();
    visual.classList.remove("ready");pauseButton.hidden=true;
    ready=false;frameId=0;
  }

  const viewObs=new IntersectionObserver(entries=>{visible=entries[0]?.isIntersecting??false;if(visible&&!ready)initialize();updateAnimation()},{rootMargin:"120px"});
  viewObs.observe(visual);
  pauseButton.addEventListener("click",()=>{
    paused=!paused;pauseButton.textContent=paused?"Resume animation":"Pause animation";
    pauseButton.setAttribute("aria-pressed",String(paused));updateAnimation();
  });
  document.addEventListener("visibilitychange",updateAnimation);
  motionQuery.addEventListener("change",()=>{if(motionQuery.matches){paused=true;updateAnimation()}});
  desktopQuery.addEventListener("change",()=>{if(!desktopQuery.matches){paused=true;updateAnimation()}});
  canvas.addEventListener("pointerdown",event=>{if(event.pointerType==="mouse"||event.pointerType==="pen"){drag=true;lastX=event.clientX;canvas.setPointerCapture(event.pointerId)}});
  canvas.addEventListener("pointermove",event=>{if(!drag||!ready)return;earthGroup.rotation.y+=(event.clientX-lastX)*.005;lastX=event.clientX;renderer.render(scene,camera)});
  for(const ev of ["pointerup","pointercancel","lostpointercapture"])canvas.addEventListener(ev,()=>drag=false);
  canvas.addEventListener("webglcontextlost",e=>{e.preventDefault();destroy()},{once:true});
  window.addEventListener("pagehide",()=>{viewObs.disconnect();destroy()},{once:true});
}
