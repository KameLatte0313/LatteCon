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
    rr_p1: '',
    rr_p2: '',
    rr_p3: '',
    rr_p1_h: '',
    rr_p2_h: '',
    rr_p3_h: '',
    rr_1vs2_1 : '',
    rr_1vs2_2 : '',
    rr_1vs3_1 : '',
    rr_1vs3_3 : '',
    rr_2vs1_2 : '',
    rr_2vs1_1 : '',
    rr_2vs3_2 : '',
    rr_2vs3_3 : '',
    rr_3vs1_3 : '',
    rr_3vs1_1 : '',
    rr_3vs2_3 : '',
    rr_3vs2_2 : '',
    rr_p1_w : '',
    rr_p1_wset : '',
    rr_p1_lset : '',
    rr_p1_rank : '',
    rr_p2_w : '',
    rr_p2_wset : '',
    rr_p2_lset : '',
    rr_p2_rank : '', 
    rr_p3_w : '',
    rr_p3_wset : '',
    rr_p3_lset : '',
    rr_p3_rank : ''
}

var calcScore = {
    rr_p1_w : '',
    rr_p1_wset : '',
    rr_p1_lset : '',
    rr_p2_w : '',
    rr_p2_wset : '',
    rr_p2_lset : '',
    rr_p3_w : '',
    rr_p3_wset : '',
    rr_p3_lset : ''
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
	xhr.open('GET', "streamcontrol.json?"+cacheBusterValiable+"="+cacheBuster,true);
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
        document.getElementById("rr_p1").innerHTML = scObjOld['rr_p1'] = scObj["rr_p1"].toString(); 
        document.getElementById("rr_p2").innerHTML = scObjOld['rr_p2'] = scObj["rr_p2"].toString(); 
        document.getElementById("rr_p3").innerHTML = scObjOld['rr_p3'] = scObj["rr_p3"].toString();
        document.getElementById("rr_p1_h").innerHTML = scObjOld['rr_p1_h'] = scObj["rr_p1_h"].toString(); 
        document.getElementById("rr_p2_h").innerHTML = scObjOld['rr_p2_h'] = scObj["rr_p2_h"].toString(); 
        document.getElementById("rr_p3_h").innerHTML = scObjOld['rr_p3_h'] = scObj["rr_p3_h"].toString();

        setRRscore("1", "2");
        setRRscore("1", "3");
        setRRscore("2", "1");
        setRRscore("2", "3");
        setRRscore("3", "1");
        setRRscore("3", "2");

        calcMatchScore("1", "2", "3");
        calcMatchScore("2", "1", "3");
        calcMatchScore("3", "1", "2");

        setMatchScore("1");
        setMatchScore("2");
        setMatchScore("3");

        setRank();

        firstupdate = false;

    // スコアボードを始めて読み込んだ時の書き換え処理を記述する箇所
    } else if (!animating) {
        // 左端プレイヤー名
        changeRRname("1");
        changeRRname("2");
        changeRRname("3");

        // ヘッダー部プレイヤー名
        changeRRname("1_h");
        changeRRname("2_h");
        changeRRname("3_h");

        // 対戦スコア
        changeRRscore("1", "2");
        changeRRscore("1", "3");
        changeRRscore("2", "1");
        changeRRscore("2", "3");
        changeRRscore("3", "1");
        changeRRscore("3", "2");

        // 総当たり結果
        calcMatchScore("1", "2", "3");
        calcMatchScore("2", "1", "3");
        calcMatchScore("3", "1", "2");
        changeMatchScore("1");
        changeMatchScore("2");
        changeMatchScore("3");

        changeRank();
    }
    
}

function setRRscore(lPlayer, rPlayer) {
    let id_name = "rr_" + lPlayer + "vs" + rPlayer;
    let lProperty = id_name + "_" + lPlayer;
    let rProperty = id_name + "_" + rPlayer;
    let id = document.getElementById(id_name);
    scObjOld[lProperty] = scObj[lProperty];
    scObjOld[rProperty] = scObj[rProperty];
    id.innerHTML = scObjOld[lProperty] + " - " + scObjOld[rProperty];
}

function changeRRname(player) {
    let id_name = "rr_p" + player;
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

function changeRRscore(lPlayer, rPlayer) {
    let id_name = "rr_" + lPlayer + "vs" + rPlayer;
    let lProperty = id_name + "_" + lPlayer;
    let rProperty = id_name + "_" + rPlayer;

    if (scObjOld[lProperty] != scObj[lProperty] || scObjOld[rProperty] != scObj[rProperty]) {
        animating = true;
        let id = document.getElementById(id_name);
        scObjOld[lProperty] = scObj[lProperty];
        scObjOld[rProperty] = scObj[rProperty];
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = scObjOld[lProperty] + " - " + scObjOld[rProperty];
            // fitty("#" + id_name, {maxSize: 25});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}

function calcMatchScore(player, opponent1, opponent2) {
    let id_base = "rr_p" + player + "_";
    let match1 = "rr_" + player + "vs" + opponent1;
    let match2 = "rr_" + player + "vs" + opponent2;
    let w = 0;
    let wset = 0;
    let lset = 0;

    if (scObj[match1 + "_" + player] > scObj[match1 + "_" + opponent1]) {
        w++;
    }
    if (scObj[match2 + "_" + player] > scObj[match2 + "_" + opponent2]) {
        w++;
    }
    wset = Number(scObj[match1 + "_" + player]) + Number(scObj[match2 + "_" + player]);
    lset = Number(scObj[match1 + "_" + opponent1]) + Number(scObj[match2 + "_" + opponent2]);

    calcScore[id_base + "w"] = w.toString();
    calcScore[id_base + "wset"] = wset.toString();
    calcScore[id_base + "lset"] = lset.toString();
}

function setMatchScore(player) {
    let id_base = "rr_p" + player + "_";
    let id_tag = ["w", "wset", "lset"];
    for (let i = 0; i < 3; i++) {
        document.getElementById(id_base + id_tag[i]).innerHTML = scObjOld[id_base + id_tag[i]] = calcScore[id_base + id_tag[i]].toString(); 
    }
}

function changeMatchScore(player) {
    let id_base = "rr_p" + player + "_";
    let id_tag = ["w", "wset", "lset"];

    for (let i = 0; i < 3; i++) {
        let id_name = id_base + id_tag[i];
        if (scObjOld[id_name] != calcScore[id_name]) {
            animating = true;
            let id = document.getElementById(id_name);
            TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
                id.innerHTML = scObjOld[id_name] = calcScore[id_name].toString(); 
                // fitty("#" + id_name, {maxSize: 25});
            }});
            TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
                animating = false;
            }});
        }
    }
}

function setRank() {
    for (let i = 1; i < 4; i++) {
        let pRank = "rr_p" + i.toString() + "_rank";
        document.getElementById(pRank).innerHTML = scObjOld[pRank] = scObj[pRank];
    }
}

function changeRank() {
    for (let i = 1; i < 4; i++) {
        let id_name = "rr_p" + i.toString() + "_rank";
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
}