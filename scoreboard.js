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

var currPlayer1;
var currPlayer2;

var currScore1;
var currScore2;

var boN;
var game1;
var game2;
var game3;
var game4;
var game5;

var animating = 0;

var switchCount = 0;
var currPlayerElement = "pName";

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


    //TweenMax の引数について： http://qiita.com/ANTON072/items/a1302f4761bf0ffcf525
    /*TweenMax.to('#board1', 0.3, {
        top:"0px",
        repeat:0,
        ease: Power2.Linear, //Linearは一定の速度で変化する。
        delay: 0,
        yoyo:false
    });
    TweenMax.to('#board2', 0.6, {
        top:"0px",
        repeat:0,
        ease: Power3.Linear,
        delay: 0.1,
        yoyo:false
    });
    TweenMax.to('#board3', 0.8, {
        left:"0px",
        repeat:0,
        ease: Power2.easeOut, //easeoutは終わり際の動きをゆっくりにする
        delay: 0.7,
        yoyo:false
    });
    TweenMax.to('#board4', 0.8, {
        left:"0px",
        repeat:0,
        ease: Power2.easeOut,
        delay: 0.7,
        yoyo:false
    });*/

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

function switchTagTwitter(){
    switch (currPlayerElement) {
        case 'pName':
            if (scObj["pTwitter1"] || scObj["pTwitter2"]) { 
                currPlayerElement = 'pTwitter';
            }
            break;
        case 'pTwitter':
            currPlayerElement = 'pName';
            break;
    }
    if (scObj["pTwitter1"] && currPlayerElement == 'pTwitter' || document.getElementById("player1").innerHTML != currPlayer1) {
        TweenMax.to(document.getElementById("player1"),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
            document.getElementById("player1").innerHTML = scObj[currPlayerElement + "1"].toString();
            textFit(document.getElementsByClassName('player1'), {minFontSize:14, maxFontSize: 20,multiLine: false});
        }});
        TweenMax.to(document.getElementById("player1"),0.5,{opacity:1,ease:Quad.easeOut,delay:0.5});
    }
    
    if (scObj["pTwitter2"] && currPlayerElement == 'pTwitter' || document.getElementById("player2").innerHTML != currPlayer2) {
        TweenMax.to(document.getElementById("player2"),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
            document.getElementById("player2").innerHTML = scObj[currPlayerElement + "2"].toString();
            textFit(document.getElementsByClassName('player2'), {minFontSize:14, maxFontSize: 20,multiLine: false});
        }});
        TweenMax.to(document.getElementById("player2"),0.5,{opacity:1,ease:Quad.easeOut,delay:0.5});
    }
    switchCount = 0;
}

//scLoaded関数...StreamControlで入力した内容を取得し、update関数で表示内容を変更する
function scLoaded() {
    
	if (xhr.readyState === 4) {
        
		scObj = JSON.parse(xhr.responseText);
        
		timestampOld = timestamp;
		timestamp = scObj["timestamp"];
		//console.log(timestamp);
        if (timestamp != timestampOld && animating == 0 || firstupdate) {
            update();
        } else if(animating == 0 && switchCount > 10) {
            // switchTagTwitter();
        } else {
            // switchCount++;
        }
	}
}

function update() {
    
	var datetime = new Date();
	var unixTime = Math.round(datetime.getTime()/1000);

	if (firstupdate) {
		animating++;

		// document.getElementById("scoreboardintro").play();
        // document.getElementById("scoreboardintro").onended = function() {};
        
        currPlayer1 = scObj["pTeam1"].toString() + " " + scObj["pName1"].toString();
        currPlayer2 = scObj["pTeam2"].toString() + " " + scObj["pName2"].toString();
        document.getElementById("player1").innerHTML = currPlayer1;
        document.getElementById("player2").innerHTML = currPlayer2;

        currScore1 = scObj["pScore1"];
        currScore2 = scObj["pScore2"];
        document.getElementById("score1").innerHTML = currScore1;
        document.getElementById("score2").innerHTML = currScore2;

        stage = scObj['stage'];
        if (stage == "stage_typing") {
            stage = scObj['stage_typing'];
        }
        document.getElementById('stage').innerHTML = stage;
        document.getElementById('bestofN').innerHTML = scObj['bestofN']


        TweenMax.from(document.getElementById("player1"),0.5,{x:"+50",opacity:0,delay:1.5});
        TweenMax.from(document.getElementById("player2"),0.5,{x:"-50",opacity:0,delay:1.5});

        TweenMax.from(document.getElementById("score1"),0.5,{opacity:0,delay:1.5});
        TweenMax.from(document.getElementById("score2"),0.5,{opacity:0,delay:1.5});

        // loadFlags();

        // TweenMax.from(document.getElementById("flag1"),0.5,{opacity:0,delay:1.5});
        // TweenMax.from(document.getElementById("flag2"),0.5,{opacity:0,delay:1.5});

        TweenMax.from(document.getElementById('stage'),0.5,{opacity:0,delay:1.5});
        TweenMax.from(document.getElementById('bestofN'),0.5,{opacity:0,delay:1.5,onComplete:function(){animating--;}});

        document.getElementById("container").style.display="block";
        // textFit(document.getElementsByClassName('stage'), {minFontSize:10, maxFontSize: 14,multiLine: false});

        // textFit(document.getElementsByClassName('player1'), {minFontSize:14, maxFontSize: 20,multiLine: false});
        // textFit(document.getElementsByClassName('player2'), {minFontSize:14, maxFontSize: 20,multiLine: false});

        boN = scObj["boN"];

        if (boN == "bo3") {
            game1 = scObj["game1"];
            game2 = scObj["game2"];
            game3 = scObj["game3"];

            setGameScore(game1, "bo3-game1");
            setGameScore(game2, "bo3-game2");
            setGameScore(game3, "bo3-game3");

            TweenMax.to(document.getElementById("bo3-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});

        } else if (boN == "bo5") {
            game1 = scObj["game1"];
            game2 = scObj["game2"];
            game3 = scObj["game3"];
            game4 = scObj["game4"];
            game5 = scObj["game5"];

            setGameScore(game1, "bo5-game1");
            setGameScore(game2, "bo5-game2");
            setGameScore(game3, "bo5-game3");
            setGameScore(game4, "bo5-game4");
            setGameScore(game5, "bo5-game5");

            TweenMax.to(document.getElementById("bo5-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});
        }

        gfwl1 = scObj["GF-WL1"];
        gfwl2 = scObj["GF-WL2"];
        
        if (gfwl1 == "no") {
            document.getElementById("gf-wl1").innerHTML = " "
        } else if (gfwl1 == "W") {
            document.getElementById("gf-wl1").innerHTML = "[W]"
        } else if (gfwl1 == "L") {
            document.getElementById("gf-wl1").innerHTML = "[L]"
        }

        if (gfwl2 == "no") {
            document.getElementById("gf-wl2").innerHTML = " "
        } else if (gfwl2 == "W") {
            document.getElementById("gf-wl2").innerHTML = "[W]"
        } else if (gfwl2 == "L") {
            document.getElementById("gf-wl2").innerHTML = "[L]"
        }

        TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});
        TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1.5});

        firstupdate = false;

    } else if (animating == 0) {

		if (currPlayer1 != scObj["pTeam1"].toString() + " " + scObj["pName1"].toString() 
            || currPlayer2 != scObj["pTeam2"].toString() + " " + scObj["pName2"].toString()) {
            animating++;
            
            // 左プレイヤー
            TweenMax.to(document.getElementById("player1"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                currPlayer1 = scObj["pTeam1"].toString() + " " + scObj["pName1"].toString(); 
                document.getElementById("player1").innerHTML = currPlayer1; 
                textFit(document.getElementsByClassName('player1'), {minFontSize:14, maxFontSize: 20,multiLine: false}); 
            }});
            TweenMax.to(document.getElementById("player1"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});

            // 右プレイヤー
            TweenMax.to(document.getElementById("player2"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                currPlayer2 = scObj["pTeam2"].toString() + " " + scObj["pName2"].toString();
                document.getElementById("player2").innerHTML = currPlayer2; 
                textFit(document.getElementsByClassName('player2'), {minFontSize:14, maxFontSize: 20,multiLine: false}); 
            }});
            TweenMax.to(document.getElementById("player2"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1,onComplete:function(){
                animating--;
            }});
            

            // switchCount = 0;
            currPlayerElement = "pName";
    	}

        if (currScore1 != scObj["pScore1"].toString()) {
            animating++;
            currScore1 = scObj['pScore1'].toString();
            TweenMax.to(document.getElementById('score1'),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
                document.getElementById("score1").innerHTML = currScore1;
            }});
            TweenMax.to(document.getElementById('score1'),0.5,{opacity:1,ease:Quad.easeOut,delay:1,onComplete: function(){
                animating--;
            }});
        }
        if (currScore2 != scObj["pScore2"].toString()) {
            animating++;
            currScore2 = scObj['pScore2'].toString();
            TweenMax.to(document.getElementById('score2'),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
                document.getElementById("score2").innerHTML = currScore2;
            }});
            TweenMax.to(document.getElementById('score2'),0.5,{opacity:1,ease:Quad.easeOut,delay:1,onComplete: function(){
                animating--;
            }});
        }

        if (scObj['stage'] == "stage_typing" && stage != scObj['stage_typing']) {
            animating++;
            TweenMax.to(document.getElementById('stage'),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
                stage = scObj['stage_typing'];
                document.getElementById('stage').innerHTML = stage;
                // textFit(document.getElementsByClassName('stage'), {minFontSize:10, maxFontSize: 14,multiLine: false});
            }});
            TweenMax.to(document.getElementById('stage'),0.5,{opacity:1,delay:1,ease:Quad.easeOut,onComplete: function(){
                animating--;
            }});
        } else if (scObj['stage'] != "stage_typing" && stage != scObj['stage']) {
            animating++;
            TweenMax.to(document.getElementById('stage'),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
                stage = scObj['stage'];
                document.getElementById('stage').innerHTML = stage;
                // textFit(document.getElementsByClassName('stage'), {minFontSize:10, maxFontSize: 14,multiLine: false});
            }});
            TweenMax.to(document.getElementById('stage'),0.5,{opacity:1,delay:1,ease:Quad.easeOut,onComplete: function(){
                animating--;
            }});
        }

        if (document.getElementById('bestofN').innerHTML != scObj['bestofN']) {
            animating++;
            TweenMax.to(document.getElementById('bestofN'),0.5,{opacity:0,ease:Quad.easeIn,onComplete: function() {
                document.getElementById('bestofN').innerHTML = scObj['bestofN'];
                textFit(document.getElementsByClassName('stage'), {minFontSize:10, maxFontSize: 14,multiLine: false});
            }});
            TweenMax.to(document.getElementById('bestofN'),0.5,{opacity:1,delay:1,ease:Quad.easeOut,onComplete: function(){
                animating--;
            }});
        }

        if (boN != scObj["boN"]) {
            animating++;
            boN = scObj["boN"]
            if (boN == "bo3") {
                TweenMax.to(document.getElementById("bo5-scorebar"),0.5,{opacity:"0",ease:Quad.easeOut});
                TweenMax.to(document.getElementById("bo3-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            } else if (boN == "bo5") {
                TweenMax.to(document.getElementById("bo3-scorebar"),0.5,{opacity:"0",ease:Quad.easeOut});
                TweenMax.to(document.getElementById("bo5-scorebar"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            }
            animating--;
        }

        if (boN == "bo3") {
            game1 = scObj["game1"];
            game2 = scObj["game2"];
            game3 = scObj["game3"];

            setGameScore(game1, "bo3-game1");
            setGameScore(game2, "bo3-game2");
            setGameScore(game3, "bo3-game3");
        } else if (boN == "bo5") {
            game1 = scObj["game1"];
            game2 = scObj["game2"];
            game3 = scObj["game3"];
            game4 = scObj["game4"];
            game5 = scObj["game5"];

            setGameScore(game1, "bo5-game1");
            setGameScore(game2, "bo5-game2");
            setGameScore(game3, "bo5-game3");
            setGameScore(game4, "bo5-game4");
            setGameScore(game5, "bo5-game5");
        }

        if (gfwl1 != scObj["GF-WL1"]) {
            animating++;
            gfwl1 = scObj["GF-WL1"]
            if (gfwl1 == "no") {
                TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                    document.getElementById('gf-wl1').innerHTML = " ";
                }});
                TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            } else if (gfwl1 == "W") {
                TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                    document.getElementById('gf-wl1').innerHTML = "[W]";
                }});
                TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            } else if (gfwl1 == "L") {
                TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                    document.getElementById('gf-wl1').innerHTML = "[L]";
                }});
                TweenMax.to(document.getElementById("gf-wl1"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            }
            animating--;
        }

        if (gfwl2 != scObj["GF-WL2"]) {
            animating++;
            gfwl2 = scObj["GF-WL2"]
            if (gfwl2 == "no") {
                TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                    document.getElementById('gf-wl2').innerHTML = " ";
                }});
                TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            } else if (gfwl2 == "W") {
                TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                    document.getElementById('gf-wl2').innerHTML = "[W]";
                }});
                TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            } else if (gfwl2 == "L") {
                TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"0",ease:Quad.easeOut,onComplete: function() {
                    document.getElementById('gf-wl2').innerHTML = "[L]";
                }});
                TweenMax.to(document.getElementById("gf-wl2"),0.5,{opacity:"1",ease:Quad.easeOut,delay:1});
            }
            animating--;
        }

	}
}

function loadFlags() {

	currCountry1 = getCountry(scObj["pCountry1"].toString());
	currCountry2 = getCountry(scObj["pCountry2"].toString());

	document.getElementById("flag1").src = "GoSquared/expanded/" + currCountry1 + ".png";
	document.getElementById("flag2").src = "GoSquared/expanded/" + currCountry2 + ".png";

}

function getCountry (country) {

	var count = iso.findCountryByName(country);
	if (!count)
		count = iso.findCountryByCode(country);
	if (!count) {
		var count = new Array();
		count['value'] = country;
	}

	return count['value'];
}

function setGameScore (game, id) {

    if (game == "p1") {
        // document.getElementById(id).style.background="rgba(254, 51, 52, 0.7)";
        document.getElementById(id).style.background="rgb(254, 51, 52)";
    } else if (game == "p2") {
        // document.getElementById(id).style.background="rgba(41, 139, 255, 0.7)";
        document.getElementById(id).style.background="rgb(41, 139, 255)";
    } else if (game == "no") {
        // document.getElementById(id).style.background="rgba(80, 80, 80, 0.7)";
        document.getElementById(id).style.background="rgb(80, 80, 80)";
    }
}