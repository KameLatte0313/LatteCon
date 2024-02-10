# LatteCon（ラテコン）
<a href="https://github.com/KameLatte0313/LatteCon/releases">ダウンロードページはこちら</a>

<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/cb103d60-11f2-4d21-860e-4fc32c7a7fdd"  style="width:600px;height:auto;">

LatteConは格闘ゲームの大会で使用されることを想定し、様々なレイアウトを実装したスコアボードツールです。<br>

※現時点ではWindowsでのみ使用可能です。Macを使用している方はご注意ください。

## 導入方法
ダウンロードしたzipファイルを解凍します。

基本的には各フォルダ内の`html`形式のファイルをOBSで読み込むことでレイアウトを表示し、`LatteCon.exe`を起動してプレイヤー名などのデータを変更します。


### 詳細な導入方法の解説
1.OBSのソースウィンドウの「＋」からブラウザを選択し、どのレイアウトか識別できるよう名前を付けます。（例：スコアボード）

2.ローカルファイルにチェックを入れ、その下の「参照」から使用したいレイアウトのhtmlファイルを選択してください。（スコアボードの場合：scoreboardフォルダのscoreboard.html）どれがhtmlファイルか分からない方は`Windowsキー + E`でエクスプローラーを開き、左上の「表示」から「ファイル名拡張子」にチェックを入れることでファイル形式が見えるようになります。

3.幅を**1920**、高さを**1080**にして右下の「OK」をクリックすることでOBS上に選択したレイアウトを表示することができます。

4.プレイヤー名やスコアを変更する際は`LatteCon.exe`を起動します。表示された画面で文字を入力し、左上にある「適用する」ボタンを押すことで表示を変更できます。

## レイアウト一覧
### 【スコアボード】
scoreboard.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/7ebc99b8-4078-456d-9cb0-02e30d4e8a98"  style="width:600px;height:auto;">

scoreboard-type2.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/5b1a0c7c-bd5b-4880-8b87-90ef811033f7"  style="width:600px;height:auto;">

scoreboard-type3.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/cbf49187-1060-451f-a376-a3ed4e01f6b4"  style="width:600px;height:auto;">

### 【TOP8ブラケット】
top8.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/d386f223-1874-4920-997f-ddbf175d16a9"  style="width:600px;height:auto;">

### 【クルーバトル】
1対1から9対9まで対応可能なクルーバトルレイアウトです。
同フォルダにあるteam-scoreboard.htmlはcrewbattle.htmlのメンバー残ストックからチーム残ストックを自動計算できます。<br>
crewbattle.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/fc4c0693-0470-4cd9-81df-82d53c369650"  style="width:600px;height:auto;">

### 【3人総当たり】
roundrobin.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/fd75eed2-15d7-4bc7-bc9a-adb35af7c310"  style="width:600px;height:auto;">

### 【インターバル】
interval.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/1fe0ba11-a47d-4b36-88bb-9e017ad2bbdf"  style="width:600px;height:auto;">

interval-type2.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/0d90d4c4-ef43-4b41-8617-96d5a1d5c3e7"  style="width:600px;height:auto;">

### 【MC】
mc.html <br>
<img src="https://github.com/KameLatte0313/ScoreBoard-LatteCon_forSSBU_1.0/assets/75975584/523b43ec-c9b9-4024-8cc8-eed1bab0f122"  style="width:600px;height:auto;">

## コミュニティ
LatteConコミュニティーサーバーをDiscordにて作成しました。
開発の進捗報告やユーザーサポートを行っておりますので、開発に興味のある方は<a href="https://discord.com/invite/WPpS3TVuwp">こちらから</a>ご参加ください。

## LISCENSE

### LatteCon.exe
Copyright (c) 2023, Kamelatte

## StreamControl.exe
Original work Copyright (c) 2012-2015, Tan Yu Sheng
Modified work Copyright (c) 2019, Miguel Müller


All rights reserved.

<https://github.com/farpenoodle/StreamControl>
