var xjs = require('xjs');
var App = new xjs.App();

window.onload = init;

var isXsplit = false;

var xhr = new XMLHttpRequest();

var timestampOld=0;
var timestamp=0;
var cacheBusterValiable=Date.now();
var cacheBuster=0;

var animating = false;
var firstupdate = true;

var scObj;


var scObjOld = {
    cb_1_1: '',
    cb_1_2: '',
    cb_1_3: '',
    cb_1_4: '',
    cb_1_5: '',
    cb_1_6: '',
    cb_1_7: '',
    cb_1_8: '',
    cb_1_9: '',
    cb_2_1: '',
    cb_2_2: '',
    cb_2_3: '',
    cb_2_4: '',
    cb_2_5: '',
    cb_2_6: '',
    cb_2_7: '',
    cb_2_8: '',
    cb_2_9: '',
    cb_1_1_score: '',
    cb_1_2_score: '',
    cb_1_3_score: '',
    cb_1_4_score: '',
    cb_1_5_score: '',
    cb_1_6_score: '',
    cb_1_7_score: '',
    cb_1_8_score: '',
    cb_1_9_score: '',
    cb_2_1_score: '',
    cb_2_2_score: '',
    cb_2_3_score: '',
    cb_2_4_score: '',
    cb_2_5_score: '',
    cb_2_6_score: '',
    cb_2_7_score: '',
    cb_2_8_score: '',
    cb_2_9_score: '',
    select_Lmember: '0',
    select_Rmember: '0',
    cb_memberNum: ''
}

var isPreview = false;

function init() {
    //アニメーションは、基本init()内部で GSAP の TweenMax を用いて描写。
    xjs.ready().then(xjs.Source.getCurrentSource).then(function(curItem) {
        var sourceWindow = xjs.SourcePluginWindow.getInstance();
        App.getVersion().then(function(res) {
            var version = res;
            console.log(version);
        });
        isXsplit = true;

        XJSitem = curItem;

        XJSitem.setBrowserCustomSize(xjs.Rectangle.fromDimensions(1280,48));
        XJSitem.setPosition(xjs.Rectangle.fromCoordinates(0,0,1,0.0666666666666667));
        XJSitem.setPositionLocked(true);

        XJSitem.getView().then(function(view) {
            console.log("view:" +view);
            if (view != 0) {
                isPreview = true;
            }
        });

        App.getTransition().then(function(res) {
            var currTransition = res._value;
            console.log(currTransition);
            if (currTransition.indexOf(".webm") == -1 ){
                setTimeout(update,300);
            } else {
                var transitionDuration = currTransition.split('.webm,')[1] / 10000 ;
                if (!transitionDuration) {
                    transitionDuration = 2000;
                }
                console.log(transitionDuration);
                setTimeout(update,transitionDuration);
            }
        });
    });

    //真下の行は、Xsplit専用の式。Xsplitでhtmlを60fpsとするのに必要。
    //ブラウザで動作チェックする分には、コメントアウトして頂いて問題なし
    if (isXsplit) {
        window.external.SetLocalProperty("prop:Browser60fps","1");
    }

    //以下から普通に必要な式
    xhr.overrideMimeType('application/json');
    
	xhr.onreadystatechange = scLoaded;
	pollHandler();
	setInterval(function() {
		pollHandler();
	}, 500);
}

function pollHandler() {
    // パスに注意
	xhr.open('GET', "../StreamControl/streamcontrol.json?"+cacheBusterValiable+"="+cacheBuster,true);
	xhr.send();
	cacheBuster++;
}

//scLoaded関数...StreamControlで入力した内容を取得し、update関数で表示内容を変更する
function scLoaded() {
    
	if (xhr.readyState === 4) {
        
		scObj = JSON.parse(xhr.responseText);
        
		timestampOld = timestamp;
		timestamp = scObj["timestamp"];
		//console.log(timestamp);
        if (timestamp != timestampOld && !animating) {
            update();
        }
	}
}

function update() {
    for (let i = 1; i < 3; i++) {
        for (let j = 1; j < 10; j++) {
            let id_name = "cb_" + i.toString() + "_" + j.toString();
            changeVal(id_name);
            id_name = id_name + "_score";
            changeVal(id_name);
            detectCrewScore(i.toString(), j.toString());
        }
    }
    detectCrewMember("l");
    detectCrewMember("r");
    showMember();
}

function changeVal(id_name) {
    if (scObjOld[id_name] != scObj[id_name]) {
        animating = true;
        let id = document.getElementById(id_name);
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = scObjOld[id_name] = scObj[id_name].toString(); 
            // fitty("#" + id_name, {maxSize: 25});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}

function detectCrewScore(team, player) {
    let id_bg_ele;
    let id_name = "cb_" + team + "_" + player;
    let id_score = id_name + "_score";
    let id_name_ele = document.getElementById(id_name);
    let id_score_ele = document.getElementById(id_score);
    if (team == 1) {
        id_bg_ele = document.getElementById("l" + player + "_bg");
    } else {
        id_bg_ele = document.getElementById("r" + player + "_bg");
    }

    if (scObj[id_score] == "0") {
        animating = true;
        TweenMax.to(id_bg_ele,0.5,{background:"#000",ease:Quad.easeOut,delay:1})
        TweenMax.to(id_name_ele,0.5,{color:"#ddd",ease:Quad.easeOut,delay:1})
        TweenMax.to(id_score_ele,0.5,{color:"#ddd",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }})
    } else {
        animating = true;
        if (team == "1") {
            TweenMax.to(id_bg_ele,0.5,{background:"linear-gradient(-90deg, #fe0000 0%, #fe0000 60%, #000 100%)",ease:Quad.easeOut,delay:1})
        } else {
            TweenMax.to(id_bg_ele,0.5,{background:"linear-gradient(90deg, #0071bc 0%, #0071bc 60%, #000 100%)",ease:Quad.easeOut,delay:1})
        }
        TweenMax.to(id_name_ele,0.5,{color:"#fff",ease:Quad.easeOut,delay:1})
        TweenMax.to(id_score_ele,0.5,{color:"#fff",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }})
    }
}

function detectCrewMember(team) {
    let property = "select_" + team.toUpperCase() + "member";
    let id_name_new = team + "Check" + scObj[property];
    let id_name_old = team + "Check" + scObjOld[property];
    let id_new;
    let id_old;
    if (scObj[property] != "0") {
        id_new = document.getElementById(id_name_new);
    }
    if (scObjOld[property] != "0") {
        id_old = document.getElementById(id_name_old);
    }

    if (scObj[property] != scObjOld[property]) {
        if (scObj[property] != "0") {
            animating = true;
            if (scObjOld[property] != "0") {
                TweenMax.to(id_old,0.5,{opacity:"0",ease:Quad.easeOut})
            }
            TweenMax.to(id_new,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
                animating = false;
            }})
        } else {
            animating = true;
            TweenMax.to(id_old,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                animating = false;
            }})
        }
        scObjOld[property] = scObj[property].toString();
    }
}

function showMember() {
    if (scObj["cb_memberNum"] != scObjOld["cb_memberNum"]) {
        let id_r;
        let id_l;
        if (scObj["cb_memberNum"] > scObjOld["cb_memberNum"]) {
            for (let i = 1; i <= scObj["cb_memberNum"]; i++) {
                id_r = document.getElementById("r" + i.toString() + "_bg");
                id_l = document.getElementById("l" + i.toString() + "_bg");
                TweenMax.to(id_r,0.5,{opacity:"0.9",ease:Quad.easeOut})
                TweenMax.to(id_l,0.5,{opacity:"0.9",ease:Quad.easeOut})
            }
        } else {
            for (let i = Number(scObj["cb_memberNum"]) + 1; i <= Number(scObjOld["cb_memberNum"]); i++) {
                id_r = document.getElementById("r" + i.toString() + "_bg");
                id_l = document.getElementById("l" + i.toString() + "_bg");
                TweenMax.to(id_r,0.5,{opacity:"0",ease:Quad.easeOut})
                TweenMax.to(id_l,0.5,{opacity:"0",ease:Quad.easeOut})
            }
        }
        scObjOld["cb_memberNum"] = scObj["cb_memberNum"];
    }
}