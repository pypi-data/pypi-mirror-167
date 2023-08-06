import Y from"../components/Aside.js";import e,{useEffect as w,useMemo as Z,useState as n}from"../../__snowpack__/pkg/react.js";import{asideWidth as ee,rem as a}from"../utils/style.js";import te from"../components/Content.js";import ne from"../components/ProfilerPage/overview/overview.js";import re from"../components/ProfilerPage/OperatorView/OperatorView.js";import le from"../components/ProfilerPage/MemoryView/MemoryView.js";import se from"../components/ProfilerPage/TracingView.js";import ae from"../components/ProfilerPage/Distributed/Distributed.js";import oe from"../components/ProfilerPage/ComparedView/ComparedView.js";import ie from"../components/Select.js";import{fetcher as v}from"../utils/fetch.js";import m from"../components/Field.js";import ce from"../components/Title.js";import d from"../../__snowpack__/pkg/styled-components.js";import{useTranslation as me}from"../../__snowpack__/pkg/react-i18next.js";ee;const pe=d.div`
    padding: ${a(20)};
    border-bottom: 1px solid #dddddd;
`,p=d(ie)`
    width: 100%;
`,ue=d.div`
    font-family: PingFangSC-Regular;
    font-size: ${a(14)};
    color: #000000;
    letter-spacing: 0;
    line-height: ${a(14)};
    font-weight: 400;
    // margin-bottom: ${a(20)};
`,de=d.div`
    width: 100%;
    border-radius: 4px;
    padding: ${a(20)};
`,u=d.div`
    margin-bottom: ${a(20)};
`,fe=d.div`
    padding: ${a(0)} ${a(20)};
    padding-bottom: 0px;
    .Groups {
        .Selectlist {
            width: 100%;
            border-radius: ${a(4)};
            padding-bottom: ${a(20)};
        }
    }
`,G=d.div`
    border-top: 1px solid #dddddd;
    padding-top: ${a(20)};
    margin-bottom: ${a(20)};
    font-family: PingFangSC-Regular;
    font-size: ${a(14)};
    color: #999999;
    -webkit-letter-spacing: 0;
    -moz-letter-spacing: 0;
    -ms-letter-spacing: 0;
    letter-spacing: 0;
    line-height: ${a(14)};
    font-weight: 400;
`,ge=d.div`
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: stretch;
    align-items: stretch;
`,Ee=d.div`
    width: 100%;
    flex-grow: 1;
    position: relative;
`,ve=()=>{const{t:f,i18n:D}=me(["profiler","common"]),[$,we]=n(!1),[r,k]=n(""),[P,M]=n(""),[j,N]=n(""),[t,S]=n(""),[i,L]=n(""),[V,z]=n(""),[y,A]=n(""),[g,_]=n(""),[E,U]=n("us"),[W,H]=n(""),[x,I]=n(""),[h,K]=n(),[T,q]=n(),[b,B]=n(),[C,J]=n(),[R,F]=n(),[O,Q]=n();w(()=>{D.language&&v(`/profiler/descriptions?lang=${D.language}`).then(o=>{Q(o)})},[D.language]),w(()=>{v("/profiler/runs").then(o=>{const s=o,c=s.map(l=>({label:l,value:l}));K(c),k(s[0])}),v("/profiler/timeunits").then(o=>{const c=o.map(l=>({label:l,value:l}));F(c)})},[]),w(()=>{v("/profiler/timeunits").then(o=>{const c=o.map(l=>({label:l,value:l}));F(c)})},[]),w(()=>{r&&v(`/profiler/views?run=${r}`).then(o=>{const s=o,c=s.map(l=>({label:l,value:l}));q(c),S(s[0])})},[r]),w(()=>{r&&t&&v(`/profiler/workers?run=${r}&view=${t}`).then(o=>{const s=o,c=s.map(l=>({label:l,value:l}));B(c),L(s[0])})},[r,t]),w(()=>{r&&i&&v(`/profiler/spans?run=${r}&worker=${i}`).then(o=>{const s=o,c=s.map(l=>({label:l,value:l}));J(c),_(s[0])})},[r,i]);const X=Z(()=>e.createElement(Y,null,e.createElement(pe,null,e.createElement(ue,null,f("performance-analysis"))),$?e.createElement(fe,null,e.createElement("div",{className:"Groups"},e.createElement(G,{style:{border:"none"}},"\u57FA\u7EBF\u7EC4"),e.createElement("div",{className:"Selectlist"},e.createElement(u,null,e.createElement(m,{label:"\u6570\u636E\u6D41"},e.createElement(p,{list:h,value:P,onChange:M}))),e.createElement(u,null,e.createElement(m,{label:"\u8FDB\u7A0B"},e.createElement(p,{list:b,value:V,onChange:z}))),e.createElement(u,null,e.createElement(m,{label:"\u8FDB\u7A0B\u8DE8\u5EA6"},e.createElement(p,{list:C,value:W,onChange:H}))))),e.createElement("div",{className:"Groups"},e.createElement(G,null,"\u57FA\u7EBF\u7EC4"),e.createElement("div",{className:"Selectlist"},e.createElement(u,null,e.createElement(m,{label:"\u6570\u636E\u6D41"},e.createElement(p,{list:h,value:j,onChange:N}))),e.createElement(u,null,e.createElement(m,{label:"\u8FDB\u7A0B"},e.createElement(p,{list:b,value:y,onChange:A}))),e.createElement(u,null,e.createElement(m,{label:"\u8FDB\u7A0B\u8DE8\u5EA6"},e.createElement(p,{list:C,value:x,onChange:I})))))):e.createElement(de,null,e.createElement(u,null,e.createElement(m,{label:f("data-flow")},e.createElement(p,{list:h,value:r,onChange:k}))),e.createElement(u,null,e.createElement(m,{label:f("view")},e.createElement(p,{list:T,value:t,onChange:S}))),e.createElement(u,null,e.createElement(m,{label:f("process")},e.createElement(p,{list:b,value:i,onChange:L}))),e.createElement(u,null,e.createElement(m,{label:f("process-span")},e.createElement(p,{list:C,value:g,onChange:_}))),t!=="Trace"?e.createElement(u,null,e.createElement(m,{label:f("time-unit")},e.createElement(p,{list:R,value:E,onChange:U}))):null)),[C,g,b,i,T,t,h,r,$,y,j,V,P,W,x,E,R,f]);return e.createElement(e.Fragment,null,e.createElement(ce,null,f("common:hyper-parameter")),e.createElement(te,{aside:X,isProfiler:!0},e.createElement(ge,null,e.createElement(Ee,null,t==="Overview"?e.createElement(ne,{runs:r,views:t,workers:i,units:E,spans:g,descriptions:O}):null,t==="Operator"?e.createElement(re,{runs:r,views:t,workers:i,units:E,spans:g}):null,t==="Distributed"?e.createElement(ae,{runs:r,views:t,workers:i,units:E,spans:g,descriptions:O}):null,t==="GPU Kernel"?e.createElement(oe,{runs:r,views:t,workers:i,units:E,spans:g}):null,t==="Memory"?e.createElement(le,{runs:r,views:t,workers:i,units:E,spans:g}):null,t==="Trace"?e.createElement(se,{runs:r,views:t,workers:i,spans:g}):null))))};export default ve;
