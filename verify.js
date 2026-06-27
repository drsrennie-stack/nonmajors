const DAY_MS = 86400000;
// Chelsea's active study days (total>0) from the report
const activeDays = ["2026-06-09","2026-06-10","2026-06-11","2026-06-12","2026-06-15",
"2026-06-16","2026-06-17","2026-06-19","2026-06-20","2026-06-23","2026-06-24","2026-06-25","2026-06-26"];
const today = "2026-06-26";

function expectedWeekdays(){
  const sorted = activeDays.slice().sort();
  const start = new Date(sorted[0]+"T00:00:00");
  const end = new Date(today+"T00:00:00");
  let cnt=0;
  for(let t=start.getTime();t<=end.getTime();t+=DAY_MS){
    const dow=new Date(t).getDay();
    if(dow>=1&&dow<=5) cnt++;
  }
  return Math.max(1,cnt);
}
const expected = expectedWeekdays();

// fixed components from report
const coverage=1.00, depth=0.61;
const composite=(con)=>Math.round((0.5*coverage+0.3*con+0.2*depth)*100);

// ---- OLD logic ----
function oldConsistency(clearedDays){
  const anyTracked = clearedDays.length>0;
  const compliant = anyTracked ? new Set(clearedDays).size : activeDays.length;
  return Math.min(1, compliant/expected);
}
// ---- NEW logic ----
function newConsistency(clearedDays, trackingStart){
  const clearedSet=new Set(clearedDays);
  const compliant = activeDays.filter(d=> d<trackingStart || clearedSet.has(d)).length;
  return Math.min(1, compliant/expected);
}

console.log("expected weekdays in range:", expected);
console.log("\n=== OLD (buggy) logic ===");
let oBefore=oldConsistency([]);          // before clearing any day today
let oAfter =oldConsistency([today]);     // after completing daily review
console.log("before review: consistency", Math.round(oBefore*100)+"%, TOTAL", composite(oBefore)+"%");
console.log("after  review: consistency", Math.round(oAfter*100)+"%, TOTAL", composite(oAfter)+"%  <-- drops!");

console.log("\n=== NEW (fixed) logic, trackingStart="+today+" ===");
let nBefore=newConsistency([], today);     // today not yet cleared
let nAfter =newConsistency([today], today);// after completing daily review
console.log("before review: consistency", Math.round(nBefore*100)+"%, TOTAL", composite(nBefore)+"%");
console.log("after  review: consistency", Math.round(nAfter*100)+"%, TOTAL", composite(nAfter)+"%  <-- goes up, never down");

console.log("\n=== Future new student (no past days), trackingStart=day1 ===");
// simulate: fresh student studies 1 weekday, clears it
const fActive=["2026-08-25"]; // a Monday
const fExpected=1;
const fCompliantCleared = fActive.filter(d=> d<"2026-08-25" || new Set(["2026-08-25"]).has(d)).length;
console.log("studies & clears day 1: consistency", Math.round(Math.min(1,fCompliantCleared/fExpected)*100)+"%");
