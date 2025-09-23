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
    st_p1_0_tournament_name: '',
    st_p1_0_entrants: '',
    st_p1_0_placement: '',
    st_p1_1_tournament_name: '',
    st_p1_1_entrants: '',
    st_p1_1_placement: '',
    st_p1_2_tournament_name: '',
    st_p1_2_entrants: '',
    st_p1_2_placement: '',
    st_p1_3_tournament_name: '',
    st_p1_3_entrants: '',
    st_p1_3_placement: '',
    st_p1_4_tournament_name: '',
    st_p1_4_entrants: '',
    st_p1_4_placement: '',
    st_p2_0_tournament_name: '',
    st_p2_0_entrants: '',
    st_p2_0_placement: '',
    st_p2_1_tournament_name: '',
    st_p2_1_entrants: '',
    st_p2_1_placement: '',
    st_p2_2_tournament_name: '',
    st_p2_2_entrants: '',
    st_p2_2_placement: '',
    st_p2_3_tournament_name: '',
    st_p2_3_entrants: '',
    st_p2_3_placement: '',
    st_p2_4_tournament_name: '',
    st_p2_4_entrants: '',
    st_p2_4_placement: ''
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
    // スコアボードを初めて読み込んだ時の処理を記述
    if (firstupdate) {
        for (i = 0; i < 5; i++) {
            document.getElementById("st_p1_" + i + "_tournament_name").innerHTML = scObjOld["st_p1_" + i + "_tournament_name"] = scObj["st_p1_" + i + "_tournament_name"].toString();
            document.getElementById("st_p2_" + i + "_tournament_name").innerHTML = scObjOld["st_p2_" + i + "_tournament_name"] = scObj["st_p2_" + i + "_tournament_name"].toString();
            scObjOld["st_p1_" + i + "_entrants"] = scObj["st_p1_" + i + "_entrants"].toString();
            scObjOld["st_p1_" + i + "_placement"] = scObj["st_p1_" + i + "_placement"].toString();
            scObjOld["st_p2_" + i + "_entrants"] = scObj["st_p2_" + i + "_entrants"].toString();
            scObjOld["st_p2_" + i + "_placement"] = scObj["st_p2_" + i + "_placement"].toString();

            document.getElementById("st_p1_" + i + "_stats").innerHTML = createStatsData("p1", i)
            document.getElementById("st_p2_" + i + "_stats").innerHTML = createStatsData("p2", i)
        }

        firstupdate = false;

    // 更新処理
    } else if (!animating) {
        for (j = 0; j < 5; j++) {
            changeVal("st_p1_" + j + "_tournament_name")
            changeVal("st_p2_" + j + "_tournament_name")
            changeStatsVal("p1", j);
            changeStatsVal("p2", j);
        }
    }
}

// OBS上の表示を変更する関数
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

// OBS上のStatsを変更する関数
function changeStatsVal(player, index) {
    id_header = "st_" + player + "_" + index
    if (scObjOld[id_header + "_entrants"] != scObj[id_header + "_entrants"]
        || scObjOld[id_header + "_placement"] != scObj[id_header + "_placement"]) {
        
        animating = true;
        let id = document.getElementById(id_header + "_stats");
        scObjOld[id_header + "_entrants"] = scObj[id_header + "_entrants"].toString();
        scObjOld[id_header + "_placement"] = scObj[id_header + "_placement"].toString();
        TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() { 
            id.innerHTML = createStatsData(player, index)
            // fitty("#" + id_name, {maxSize: 40});
        }});
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete: function() {
            animating = false;
        }});
    }
}

// stats用のデータを組み上げる関数
function createStatsData(player, index) {
    id_header = "st_" + player + "_" + index
    entrant = scObjOld[id_header + "_entrants"];
    placement = scObjOld[id_header + "_placement"];

    // 順位と人数のいずれかが空白の場合は空文字を返す
    if (entrant == "" || placement == "") {
        return "";
    }

    return addSuffix(placement) + "/" + entrant;
}

// 順位の接尾語を付加する関数
function addSuffix(placement) {
    if (placement == "1") {
        return "1st";
    } else if (placement == "2") {
        return "2nd";
    } else if (placement == "3") {
        return "3rd";
    } else {
        return placement + "th";
    }
}
