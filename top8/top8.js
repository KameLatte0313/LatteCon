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
    top8_1_1: '',
    top8_1_2: '',
    top8_1_3: '',
    top8_1_4: '',
    top8_1_5: '',
    top8_1_6: '',
    top8_1_7: '',
    top8_1_8: '',
    top8_2_1: '',
    top8_2_2: '',
    top8_2_3: '',
    top8_2_4: '',
    top8_2_5: '',
    top8_2_6: '',
    top8_3_1: '',
    top8_3_2: '',
    top8_3_3: '',
    top8_3_4: '',
    top8_4_1: '',
    top8_4_2: '',
    top8_4_3: '',
    top8_4_4: '',
    top8_1_1_score: '',
    top8_1_2_score: '',
    top8_1_3_score: '',
    top8_1_4_score: '',
    top8_1_5_score: '',
    top8_1_6_score: '',
    top8_1_7_score: '',
    top8_1_8_score: '',
    top8_2_1_score: '',
    top8_2_2_score: '',
    top8_2_3_score: '',
    top8_2_4_score: '',
    top8_2_5_score: '',
    top8_2_6_score: '',
    top8_3_1_score: '',
    top8_3_2_score: '',
    top8_3_3_score: '',
    top8_3_4_score: '',
    top8_4_1_score: '',
    top8_4_2_score: '',
    top8_4_3_score: '',
    top8_4_4_score: ''
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
    for (let i = 1; i < 5; i++) {
        for (let j = 1; j < 9; j++) {
            if ((i == 2 && j > 7) || (i == 3 && j > 5)) {
                break;
            } else if (i == 4) {
                if (j == 1 || j == 2) {
                    continue;
                } else if (j > 5) {
                    break;
                }
            }

            let id_name = "top8_" + i.toString() + "_" + j.toString();
            changeVal(id_name);
            id_name = id_name + "_score";
            changeVal(id_name);
        }
    }
}

function changeVal(id_name) {
    if (scObjOld[id_name] != scObj[id_name]) {
        animating = true;
        let id = document.getElementById(id_name);
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = scObjOld[id_name] = scObj[id_name].toString(); 
            fitty("#" + id_name, {maxSize: 25});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}