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
    cb_upperleft: '',
    cb_upperright: '',
    cb_team1: '',
    cb_team1_score: 0,
    cb_team2: '',
    cb_team2_score: 0,
    cb_memberNum: '',
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
    cb_autocalc: ''
}

var team1score = 0;
var team2score = 0;

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

// StreamControlの入力に応じてスコアボードを書き換える処理を行う関数
function update() {
    // スコアボードを始めて読み込んだ時の書き換え処理を記述する箇所
    if (firstupdate) {
        document.getElementById("cb_upperleft").innerHTML = scObjOld['cb_upperleft'] = scObj["cb_upperleft"].toString();
        document.getElementById("cb_upperright").innerHTML = scObjOld['cb_upperright'] = scObj["cb_upperright"].toString();
        document.getElementById("cb_team1").innerHTML = scObjOld['cb_team1'] = scObj["cb_team1"].toString();
        document.getElementById("cb_team2").innerHTML = scObjOld['cb_team2'] = scObj["cb_team2"].toString();

        scObjOld['cb_memberNum'] = scObj["cb_memberNum"];
        // scObjOld['cb_team1_score'] = scObj["cb_team1_score"];
        // scObjOld['cb_team2_score'] = scObj["cb_team2_score"];

        scObjOld['cb_autocalc'] = scObj["cb_autocalc"];

        for (let i = 1; i < 10; i++) {
            let cb_memberScore = "cb_1_" + i.toString() + "_score";
            scObjOld[cb_memberScore] = scObj[cb_memberScore];
            cb_memberScore = "cb_2_" + i.toString() + "_score";
            scObjOld[cb_memberScore] = scObj[cb_memberScore];
        }

        if (scObjOld['cb_autocalc'] == "0") {
            team1score = scObj['cb_team1_score'];
            team2score = scObj['cb_team2_score'];
        } else {
            for (let i = 1; i <= Number(scObjOld['cb_memberNum']); i++) {
                let cb_memberScore = "cb_1_" + i.toString() + "_score";
                team1score = team1score + Number(scObjOld[cb_memberScore]);

                cb_memberScore = "cb_2_" + i.toString() + "_score";
                team2score = team2score + Number(scObjOld[cb_memberScore]);
            }
        }

        document.getElementById("cb_team1_score").innerHTML = scObjOld['cb_team1_score'] = team1score;
        document.getElementById("cb_team2_score").innerHTML = scObjOld['cb_team2_score'] = team2score;

        // document.getElementById("cb_team1_score").innerHTML = scObjOld['cb_team1_score'] = scObj["cb_team1_score"].toString();
        // document.getElementById("cb_team2_score").innerHTML = scObjOld['cb_team2_score'] = scObj["cb_team2_score"].toString();

        firstupdate = false;

    } else if (!animating) {
        changeVal("cb_upperleft");
        changeVal("cb_upperright");
        changeVal("cb_team1");
        changeVal("cb_team2");

        // if (scObjOld['cb_autocalc'] != scObj['cb_autocalc']) {
        //     scObjOld['cb_autocalc'] = scObj["cb_autocalc"];

        //     if (scObjOld['cb_autocalc'] == "0") {
                
        //     } else {

        //     }
        // }

        if (scObj['cb_autocalc'] == "0") {
            team1score = scObj['cb_team1_score'];
            team2score = scObj['cb_team2_score'];
        } else {
            for (let i = 1; i < 10; i++) {
                let cb_memberScore = "cb_1_" + i.toString() + "_score";
                scObjOld[cb_memberScore] = scObj[cb_memberScore];
                cb_memberScore = "cb_2_" + i.toString() + "_score";
                scObjOld[cb_memberScore] = scObj[cb_memberScore];
            }
            team1score = 0;
            team2score = 0;
            for (let i = 1; i <= Number(scObj['cb_memberNum']); i++) {
                let cb_memberScore = "cb_1_" + i.toString() + "_score";
                team1score = team1score + Number(scObjOld[cb_memberScore]);

                cb_memberScore = "cb_2_" + i.toString() + "_score";
                team2score = team2score + Number(scObjOld[cb_memberScore]);
            }
        }
        
        // changeVal("cb_team1_score");
        // changeVal("cb_team2_score");
        changeValtoAddData("cb_team1_score", team1score);
        changeValtoAddData("cb_team2_score", team2score);

        fitty("#cb_team1", {maxSize: 35});
        fitty("#cb_team2", {maxSize: 35});
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

function changeValtoAddData(id_name, data) {
    if (scObjOld[id_name] != data) {
        animating = true;
        let id = document.getElementById(id_name);
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = scObjOld[id_name] = data.toString(); 
            // fitty("#" + id_name, {maxSize: 40});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}