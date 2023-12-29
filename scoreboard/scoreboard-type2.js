var xjs = require('xjs');
var App = new xjs.App();

window.onload = init;

var isXsplit = false;

var xhr = new XMLHttpRequest();

var timestampOld=0;
var timestamp=0;
var cacheBusterValiable=Date.now();
var cacheBuster=0;

var firstupdate = true;

var scObj;

var scObjOld = {
    pName1: '',
    pName2: '',
    score1: '',
    score2: '',
    bestofN: '',
    boN: '',
    stage: '',
    stage_typing: '',
    gf_wl1: '',
    gf_wl2: '',
    game1: '',
    game2: '',
    game3: '',
    game4: '',
    game5: ''
}

var animating = false;

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
        if (timestamp != timestampOld && !animating) {
            update();
        }
	}
}

function update() {

	if (firstupdate) {
		animating = true;

        // プレイヤー名
        setValtoAddData("player1", scObj["pTeam1"].toString() + " " + scObj["pName1"].toString());
        setValtoAddData("player2", scObj["pTeam2"].toString() + " " + scObj["pName2"].toString());

        fitty("#player1", {maxSize: 35});
        fitty("#player2", {maxSize: 35});

        TweenMax.from(document.getElementById("player1"),0.5,{opacity:0,delay:1.5});
        TweenMax.from(document.getElementById("player2"),0.5,{opacity:0,delay:1.5});

        // スコア
        scObjOld["score1"] = 0;
        scObjOld["score2"] = 0;
        set_timing = [scObj["game1"], scObj["game2"], scObj["game3"], scObj["game4"], scObj["game5"]];
        for (var game of set_timing) {
            if (game == "p1") {
                scObjOld["score1"]++;
            } else if (game == "p2") {
                scObjOld["score2"]++;
            }
        }
        
        document.getElementById("score1").innerHTML = scObjOld["score1"];
        document.getElementById("score2").innerHTML = scObjOld["score2"];

        TweenMax.from(document.getElementById("score1"),0.5,{opacity:0,delay:1.5});
        TweenMax.from(document.getElementById("score2"),0.5,{opacity:0,delay:1.5});

        // stage
        scObjOld["stage"] = scObj['stage'];
        if (scObjOld["stage"] == "stage_typing") {
            scObjOld["stage"] = scObj['stage_typing'];
        }
        document.getElementById('stage').innerHTML = scObjOld["stage"];
        TweenMax.from(document.getElementById('stage'),0.5,{opacity:0,delay:1.5});

        // BEST OF N
        setVal("bestofN");
        TweenMax.from(document.getElementById('bestofN'),0.5,{opacity:0,delay:1.5});

        // セットストーリー
        scObjOld["boN"] = scObj["boN"];

        setSetstory();

        // GF用WinLose表示
        scObjOld['gf_wl1'] = scObj["GF-WL1"];
        scObjOld['gf_wl2'] = scObj["GF-WL2"];
        
        if (scObjOld['gf_wl1'] == "no") {
            document.getElementById("gf-wl1").innerHTML = " "
        } else if (scObjOld['gf_wl1'] == "W") {
            document.getElementById("gf-wl1").innerHTML = "[W]"
        } else if (scObjOld['gf_wl1'] == "L") {
            document.getElementById("gf-wl1").innerHTML = "[L]"
        }

        if (scObjOld['gf_wl2'] == "no") {
            document.getElementById("gf-wl2").innerHTML = " "
        } else if (scObjOld['gf_wl2'] == "W") {
            document.getElementById("gf-wl2").innerHTML = "[W]"
        } else if (scObjOld['gf_wl2'] == "L") {
            document.getElementById("gf-wl2").innerHTML = "[L]"
        }

        TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});
        TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});

        firstupdate = false;
        animating = false;

    } else if (!animating) {

        // プレイヤー名
        changeValtoAddData("player1", scObj["pTeam1"].toString() + " " + scObj["pName1"].toString());
        changeValtoAddData("player2", scObj["pTeam2"].toString() + " " + scObj["pName2"].toString());
        fitty("#player1", {maxSize: 35});
        fitty("#player2", {maxSize: 35});

        // スコア
        nowScore1 = 0;
        nowScore2 = 0;
        set_timing = [scObj["game1"], scObj["game2"], scObj["game3"], scObj["game4"], scObj["game5"]];
        for (var game of set_timing) {
            if (game == "p1") {
                nowScore1++;
            } else if (game == "p2") {
                nowScore2++;
            }
        }

        changeValtoAddData("score1", nowScore1);
        changeValtoAddData("score2", nowScore2);

        // stage
        if (scObj['stage'] == "stage_typing") {
            changeValtoAddData("stage", scObj["stage_typing"].toString());
        } else if (scObj['stage'] != "stage_typing") {
            changeVal("stage");
        }

        // BEST OF N
        changeVal("bestofN");

        // セットストーリー
        if (scObjOld["boN"] != scObj["boN"]) {
            animating = true;
            scObjOld["boN"] = scObj["boN"]
            if (scObjOld["boN"] == "bo3") {
                TweenMax.to(document.getElementById("bo5-scorebar"),0.5,{opacity:"0",ease:Quad.easeOut});
                TweenMax.to(document.getElementById("bo3-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            } else if (scObjOld["boN"] == "bo5") {
                TweenMax.to(document.getElementById("bo3-scorebar"),0.5,{opacity:"0",ease:Quad.easeOut});
                TweenMax.to(document.getElementById("bo5-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            }
            animating = false;
        }

        changeSetstory();

        // GF用WinLose表示
        changeGFWL("gf-wl1", "GF-WL1");
        changeGFWL("gf-wl2", "GF-WL2");
	}
}

// 以下メソッド
function setVal(id_name) {
    document.getElementById(id_name).innerHTML = scObjOld[id_name] = scObj[id_name].toString();
}

function setValtoAddData(id_name, data) {
    document.getElementById(id_name).innerHTML = scObjOld[id_name] = data.toString();
}

function setSetstory() {
    for (let i = 1; i < 4; i++) {
        let id_name = "bo3-game" + i.toString() + "-" + scObj["game" + i.toString()];
        let property = "game" + i.toString();
        let id = document.getElementById(id_name);
        scObjOld[property] = scObj["game" + i.toString()];
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});
    }
    for (let i = 1; i < 6; i++) {
        let id_name = "bo5-game" + i.toString() + "-" + scObj["game" + i.toString()];
        let property = "game" + i.toString();
        let id = document.getElementById(id_name);
        scObjOld[property] = scObj["game" + i.toString()];
        TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});
    }
    TweenMax.to(document.getElementById(scObj["boN"] + "-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});
}

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

function changeSetstory() {
    for (let i = 1; i < 4; i++) {
        let property = "game" + i.toString();
        if (scObjOld[property] != scObj["game" + i.toString()]) {
            let id_name = "bo3-game" + i.toString() + "-" + scObj["game" + i.toString()];
            let old_id_name = "bo3-game" + i.toString() + "-" + scObjOld[property];
            let id = document.getElementById(id_name);
            let old_id = document.getElementById(old_id_name);
            
            TweenMax.to(old_id,0.5,{opacity:"0",ease:Quad.easeOut});
            TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
        }
    }
    for (let i = 1; i < 6; i++) {
        let property = "game" + i.toString();
        if (scObjOld[property] != scObj["game" + i.toString()]) {
            let id_name = "bo5-game" + i.toString() + "-" + scObj["game" + i.toString()];
            let old_id_name = "bo5-game" + i.toString() + "-" + scObjOld[property];
            let id = document.getElementById(id_name);
            let old_id = document.getElementById(old_id_name);
            
            TweenMax.to(old_id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                scObjOld[property] = scObj["game" + i.toString()];
            }});
            TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
        }
    }
}

function changeGFWL(id_name, property) {
    if (scObjOld[id_name] != scObj[property]) {
        animating = true;
        scObjOld[id_name] = scObj[property]
        let id = document.getElementById(id_name);
        if (scObjOld[id_name] == "no") {
            TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                id.innerHTML = " ";
            }});
            TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
        } else if (scObjOld[id_name] == "W") {
            TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                id.innerHTML = "[W]";
            }});
            TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
        } else if (scObjOld[id_name] == "L") {
            TweenMax.to(id,0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                id.innerHTML = "[L]";
            }});
            TweenMax.to(id,0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
        }
        animating = false;
    }
}