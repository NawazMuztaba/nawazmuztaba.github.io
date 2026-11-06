/**
 * APEX Portfolio — Globe V2.2
 * A luminous geographically recognizable Earth, not an abstract mesh.
 * Orbit and radar lights are illustrative and NOT live SOC telemetry.
 */
import * as THREE from "three";

const host = document.querySelector("[data-globe]");
const canvas = document.getElementById("globe-canvas");
const button = document.getElementById("globe-pause");
const desktop = matchMedia("(min-width: 741px)");
const motion = matchMedia("(prefers-reduced-motion: reduce)");

if (host && canvas && button) {
  const stage = host.querySelector(".globe-stage");
  const owns = [];
  const routes = [];
  const orbitSignals = [];
  const localSignals = [];
  const temp = new THREE.Vector3();
  const clock = new THREE.Clock(false);
  const R = 1.23; // slightly smaller than the original 1.32-radius sphere
  const C = {cyan:0x31e5e2,emerald:0x19d99a,ice:0xb6ffff,red:0xff526d,blue:0x46c8ff};
  let renderer,scene,camera,earth,orbitalRig,baseRig,glowMap,texture,observer,resizeObserver;
  let frame=0,ready=false,initializing=false,disposed=false,visible=false,paused=false,dragging=false;
  let lastX=0,lastY=0;

  const own = item => { owns.push(item); return item; };
  const allowed = () => desktop.matches && !motion.matches;
  const active = () => ready && !disposed && !paused && visible && !document.hidden && allowed();

  function point(lat,lon,r=R) {
    const a=THREE.MathUtils.degToRad(lat), b=THREE.MathUtils.degToRad(lon);
    return new THREE.Vector3(Math.cos(a)*Math.sin(b)*r,Math.sin(a)*r,Math.cos(a)*Math.cos(b)*r);
  }
  function glowTexture() {
    const c=document.createElement("canvas");
    c.width=c.height=128;
    const x=c.getContext("2d");
    const gradient=x.createRadialGradient(64,64,0,64,64,63);
    gradient.addColorStop(0,"rgba(255,255,255,1)");
    gradient.addColorStop(.13,"rgba(255,255,255,.90)");
    gradient.addColorStop(.36,"rgba(180,250,255,.27)");
    gradient.addColorStop(1,"rgba(60,190,245,0)");
    x.fillStyle=gradient;x.fillRect(0,0,128,128);
    const map=own(new THREE.CanvasTexture(c));
    map.colorSpace=THREE.SRGBColorSpace;
    return map;
  }
  function light(parent,position,color,size) {
    const material=own(new THREE.SpriteMaterial({
      map:glowMap,color,transparent:true,opacity:1,
      blending:THREE.AdditiveBlending,depthWrite:false
    }));
    const item=new THREE.Sprite(material);
    item.position.copy(position);item.scale.set(size,size,1);
    parent.add(item);return item;
  }
  function track(parent,positions,color,opacity) {
    const geometry=own(new THREE.BufferGeometry().setFromPoints(positions));
    const material=own(new THREE.LineBasicMaterial({
      color,transparent:true,opacity,depthWrite:false,
      blending:THREE.AdditiveBlending
    }));
    const line=new THREE.Line(geometry,material);
    line.frustumCulled=false;parent.add(line);return line;
  }

  function createEarth() {
    earth=new THREE.Group();
    earth.rotation.set(.09,.69,.03);
    scene.add(earth);

    const geometry=own(new THREE.SphereGeometry(R,96,64));
    const material=own(new THREE.ShaderMaterial({
      uniforms:{earthMap:{value:texture}},
      vertexShader:[
        "varying vec2 texCoord;",
        "varying vec3 normalEye;",
        "varying vec3 eyeVector;",
        "void main(){",
        "texCoord=uv;",
        "vec4 mv=modelViewMatrix*vec4(position,1.0);",
        "normalEye=normalize(normalMatrix*normal);",
        "eyeVector=normalize(-mv.xyz);",
        "gl_Position=projectionMatrix*mv;",
        "}"
      ].join("\n"),
      fragmentShader:[
        "uniform sampler2D earthMap;",
        "varying vec2 texCoord;",
        "varying vec3 normalEye;",
        "varying vec3 eyeVector;",
        "void main(){",
        "vec3 g=texture2D(earthMap,texCoord).rgb;",
        "float land=smoothstep(.025,.09,g.g);",
        "vec3 ocean=vec3(.013,.090,.140);",
        "vec3 mapped=g*vec3(1.80,3.00,2.40)+vec3(.018,.14,.10);",
        "float light=.59+.41*max(dot(normalize(normalEye),normalize(vec3(-.38,.32,.87))),0.);",
        "vec3 col=mix(ocean,mapped,land*.97)*light;",
        "float rim=pow(1.-max(dot(normalize(normalEye),normalize(eyeVector)),0.),2.8);",
        "col+=vec3(.09,.56,.76)*rim*.50;",
        "gl_FragColor=vec4(col,1.);",
        "#include <colorspace_fragment>",
        "}"
      ].join("\n")
    }));
    earth.add(new THREE.Mesh(geometry,material));

    // Fresnel atmosphere gives the globe a bright yet soft cyan rim.
    const atmosphere=own(new THREE.SphereGeometry(R*1.057,80,50));
    const atmosphereMaterial=own(new THREE.ShaderMaterial({
      vertexShader:[
        "varying vec3 n; varying vec3 v;",
        "void main(){vec4 mv=modelViewMatrix*vec4(position,1.);",
        "n=normalize(normalMatrix*normal);v=normalize(-mv.xyz);",
        "gl_Position=projectionMatrix*mv;}"
      ].join("\n"),
      fragmentShader:[
        "varying vec3 n; varying vec3 v;",
        "void main(){float edge=1.-max(dot(normalize(n),normalize(v)),0.);",
        "float alpha=pow(edge,2.45)*.81;",
        "gl_FragColor=vec4(.17,.88,1.,alpha);",
        "#include <colorspace_fragment>",
        "}"
      ].join("\n"),
      transparent:true,depthWrite:false,blending:THREE.AdditiveBlending
    }));
    earth.add(new THREE.Mesh(atmosphere,atmosphereMaterial));

    // Thin lat/long construction lines leave the continents visible.
    for(let lat=-60;lat<=60;lat+=30){
      const positions=[];
      for(let lon=-180;lon<=180;lon+=4)positions.push(point(lat,lon,R*1.006));
      track(earth,positions,C.cyan,.082);
    }
    for(let lon=-180;lon<180;lon+=30){
      const positions=[];
      for(let lat=-88;lat<=88;lat+=4)positions.push(point(lat,lon,R*1.006));
      track(earth,positions,C.cyan,.063);
    }

    const sites=[
      [28,77],[52,13],[41,-74],[1,104],[-34,18],[35,139],
      [25,55],[49,2],[37,-122],[-23,-46],[13,80],[31,121],[55,38],
      [-33,151],[40,116],[19,-99]
    ];
    const pairs=[
      [0,1],[0,5],[0,6],[1,2],[1,7],[2,8],[3,5],
      [4,6],[7,9],[8,10],[5,11],[6,14],[9,15],[11,12]
    ];
    sites.forEach((item,i)=>light(earth,point(...item,R*1.027),
      i%5===0?C.ice:C.emerald,i%5===0?.20:.115));
    pairs.forEach(([a,b],i)=>{
      const start=point(...sites[a],R*1.03),end=point(...sites[b],R*1.03);
      const middle=start.clone().add(end);
      if(middle.length()<.4)return;
      middle.normalize().multiplyScalar(R*1.28);
      const curve=new THREE.QuadraticBezierCurve3(start,middle,end);
      track(earth,curve.getPoints(56),i%5===0?C.red:C.cyan,i%5===0?.40:.27);
      if(i%2===0){
        localSignals.push({
          curve,sprite:light(earth,start,i%5===0?C.red:C.ice,.118),
          phase:(i*.121)%1,speed:i%5===0?.47:.26
        });
      }
    });
  }

  function createOrbits(){
    orbitalRig=new THREE.Group();scene.add(orbitalRig);

    const definitions=[
      {a:1.64,b:.99,rx:.42,ry:.19,rz:.15,c:C.emerald,opacity:.34,speed:.12,tail:.14},
      {a:1.67,b:1.15,rx:-.59,ry:.36,rz:-.17,c:C.cyan,opacity:.30,speed:.19,tail:.12},
      {a:1.59,b:1.22,rx:1.05,ry:-.22,rz:.07,c:C.red,opacity:.31,speed:.40,tail:.16},
      {a:1.64,b:.78,rx:-.79,ry:.31,rz:-.22,c:C.red,opacity:.28,speed:.49,tail:.16},
      {a:1.54,b:1.30,rx:.19,ry:.80,rz:.43,c:C.red,opacity:.22,speed:.55,tail:.12}
    ];
    definitions.forEach((d,i)=>{
      const group=new THREE.Group();
      group.rotation.set(d.rx,d.ry,d.rz);
      orbitalRig.add(group);
      const samples=[];
      for(let k=0;k<145;k++){
        const a=k/145*Math.PI*2;
        samples.push(new THREE.Vector3(d.a*Math.cos(a),d.b*Math.sin(a),.016*Math.sin(a*3)));
      }
      const curve=new THREE.CatmullRomCurve3(samples,true,"centripetal",.5);
      track(group,curve.getPoints(175),d.c,d.opacity);

      // Preallocated geometry: the red radar light really travels along its route.
      const count=35;
      const positions=new Float32Array(count*3);
      const geometry=own(new THREE.BufferGeometry());
      const attribute=new THREE.BufferAttribute(positions,3);
      attribute.setUsage(THREE.DynamicDrawUsage);
      geometry.setAttribute("position",attribute);
      const material=own(new THREE.LineBasicMaterial({
        color:d.c,transparent:true,opacity:d.c===C.red?.99:.89,
        depthWrite:false,blending:THREE.AdditiveBlending
      }));
      const line=new THREE.Line(geometry,material);
      line.frustumCulled=false;
      group.add(line);
      const signal=light(group,new THREE.Vector3(),d.c,d.c===C.red?.28:.26);
      orbitSignals.push({
        curve,attribute,count,signal,phase:i*.17,speed:d.speed,tail:d.tail
      });
    });

    // Sparse technical ring grid + subtle orbital particles.
    [[1.49,.26],[1.81,.12]].forEach(([r,opacity])=>{
      const pts=[];
      for(let j=0;j<=172;j++){
        const a=j/172*Math.PI*2;
        pts.push(new THREE.Vector3(r*Math.cos(a),r*Math.sin(a)*.37,.08));
      }
      track(orbitalRig,pts,C.cyan,opacity);
    });
    const count=145,coords=new Float32Array(count*3);
    for(let i=0;i<count;i++){
      const phi=Math.acos(1-2*(i+.5)/count),theta=i*2.399963;
      const r=1.42+((i*7)%23)/23*.64;
      coords.set([
        r*Math.cos(theta)*Math.sin(phi),
        r*Math.sin(theta)*Math.sin(phi),
        r*Math.cos(phi)
      ],i*3);
    }
    const points=own(new THREE.BufferGeometry());
    points.setAttribute("position",new THREE.BufferAttribute(coords,3));
    const mat=own(new THREE.PointsMaterial({
      color:C.cyan,size:.015,transparent:true,opacity:.44,
      sizeAttenuation:true,depthWrite:false,
      blending:THREE.AdditiveBlending
    }));
    orbitalRig.add(new THREE.Points(points,mat));
  }

  function createBase(){
    baseRig=new THREE.Group();
    baseRig.position.y=-1.55;
    scene.add(baseRig);
    for(const [r,opacity,color] of [
      [1.35,.70,C.cyan],[1.13,.61,C.emerald],
      [.86,.43,C.cyan],[1.64,.27,C.cyan]
    ]){
      const geo=own(new THREE.TorusGeometry(r,.009,3,144));
      const mat=own(new THREE.MeshBasicMaterial({
        color,transparent:true,opacity,depthWrite:false,
        blending:THREE.AdditiveBlending
      }));
      const mesh=new THREE.Mesh(geo,mat);
      mesh.rotation.x=Math.PI/2.55;
      mesh.scale.y=.28;
      baseRig.add(mesh);
    }
  }

  function resize(){
    if(!renderer||!camera)return;
    const w=Math.max(1,stage.clientWidth),h=Math.max(1,stage.clientHeight);
    renderer.setSize(w,h,false);
    camera.aspect=w/h;camera.updateProjectionMatrix();
    if(ready&&!frame)renderer.render(scene,camera);
  }
  function tick(){
    frame=0;
    if(!active())return;
    const dt=Math.min(clock.getDelta(),.05);
    if(!dragging)earth.rotation.y+=dt*.17;
    orbitalRig.rotation.y+=dt*.11;
    orbitalRig.rotation.z+=dt*.025;
    baseRig.rotation.z+=dt*.14;

    for(const route of orbitSignals){
      route.phase=(route.phase+dt*route.speed)%1;
      for(let j=0;j<route.count;j++){
        const t=(route.phase-(route.count-1-j)/(route.count-1)*route.tail+1)%1;
        route.curve.getPoint(t,temp);
        route.attribute.setXYZ(j,temp.x,temp.y,temp.z);
      }
      route.attribute.needsUpdate=true;
      route.curve.getPoint(route.phase,temp);
      route.signal.position.copy(temp);
    }
    for(const p of localSignals){
      p.phase=(p.phase+dt*p.speed)%1;
      p.curve.getPoint(p.phase,temp);
      p.sprite.position.copy(temp);
    }
    renderer.render(scene,camera);
    frame=requestAnimationFrame(tick);
  }
  function sync(){
    host.classList.toggle("paused",!active());
    if(!active()){
      if(frame)cancelAnimationFrame(frame);
      frame=0;clock.stop();return;
    }
    if(!frame){clock.start();frame=requestAnimationFrame(tick);}
  }
  function destroy(){
    if(disposed)return;
    disposed=true;
    if(frame)cancelAnimationFrame(frame);
    frame=0;clock.stop();
    resizeObserver?.disconnect();
    observer?.disconnect();
    for(const item of owns){try{item.dispose()}catch{}}
    texture?.dispose();
    renderer?.dispose();
    host.classList.remove("ready");button.hidden=true;ready=false;
  }
  function initialize(){
    if(initializing||ready||disposed||!allowed())return;
    initializing=true;
    try{
      if(!canvas.getContext("webgl2",{alpha:true,antialias:true})){
        initializing=false;return;
      }
    }catch{
      initializing=false;return;
    }
    new THREE.TextureLoader().load("./assets/earth-texture.svg",map=>{
      if(disposed){map.dispose();return}
      try{
        texture=map;
        map.colorSpace=THREE.SRGBColorSpace;
        scene=new THREE.Scene();
        camera=new THREE.PerspectiveCamera(38,1,.1,60);
        camera.position.set(0,.02,4.85);
        renderer=new THREE.WebGLRenderer({
          canvas,alpha:true,antialias:true,powerPreference:"default"
        });
        renderer.setClearColor(0x000000,0);
        renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));
        renderer.outputColorSpace=THREE.SRGBColorSpace;
        map.anisotropy=Math.min(4,renderer.capabilities.getMaxAnisotropy());
        glowMap=glowTexture();
        createEarth();createOrbits();createBase();
        resize();renderer.render(scene,camera);
        ready=true;initializing=false;
        host.classList.add("ready");button.hidden=false;
        resizeObserver=new ResizeObserver(resize);
        resizeObserver.observe(stage);
        sync();
      }catch(error){
        console.warn("3D globe failed; keeping static fallback.",error);
        destroy();
      }
    },undefined,error=>{
      initializing=false;
      console.warn("Earth asset failed to load; static fallback remains.",error);
    });
  }
  observer=new IntersectionObserver(entries=>{
    visible=Boolean(entries[0]?.isIntersecting);
    if(visible&&!ready)initialize();
    sync();
  },{rootMargin:"140px"});
  observer.observe(host);
  button.addEventListener("click",()=>{
    paused=!paused;
    button.textContent=paused?"Resume animation":"Pause animation";
    button.setAttribute("aria-pressed",String(paused));
    sync();
  });
  document.addEventListener("visibilitychange",sync);
  motion.addEventListener("change",()=>{
    if(motion.matches)paused=true;
    sync();
  });
  desktop.addEventListener("change",()=>{
    if(desktop.matches&&!ready)initialize();
    sync();
  });
  canvas.addEventListener("pointerdown",event=>{
    if(!ready||event.pointerType==="touch")return;
    dragging=true;lastX=event.clientX;lastY=event.clientY;
    canvas.setPointerCapture(event.pointerId);
  });
  canvas.addEventListener("pointermove",event=>{
    if(!ready||!dragging)return;
    earth.rotation.y+=(event.clientX-lastX)*.005;
    earth.rotation.x=THREE.MathUtils.clamp(
      earth.rotation.x+(event.clientY-lastY)*.002,-.36,.36);
    lastX=event.clientX;lastY=event.clientY;
    renderer.render(scene,camera);
  });
  ["pointerup","pointercancel","lostpointercapture"].forEach(eventName=>
    canvas.addEventListener(eventName,()=>dragging=false));
  canvas.addEventListener("webglcontextlost",event=>{
    event.preventDefault();destroy();
  },{once:true});
  addEventListener("pagehide",destroy,{once:true});
}
