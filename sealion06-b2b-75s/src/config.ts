// All model copy, figures, colors and motion parameters live here.
// Values are USER BRIEF ONLY until the supplied configuration table can be read.
export const CONFIG={
 width:1920,height:1080,fps:30,total:2250,model:'BYD SEALION 06 EV',series:'UNILAND SPEC LAB',
 specsVerified:true,
 colors:{background:'#f4f3f0',surface:'#e9eceb',ink:'#26383f',muted:'#69797e',accent:'#557d8b',line:'#bac8cd',white:'#ffffff'},
 fonts:{body:'Display',data:'Data'},
 motion:{fade:24,transition:12,roll:32,stagger:4,stroke:66,photoScale:1},
 typography:{title:68,value:106,subtitle:56,label:34,metadata:32},
 cta:'Contact Us for Bulk Order',
 copy:{draft:'DRAFT · CONFIGURATION TABLE PENDING',photoPending:'ORIGINAL PHOTOGRAPH PENDING',photoPendingNote:'No substitute vehicle image has been used.',rangeScale:'CLTC RANGE',rangeEnd:'605 km',powerCaption:'REAR-WHEEL DRIVE',chargingInterval:'30–80% DC',minutes:'minutes',chargingBenefit:'More time for the journey.',adasTitle:'DiPilot 100',adasHardware:'Three-eye ADAS',adasFunctions:'Highway + Parking Assist',adasDescription:'Navigation & parking assistance',suspension:'Adjustable Suspension',seats:'5-Seater SUV',safetyControl:'ESC + Tyre Pressure Monitoring',airbagTitle:'Occupant Protection',airbagLocations:'Front · Side · Curtain · Centre',airbagLabel:'Airbag Coverage',dimension:'2820 mm wheelbase'},
 notes:{range:'CLTC laboratory cycle. Actual range varies.',charge:'Charging time depends on battery and charger conditions.',adas:'L2 assistance. Driver supervision required. Features vary by market.',general:'Configuration and market availability may vary.'},
};
export type PhotoSet={range:string;performance:string;charging:string;assistance:string;comfort:string;safety:string};
export const DEFAULT_PHOTOS:PhotoSet={range:'',performance:'',charging:'',assistance:'',comfort:'',safety:''};
export const SCENES=[
 {id:'range',from:0,duration:420,title:'Go further. Every day.',eyebrow:'RANGE & ENERGY',numbers:[{value:'605',unit:'km',label:'CLTC Long Range',delay:25},{value:'78.72',unit:'kWh',label:'Blade LFP Battery',delay:216}],voice:['The Sealion Zero Six EV offers six hundred and five kilometres of CLTC range.','A seventy-eight point seven two kilowatt-hour Blade battery powers the journey.']},
 {id:'performance',from:420,duration:300,title:'Responsive. Rear-wheel driven.',eyebrow:'POWER & RESPONSE',numbers:[{value:'180',unit:'kW',label:'Rear Motor',delay:20},{value:'7.7',unit:'s',label:'0–100 km/h',delay:145}],voice:['A one-hundred-and-eighty-kilowatt rear motor.','Zero to one hundred kilometres per hour in seven point seven seconds.']},
 {id:'charging',from:720,duration:300,title:'Less waiting. More possibility.',eyebrow:'DC FAST CHARGING',numbers:[{value:'18',unit:'min',label:'30–80% DC Fast Charge',delay:55}],voice:['DC charging from thirty to eighty percent takes about eighteen minutes,','under suitable battery and charging conditions.']},
 {id:'assistance',from:1020,duration:360,title:'Confidence, with assistance.',eyebrow:'INTELLIGENT DRIVING',numbers:[],voice:['DiPilot One Hundred combines three-camera vision with highway and parking assistance.','Features depend on configuration and market. Driver supervision is required.']},
 {id:'comfort',from:1380,duration:360,title:'Room to relax. Control to enjoy.',eyebrow:'COMFORT & SPACE',numbers:[{value:'2820',unit:'mm',label:'Wheelbase',delay:25}],voice:['A two-thousand-eight-hundred-and-twenty-millimetre wheelbase creates space for five.','Adjustable suspension supports everyday ride comfort.']},
 {id:'safety',from:1740,duration:390,title:'Protection, engineered in.',eyebrow:'BODY & OCCUPANT SAFETY',numbers:[],voice:['Front, side, curtain and centre airbags provide occupant protection.','Electronic stability control and tyre pressure monitoring add everyday reassurance.']},
 {id:'cta',from:2130,duration:120,title:'BYD SEALION 06 EV',eyebrow:'',numbers:[],voice:['Contact UNILAND for bulk orders.']},
] as const;
