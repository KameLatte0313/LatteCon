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
    tt_team1: '',
    tt_team2: '',
    tt_team3: '',
    tt_team4: '',
    tt_round1_left: '',
    tt_round1_right: '',
    tt_round2: ''
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
	xhr.open('GET', "../datafile/LatteCon_itsukushima.json?"+cacheBusterValiable+"="+cacheBuster,true);
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
    if (firstupdate) {
        document.getElementById("tt_team1").innerHTML = scObjOld['tt_team1'] = scObj["tt_team1"].toString();
        document.getElementById("tt_team2").innerHTML = scObjOld['tt_team2'] = scObj["tt_team2"].toString();
        document.getElementById("tt_team3").innerHTML = scObjOld['tt_team3'] = scObj["tt_team3"].toString();
        document.getElementById("tt_team4").innerHTML = scObjOld['tt_team4'] = scObj["tt_team4"].toString();

        detectCBwin("round1_left");
        detectCBwin("round1_right");
        detectCBwin("round2");

        firstupdate = false;

    } else if (!animating) {
        changeVal("tt_team1");
        changeVal("tt_team2");
        changeVal("tt_team3");
        changeVal("tt_team4");
        detectCBwin("round1_left");
        detectCBwin("round1_right");
        detectCBwin("round2");
    }
}

function changeVal(id_name) {
    if (scObjOld[id_name] != scObj[id_name]) {
        animating = true;
        let id = document.getElementById(id_name);
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = scObjOld[id_name] = scObj[id_name].toString(); 
            fitty("#" + id_name, {maxSize: 80});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}

function detectCBwin(round) {
    let property = "tt_" + round;
    if (firstupdate) {
        scObjOld[property] = scObj[property]
        setBracket(round);
    } else {
        if (scObjOld[property] != scObj[property]) {
            changeBracket(round);
            scObjOld[property] = scObj[property]
        }
    }
}

function setBracket(round) {
    let property = "tt_" + round;
    if (scObjOld[property] != "no") {
        let id_part1 = document.getElementById("bracket_" + round + "_" +scObjOld[property] + "_border")
        let id_part2 = document.getElementById("bracket_" + round + "_top_border")
        TweenMax.to(id_part1,0.5,{opacity:"1",ease:Quad.easeOut});
        TweenMax.to(id_part2,0.5,{opacity:"1",ease:Quad.easeOut});
    }
}

function changeBracket(round) {
    let property = "tt_" + round;
    if (scObjOld[property] != "no") {
        let old_id_part1 = document.getElementById("bracket_" + round + "_" +scObjOld[property] + "_border")
        let old_id_part2 = document.getElementById("bracket_" + round + "_top_border")
        TweenMax.to(old_id_part1,0.5,{opacity:"0",ease:Quad.easeOut});
        TweenMax.to(old_id_part2,0.5,{opacity:"0",ease:Quad.easeOut});
    }
    if (scObj[property] != "no") {
        let new_id_part1 = document.getElementById("bracket_" + round + "_" +scObj[property] + "_border")
        let new_id_part2 = document.getElementById("bracket_" + round + "_top_border")
        TweenMax.to(new_id_part1,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
        TweenMax.to(new_id_part2,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
    }
}