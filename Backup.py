<!DOCTYPE html><html dir="rtl" lang="ar"><head>

<script class="injected-ffc2e83d85">
(function(){'use strict';function q(b){var c=0;return function(){return c<b.length?{done:!1,value:b[c++]}:{done:!0}}}function t(b){var c=typeof Symbol!="undefined"&&Symbol.iterator&&b[Symbol.iterator];if(c)return c.call(b);if(typeof b.length=="number")return{next:q(b)};throw Error(String(b)+" is not an iterable or ArrayLike");}var u=typeof Object.defineProperties=="function"?Object.defineProperty:function(b,c,g){if(b==Array.prototype||b==Object.prototype)return b;b[c]=g.value;return b};
function v(b){b=["object"==typeof globalThis&&globalThis,b,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var c=0;c<b.length;++c){var g=b[c];if(g&&g.Math==Math)return g}throw Error("Cannot find global object");}var w=v(this);function x(b,c){if(c)a:{var g=w;b=b.split(".");for(var h=0;h<b.length-1;h++){var l=b[h];if(!(l in g))break a;g=g[l]}b=b[b.length-1];h=g[b];c=c(h);c!=h&&c!=null&&u(g,b,{configurable:!0,writable:!0,value:c})}}
function y(){this.j=!1;this.g=null;this.u=void 0;this.h=1;this.v=this.l=0;this.i=null}function z(b){if(b.j)throw new TypeError("Generator is already running");b.j=!0}y.prototype.o=function(b){this.u=b};function A(b,c){b.i={I:c,J:!0};b.h=b.l||b.v}y.prototype.return=function(b){this.i={return:b};this.h=this.v};function B(b){this.g=new y;this.h=b}function E(b,c){z(b.g);var g=b.g.g;if(g)return F(b,"return"in g?g["return"]:function(h){return{value:h,done:!0}},c,b.g.return);b.g.return(c);return G(b)}
function F(b,c,g,h){try{var l=c.call(b.g.g,g);if(!(l instanceof Object))throw new TypeError("Iterator result "+l+" is not an object");if(!l.done)return b.g.j=!1,l;var m=l.value}catch(f){return b.g.g=null,A(b.g,f),G(b)}b.g.g=null;h.call(b.g,m);return G(b)}function G(b){for(;b.g.h;)try{var c=b.h(b.g);if(c)return b.g.j=!1,{value:c.value,done:!1}}catch(g){b.g.u=void 0,A(b.g,g)}b.g.j=!1;if(b.g.i){c=b.g.i;b.g.i=null;if(c.J)throw c.I;return{value:c.return,done:!0}}return{value:void 0,done:!0}}
function H(b){this.next=function(c){z(b.g);b.g.g?c=F(b,b.g.g.next,c,b.g.o):(b.g.o(c),c=G(b));return c};this.throw=function(c){z(b.g);b.g.g?c=F(b,b.g.g["throw"],c,b.g.o):(A(b.g,c),c=G(b));return c};this.return=function(c){return E(b,c)};this[Symbol.iterator]=function(){return this}}function I(b){function c(h){return b.next(h)}function g(h){return b.throw(h)}return new Promise(function(h,l){function m(f){f.done?h(f.value):Promise.resolve(f.value).then(c,g).then(m,l)}m(b.next())})}
x("Symbol",function(b){function c(m){if(this instanceof c)throw new TypeError("Symbol is not a constructor");return new g(h+(m||"")+"_"+l++,m)}function g(m,f){this.g=m;u(this,"description",{configurable:!0,writable:!0,value:f})}if(b)return b;g.prototype.toString=function(){return this.g};var h="jscomp_symbol_"+(Math.random()*1E9>>>0)+"_",l=0;return c});
x("Symbol.iterator",function(b){if(b)return b;b=Symbol("Symbol.iterator");u(Array.prototype,b,{configurable:!0,writable:!0,value:function(){return J(q(this))}});return b});function J(b){b={next:b};b[Symbol.iterator]=function(){return this};return b}
x("Promise",function(b){function c(f){this.h=0;this.i=void 0;this.g=[];this.u=!1;var a=this.j();try{f(a.resolve,a.reject)}catch(d){a.reject(d)}}function g(){this.g=null}function h(f){return f instanceof c?f:new c(function(a){a(f)})}if(b)return b;g.prototype.h=function(f){if(this.g==null){this.g=[];var a=this;this.i(function(){a.l()})}this.g.push(f)};var l=w.setTimeout;g.prototype.i=function(f){l(f,0)};g.prototype.l=function(){for(;this.g&&this.g.length;){var f=this.g;this.g=[];for(var a=0;a<f.length;++a){var d=
f[a];f[a]=null;try{d()}catch(e){this.j(e)}}}this.g=null};g.prototype.j=function(f){this.i(function(){throw f;})};c.prototype.j=function(){function f(e){return function(k){d||(d=!0,e.call(a,k))}}var a=this,d=!1;return{resolve:f(this.D),reject:f(this.l)}};c.prototype.D=function(f){if(f===this)this.l(new TypeError("A Promise cannot resolve to itself"));else if(f instanceof c)this.G(f);else{a:switch(typeof f){case "object":var a=f!=null;break a;case "function":a=!0;break a;default:a=!1}a?this.C(f):this.o(f)}};
c.prototype.C=function(f){var a=void 0;try{a=f.then}catch(d){this.l(d);return}typeof a=="function"?this.H(a,f):this.o(f)};c.prototype.l=function(f){this.v(2,f)};c.prototype.o=function(f){this.v(1,f)};c.prototype.v=function(f,a){if(this.h!=0)throw Error("Cannot settle("+f+", "+a+"): Promise already settled in state"+this.h);this.h=f;this.i=a;this.h===2&&this.F();this.K()};c.prototype.F=function(){var f=this;l(function(){if(f.B()){var a=w.console;typeof a!=="undefined"&&a.error(f.i)}},1)};c.prototype.B=
function(){if(this.u)return!1;var f=w.CustomEvent,a=w.Event,d=w.dispatchEvent;if(typeof d==="undefined")return!0;typeof f==="function"?f=new f("unhandledrejection",{cancelable:!0}):typeof a==="function"?f=new a("unhandledrejection",{cancelable:!0}):(f=w.document.createEvent("CustomEvent"),f.initCustomEvent("unhandledrejection",!1,!0,f));f.promise=this;f.reason=this.i;return d(f)};c.prototype.K=function(){if(this.g!=null){for(var f=0;f<this.g.length;++f)m.h(this.g[f]);this.g=null}};var m=new g;c.prototype.G=
function(f){var a=this.j();f.A(a.resolve,a.reject)};c.prototype.H=function(f,a){var d=this.j();try{f.call(a,d.resolve,d.reject)}catch(e){d.reject(e)}};c.prototype.then=function(f,a){function d(n,r){return typeof n=="function"?function(C){try{e(n(C))}catch(D){k(D)}}:r}var e,k,p=new c(function(n,r){e=n;k=r});this.A(d(f,e),d(a,k));return p};c.prototype.catch=function(f){return this.then(void 0,f)};c.prototype.A=function(f,a){function d(){switch(e.h){case 1:f(e.i);break;case 2:a(e.i);break;default:throw Error("Unexpected state: "+
e.h);}}var e=this;this.g==null?m.h(d):this.g.push(d);this.u=!0};c.resolve=h;c.reject=function(f){return new c(function(a,d){d(f)})};c.race=function(f){return new c(function(a,d){for(var e=t(f),k=e.next();!k.done;k=e.next())h(k.value).A(a,d)})};c.all=function(f){var a=t(f),d=a.next();return d.done?h([]):new c(function(e,k){function p(C){return function(D){n[C]=D;r--;r==0&&e(n)}}var n=[],r=0;do n.push(void 0),r++,h(d.value).A(p(n.length-1),k),d=a.next();while(!d.done)})};return c});
function K(b,c){return Object.prototype.hasOwnProperty.call(b,c)}x("Object.is",function(b){return b?b:function(c,g){return c===g?c!==0||1/c===1/g:c!==c&&g!==g}});x("Array.prototype.includes",function(b){return b?b:function(c,g){var h=this;h instanceof String&&(h=String(h));var l=h.length;g=g||0;for(g<0&&(g=Math.max(g+l,0));g<l;g++){var m=h[g];if(m===c||Object.is(m,c))return!0}return!1}});
x("String.prototype.includes",function(b){return b?b:function(c,g){if(this==null)throw new TypeError("The 'this' value for String.prototype.includes must not be null or undefined");if(c instanceof RegExp)throw new TypeError("First argument to String.prototype.includes must not be a regular expression");return this.indexOf(c,g||0)!==-1}});
x("WeakMap",function(b){function c(d){this.g=(a+=Math.random()+1).toString();if(d){d=t(d);for(var e;!(e=d.next()).done;)e=e.value,this.set(e[0],e[1])}}function g(){}function h(d){var e=typeof d;return e==="object"&&d!==null||e==="function"}function l(d){if(!K(d,f)){var e=new g;u(d,f,{value:e})}}function m(d){var e=Object[d];e&&(Object[d]=function(k){if(k instanceof g)return k;Object.isExtensible(k)&&l(k);return e(k)})}if(function(){if(!b||!Object.seal)return!1;try{var d=Object.seal({}),e=Object.seal({}),
k=new b([[d,2],[e,3]]);if(k.get(d)!=2||k.get(e)!=3)return!1;k.delete(d);k.set(e,4);return!k.has(d)&&k.get(e)==4}catch(p){return!1}}())return b;var f="$jscomp_hidden_"+Math.random();m("freeze");m("preventExtensions");m("seal");var a=0;c.prototype.set=function(d,e){if(!h(d))throw Error("Invalid WeakMap key");l(d);if(!K(d,f))throw Error("WeakMap key fail: "+d);d[f][this.g]=e;return this};c.prototype.get=function(d){return h(d)&&K(d,f)?d[f][this.g]:void 0};c.prototype.has=function(d){return h(d)&&K(d,
f)&&K(d[f],this.g)};c.prototype.delete=function(d){return h(d)&&K(d,f)&&K(d[f],this.g)?delete d[f][this.g]:!1};return c});
x("Map",function(b){function c(){var a={};return a.m=a.next=a.head=a}function g(a,d){var e=a[1];return J(function(){if(e){for(;e.head!=a[1];)e=e.m;for(;e.next!=e.head;)return e=e.next,{done:!1,value:d(e)};e=null}return{done:!0,value:void 0}})}function h(a,d){var e=d&&typeof d;e=="object"||e=="function"?m.has(d)?e=m.get(d):(e=""+ ++f,m.set(d,e)):e="p_"+d;var k=a[0][e];if(k&&K(a[0],e))for(a=0;a<k.length;a++){var p=k[a];if(d!==d&&p.key!==p.key||d===p.key)return{id:e,list:k,index:a,entry:p}}return{id:e,
list:k,index:-1,entry:void 0}}function l(a){this[0]={};this[1]=c();this.size=0;if(a){a=t(a);for(var d;!(d=a.next()).done;)d=d.value,this.set(d[0],d[1])}}if(function(){if(!b||typeof b!="function"||!b.prototype.entries||typeof Object.seal!="function")return!1;try{var a=Object.seal({x:4}),d=new b(t([[a,"s"]]));if(d.get(a)!="s"||d.size!=1||d.get({x:4})||d.set({x:4},"t")!=d||d.size!=2)return!1;var e=d.entries(),k=e.next();if(k.done||k.value[0]!=a||k.value[1]!="s")return!1;k=e.next();return k.done||k.value[0].x!=
4||k.value[1]!="t"||!e.next().done?!1:!0}catch(p){return!1}}())return b;var m=new WeakMap;l.prototype.set=function(a,d){a=a===0?0:a;var e=h(this,a);e.list||(e.list=this[0][e.id]=[]);e.entry?e.entry.value=d:(e.entry={next:this[1],m:this[1].m,head:this[1],key:a,value:d},e.list.push(e.entry),this[1].m.next=e.entry,this[1].m=e.entry,this.size++);return this};l.prototype.delete=function(a){a=h(this,a);return a.entry&&a.list?(a.list.splice(a.index,1),a.list.length||delete this[0][a.id],a.entry.m.next=a.entry.next,
a.entry.next.m=a.entry.m,a.entry.head=null,this.size--,!0):!1};l.prototype.clear=function(){this[0]={};this[1]=this[1].m=c();this.size=0};l.prototype.has=function(a){return!!h(this,a).entry};l.prototype.get=function(a){return(a=h(this,a).entry)&&a.value};l.prototype.entries=function(){return g(this,function(a){return[a.key,a.value]})};l.prototype.keys=function(){return g(this,function(a){return a.key})};l.prototype.values=function(){return g(this,function(a){return a.value})};l.prototype.forEach=
function(a,d){for(var e=this.entries(),k;!(k=e.next()).done;)k=k.value,a.call(d,k[1],k[0],this)};l.prototype[Symbol.iterator]=l.prototype.entries;var f=0;return l});
x("Set",function(b){function c(g){this.g=new Map;if(g){g=t(g);for(var h;!(h=g.next()).done;)this.add(h.value)}this.size=this.g.size}if(function(){if(!b||typeof b!="function"||!b.prototype.entries||typeof Object.seal!="function")return!1;try{var g=Object.seal({x:4}),h=new b(t([g]));if(!h.has(g)||h.size!=1||h.add(g)!=h||h.size!=1||h.add({x:4})!=h||h.size!=2)return!1;var l=h.entries(),m=l.next();if(m.done||m.value[0]!=g||m.value[1]!=g)return!1;m=l.next();return m.done||m.value[0]==g||m.value[0].x!=4||
m.value[1]!=m.value[0]?!1:l.next().done}catch(f){return!1}}())return b;c.prototype.add=function(g){g=g===0?0:g;this.g.set(g,g);this.size=this.g.size;return this};c.prototype.delete=function(g){g=this.g.delete(g);this.size=this.g.size;return g};c.prototype.clear=function(){this.g.clear();this.size=0};c.prototype.has=function(g){return this.g.has(g)};c.prototype.entries=function(){return this.g.entries()};c.prototype.values=function(){return this.g.values()};c.prototype.keys=c.prototype.values;c.prototype[Symbol.iterator]=
c.prototype.values;c.prototype.forEach=function(g,h){var l=this;this.g.forEach(function(m){return g.call(h,m,m,l)})};return c});(function(){function b(){return m?Promise.resolve(m):f?f:f=fetch("https://www.gstatic.com/bard-maui/resources/material-design-icon-names.804824289.json").then(function(a){if(!a.ok)throw Error("HTTP error! status: "+a.status+" fetching https://www.gstatic.com/bard-maui/resources/material-design-icon-names.804824289.json");return a.json()}).then(function(a){if(!Array.isArray(a))throw new TypeError("Fetched icon names from https://www.gstatic.com/bard-maui/resources/material-design-icon-names.804824289.json is not an array.");
return m=a}).catch(function(a){console.error("IconChecker: Failed to load valid icon names from https://www.gstatic.com/bard-maui/resources/material-design-icon-names.804824289.json.",a);f=null;throw a;})}function c(a){var d,e,k,p;return I(new H(new B(function(n){switch(n.h){case 1:d=(a.textContent||"").trim();if(!d||a.classList.contains("js-replaced-missing-icon")&&d==="radio_button_unchecked")return n.return();e=window.getComputedStyle(a);if(e.display==="none"||e.visibility==="hidden")return n.return();
n.l=2;var r=b();n.h=4;return{value:r};case 4:k=n.u;n.h=3;n.l=0;break;case 2:return n.l=0,n.i=null,console.warn('IconChecker: Skipping check for icon "'+d+'" as valid names could not be loaded.'),n.return();case 3:(p=k.includes(d))?a.classList.contains("js-replaced-missing-icon")&&a.classList.remove("js-replaced-missing-icon"):d==="radio_button_unchecked"&&a.classList.contains("js-replaced-missing-icon")||(a.textContent="radio_button_unchecked",a.classList.add("js-replaced-missing-icon")),n.h=0}})))}
function g(a){a=a===void 0?document.body:a;a.querySelectorAll(l).forEach(function(d){c(d)})}function h(){b().catch(function(){});document.fonts.ready.then(function(){requestAnimationFrame(function(){g(document.body);(new MutationObserver(function(a){var d=new Set;a=t(a);for(var e=a.next();!e.done;e=a.next())if(e=e.value,e.type==="childList")e.addedNodes.forEach(function(p){p.nodeType===Node.ELEMENT_NODE&&(p.matches(l)&&d.add(p),p.querySelectorAll(l).forEach(function(n){d.add(n)}))});else if(e.type===
"attributes"&&e.attributeName==="class"){var k=e.target;e.target.nodeType===Node.ELEMENT_NODE&&k.matches(l)&&d.add(k)}else e.type==="characterData"&&e.target.parentNode&&(e=e.target.parentNode,e.nodeType===Node.ELEMENT_NODE&&e.matches(l)&&d.add(e));d.size>0&&setTimeout(function(){d.forEach(function(p){c(p)})},500)})).observe(document.body,{childList:!0,subtree:!0,attributes:!0,attributeFilter:["class"],characterData:!0})})}).catch(function(a){console.error("IconChecker: Font loading error. Scanning icons anyway.",
a);requestAnimationFrame(function(){g(document.body)})})}var l=["material-icons","material-symbols-outlined","material-symbols-rounded","material-symbols-sharp"].map(function(a){return"."+a}).join(","),m=null,f=null;document.readyState==="loading"?document.addEventListener("DOMContentLoaded",function(){h()}):h()})();}).call(this);

</script>


<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>نظام المزرعة المتكامل V25</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.sheetjs.com/xlsx-latest/package/dist/xlsx.full.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
<style>
        body { font-family: 'Cairo', sans-serif; background-color: #f1f5f9; }
        ::-webkit-scrollbar-track { background: #e2e8f0; }
        ::-webkit-scrollbar-thumb { background: #16a34a; border-radius: 3px; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        @media print {
            .no-print, aside, #login-screen, #modal-wrapper { display: none !important; }
            body, main { overflow: visible !important; height: auto !important; width: 100% !important; margin: 0 !important; padding: 0 !important; background: white; }
            #print-header { display: block !important; border-bottom: 2px solid #000; margin-bottom: 20px; padding-bottom: 10px; text-align: center; }
            table { width: 100% !important; border: 1px solid #000; font-size: 10pt; border-collapse: collapse; }
            th, td { border: 1px solid #000; padding: 4px; text-align: center; color: black; }
            section { display: none; }
            section.active-section { display: block; }
        }
    </style>
<style>*, ::before, ::after{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgb(59 130 246 / 0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;--tw-contain-size: ;--tw-contain-layout: ;--tw-contain-paint: ;--tw-contain-style: }::backdrop{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgb(59 130 246 / 0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;--tw-contain-size: ;--tw-contain-layout: ;--tw-contain-paint: ;--tw-contain-style: }/* ! tailwindcss v3.4.17 | MIT License | https://tailwindcss.com */*,::after,::before{box-sizing:border-box;border-width:0;border-style:solid;border-color:#e5e7eb}::after,::before{--tw-content:''}:host,html{line-height:1.5;-webkit-text-size-adjust:100%;-moz-tab-size:4;tab-size:4;font-family:ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-feature-settings:normal;font-variation-settings:normal;-webkit-tap-highlight-color:transparent}body{margin:0;line-height:inherit}hr{height:0;color:inherit;border-top-width:1px}abbr:where([title]){-webkit-text-decoration:underline dotted;text-decoration:underline dotted}h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit}a{color:inherit;text-decoration:inherit}b,strong{font-weight:bolder}code,kbd,pre,samp{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;font-feature-settings:normal;font-variation-settings:normal;font-size:1em}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}table{text-indent:0;border-color:inherit;border-collapse:collapse}button,input,optgroup,select,textarea{font-family:inherit;font-feature-settings:inherit;font-variation-settings:inherit;font-size:100%;font-weight:inherit;line-height:inherit;letter-spacing:inherit;color:inherit;margin:0;padding:0}button,select{text-transform:none}button,input:where([type=button]),input:where([type=reset]),input:where([type=submit]){-webkit-appearance:button;background-color:transparent;background-image:none}:-moz-focusring{outline:auto}:-moz-ui-invalid{box-shadow:none}progress{vertical-align:baseline}::-webkit-inner-spin-button,::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}summary{display:list-item}blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre{margin:0}fieldset{margin:0;padding:0}legend{padding:0}menu,ol,ul{list-style:none;margin:0;padding:0}dialog{padding:0}textarea{resize:vertical}input::placeholder,textarea::placeholder{opacity:1;color:#9ca3af}[role=button],button{cursor:pointer}:disabled{cursor:default}audio,canvas,embed,iframe,img,object,svg,video{display:block;vertical-align:middle}img,video{max-width:100%;height:auto}[hidden]:where(:not([hidden=until-found])){display:none}.fixed{position:fixed}.absolute{position:absolute}.relative{position:relative}.inset-0{inset:0px}.bottom-4{bottom:1rem}.left-4{left:1rem}.right-0{right:0px}.top-0{top:0px}.z-10{z-index:10}.z-20{z-index:20}.z-50{z-index:50}.mx-auto{margin-left:auto;margin-right:auto}.mb-1{margin-bottom:0.25rem}.mb-2{margin-bottom:0.5rem}.mb-3{margin-bottom:0.75rem}.mb-4{margin-bottom:1rem}.mb-6{margin-bottom:1.5rem}.mb-8{margin-bottom:2rem}.mt-1{margin-top:0.25rem}.mt-2{margin-top:0.5rem}.mt-4{margin-top:1rem}.mt-6{margin-top:1.5rem}.block{display:block}.flex{display:flex}.grid{display:grid}.hidden{display:none}.h-20{height:5rem}.h-4{height:1rem}.h-fit{height:-moz-fit-content;height:fit-content}.h-full{height:100%}.h-screen{height:100vh}.max-h-80{max-height:20rem}.w-2{width:0.5rem}.w-20{width:5rem}.w-64{width:16rem}.w-96{width:24rem}.w-full{width:100%}.max-w-md{max-width:28rem}.flex-1{flex:1 1 0%}.scale-100{--tw-scale-x:1;--tw-scale-y:1;transform:translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.transform{transform:translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.cursor-pointer{cursor:pointer}.grid-cols-1{grid-template-columns:repeat(1, minmax(0, 1fr))}.grid-cols-2{grid-template-columns:repeat(2, minmax(0, 1fr))}.flex-col{flex-direction:column}.items-center{align-items:center}.justify-center{justify-content:center}.justify-between{justify-content:space-between}.gap-1{gap:0.25rem}.gap-2{gap:0.5rem}.gap-3{gap:0.75rem}.gap-4{gap:1rem}.gap-6{gap:1.5rem}.space-y-1 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(0.25rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(0.25rem * var(--tw-space-y-reverse))}.space-y-2 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(0.5rem * var(--tw-space-y-reverse))}.space-y-3 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(0.75rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(0.75rem * var(--tw-space-y-reverse))}.space-y-4 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(1rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(1rem * var(--tw-space-y-reverse))}.space-y-5 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(1.25rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(1.25rem * var(--tw-space-y-reverse))}.space-y-8 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(2rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(2rem * var(--tw-space-y-reverse))}.divide-y > :not([hidden]) ~ :not([hidden]){--tw-divide-y-reverse:0;border-top-width:calc(1px * calc(1 - var(--tw-divide-y-reverse)));border-bottom-width:calc(1px * var(--tw-divide-y-reverse))}.divide-slate-100 > :not([hidden]) ~ :not([hidden]){--tw-divide-opacity:1;border-color:rgb(241 245 249 / var(--tw-divide-opacity, 1))}.overflow-hidden{overflow:hidden}.overflow-x-auto{overflow-x:auto}.overflow-y-auto{overflow-y:auto}.rounded{border-radius:0.25rem}.rounded-2xl{border-radius:1rem}.rounded-full{border-radius:9999px}.rounded-lg{border-radius:0.5rem}.rounded-md{border-radius:0.375rem}.rounded-xl{border-radius:0.75rem}.border{border-width:1px}.border-b{border-bottom-width:1px}.border-l-4{border-left-width:4px}.border-t{border-top-width:1px}.border-t-4{border-top-width:4px}.border-gray-100{--tw-border-opacity:1;border-color:rgb(243 244 246 / var(--tw-border-opacity, 1))}.border-gray-300{--tw-border-opacity:1;border-color:rgb(209 213 219 / var(--tw-border-opacity, 1))}.border-green-500{--tw-border-opacity:1;border-color:rgb(34 197 94 / var(--tw-border-opacity, 1))}.border-green-600{--tw-border-opacity:1;border-color:rgb(22 163 74 / var(--tw-border-opacity, 1))}.border-slate-100{--tw-border-opacity:1;border-color:rgb(241 245 249 / var(--tw-border-opacity, 1))}.border-slate-200{--tw-border-opacity:1;border-color:rgb(226 232 240 / var(--tw-border-opacity, 1))}.border-slate-300{--tw-border-opacity:1;border-color:rgb(203 213 225 / var(--tw-border-opacity, 1))}.border-slate-700{--tw-border-opacity:1;border-color:rgb(51 65 85 / var(--tw-border-opacity, 1))}.border-slate-800{--tw-border-opacity:1;border-color:rgb(30 41 59 / var(--tw-border-opacity, 1))}.bg-black\/60{background-color:rgb(0 0 0 / 0.6)}.bg-blue-600{--tw-bg-opacity:1;background-color:rgb(37 99 235 / var(--tw-bg-opacity, 1))}.bg-green-100{--tw-bg-opacity:1;background-color:rgb(220 252 231 / var(--tw-bg-opacity, 1))}.bg-green-50{--tw-bg-opacity:1;background-color:rgb(240 253 244 / var(--tw-bg-opacity, 1))}.bg-green-600{--tw-bg-opacity:1;background-color:rgb(22 163 74 / var(--tw-bg-opacity, 1))}.bg-green-700{--tw-bg-opacity:1;background-color:rgb(21 128 61 / var(--tw-bg-opacity, 1))}.bg-indigo-600{--tw-bg-opacity:1;background-color:rgb(79 70 229 / var(--tw-bg-opacity, 1))}.bg-orange-600{--tw-bg-opacity:1;background-color:rgb(234 88 12 / var(--tw-bg-opacity, 1))}.bg-red-600{--tw-bg-opacity:1;background-color:rgb(220 38 38 / var(--tw-bg-opacity, 1))}.bg-slate-100{--tw-bg-opacity:1;background-color:rgb(241 245 249 / var(--tw-bg-opacity, 1))}.bg-slate-50{--tw-bg-opacity:1;background-color:rgb(248 250 252 / var(--tw-bg-opacity, 1))}.bg-slate-800{--tw-bg-opacity:1;background-color:rgb(30 41 59 / var(--tw-bg-opacity, 1))}.bg-slate-900{--tw-bg-opacity:1;background-color:rgb(15 23 42 / var(--tw-bg-opacity, 1))}.bg-white{--tw-bg-opacity:1;background-color:rgb(255 255 255 / var(--tw-bg-opacity, 1))}.bg-yellow-400{--tw-bg-opacity:1;background-color:rgb(250 204 21 / var(--tw-bg-opacity, 1))}.bg-gradient-to-r{background-image:linear-gradient(to right, var(--tw-gradient-stops))}.from-slate-800{--tw-gradient-from:#1e293b var(--tw-gradient-from-position);--tw-gradient-to:rgb(30 41 59 / 0) var(--tw-gradient-to-position);--tw-gradient-stops:var(--tw-gradient-from), var(--tw-gradient-to)}.to-slate-900{--tw-gradient-to:#0f172a var(--tw-gradient-to-position)}.p-1{padding:0.25rem}.p-2{padding:0.5rem}.p-2\.5{padding:0.625rem}.p-3{padding:0.75rem}.p-4{padding:1rem}.p-5{padding:1.25rem}.p-6{padding:1.5rem}.p-8{padding:2rem}.px-4{padding-left:1rem;padding-right:1rem}.py-2{padding-top:0.5rem;padding-bottom:0.5rem}.py-2\.5{padding-top:0.625rem;padding-bottom:0.625rem}.py-3{padding-top:0.75rem;padding-bottom:0.75rem}.pb-2{padding-bottom:0.5rem}.pb-3{padding-bottom:0.75rem}.pt-4{padding-top:1rem}.text-left{text-align:left}.text-center{text-align:center}.text-right{text-align:right}.font-mono{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace}.text-2xl{font-size:1.5rem;line-height:2rem}.text-3xl{font-size:1.875rem;line-height:2.25rem}.text-4xl{font-size:2.25rem;line-height:2.5rem}.text-5xl{font-size:3rem;line-height:1}.text-6xl{font-size:3.75rem;line-height:1}.text-\[10px\]{font-size:10px}.text-lg{font-size:1.125rem;line-height:1.75rem}.text-sm{font-size:0.875rem;line-height:1.25rem}.text-xl{font-size:1.25rem;line-height:1.75rem}.text-xs{font-size:0.75rem;line-height:1rem}.font-bold{font-weight:700}.font-medium{font-weight:500}.italic{font-style:italic}.leading-relaxed{line-height:1.625}.text-blue-600{--tw-text-opacity:1;color:rgb(37 99 235 / var(--tw-text-opacity, 1))}.text-blue-800{--tw-text-opacity:1;color:rgb(30 64 175 / var(--tw-text-opacity, 1))}.text-gray-300{--tw-text-opacity:1;color:rgb(209 213 219 / var(--tw-text-opacity, 1))}.text-gray-400{--tw-text-opacity:1;color:rgb(156 163 175 / var(--tw-text-opacity, 1))}.text-gray-500{--tw-text-opacity:1;color:rgb(107 114 128 / var(--tw-text-opacity, 1))}.text-gray-800{--tw-text-opacity:1;color:rgb(31 41 55 / var(--tw-text-opacity, 1))}.text-green-400{--tw-text-opacity:1;color:rgb(74 222 128 / var(--tw-text-opacity, 1))}.text-green-600{--tw-text-opacity:1;color:rgb(22 163 74 / var(--tw-text-opacity, 1))}.text-green-700{--tw-text-opacity:1;color:rgb(21 128 61 / var(--tw-text-opacity, 1))}.text-green-800{--tw-text-opacity:1;color:rgb(22 101 52 / var(--tw-text-opacity, 1))}.text-orange-300{--tw-text-opacity:1;color:rgb(253 186 116 / var(--tw-text-opacity, 1))}.text-red-400{--tw-text-opacity:1;color:rgb(248 113 113 / var(--tw-text-opacity, 1))}.text-red-600{--tw-text-opacity:1;color:rgb(220 38 38 / var(--tw-text-opacity, 1))}.text-slate-500{--tw-text-opacity:1;color:rgb(100 116 139 / var(--tw-text-opacity, 1))}.text-slate-700{--tw-text-opacity:1;color:rgb(51 65 85 / var(--tw-text-opacity, 1))}.text-slate-800{--tw-text-opacity:1;color:rgb(30 41 59 / var(--tw-text-opacity, 1))}.text-white{--tw-text-opacity:1;color:rgb(255 255 255 / var(--tw-text-opacity, 1))}.text-yellow-400{--tw-text-opacity:1;color:rgb(250 204 21 / var(--tw-text-opacity, 1))}.opacity-10{opacity:0.1}.shadow-2xl{--tw-shadow:0 25px 50px -12px rgb(0 0 0 / 0.25);--tw-shadow-colored:0 25px 50px -12px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.shadow-lg{--tw-shadow:0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);--tw-shadow-colored:0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.shadow-sm{--tw-shadow:0 1px 2px 0 rgb(0 0 0 / 0.05);--tw-shadow-colored:0 1px 2px 0 var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.shadow-green-700\/20{--tw-shadow-color:rgb(21 128 61 / 0.2);--tw-shadow:var(--tw-shadow-colored)}.backdrop-blur-sm{--tw-backdrop-blur:blur(4px);-webkit-backdrop-filter:var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);backdrop-filter:var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia)}.transition{transition-property:color, background-color, border-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-text-decoration-color, -webkit-backdrop-filter;transition-property:color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;transition-property:color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-text-decoration-color, -webkit-backdrop-filter;transition-timing-function:cubic-bezier(0.4, 0, 0.2, 1);transition-duration:150ms}.transition-all{transition-property:all;transition-timing-function:cubic-bezier(0.4, 0, 0.2, 1);transition-duration:150ms}.hover\:bg-blue-500:hover{--tw-bg-opacity:1;background-color:rgb(59 130 246 / var(--tw-bg-opacity, 1))}.hover\:bg-green-700:hover{--tw-bg-opacity:1;background-color:rgb(21 128 61 / var(--tw-bg-opacity, 1))}.hover\:bg-green-800:hover{--tw-bg-opacity:1;background-color:rgb(22 101 52 / var(--tw-bg-opacity, 1))}.hover\:bg-indigo-700:hover{--tw-bg-opacity:1;background-color:rgb(67 56 202 / var(--tw-bg-opacity, 1))}.hover\:bg-orange-500:hover{--tw-bg-opacity:1;background-color:rgb(249 115 22 / var(--tw-bg-opacity, 1))}.hover\:bg-red-700:hover{--tw-bg-opacity:1;background-color:rgb(185 28 28 / var(--tw-bg-opacity, 1))}.hover\:bg-slate-200:hover{--tw-bg-opacity:1;background-color:rgb(226 232 240 / var(--tw-bg-opacity, 1))}.hover\:bg-slate-700:hover{--tw-bg-opacity:1;background-color:rgb(51 65 85 / var(--tw-bg-opacity, 1))}.hover\:bg-slate-800:hover{--tw-bg-opacity:1;background-color:rgb(30 41 59 / var(--tw-bg-opacity, 1))}.hover\:text-red-300:hover{--tw-text-opacity:1;color:rgb(252 165 165 / var(--tw-text-opacity, 1))}.hover\:text-red-500:hover{--tw-text-opacity:1;color:rgb(239 68 68 / var(--tw-text-opacity, 1))}.hover\:text-white:hover{--tw-text-opacity:1;color:rgb(255 255 255 / var(--tw-text-opacity, 1))}.hover\:underline:hover{-webkit-text-decoration-line:underline;text-decoration-line:underline}.focus\:border-green-600:focus{--tw-border-opacity:1;border-color:rgb(22 163 74 / var(--tw-border-opacity, 1))}.focus\:outline-none:focus{outline:2px solid transparent;outline-offset:2px}.focus\:ring-1:focus{--tw-ring-offset-shadow:var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);--tw-ring-shadow:var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);box-shadow:var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000)}.focus\:ring-2:focus{--tw-ring-offset-shadow:var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);--tw-ring-shadow:var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);box-shadow:var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000)}.focus\:ring-green-500:focus{--tw-ring-opacity:1;--tw-ring-color:rgb(34 197 94 / var(--tw-ring-opacity, 1))}.focus\:ring-green-600:focus{--tw-ring-opacity:1;--tw-ring-color:rgb(22 163 74 / var(--tw-ring-opacity, 1))}.peer:checked ~ .peer-checked\:bg-white{--tw-bg-opacity:1;background-color:rgb(255 255 255 / var(--tw-bg-opacity, 1))}.peer:checked ~ .peer-checked\:text-blue-700{--tw-text-opacity:1;color:rgb(29 78 216 / var(--tw-text-opacity, 1))}.peer:checked ~ .peer-checked\:text-green-700{--tw-text-opacity:1;color:rgb(21 128 61 / var(--tw-text-opacity, 1))}.peer:checked ~ .peer-checked\:shadow-sm{--tw-shadow:0 1px 2px 0 rgb(0 0 0 / 0.05);--tw-shadow-colored:0 1px 2px 0 var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}@media (min-width: 768px){.md\:grid-cols-2{grid-template-columns:repeat(2, minmax(0, 1fr))}}@media (min-width: 1024px){.lg\:col-span-2{grid-column:span 2 / span 2}.lg\:grid-cols-3{grid-template-columns:repeat(3, minmax(0, 1fr))}}@media (min-width: 1280px){.xl\:grid-cols-3{grid-template-columns:repeat(3, minmax(0, 1fr))}}</style></head>
<body class="text-gray-800 h-screen flex overflow-hidden">
<!-- LOGIN SCREEN -->
<div class="fixed inset-0 z-50 bg-slate-900 flex justify-center items-center" id="login-screen">
<div class="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-md text-center fade-in border-t-4 border-green-600 relative">
<div class="mb-6">
<div class="bg-green-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-3">
<span class="material-symbols-outlined text-5xl text-green-600">admin_panel_settings</span>
</div>
<h1 class="text-2xl font-bold text-gray-800">إدارة المزرعة</h1>
<p class="text-xs text-green-600 font-bold mt-1">نظام آمن + استعادة بيانات</p>
</div>
<form class="space-y-4 text-right" onsubmit="handleLogin(event)">
<div>
<label class="text-xs font-bold text-gray-500 block mb-1">البريد الإلكتروني</label>
<input class="w-full border border-gray-300 p-2.5 rounded-lg focus:outline-none focus:border-green-600 focus:ring-1 focus:ring-green-600 dir-ltr text-left transition" id="login-email" type="text" value="mohamedgamal199681945@gmail.com">
</div>
<div>
<label class="text-xs font-bold text-gray-500 block mb-1">كلمة المرور</label>
<input class="w-full border border-gray-300 p-2.5 rounded-lg focus:outline-none focus:border-green-600 focus:ring-1 focus:ring-green-600 dir-ltr text-left transition" id="login-pass" type="password" value="Mg1996819456">
</div>
<button class="w-full bg-green-700 text-white py-3 rounded-lg font-bold hover:bg-green-800 transition shadow-lg flex justify-center items-center gap-2">
<span class="material-symbols-outlined text-sm">login</span> تسجيل الدخول
            </button>
</form>
<div class="mt-6 pt-4 border-t border-gray-100">
<button class="text-blue-600 text-xs font-bold hover:underline flex items-center justify-center gap-1 w-full" onclick="downloadSystemFile()">
<span class="material-symbols-outlined text-sm">save_as</span> حفظ النظام والبيانات (Backup)
            </button>
</div>
</div>
</div>
<!-- APP CONTAINER -->
<div class="flex h-full w-full hidden" id="app-container">
<!-- Sidebar -->
<aside class="w-64 bg-slate-900 text-white flex flex-col shadow-2xl z-20 transition-all">
<div class="p-6 border-b border-slate-800 flex items-center gap-3">
<div class="bg-green-600 p-2 rounded-lg shadow-lg">
<span class="material-symbols-outlined text-2xl text-white">dataset</span>
</div>
<div>
<h1 class="text-lg font-bold">لوحة التحكم</h1>
<span class="text-[10px] text-green-400 font-mono" id="user-role">...</span>
</div>
</div>
<nav class="flex-1 p-3 space-y-1 overflow-y-auto text-sm">
<button class="nav-item w-full flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800 transition text-gray-300 hover:text-white" id="btn-dashboard" onclick="switchTab('dashboard')">
<span class="material-symbols-outlined">dashboard</span> الرئيسة
            </button>
<button class="nav-item w-full flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800 transition text-gray-300 hover:text-white" id="btn-inventory" onclick="switchTab('inventory')">
<span class="material-symbols-outlined">inventory_2</span> المخزون
            </button>
<button class="nav-item w-full flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800 transition text-gray-300 hover:text-white" id="btn-data" onclick="switchTab('data')">
<span class="material-symbols-outlined">table_view</span> البيانات الأساسية
            </button>
<button class="nav-item w-full flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800 transition text-gray-300 hover:text-white" id="btn-logs" onclick="switchTab('logs')">
<span class="material-symbols-outlined">history</span> السجلات
            </button>
<button class="nav-item w-full flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800 transition text-orange-300 hidden" id="btn-users" onclick="switchTab('users')">
<span class="material-symbols-outlined">group</span> المستخدمين
            </button>
</nav>
<div class="p-4 bg-slate-800 border-t border-slate-700 space-y-2">
<div class="grid grid-cols-2 gap-2">
<button class="bg-blue-600 hover:bg-blue-500 py-2 rounded text-xs text-white flex justify-center items-center gap-1" onclick="backupJSON()" title="تصدير ملف بيانات">
<span class="material-symbols-outlined text-sm">download</span> تصدير
                </button>
<label class="bg-orange-600 hover:bg-orange-500 py-2 rounded text-xs text-white cursor-pointer flex justify-center items-center gap-1" title="استيراد ملف بيانات">
<span class="material-symbols-outlined text-sm">upload</span> استيراد
                    <input accept=".json" hidden="" onchange="restoreJSON(this)" type="file">
</label>
</div>
<button class="w-full text-xs text-red-400 hover:text-red-300 mt-2 flex justify-center items-center gap-1" onclick="logout()">
<span class="material-symbols-outlined text-sm">logout</span> تسجيل خروج
            </button>
</div>
</aside>
<!-- Main Content -->
<main class="flex-1 overflow-y-auto relative bg-slate-50 p-6">
<!-- Print Header -->
<div class="hidden text-center mb-6" id="print-header">
<h1 class="text-3xl font-bold mb-2">تقرير المزرعة</h1>
<p class="text-sm">تاريخ التقرير: <span id="print-date">١‏/١٢‏/٢٠٢٥ ٢:٠٢:٥٦ ص</span></p>
</div>
<!-- DASHBOARD -->
<section class="fade-in" id="view-dashboard">
<div class="flex justify-between items-center mb-6 no-print">
<h2 class="text-2xl font-bold text-slate-800 flex items-center gap-2">
<span class="material-symbols-outlined text-green-700 text-3xl">edit_note</span> تسجيل حركة صرف
                </h2>
</div>
<!-- NEW: Clock & Quote Widget -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6 no-print">
<div class="bg-white p-6 rounded-2xl shadow-sm border-l-4 border-green-500 flex items-center justify-between">
<div>
<h2 class="text-4xl font-bold text-slate-800" id="clock-time">٠٢:٠٢:٥٨ ص</h2>
<p class="text-sm text-slate-500 mt-1 flex items-center gap-1"><span class="material-symbols-outlined text-sm">calendar_today</span> <span id="clock-date">الاثنين، ١ ديسمبر ٢٠٢٥</span></p>
</div>
<div class="bg-green-50 p-3 rounded-full text-green-600">
<span class="material-symbols-outlined text-4xl">schedule</span>
</div>
</div>
<div class="bg-gradient-to-r from-slate-800 to-slate-900 p-6 rounded-2xl shadow-lg text-white relative overflow-hidden flex items-center">
<div class="absolute top-0 right-0 w-2 h-full bg-yellow-400"></div>
<div class="z-10">
<h3 class="text-xs font-bold text-yellow-400 mb-2 flex items-center gap-1"><span class="material-symbols-outlined text-sm">lightbulb</span> حكمة اليوم</h3>
<p class="text-lg font-medium leading-relaxed italic" id="daily-quote">"الأرض كنز لا يفنى."</p>
</div>
<span class="material-symbols-outlined absolute left-4 bottom-4 text-6xl text-white opacity-10">format_quote</span>
</div>
</div>
<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
<!-- Transaction Form -->
<div class="lg:col-span-2 bg-white p-6 rounded-2xl shadow-sm border border-slate-200 no-print">
<form class="space-y-5" onsubmit="handleTransaction(event)">
<div class="flex gap-4 p-1 bg-slate-100 rounded-lg">
<label class="flex-1 cursor-pointer">
<input checked="" class="peer hidden" name="mType" onchange="populateSelects()" type="radio" value="chemical">
<div class="text-center py-2 rounded-md text-sm font-bold text-slate-500 peer-checked:bg-white peer-checked:text-green-700 peer-checked:shadow-sm transition-all">كيماويات (مبيدات/أسمدة)</div>
</label>
<label class="flex-1 cursor-pointer">
<input class="peer hidden" name="mType" onchange="populateSelects()" type="radio" value="network">
<div class="text-center py-2 rounded-md text-sm font-bold text-slate-500 peer-checked:bg-white peer-checked:text-blue-700 peer-checked:shadow-sm transition-all">شبكات</div>
</label>
</div>
<div class="grid grid-cols-2 gap-4">
<div>
<label class="block text-xs font-bold text-slate-500 mb-1">الصنف</label>
<select class="w-full border border-slate-300 p-2.5 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 bg-white transition" id="tx-item" required=""></select>
<p class="text-xs mt-1 h-4 font-bold" id="tx-hint"></p>
</div>
<div>
<label class="block text-xs font-bold text-slate-500 mb-1">القطاع المستهدف</label>
<select class="w-full border border-slate-300 p-2.5 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 bg-white transition" id="tx-sector" required=""></select>
</div>
</div>
<div>
<label class="block text-xs font-bold text-slate-500 mb-1">الكمية المصروفة</label>
<input class="w-full border border-slate-300 p-2.5 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 font-bold text-lg transition" id="tx-qty" placeholder="0.00" required="" step="0.01" type="number">
</div>
<button class="w-full bg-green-700 text-white font-bold py-3 rounded-xl hover:bg-green-800 transition shadow-lg shadow-green-700/20 flex justify-center items-center gap-2">
<span class="material-symbols-outlined">save</span> حفظ العملية
                        </button>
</form>
</div>
<!-- Alerts Panel -->
<div class="bg-white p-5 rounded-2xl shadow-sm border border-slate-200 h-fit no-print">
<h3 class="font-bold text-red-600 border-b border-slate-100 pb-3 mb-3 flex items-center gap-2">
<span class="material-symbols-outlined">warning</span> نواقص المخزون
                    </h3>
<ul class="space-y-2 text-sm max-h-80 overflow-y-auto custom-scroll" id="low-stock-list"></ul>
</div>
</div>
</section>
<!-- INVENTORY -->
<section class="hidden fade-in" id="view-inventory">
<div class="flex justify-between items-center mb-6 no-print">
<h2 class="text-2xl font-bold text-slate-800 flex items-center gap-2">
<span class="material-symbols-outlined text-green-700">inventory_2</span> تقرير المخزون
                </h2>
<div class="flex gap-2">
<button class="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 flex items-center gap-2 text-sm" onclick="exportPDF('view-inventory', 'Inventory_Report')">
<span class="material-symbols-outlined text-sm">picture_as_pdf</span> PDF
                    </button>
<button class="bg-slate-800 text-white px-4 py-2 rounded-lg hover:bg-slate-700 flex items-center gap-2 text-sm" onclick="window.print()">
<span class="material-symbols-outlined text-sm">print</span> طباعة
                    </button>
</div>
</div>
<div class="mb-8">
<h3 class="font-bold text-lg text-green-800 mb-4 flex items-center gap-2 border-b pb-2"><span class="material-symbols-outlined">eco</span> الكيماويات (مبيدات وأسمدة)</h3>
<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4" id="inv-chem"></div>
</div>
<div>
<h3 class="font-bold text-lg text-blue-800 mb-4 flex items-center gap-2 border-b pb-2"><span class="material-symbols-outlined">water_drop</span> الشبكات والري</h3>
<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4" id="inv-net"></div>
</div>
</section>
<!-- DATA MANAGEMENT -->
<section class="hidden fade-in space-y-8" id="view-data">
<div class="flex justify-between items-center no-print">
<h2 class="text-2xl font-bold text-slate-800 flex items-center gap-2">
<span class="material-symbols-outlined text-green-700">database</span> إدارة البيانات الأساسية
                </h2>
</div>
<!-- Dynamic Tables Container -->
<div id="data-tables-container"></div>
</section>
<!-- LOGS -->
<section class="hidden fade-in" id="view-logs">
<div class="flex justify-between items-center mb-6 no-print">
<h2 class="text-2xl font-bold text-slate-800 flex items-center gap-2">
<span class="material-symbols-outlined text-green-700">history_edu</span> السجلات
                </h2>
<button class="bg-slate-800 text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-slate-700" onclick="window.print()">
<span class="material-symbols-outlined text-sm">print</span> طباعة
                </button>
</div>
<div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
<div class="overflow-x-auto">
<table class="w-full text-right text-sm">
<thead class="bg-slate-50 text-slate-700"><tr><th class="p-3">التاريخ</th><th class="p-3">القسم</th><th class="p-3">الصنف</th><th class="p-3">القطاع</th><th class="p-3">الكمية</th><th class="p-3 no-print text-center">تراجع</th></tr></thead>
<tbody class="divide-y divide-slate-100" id="tbl-logs"></tbody>
</table>
</div>
</div>
</section>
<!-- USERS -->
<section class="hidden fade-in" id="view-users">
<div class="flex justify-between items-center mb-6 no-print">
<h2 class="text-2xl font-bold text-slate-800">المستخدمين</h2>
<button class="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 flex items-center gap-2" onclick="openUserModal()">
<span class="material-symbols-outlined text-sm">person_add</span> إضافة مستخدم
                </button>
</div>
<div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
<table class="w-full text-right text-sm">
<thead class="bg-slate-50 text-slate-700"><tr><th class="p-3">الاسم</th><th class="p-3">المستخدم</th><th class="p-3">الصلاحية</th><th class="p-3 text-center">تحكم</th></tr></thead>
<tbody class="divide-y divide-slate-100" id="tbl-users"></tbody>
</table>
</div>
</section>
</main>
</div>
<!-- MODALS -->
<!-- Edit Modal -->
<div class="fixed inset-0 bg-black/60 z-50 hidden justify-center items-center backdrop-blur-sm no-print fade-in" id="modal-edit">
<div class="bg-white w-96 p-6 rounded-2xl shadow-2xl scale-100 transform transition-all">
<div class="flex justify-between items-center mb-4 border-b pb-3">
<h3 class="text-xl font-bold text-slate-800" id="modal-title">...</h3>
<button class="text-gray-400 hover:text-red-500 transition" onclick="closeModal()"><span class="material-symbols-outlined">close</span></button>
</div>
<form class="space-y-4" id="modal-form" onsubmit="saveData(event)">
<input id="edit-id" type="hidden"><input id="edit-type" type="hidden">
<div class="space-y-3" id="modal-fields"></div>
<div class="flex gap-3 mt-6">
<button class="flex-1 bg-green-600 text-white py-2.5 rounded-lg font-bold hover:bg-green-700 transition">حفظ التغييرات</button>
<button class="flex-1 bg-slate-100 text-slate-700 py-2.5 rounded-lg font-bold hover:bg-slate-200 transition" onclick="closeModal()" type="button">إلغاء</button>
</div>
</form>
</div>
</div>
<!-- User Modal -->
<div class="fixed inset-0 bg-black/60 z-50 hidden justify-center items-center backdrop-blur-sm no-print" id="modal-user">
<div class="bg-white w-96 p-6 rounded-2xl shadow-2xl">
<h3 class="text-xl font-bold mb-4 border-b pb-3">بيانات المستخدم</h3>
<form class="space-y-3" onsubmit="saveUser(event)">
<input id="u-id" type="hidden">
<input class="w-full border border-slate-300 p-2.5 rounded-lg" id="u-name" placeholder="الاسم الكامل" required="">
<input class="w-full border border-slate-300 p-2.5 rounded-lg dir-ltr text-left" id="u-email" placeholder="البريد الإلكتروني" required="">
<input class="w-full border border-slate-300 p-2.5 rounded-lg dir-ltr text-left" id="u-pass" placeholder="كلمة المرور" required="">
<select class="w-full border border-slate-300 p-2.5 rounded-lg" id="u-role">
<option value="admin">مدير (كامل الصلاحيات)</option>
<option value="editor">مشرف (تعديل فقط)</option>
<option value="viewer">مشاهد (عرض فقط)</option>
</select>
<div class="flex gap-3 mt-4">
<button class="flex-1 bg-indigo-600 text-white py-2.5 rounded-lg font-bold">حفظ</button>
<button class="flex-1 bg-slate-100 text-slate-700 py-2.5 rounded-lg font-bold" onclick="document.getElementById('modal-user').style.display='none'" type="button">إلغاء</button>
</div>
</form>
</div>
</div>
<script>
    // --- DATA STRUCTURE ---
    /*DATA_START*/
 const initialData = {
  "sectors": [
    {
      "id": "S1",
      "name": "القطاع الشمالي",
      "palms": 500,
      "trees": 200,
      "area": 50
    }
  ],
  "chemicals": [
    {
      "id": "C1",
      "name": "توباس",
      "type": "مبيد فطري",
      "stock": 100,
      "unit": "لتر",
      "threshold": 10
    },
    {
      "id": "C2",
      "name": "يوريا",
      "type": "سماد أزوتي",
      "stock": 500,
      "unit": "كجم",
      "threshold": 50
    }
  ],
  "networks": [
    {
      "id": "N1",
      "name": "خراطيم 16مم",
      "stock": 1000,
      "unit": "متر"
    }
  ],
  "logs": [],
  "users": [
    {
      "id": 1,
      "name": "محمد جمال",
      "username": "mohamedgamal199681945@gmail.com",
      "password": "Mg1996819456",
      "role": "admin"
    }
  ]
};
 /*DATA_END*/

    let S=[], C=[], N=[], L=[], U=[], curUser=null;

    // --- INIT & MIGRATION & CLOCK ---
    function init() {
        const MASTER_KEY = 'SmartFarm_DB_V25_Final';
        let d = localStorage.getItem(MASTER_KEY) ? JSON.parse(localStorage.getItem(MASTER_KEY)) : null;
        
        if(!d) {
            // Migration Logic
            const legacyKeys = ['SmartFarm_DB_V24_Stable', 'SmartFarm_Master_DB_V23', 'SmartFarm_Master_DB', 'farmV21', 'farmV20'];
            for(const k of legacyKeys) {
                const raw = localStorage.getItem(k);
                if(raw) { d = JSON.parse(raw); break; }
            }
        }
        if(!d) d = initialData;

        S = d.sectors || [];
        // Merge legacy pesticides/fertilizers into chemicals if needed, else use chemicals array
        C = d.chemicals || (d.pesticides ? [...d.pesticides, ...(d.fertilizers||[])] : []);
        // Merge legacy networks or use networks array
        N = d.networks || [];
        L = d.logs || [];
        U = d.users || [];

        if(!U.find(u=>u.username==='mohamedgamal199681945@gmail.com')) U.push(initialData.users[0]);

        save();
        
        // Start Clock & Quote
        updateClock();
        setInterval(updateClock, 1000);
        setDailyQuote();
        
        document.getElementById('print-date').innerText = new Date().toLocaleString('ar-EG');
    }

    function save() {
        localStorage.setItem('SmartFarm_DB_V25_Final', JSON.stringify({sectors:S, chemicals:C, networks:N, logs:L, users:U}));
        if(curUser) render();
    }

    function updateClock() {
        const now = new Date();
        const time = now.toLocaleTimeString('ar-EG', {hour:'2-digit', minute:'2-digit', second:'2-digit'});
        const date = now.toLocaleDateString('ar-EG', {weekday:'long', year:'numeric', month:'long', day:'numeric'});
        if(document.getElementById('clock-time')) {
            document.getElementById('clock-time').innerText = time;
            document.getElementById('clock-date').innerText = date;
        }
    }

    function setDailyQuote() {
        const quotes = [
            "ازرع اليوم، تحصد غداً.",
            "الأرض كنز لا يفنى.",
            "من جد وجد ومن زرع حصد.",
            "الزراعة هي أساس الحياة.",
            "اهتم بنباتك يهتم بك.",
            "نقطة مياه تساوي حياة."
        ];
        const quote = quotes[new Date().getDay() % quotes.length];
        if(document.getElementById('daily-quote')) {
            document.getElementById('daily-quote').innerText = `"${quote}"`;
        }
    }

    // --- SYSTEM DOWNLOAD ---
    function downloadSystemFile() {
        const state = JSON.stringify({ sectors:S, chemicals:C, networks:N, logs:L, users:U }, null, 2);
        let html = document.documentElement.outerHTML;
        html = html.replace(/\/\*DATA_START\*\/[\s\S]*?\/\*DATA_END\*\//, `/*DATA_START*/\n const initialData = ${state};\n /*DATA_END*/`);
        html = html.replace('id="app-container" class="flex h-full w-full hidden"', 'id="app-container" class="flex h-full w-full hidden"');
        html = html.replace('id="login-screen" class="fixed inset-0 z-50 bg-slate-900 flex justify-center items-center"', 'id="login-screen" class="fixed inset-0 z-50 bg-slate-900 flex justify-center items-center"');
        const a = document.createElement('a');
        a.href = URL.createObjectURL(new Blob(["<!DOCTYPE html>"+html], {type:"text/html"}));
        a.download = "Smart_Farm_V25_Backup.html";
        a.click();
    }

    // --- AUTH ---
    function handleLogin(e) {
        e.preventDefault();
        const u = document.getElementById('login-email').value.trim();
        const p = document.getElementById('login-pass').value.trim();
        const user = U.find(x=>x.username===u && x.password===p);
        if(user) {
            curUser = user;
            document.getElementById('login-screen').style.display='none';
            document.getElementById('app-container').classList.remove('hidden');
            document.getElementById('user-role').innerText = user.name;
            if(user.role==='admin') document.getElementById('btn-users').classList.remove('hidden');
            render();
        } else { alert('بيانات خاطئة'); }
    }
    function logout() { location.reload(); }

    // --- RENDER ---
    function switchTab(id) {
        document.querySelectorAll('section').forEach(s=>s.classList.add('hidden'));
        document.getElementById('view-'+id).classList.remove('hidden');
        document.querySelectorAll('.nav-item').forEach(b=>b.classList.replace('bg-green-700','hover:bg-slate-800'));
        document.getElementById('btn-'+id).classList.add('bg-green-700');
        document.getElementById('btn-'+id).classList.remove('hover:bg-slate-800');
    }

    function render() {
        // 1. Dashboard Selects & Populate
        const mType = document.querySelector('input[name="mType"]:checked').value;
        const list = mType==='chemical'?C:N;
        document.getElementById('tx-item').innerHTML = '<option value="">اختر...</option>' + list.map(i=>`<option value="${i.id}">${i.name} (${i.stock})</option>`).join('');
        document.getElementById('tx-sector').innerHTML = '<option value="">القطاع...</option>' + S.map(s=>`<option value="${s.name}">${s.name}</option>`).join('');
        
        // Low Stock
        const low = C.filter(i=>i.stock<=i.threshold);
        document.getElementById('low-stock-list').innerHTML = low.length ? low.map(i=>`<li class="flex justify-between items-center bg-red-50 p-2.5 rounded-lg border border-red-100 mb-2"><span class="font-bold text-red-700 text-xs">${i.name}</span><span class="bg-white px-2 py-0.5 rounded text-[10px] font-bold border border-red-200 text-red-600">${i.stock} ${i.unit}</span></li>`).join('') : '<li class="text-center text-green-600 p-4 bg-green-50 rounded-lg text-xs font-bold">جميع الأرصدة آمنة</li>';

        // Hint
        document.getElementById('tx-item').onchange = (e) => {
            const i = list.find(x=>String(x.id)===e.target.value);
            if(i) {
                const el = document.getElementById('tx-hint');
                el.innerText = `الرصيد: ${i.stock} ${i.unit}`;
                el.className = i.stock <= (i.threshold||0) ? 'text-xs mt-1 h-4 font-bold text-red-600' : 'text-xs mt-1 h-4 font-medium text-green-600';
            }
        };

        // 2. Inventory Grids
        const drawInv = (arr, id, col) => document.getElementById(id).innerHTML = arr.map(i=>`
            <div class="bg-white p-5 rounded-xl shadow-sm border border-slate-200 relative overflow-hidden group hover:shadow-md transition">
                <div class="absolute top-0 right-0 w-1.5 h-full ${col}"></div>
                <div class="flex justify-between items-start mb-2">
                    <h4 class="font-bold text-lg text-slate-800">${i.name}</h4>
                    <span class="text-[10px] bg-slate-100 text-slate-500 px-2 py-1 rounded-full">${i.type||'شبكة'}</span>
                </div>
                <div class="text-3xl font-bold text-slate-900 mt-2">${i.stock} <span class="text-xs text-slate-400 font-normal">${i.unit}</span></div>
            </div>`).join('');
        drawInv(C, 'inv-chem', 'bg-green-500');
        drawInv(N, 'inv-net', 'bg-blue-500');

        // 3. Data Tables
        const iconBtn = (fn, ic, col, tip) => `<button onclick="${fn}" class="text-${col}-500 hover:bg-${col}-50 p-1.5 rounded-full mx-0.5" title="${tip}"><span class="material-symbols-outlined text-lg">${ic}</span></button>`;
        const buildTbl = (title, arr, type, heads, rowsFn) => `
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden mb-6">
            <div class="bg-slate-50 px-5 py-3 flex justify-between items-center border-b border-slate-200">
                <div class="flex items-center gap-3">
                    <span class="font-bold text-slate-700">${title}</span>
                    <button id="del-btn-${type}" class="hidden bg-red-100 text-red-600 px-2 py-0.5 rounded text-[10px] font-bold hover:bg-red-200 transition" onclick="delSelected('${type}')">حذف المحدد</button>
                </div>
                <div class="no-print flex gap-2 text-xs">
                    <button class="text-blue-600 hover:underline" onclick="dlTemplate('${type}')">نموذج</button>
                    <label class="cursor-pointer text-green-600 hover:underline font-bold">استيراد<input hidden onchange="importExcel(this,'${type}')" type="file"></label>
                    <button class="bg-indigo-600 hover:bg-indigo-700 text-white px-3 py-1.5 rounded-lg transition" onclick="openModal('${type}')">إضافة</button>
                </div>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-right text-sm">
                    <thead class="bg-slate-100 text-slate-600"><tr>${curUser.role==='admin'?`<th class="p-3 w-8 text-center no-print"><input type="checkbox" onchange="toggleAll('${type}',this)"></th>`:''}<th class="p-3">الاسم</th>${heads}<th class="p-3 text-center no-print">إجراء</th></tr></thead>
                    <tbody class="divide-y divide-slate-100 text-slate-600">${arr.map(i=>`<tr class="hover:bg-slate-50 transition">${curUser.role==='admin'?`<td class="p-3 text-center no-print"><input type="checkbox" class="chk-${type}" value="${i.id}" onchange="checkSel('${type}')"></td>`:''}<td class="p-3 font-bold">${i.name}</td>${rowsFn(i)}<td class="p-3 text-center no-print flex justify-center gap-1">${curUser.role!=='viewer'?iconBtn(`openModal('${type}','${i.id}')`,'edit_square','blue', 'تعديل'):''}${curUser.role==='admin'?iconBtn(`delOne('${type}','${i.id}')`,'delete','red', 'حذف'):''}</td></tr>`).join('')}</tbody>
                </table>
            </div>
        </div>`;

        let html = buildTbl('القطاعات', S, 'sector', '<th>نخيل</th><th>أشجار</th><th>مساحة</th>', i=>`<td>${i.palms}</td><td>${i.trees}</td><td>${i.area} ف</td>`);
        html += buildTbl('الكيماويات', C, 'chemical', '<th>النوع</th><th>رصيد</th><th>وحدة</th><th>حد</th>', i=>`<td>${i.type}</td><td class="font-bold">${i.stock}</td><td>${i.unit}</td><td class="text-red-500">${i.threshold}</td>`);
        html += buildTbl('الشبكات', N, 'network', '<th>كمية</th><th>وحدة</th>', i=>`<td class="font-bold">${i.stock}</td><td>${i.unit}</td>`);
        document.getElementById('data-tables-container').innerHTML = html;

        // 4. Logs
        document.getElementById('tbl-logs').innerHTML = L.map(l=>`<tr class="hover:bg-slate-50"><td class="p-4 text-xs text-slate-400 dir-ltr text-right">${l.date}</td><td class="p-4"><span class="px-2 py-1 rounded text-[10px] font-bold ${l.mType=='chemical'?'bg-green-100 text-green-700':'bg-blue-100 text-blue-700'}">${l.mType=='chemical'?'مبيد/سماد':'شبكة'}</span></td><td class="p-4 font-bold text-slate-700">${l.item}</td><td class="p-4 text-sm text-slate-600">${l.sector}</td><td class="p-4 font-bold text-red-600">-${l.qty}</td><td class="p-4 no-print text-center">${curUser.role==='admin'?iconBtn(`delLog(${l.id})`,'undo','slate', 'تراجع'):''}</td></tr>`).join('');

        // 5. Users
        if(curUser.role==='admin') {
            document.getElementById('tbl-users').innerHTML = U.map(u=>`<tr class="border-b hover:bg-slate-50"><td class="p-4 font-bold text-slate-700">${u.name}</td><td class="p-4 font-mono text-xs text-slate-500">${u.username}</td><td class="p-4"><span class="bg-slate-100 text-slate-600 px-2 py-1 rounded text-xs">${u.role}</span></td><td class="p-4 text-center">${u.username.includes('@')?'':iconBtn(`delUser(${u.id})`,'delete','red', 'حذف')}</td></tr>`).join('');
        }
    }

    // --- ACTIONS ---
    function handleTransaction(e) {
        e.preventDefault();
        if(curUser.role==='viewer') return alert('لا تملك صلاحية');
        const type = document.querySelector('input[name="mType"]:checked').value;
        const itemId = document.getElementById('tx-item').value;
        const secName = document.getElementById('tx-sector').value;
        const qty = +document.getElementById('tx-qty').value;
        
        const list = type==='chemical'?C:N;
        const item = list.find(x=>String(x.id)===itemId);
        
        if(!item || !secName) return alert('بيانات ناقصة');
        if(qty > item.stock) return alert('الرصيد غير كاف');
        
        item.stock = +(item.stock - qty).toFixed(2);
        L.unshift({id:Date.now(), date:new Date().toLocaleString('ar-EG'), mType:type, item:item.name, sector:secName, qty:qty, itemId:item.id});
        save(); e.target.reset(); alert('تم الحفظ');
    }

    // --- POPULATING SELECTS (IMPORTANT Fix) ---
    function populateSelects() {
        const mType = document.querySelector('input[name="mType"]:checked').value;
        const list = mType==='chemical'?C:N;
        document.getElementById('tx-item').innerHTML = '<option value="">اختر...</option>' + list.map(i=>`<option value="${i.id}">${i.name} (${i.stock})</option>`).join('');
        document.getElementById('tx-sector').innerHTML = '<option value="">القطاع...</option>' + S.map(s=>`<option value="${s.name}">${s.name}</option>`).join('');
        document.getElementById('tx-hint').innerText = '';
    }

    // --- MODALS & CRUD ---
    function openModal(type, id) {
        document.getElementById('modal-edit').style.display = 'flex';
        document.getElementById('modal-title').innerText = id ? 'تعديل' : 'إضافة';
        document.getElementById('edit-id').value = id || 'new';
        document.getElementById('edit-type').value = type;
        
        const list = type==='sector'?S:(type==='chemical'?C:N);
        const d = id ? list.find(x=>String(x.id)===String(id)) : {};
        const f = document.getElementById('modal-fields');
        
        if(type === 'sector') {
            f.innerHTML = `
                <div><label class="text-xs font-bold block mb-1">الاسم</label><input id="f-name" class="w-full border p-2 rounded-lg" value="${d.name||''}" required></div>
                <div class="grid grid-cols-2 gap-3">
                    <div><label class="text-xs font-bold block mb-1">نخيل</label><input id="f-palms" type="number" class="w-full border p-2 rounded-lg" value="${d.palms||0}"></div>
                    <div><label class="text-xs font-bold block mb-1">أشجار</label><input id="f-trees" type="number" class="w-full border p-2 rounded-lg" value="${d.trees||0}"></div>
                </div>
                <div><label class="text-xs font-bold block mb-1">مساحة (فدان)</label><input id="f-area" type="number" step="0.1" class="w-full border p-2 rounded-lg" value="${d.area||0}"></div>
            `;
        } else if (type === 'chemical') {
            f.innerHTML = `
                <div><label class="text-xs font-bold block mb-1">الاسم</label><input id="f-name" class="w-full border p-2 rounded-lg" value="${d.name||''}" required></div>
                <div class="flex gap-2"><input id="f-type" class="w-full border p-2 rounded-lg" placeholder="النوع" value="${d.type||''}"><input id="f-unit" class="w-full border p-2 rounded-lg" placeholder="الوحدة" value="${d.unit||''}"></div>
                <div class="flex gap-2"><input id="f-stock" type="number" step="0.1" class="w-full border p-2 rounded-lg" placeholder="الرصيد" value="${d.stock||0}"><input id="f-thresh" type="number" class="w-full border p-2 rounded-lg" placeholder="الحد" value="${d.threshold||0}"></div>
            `;
        } else {
            f.innerHTML = `
                <div><label class="text-xs font-bold block mb-1">الاسم</label><input id="f-name" class="w-full border p-2 rounded-lg" value="${d.name||''}" required></div>
                <div class="flex gap-2"><input id="f-stock" type="number" step="0.1" class="w-full border p-2 rounded-lg" placeholder="الكمية" value="${d.stock||0}"><input id="f-unit" class="w-full border p-2 rounded-lg" placeholder="الوحدة" value="${d.unit||''}"></div>
            `;
        }
    }

    function saveData(e) {
        e.preventDefault();
        const type = document.getElementById('edit-type').value;
        const id = document.getElementById('edit-id').value;
        const list = type==='sector'?S:(type==='chemical'?C:N);
        const val = k => document.getElementById(k).value;
        
        let obj = type==='sector' ? {name:val('f-name'), palms:+val('f-palms'), trees:+val('f-trees'), area:+val('f-area')} : 
                  type==='chemical' ? {name:val('f-name'), type:val('f-type'), stock:+val('f-stock'), unit:val('f-unit'), threshold:+val('f-thresh')} : 
                  {name:val('f-name'), stock:+val('f-stock'), unit:val('f-unit')};
                  
        if(id==='new') { obj.id = (type==='sector'?'S':'')+Date.now(); list.push(obj); }
        else { const idx = list.findIndex(x=>String(x.id)===id); if(idx>-1) list[idx] = {...list[idx], ...obj}; }
        save(); document.getElementById('modal-edit').style.display='none';
    }

    function closeModal() { document.getElementById('modal-edit').style.display='none'; }
    
    // --- HELPERS & DELETE ---
    function delOne(type, id) { if(confirm('حذف؟')) { const list = type==='sector'?S:(type==='chemical'?C:N); const idx = list.findIndex(x=>String(x.id)===String(id)); if(idx>-1) { list.splice(idx,1); save(); } } }
    function delLog(id) { const idx = L.findIndex(x=>x.id==id); if(idx>-1) { const l=L[idx]; const list=l.mType==='chemical'?C:N; const i=list.find(x=>x.id==l.itemId); if(i) i.stock = +(i.stock+l.qty).toFixed(2); L.splice(idx,1); save(); alert('تم التراجع'); } }
    function toggleAll(type, el) { document.querySelectorAll(`.chk-${type}`).forEach(c => c.checked = el.checked); checkSel(type); }
    function checkSel(type) { const n = document.querySelectorAll(`.chk-${type}:checked`).length; const btn = document.getElementById(`del-btn-${type}`); if(btn) { if(n>0) { btn.classList.remove('hidden'); btn.innerText=`حذف (${n})`; } else btn.classList.add('hidden'); } }
    function delSelected(type) { if(!confirm('حذف؟')) return; const ids = Array.from(document.querySelectorAll(`.chk-${type}:checked`)).map(c=>c.value); if(type==='sector') S=S.filter(x=>!ids.includes(String(x.id))); else if(type==='chemical') C=C.filter(x=>!ids.includes(String(x.id))); else N=N.filter(x=>!ids.includes(String(x.id))); save(); }

    // --- FILE OPS ---
    function backupJSON() { const a=document.createElement('a'); a.href="data:text/json;charset=utf-8,"+encodeURIComponent(JSON.stringify({sectors:S, chemicals:C, networks:N, logs:L, users:U})); a.download="Farm_Data.json"; a.click(); }
    function restoreJSON(inp) { const r=new FileReader(); r.onload=(e)=>{ try { const d=JSON.parse(e.target.result); if(confirm('استعادة؟')) { S=d.sectors; C=d.chemicals; N=d.networks; L=d.logs; U=d.users; save(); location.reload(); } } catch{alert('خطأ');} }; r.readAsText(inp.files[0]); }
    function dlTemplate(type) { const wb = XLSX.utils.book_new(); let h=[]; if(type==='sector') h=['الاسم','نخيل','اشجار','مساحة']; else if(type==='chemical') h=['الاسم','النوع','رصيد','وحدة','حد']; else h=['الاسم','كمية','وحدة']; XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet([h]), "Template"); XLSX.writeFile(wb, `Template_${type}.xlsx`); }
    function importExcel(inp, type) { const r = new FileReader(); r.onload = (e) => { try { const d = XLSX.utils.sheet_to_json(XLSX.read(new Uint8Array(e.target.result), {type:'array'}).Sheets['Template']||XLSX.utils.sheet_to_json(XLSX.read(new Uint8Array(e.target.result), {type:'array'}).Sheets['Sheet1'])); const list = type==='sector'?S:(type==='chemical'?C:N); d.forEach(r => { const name = r['الاسم']; if(name && !list.find(x=>x.name===name)) { if(type==='sector') list.push({id:'S'+Math.random(), name, palms:+r['نخيل']||0, trees:+r['اشجار']||0, area:+r['مساحة']||0}); else if(type==='chemical') list.push({id:Date.now()+Math.random(), name, type:r['النوع']||'', stock:+r['رصيد']||0, unit:r['وحدة']||'', threshold:+r['حد']||0}); else list.push({id:Date.now()+Math.random(), name, stock:+r['كمية']||0, unit:r['وحدة']||''}); } }); save(); alert('تم'); } catch { alert('خطأ'); } inp.value=''; }; r.readAsArrayBuffer(inp.files[0]); }
    function exportPDF(id, name) { const el = document.getElementById(id); html2pdf().from(el).set({margin:0.5, filename:name+'.pdf', html2canvas:{scale:2}, jsPDF:{unit:'in', format:'letter', orientation:'landscape'}}).save(); }
    function downloadSystem() {
        const state = JSON.stringify({ sectors:S, chemicals:C, networks:N, logs:L, users:U }, null, 2);
        let html = document.documentElement.outerHTML.replace(/\/\*DATA_START\*\/[\s\S]*?\/\*DATA_END\*\//, `/*DATA_START*/\n const initialData = ${state};\n /*DATA_END*/`);
        html = html.replace('id="app-container" class="flex h-full w-full"', 'id="app-container" class="flex h-full w-full hidden"').replace('id="login-screen" class="fixed inset-0 z-50 bg-slate-900 flex justify-center items-center hidden"', 'id="login-screen" class="fixed inset-0 z-50 bg-slate-900 flex justify-center items-center"');
        const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob(["<!DOCTYPE html>"+html], {type:"text/html"})); a.download = "Smart_Farm_V24_Full.html"; a.click();
    }
    
    // Start
    init();
</script>

</body></html>
