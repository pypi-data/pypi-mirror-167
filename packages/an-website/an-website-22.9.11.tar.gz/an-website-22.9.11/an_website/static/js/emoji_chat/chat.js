"use strict";// @license magnet:?xt=urn:btih:0b31508aeb0634b347b8270c7bee4d411b5d4109&dn=agpl-3.0.txt GNU-AGPL-3.0-or-later
(()=>{const o=elById("message-input"),p=o.form,g=elById("message-section"),i=elById("open-moji-attribution"),c=elById("connection-state"),u=elById("current-user");let s=100,a=0,l="";const v=e=>new Date(e+16510752e5).toLocaleString(),b=e=>{const t=document.createElement("div");if(i&&i.getAttribute("type")!=="font"){for(const n of e.author)t.append(d(n));t.innerHTML+=": ";for(const n of e.content)t.append(d(n))}else t.innerText=`${e.author.join("")}: ${e.content.join("")}`;t.setAttribute("tooltip",v(e.timestamp)),g.append(t)},k=e=>{if(u.innerHTML="",i&&i.getAttribute("type")!=="font"){for(const t of e)u.append(d(t));return}u.innerText=e.join("")},d=e=>{const t=[...e].map(M=>M.codePointAt(0).toString(16).padStart(4,"0")).join("-").toUpperCase(),n=document.createElement("img");return n.src=`/static/img/openmoji-svg-14.0/${t}.svg`,n.classList.add("emoji"),n.alt=e,n},f=()=>{l&&!o.value&&(o.value=l,l="")},r=e=>{let t;if(c.onclick=()=>{},e==="connecting")t="Versuche mit WebSocket zu verbinden";else if(e==="connected")t="Mit WebSocket verbunden!";else if(e==="disconnected")t="Verbindung getrennt. Drücke hier um erneut zu versuchen.",c.onclick=()=>{a=0,s=500,c.onclick=()=>{},m()};else{console.error("invalid state",e);return}c.setAttribute("state",e),c.setAttribute("tooltip",t)},y=e=>{const t=JSON.parse(e.data);switch(t.type){case"messages":{g.innerText="";for(const n of t.messages)b(n);break}case"message":{b(t.message);break}case"init":{k(t.current_user),console.log("Connected as",t.current_user.join("")),r("connected"),s=100,a=0;break}case"users":{console.debug("Recieved users data",t.users);break}case"ratelimit":{f(),alert(`Retry after ${t["Retry-After"]} seconds.`);break}case"error":{f(),alert(t.error);break}default:console.error(`Invalid type ${t.type}`)}},m=()=>{r("connecting");const e=new WebSocket((window.location.protocol==="https:"?"wss:":"ws:")+`//${window.location.host}/websocket/emoji-chat`),t=setInterval(()=>e.send(""),1e4);e.onclose=n=>{if(p.onsubmit=()=>{},n.wasClean){console.debug(`Connection closed cleanly, code=${n.code} reason=${n.reason}`),r("disconnected");return}if(console.debug(`Connection closed, reconnecting in ${s}ms`),r("connecting"),clearInterval(t),a>20){r("disconnected");return}setTimeout(()=>{s=Math.max(500,Math.floor(Math.min(15e3,1.5*s-200))),a++,m()},s)},e.onopen=n=>console.debug("Opened WebSocket",n),e.onmessage=y,p.onsubmit=n=>{o.value!==""&&(l=o.value,e.send(JSON.stringify({type:"message",message:o.value})),o.value=""),n.preventDefault()}};m()})();// @license-end
//# sourceMappingURL=chat.js.map
