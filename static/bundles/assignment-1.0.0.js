/*! For license information please see assignment-1.0.0.js.LICENSE.txt */
(()=>{"use strict";var e={"./static/assignment/js/src/Dropzone.js":(e,t,r)=>{r.r(t),r.d(t,{default:()=>s});var n=r("react"),o=r.n(n),a=(r("react-dom"),r("./node_modules/react-dropzone/dist/es/index.js"));function i(){return(i=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function s(e){var t=(0,n.useCallback)(e.onDrop,[]),r=(0,a.useDropzone)({onDrop:t}),s=(r.acceptedFiles,r.getRootProps),c=r.getInputProps,u=r.isDragActive;return o().createElement(o().Fragment,null,o().createElement("div",i({className:"dropzone dropzone-multiple mb-2"},s()),o().createElement("input",c()),u?o().createElement("p",null,"Drop the files here ..."):o().createElement("div",{className:"dz-default dz-message"},o().createElement("span",null,"Drag 'n' drop some files here, or click to select files"))))}},"./static/assignment/js/src/Material.js":(e,t,r)=>{r.r(t),r.d(t,{default:()=>b});var n=r("react"),o=r.n(n),a=(r("react-dom"),r("./node_modules/file-extension/file-extension.js")),i=r.n(a),s=r("./node_modules/path-browserify/index.js"),c=r("./node_modules/classnames/index.js"),u=r.n(c);function l(e){return(l="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function f(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function p(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function m(e,t){return(m=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function y(e,t){return!t||"object"!==l(t)&&"function"!=typeof t?function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function d(e){return(d=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}var b=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&m(e,t)}(l,e);var t,r,n,a,c=(n=l,a=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}(),function(){var e,t=d(n);if(a){var r=d(this).constructor;e=Reflect.construct(t,arguments,r)}else e=t.apply(this,arguments);return y(this,e)});function l(){return f(this,l),c.apply(this,arguments)}return t=l,(r=[{key:"render",value:function(){var e=this,t=this.props.m;return o().createElement("li",{className:"mb-2 position-relative"},o().createElement("a",{href:t.file,target:"_blank",className:"position-relative"},o().createElement("span",{className:u()("fiv-sqo","fiv-icon-".concat(i()(t.file)))}),o().createElement("span",{className:"text-sm font-weight-bold text-dark"},(0,s.basename)(t.file)),o().createElement("span",{onClick:function(r){e.props.onRemoveClick(r,t)},className:"px-2 position-absolute right-0"},o().createElement("i",{className:"ni ni-fat-remove"}))),t.progress?o().createElement("div",{className:"progress"},o().createElement("div",{className:"progress-bar bg-default",role:"progressbar",style:{width:"".concat(t.progress,"%")}})):"")}}])&&p(t.prototype,r),l}(o().Component)},"./static/assignment/js/src/MaterialList.js":(e,t,r)=>{r.r(t),r.d(t,{default:()=>p});var n=r("react"),o=r.n(n),a=(r("react-dom"),r("./static/assignment/js/src/Material.js"));function i(e){return(i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function s(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function c(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function u(e,t){return(u=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function l(e,t){return!t||"object"!==i(t)&&"function"!=typeof t?function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function f(e){return(f=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}var p=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&u(e,t)}(m,e);var t,r,n,i,p=(n=m,i=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}(),function(){var e,t=f(n);if(i){var r=f(this).constructor;e=Reflect.construct(t,arguments,r)}else e=t.apply(this,arguments);return l(this,e)});function m(e){var t;return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,m),(t=p.call(this,e)).state={materials:[]},t}return t=m,(r=[{key:"componentWillReceiveProps",value:function(e){e.materials!==this.state.materials&&this.setState({materials:e.materials})}},{key:"render",value:function(){var e,t=this;return o().createElement("ul",{className:"material"},(e=this.state.materials,function(e){if(Array.isArray(e))return s(e)}(e)||function(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(e)||function(e,t){if(e){if("string"==typeof e)return s(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?s(e,t):void 0}}(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).reverse().map((function(e,r){return o().createElement(a.default,{onRemoveClick:t.props.onRemoveClick,m:e,key:r})})))}}])&&c(t.prototype,r),m}(o().Component)},"./static/assignment/js/src/index.js":(e,t,r)=>{r.r(t);var n=r("react"),o=r.n(n),a=r("react-dom"),i=r.n(a),s=r("./node_modules/axios/index.js"),c=r.n(s),u=(r("./node_modules/file-extension/file-extension.js"),r("./node_modules/classnames/index.js"),r("./node_modules/path-browserify/index.js"),r("./node_modules/react-dropzone/dist/es/index.js"),r("./static/assignment/js/src/MaterialList.js")),l=r("./static/assignment/js/src/Dropzone.js");function f(e){return(f="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function p(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function m(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?p(Object(r),!0).forEach((function(t){j(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):p(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function y(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function d(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function b(e,t){return(b=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function h(e,t){return!t||"object"!==f(t)&&"function"!=typeof t?v(e):t}function v(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function g(e){return(g=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function j(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var O=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&b(e,t)}(s,e);var t,r,n,a,i=(n=s,a=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}(),function(){var e,t=g(n);if(a){var r=g(this).constructor;e=Reflect.construct(t,arguments,r)}else e=t.apply(this,arguments);return h(this,e)});function s(e){var t;return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,s),j(v(t=i.call(this,e)),"fetchMaterial",(function(e){return c().get(t.props.request_url).then(e)})),j(v(t),"handleRemoveClick",(function(e,r){if(e.preventDefault(),window.confirm("Are you sure you wish to delete this item?"))return c().delete(r.request_url).then((function(e){t.setState({materials:t.state.materials.filter((function(e){return e.id!=r.id}))})}))})),j(v(t),"handleOnDrop",(function(e){return e.forEach((function(e,r){var n,o=new FormData;return o.append("file",e),o.append(t.props.page,t.props.page_id),t.setState({materials:[].concat((n=t.state.materials,function(e){if(Array.isArray(e))return y(e)}(n)||function(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}(n)||function(e,t){if(e){if("string"==typeof e)return y(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?y(e,t):void 0}}(n)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()),[{file:e.path,id:r,beingUpload:!0}])}),c().post(t.props.request_url,o,{headers:{"content-type":"multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"},onUploadProgress:function(e){var n=+(e.loaded/e.total*100).toFixed(2);window.unsavedChanges=!0,debounce((function(){t.setState({materials:t.state.materials.map((function(e){return e.beingUpload&&e.id==r?m(m({},e),{},{progress:n}):e}))}),window.unsavedChanges=!1}),500)()}}).then((function(e){var n=e.data,o=e.config.url;n.request_url="".concat(o).concat(n.id),t.setState({uploadMaterials:t.state.uploadMaterials.filter((function(e){return e.id!=r})),materials:t.state.materials.map((function(e){return e.beingUpload&&e.id==r?m(m({},e),{},{progress:!1,beingUpload:!1},n):e}))})}))}))})),c().defaults.xsrfCookieName="csrftoken",c().defaults.xsrfHeaderName="X-CSRFTOKEN",t.state={materials:[],uploadMaterials:[]},t}return t=s,(r=[{key:"componentDidMount",value:function(){var e=this;this.fetchMaterial((function(t){e.setState({materials:t.data})}))}},{key:"render",value:function(){return o().createElement(o().Fragment,null,this.props.graded||this.props.turned?"":o().createElement(l.default,{onDrop:this.handleOnDrop}),o().createElement(u.default,{onRemoveClick:this.handleRemoveClick,materials:this.state.materials}))}}])&&d(t.prototype,r),s}(o().Component),w=o().createElement(O,window.material_list_app_props);i().render(w,document.getElementById("material-app"))},react:e=>{e.exports=React},"react-dom":e=>{e.exports=ReactDOM}},t={};function r(n){if(t[n])return t[n].exports;var o=t[n]={exports:{}};return e[n](o,o.exports,r),o.exports}r.m=e,r.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return r.d(t,{a:t}),t},r.d=(e,t)=>{for(var n in t)r.o(t,n)&&!r.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},r.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),r.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{var e={assignment:0},t=[["./static/assignment/js/src/index.js","vendors"]],n=()=>{};function o(){for(var n,o=0;o<t.length;o++){for(var a=t[o],i=!0,s=1;s<a.length;s++){var c=a[s];0!==e[c]&&(i=!1)}i&&(t.splice(o--,1),n=r(r.s=a[0]))}return 0===t.length&&(r.x(),r.x=()=>{}),n}r.x=()=>{r.x=()=>{},i=i.slice();for(var e=0;e<i.length;e++)a(i[e]);return(n=o)()};var a=o=>{for(var a,i,[c,u,l,f]=o,p=0,m=[];p<c.length;p++)i=c[p],r.o(e,i)&&e[i]&&m.push(e[i][0]),e[i]=0;for(a in u)r.o(u,a)&&(r.m[a]=u[a]);for(l&&l(r),s(o);m.length;)m.shift()();return f&&t.push.apply(t,f),n()},i=self.webpackChunksaiki=self.webpackChunksaiki||[],s=i.push.bind(i);i.push=a})(),r.x()})();
//# sourceMappingURL=assignment-1.0.0.js.map