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

// ここにStreamControlから取得したデータをため込むための変数を定義する。

var scObjOld = {
    rr_pl_p1: '',
    rr_pl_p2: '',
    rr_pl_p3: '',
    rr_pl_p1_xid: '',
    rr_pl_p2_xid: '',
    rr_pl_p3_xid: ''
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
	xhr.open('GET', "../datafile/LatteCon.json?"+cacheBusterValiable+"="+cacheBuster,true);
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

// StreamControlの入力に応じてスコアボードを書き換える処理を行う関数
function update() {
    // スコアボードを始めて読み込んだ時の書き換え処理を記述する箇所
    if (firstupdate) {
        document.getElementById("rr_pl_p1").innerHTML = scObjOld['rr_pl_p1'] = scObj["rr_pl_p1"].toString();
        document.getElementById("rr_pl_p2").innerHTML = scObjOld['rr_pl_p2'] = scObj["rr_pl_p2"].toString();
        document.getElementById("rr_pl_p3").innerHTML = scObjOld['rr_pl_p3'] = scObj["rr_pl_p3"].toString();
        document.getElementById("rr_pl_p1_xid").innerHTML = scObjOld['rr_pl_p1_xid'] = scObj["rr_pl_p1_xid"].toString();
        document.getElementById("rr_pl_p2_xid").innerHTML = scObjOld['rr_pl_p2_xid'] = scObj["rr_pl_p2_xid"].toString();
        document.getElementById("rr_pl_p3_xid").innerHTML = scObjOld['rr_pl_p3_xid'] = scObj["rr_pl_p3_xid"].toString();

        firstupdate = false;

    // スコアボードを始めて読み込んだ時の書き換え処理を記述する箇所
    } else if (!animating) {
        changeVal("rr_pl_p1");
        changeVal("rr_pl_p2");
        changeVal("rr_pl_p3");
        changeVal("rr_pl_p1_xid");
        changeVal("rr_pl_p2_xid");
        changeVal("rr_pl_p3_xid");
    }
    
}

// OBS上の表示を変更する関数
function changeVal(id_name) {
    if (scObjOld[id_name] != scObj[id_name]) {
        animating = true;
        let id = document.getElementById(id_name);
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = scObjOld[id_name] = scObj[id_name].toString(); 
            // fitty("#" + id_name, {maxSize: 40});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}
