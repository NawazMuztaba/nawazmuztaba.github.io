/* The owner's ORIGINAL portfolio globe, copied verbatim from the uploaded HTML.
 * Original script used THREE r128 and a fixed 340 × 340 canvas.
 * Only the DOMContentLoaded integration adapter below is new.
 */
function initThreeJS(){
  const canvas=document.getElementById('tc');
  if(!canvas)return;
  const renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:true});
  renderer.setSize(340,340);renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
  const scene=new THREE.Scene();
  const camera=new THREE.PerspectiveCamera(42,1,0.1,100);
  camera.position.z=3.4;

  // ── LAYER 1: Dense high-detail icosphere wireframe (outer shell)
  const outerGeo=new THREE.IcosahedronGeometry(1.02,5);
  const outerMat=new THREE.MeshBasicMaterial({color:0x00ff41,wireframe:true,transparent:true,opacity:0.07});
  const outerMesh=new THREE.Mesh(outerGeo,outerMat);
  scene.add(outerMesh);

  // ── LAYER 2: Mid-density icosphere (counter-rotating, red tint) — removed, too noisy

  // ── LAYER 3: Low-poly inner core (slowly pulsing)
  const coreGeo=new THREE.IcosahedronGeometry(0.72,2);
  const coreMat=new THREE.MeshBasicMaterial({color:0x00ff41,wireframe:true,transparent:true,opacity:0.14});
  const coreMesh=new THREE.Mesh(coreGeo,coreMat);
  scene.add(coreMesh);

  // ── LAYER 4: Solid dark inner sphere (occlusion illusion)
  const solidGeo=new THREE.SphereGeometry(0.70,32,32);
  const solidMat=new THREE.MeshBasicMaterial({color:0x010801,transparent:true,opacity:0.95});
  scene.add(new THREE.Mesh(solidGeo,solidMat));

  // ── LAYER 5: Surface node points (bright dots scattered on sphere)
  const nodeCount=48;
  const nPos=new Float32Array(nodeCount*3);
  const nData=[];
  for(let i=0;i<nodeCount;i++){
    const th=Math.random()*Math.PI*2;
    const ph=Math.acos(2*Math.random()-1);
    const x=Math.sin(ph)*Math.cos(th);
    const y=Math.sin(ph)*Math.sin(th);
    const z=Math.cos(ph);
    nPos[i*3]=x;nPos[i*3+1]=y;nPos[i*3+2]=z;
    nData.push({x,y,z});
  }
  const nGeo=new THREE.BufferGeometry();
  nGeo.setAttribute('position',new THREE.BufferAttribute(nPos,3));
  // Large glowing nodes
  const bigNodeMat=new THREE.PointsMaterial({color:0x00ff41,size:0.055,transparent:true,opacity:1.0});
  scene.add(new THREE.Points(nGeo,bigNodeMat));
  // Tiny faint secondary dots
  const smallNodeMat=new THREE.PointsMaterial({color:0x00ff41,size:0.022,transparent:true,opacity:0.45});
  scene.add(new THREE.Points(nGeo,smallNodeMat));

  // ── LAYER 6: Attack / connection lines between nodes (curved arcs)
  const lineGroup=new THREE.Group();
  scene.add(lineGroup);
  const linePairs=[];
  const numLines=22;
  for(let i=0;i<numLines;i++){
    const ai=Math.floor(Math.random()*nodeCount);
    const bi=Math.floor(Math.random()*nodeCount);
    if(ai===bi)continue;
    const a=new THREE.Vector3(nData[ai].x,nData[ai].y,nData[ai].z);
    const b=new THREE.Vector3(nData[bi].x,nData[bi].y,nData[bi].z);
    // Build curved arc (lift midpoint above sphere surface)
    const pts=[];
    for(let t=0;t<=24;t++){
      const p=new THREE.Vector3().lerpVectors(a,b,t/24);
      const lift=1+Math.sin(Math.PI*t/24)*0.22;
      p.normalize().multiplyScalar(lift);
      pts.push(p);
    }
    const isAttack=Math.random()>0.45;
    const lGeo=new THREE.BufferGeometry().setFromPoints(pts);
    const lMat=new THREE.LineBasicMaterial({
      color:isAttack?0xff2244:0x00ff41,
      transparent:true,
      opacity:isAttack?0.5:0.2
    });
    lineGroup.add(new THREE.Line(lGeo,lMat));
    linePairs.push({mat:lMat,isAttack,phase:Math.random()*Math.PI*2});
  }

  // ── LAYER 7: Particle shells — two clean shells only
  function makeParticleShell(count,rMin,rMax,color,size,opacity){
    const pos=new Float32Array(count*3);
    for(let i=0;i<count;i++){
      const th=Math.random()*Math.PI*2;
      const ph=Math.acos(2*Math.random()-1);
      const r=rMin+Math.random()*(rMax-rMin);
      pos[i*3]=r*Math.sin(ph)*Math.cos(th);
      pos[i*3+1]=r*Math.sin(ph)*Math.sin(th);
      pos[i*3+2]=r*Math.cos(ph);
    }
    const g=new THREE.BufferGeometry();
    g.setAttribute('position',new THREE.BufferAttribute(pos,3));
    return new THREE.Points(g,new THREE.PointsMaterial({color,size,transparent:true,opacity}));
  }
  const shell1=makeParticleShell(180,1.08,1.20,0x00ff41,0.015,0.45);
  const shell2=makeParticleShell(100,1.28,1.48,0x00e5ff,0.010,0.18);
  scene.add(shell1);scene.add(shell2);

  // ── LAYER 8: 3 clean orbital rings
  function addRing(radius,tubR,rotX,rotY,color,opacity){
    const m=new THREE.Mesh(
      new THREE.TorusGeometry(radius,tubR,2,160),
      new THREE.MeshBasicMaterial({color,transparent:true,opacity})
    );
    m.rotation.x=rotX;m.rotation.y=rotY;
    scene.add(m);return m;
  }
  const ring1=addRing(1.22,0.004, Math.PI/2,    0,       0x00ff41,0.38);
  const ring2=addRing(1.32,0.003,-Math.PI/4,    Math.PI/5, 0xff2244,0.20);
  const ring3=addRing(1.44,0.002, Math.PI/6,    Math.PI/3, 0x00e5ff,0.14);

  // ── LAYER 9: Orbiting satellite dot on ring3
  const satDot=new THREE.Mesh(new THREE.SphereGeometry(0.028,8,8),new THREE.MeshBasicMaterial({color:0xff2244}));
  scene.add(satDot);
  // Second satellite (cyan)
  const satDot2=new THREE.Mesh(new THREE.SphereGeometry(0.020,8,8),new THREE.MeshBasicMaterial({color:0x00e5ff}));
  scene.add(satDot2);

  // ── LAYER 10: Latitude/longitude grid lines (subtle)
  const latLngGroup=new THREE.Group();
  // Latitude lines
  for(let lat=-75;lat<=75;lat+=30){
    const r_lat=Math.cos(lat*Math.PI/180);
    const y_lat=Math.sin(lat*Math.PI/180);
    const latPts=[];
    for(let lng=0;lng<=360;lng+=4){
      latPts.push(new THREE.Vector3(r_lat*Math.cos(lng*Math.PI/180),y_lat,r_lat*Math.sin(lng*Math.PI/180)));
    }
    const latGeo=new THREE.BufferGeometry().setFromPoints(latPts);
    latLngGroup.add(new THREE.Line(latGeo,new THREE.LineBasicMaterial({color:0x00ff41,transparent:true,opacity:0.07})));
  }
  // Longitude lines
  for(let lng=0;lng<180;lng+=30){
    const lngPts=[];
    for(let lat=-90;lat<=90;lat+=3){
      const r_lat=Math.cos(lat*Math.PI/180);
      const y_lat=Math.sin(lat*Math.PI/180);
      lngPts.push(new THREE.Vector3(r_lat*Math.cos(lng*Math.PI/180),y_lat,r_lat*Math.sin(lng*Math.PI/180)));
    }
    const lngGeo=new THREE.BufferGeometry().setFromPoints(lngPts);
    latLngGroup.add(new THREE.Line(lngGeo,new THREE.LineBasicMaterial({color:0x00ff41,transparent:true,opacity:0.06})));
  }
  scene.add(latLngGroup);

  // ── ANIMATION ──
  let frame=0;
  function animate(){
    requestAnimationFrame(animate);frame++;
    outerMesh.rotation.y+=0.0030;outerMesh.rotation.x+=0.0008;
    coreMesh.rotation.y+=0.0060;coreMesh.rotation.x+=0.0015;
    latLngGroup.rotation.y=outerMesh.rotation.y;
    lineGroup.rotation.y=outerMesh.rotation.y;
    lineGroup.rotation.x=outerMesh.rotation.x;
    shell1.rotation.y+=0.0018;
    shell2.rotation.y-=0.0010;shell2.rotation.x+=0.0005;
    ring1.rotation.z+=0.006;
    ring2.rotation.z+=0.009;
    ring3.rotation.z-=0.003;
    // Pulsing opacities
    outerMat.opacity=0.05+Math.sin(frame*0.020)*0.025;
    coreMat.opacity=0.10+Math.sin(frame*0.035)*0.06;
    bigNodeMat.opacity=0.7+Math.sin(frame*0.04)*0.25;
    // Orbiting satellite — ring2 plane
    const sat1Angle=frame*0.025;
    satDot.position.set(
      1.32*Math.cos(sat1Angle),
      1.32*Math.sin(sat1Angle)*Math.sin(-Math.PI/4),
      1.32*Math.sin(sat1Angle)*Math.cos(-Math.PI/4)
    );
    const sat2Angle=frame*0.016+Math.PI;
    satDot2.position.set(
      1.44*Math.cos(sat2Angle)*Math.cos(Math.PI/6),
      1.44*Math.sin(sat2Angle),
      1.44*Math.cos(sat2Angle)*Math.sin(Math.PI/6)
    );
    linePairs.forEach(p=>{
      p.mat.opacity=p.isAttack
        ?(0.18+Math.sin(frame*0.07+p.phase)*0.28)
        :(0.06+Math.sin(frame*0.022+p.phase)*0.10);
    });
    renderer.render(scene,camera);
  }
  animate();
}

// Minimal adapter: initialize after the portfolio HTML has loaded.
// The original initThreeJS() implementation above is reproduced without edits.
window.addEventListener("DOMContentLoaded", () => {
  if (!window.THREE) { console.error("Original globe unavailable: Three.js failed to load."); return; }
  try { initThreeJS(); } catch (error) { console.error("Original globe failed to initialize.", error); }
});
