# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import json
import time
import math

# rootメインウィンドウの設定
root = tk.Tk()
root.title("LatteCon")
root.geometry("530x500")

timestamp = math.floor(time.time())


# 入力データをJSONに保存する関数
def SetJSON(event):
    GF_WL1 = ""
    GF_WL2 = ""
    cb_autocalc = "0"
    timestamp = math.floor(time.time())
    if (combo_GF_WL1.get() == "GF時に使用する項目"):
        GF_WL1 = "no"
    elif (combo_GF_WL1.get() == "[W]"):
        GF_WL1 = "W"
    elif (combo_GF_WL1.get() == "[L]"):
        GF_WL1 = "L"

    if (combo_GF_WL2.get() == "GF時に使用する項目"):
        GF_WL2 = "no"
    elif (combo_GF_WL2.get() == "[W]"):
        GF_WL2 = "W"
    elif (combo_GF_WL2.get() == "[L]"):
        GF_WL2 = "L"

    if (cb_autocalcVal.get() == True):
        cb_autocalc = "1"
    else:
        cb_autocalc = "0"

    rr_p1_h.delete(0, tk.END)
    rr_p2_h.delete(0, tk.END)
    rr_p3_h.delete(0, tk.END)
    rr_p1_h.insert(tk.END, rr_p1.get())
    rr_p2_h.insert(tk.END, rr_p2.get())
    rr_p3_h.insert(tk.END, rr_p3.get())

    dic = {
        'timestamp': str(timestamp),
        'pName1': pName1.get(),
        'pName2': pName2.get(),
        'pTeam1': pTeam1.get(),
        'pTeam2': pTeam2.get(),
        'stage': stage_text[stage_var.get()],
        'stage_typing': stage_typing.get(),
        'bestofN': bestofN.get(),
        'boN': combo_setstory.get().lower(),
        'game1': game_text[game1_var.get()],
        'game2': game_text[game2_var.get()],
        'game3': game_text[game3_var.get()],
        'game4': game_text[game4_var.get()],
        'game5': game_text[game5_var.get()],
        'GF-WL1': GF_WL1,
        'GF-WL2': GF_WL2,
        'tournament_name': tournament_name.get(),
        'mc_name1': mc_name1.get(),
        'mc_name2': mc_name2.get(),
        'mc_xid1': mc_xid1.get(),
        'mc_xid2': mc_xid2.get(),
        'top8_1_1': top8_1_1.get(),
        'top8_1_2': top8_1_2.get(),
        'top8_1_3': top8_1_3.get(),
        'top8_1_4': top8_1_4.get(),
        'top8_1_5': top8_1_5.get(),
        'top8_1_6': top8_1_6.get(),
        'top8_1_7': top8_1_7.get(),
        'top8_1_8': top8_1_8.get(),
        'top8_2_1': top8_2_1.get(),
        'top8_2_2': top8_2_2.get(),
        'top8_2_3': top8_2_3.get(),
        'top8_2_4': top8_2_4.get(),
        'top8_2_5': top8_2_5.get(),
        'top8_2_6': top8_2_6.get(),
        'top8_3_1': top8_3_1.get(),
        'top8_3_2': top8_3_2.get(),
        'top8_3_3': top8_3_3.get(),
        'top8_3_4': top8_3_4.get(),
        'top8_4_3': top8_4_3.get(),
        'top8_4_4': top8_4_4.get(),
        'top8_1_1_score': str(top8_1_1_score.get()),
        'top8_1_2_score': str(top8_1_2_score.get()),
        'top8_1_3_score': str(top8_1_3_score.get()),
        'top8_1_4_score': str(top8_1_4_score.get()),
        'top8_1_5_score': str(top8_1_5_score.get()),
        'top8_1_6_score': str(top8_1_6_score.get()),
        'top8_1_7_score': str(top8_1_7_score.get()),
        'top8_1_8_score': str(top8_1_8_score.get()),
        'top8_2_1_score': str(top8_2_1_score.get()),
        'top8_2_2_score': str(top8_2_2_score.get()),
        'top8_2_3_score': str(top8_2_3_score.get()),
        'top8_2_4_score': str(top8_2_4_score.get()),
        'top8_2_5_score': str(top8_2_5_score.get()),
        'top8_2_6_score': str(top8_2_6_score.get()),
        'top8_3_1_score': str(top8_3_1_score.get()),
        'top8_3_2_score': str(top8_3_2_score.get()),
        'top8_3_3_score': str(top8_3_3_score.get()),
        'top8_3_4_score': str(top8_3_4_score.get()),
        'top8_4_3_score': str(top8_4_3_score.get()),
        'top8_4_4_score': str(top8_4_4_score.get()),
        'cb_memberNum': str(cb_memberNum.get()),
        'cb_autocalc': cb_autocalc,
        'cb_upperleft': cb_upperleft.get(),
        'cb_upperright': cb_upperright.get(),
        'cb_team1': cb_team1.get(),
        'cb_team2': cb_team2.get(),
        'cb_team1_score': str(cb_team1_score.get()),
        'cb_team2_score': str(cb_team2_score.get()),
        'select_Lmember': cb_member_text[Lmember_var.get()],
        'select_Rmember': cb_member_text[Rmember_var.get()],
        'cb_1_1': cb_1_1.get(),
        'cb_1_2': cb_1_2.get(),
        'cb_1_3': cb_1_3.get(),
        'cb_1_4': cb_1_4.get(),
        'cb_1_5': cb_1_5.get(),
        'cb_1_6': cb_1_6.get(),
        'cb_1_7': cb_1_7.get(),
        'cb_1_8': cb_1_8.get(),
        'cb_1_9': cb_1_9.get(),
        'cb_2_1': cb_2_1.get(),
        'cb_2_2': cb_2_2.get(),
        'cb_2_3': cb_2_3.get(),
        'cb_2_4': cb_2_4.get(),
        'cb_2_5': cb_2_5.get(),
        'cb_2_6': cb_2_6.get(),
        'cb_2_7': cb_2_7.get(),
        'cb_2_8': cb_2_8.get(),
        'cb_2_9': cb_2_9.get(),
        'cb_1_1_score': str(cb_1_1_score.get()),
        'cb_1_2_score': str(cb_1_2_score.get()),
        'cb_1_3_score': str(cb_1_3_score.get()),
        'cb_1_4_score': str(cb_1_4_score.get()),
        'cb_1_5_score': str(cb_1_5_score.get()),
        'cb_1_6_score': str(cb_1_6_score.get()),
        'cb_1_7_score': str(cb_1_7_score.get()),
        'cb_1_8_score': str(cb_1_8_score.get()),
        'cb_1_9_score': str(cb_1_9_score.get()),
        'cb_2_1_score': str(cb_2_1_score.get()),
        'cb_2_2_score': str(cb_2_2_score.get()),
        'cb_2_3_score': str(cb_2_3_score.get()),
        'cb_2_4_score': str(cb_2_4_score.get()),
        'cb_2_5_score': str(cb_2_5_score.get()),
        'cb_2_6_score': str(cb_2_6_score.get()),
        'cb_2_7_score': str(cb_2_7_score.get()),
        'cb_2_8_score': str(cb_2_8_score.get()),
        'cb_2_9_score': str(cb_2_9_score.get()),
        'inad_1_1': inad_1[0].get(),
        'inad_1_2': inad_1[1].get(),
        'inad_1_3': inad_1[2].get(),
        'inad_1_4': inad_1[3].get(),
        'inad_1_5': inad_1[4].get(),
        'inad_1_6': inad_1[5].get(),
        'inad_1_7': inad_1[6].get(),
        'inad_1_8': inad_1[7].get(),
        'inad_1_9': inad_1[8].get(),
        'inad_2_1': inad_2[0].get(),
        'inad_2_2': inad_2[1].get(),
        'inad_2_3': inad_2[2].get(),
        'inad_2_4': inad_2[3].get(),
        'inad_2_5': inad_2[4].get(),
        'inad_2_6': inad_2[5].get(),
        'inad_2_7': inad_2[6].get(),
        'inad_2_8': inad_2[7].get(),
        'inad_2_9': inad_2[8].get(),
        'inad_3_1': inad_3[0].get(),
        'inad_3_2': inad_3[1].get(),
        'inad_3_3': inad_3[2].get(),
        'inad_3_4': inad_3[3].get(),
        'inad_3_5': inad_3[4].get(),
        'inad_3_6': inad_3[5].get(),
        'inad_3_7': inad_3[6].get(),
        'inad_3_8': inad_3[7].get(),
        'inad_3_9': inad_3[8].get(),
        'inad_4_1': inad_4[0].get(),
        'inad_4_2': inad_4[1].get(),
        'inad_4_3': inad_4[2].get(),
        'inad_4_4': inad_4[3].get(),
        'inad_4_5': inad_4[4].get(),
        'inad_4_6': inad_4[5].get(),
        'inad_4_7': inad_4[6].get(),
        'inad_4_8': inad_4[7].get(),
        'inad_4_9': inad_4[8].get(),
        'rr_pool': rr_pool.get(),
        'rr_p1': rr_p1.get(),
        'rr_p2': rr_p2.get(),
        'rr_p3': rr_p3.get(),
        'rr_p1_h': rr_p1.get(),
        'rr_p2_h': rr_p2.get(),
        'rr_p3_h': rr_p3.get(),
        'rr_1vs2_1': str(rr_1vs2_1.get()),
        'rr_1vs2_2': str(rr_1vs2_2.get()),
        'rr_1vs3_1': str(rr_1vs3_1.get()),
        'rr_1vs3_3': str(rr_1vs3_3.get()),
        'rr_2vs1_2': str(rr_1vs2_2.get()),
        'rr_2vs1_1': str(rr_1vs2_1.get()),
        'rr_2vs3_2': str(rr_2vs3_2.get()),
        'rr_2vs3_3': str(rr_2vs3_3.get()),
        'rr_3vs1_3': str(rr_1vs3_3.get()),
        'rr_3vs1_1': str(rr_1vs3_1.get()),
        'rr_3vs2_3': str(rr_2vs3_3.get()),
        'rr_3vs2_2': str(rr_2vs3_2.get()),
        'rr_p1_rank': str(rr_p1_rank.get()),
        'rr_p2_rank': str(rr_p2_rank.get()),
        'rr_p3_rank': str(rr_p3_rank.get()),
        'rr_pl_p1': rr_pl_p1.get(),
        'rr_pl_p2': rr_pl_p2.get(),
        'rr_pl_p3': rr_pl_p3.get(),
        'rr_pl_p1_xid': rr_pl_p1_xid.get(),
        'rr_pl_p2_xid': rr_pl_p2_xid.get(),
        'rr_pl_p3_xid': rr_pl_p3_xid.get()
    }
    with open("datafile/LatteCon.json", "w", encoding="utf-8") as outputFile:
        json.dump(dic, outputFile, indent=4, ensure_ascii=False )

# クルーバトルのメンバー名をクリアする関数
def cbClearAllName(event):
    cb_1_1.delete(0, tk.END)
    cb_1_2.delete(0, tk.END)
    cb_1_3.delete(0, tk.END)
    cb_1_4.delete(0, tk.END)
    cb_1_5.delete(0, tk.END)
    cb_1_6.delete(0, tk.END)
    cb_1_7.delete(0, tk.END)
    cb_1_8.delete(0, tk.END)
    cb_1_9.delete(0, tk.END)
    cb_2_1.delete(0, tk.END)
    cb_2_2.delete(0, tk.END)
    cb_2_3.delete(0, tk.END)
    cb_2_4.delete(0, tk.END)
    cb_2_5.delete(0, tk.END)
    cb_2_6.delete(0, tk.END)
    cb_2_7.delete(0, tk.END)
    cb_2_8.delete(0, tk.END)
    cb_2_9.delete(0, tk.END)

# クルーバトルの全スコアを任意の数値にセットする関数
def cbSetAllScore(event):
    cb_1_1_score.set(cb_setScore.get())
    cb_1_2_score.set(cb_setScore.get())
    cb_1_3_score.set(cb_setScore.get())
    cb_1_4_score.set(cb_setScore.get())
    cb_1_5_score.set(cb_setScore.get())
    cb_1_6_score.set(cb_setScore.get())
    cb_1_7_score.set(cb_setScore.get())
    cb_1_8_score.set(cb_setScore.get())
    cb_1_9_score.set(cb_setScore.get())
    cb_2_1_score.set(cb_setScore.get())
    cb_2_2_score.set(cb_setScore.get())
    cb_2_3_score.set(cb_setScore.get())
    cb_2_4_score.set(cb_setScore.get())
    cb_2_5_score.set(cb_setScore.get())
    cb_2_6_score.set(cb_setScore.get())
    cb_2_7_score.set(cb_setScore.get())
    cb_2_8_score.set(cb_setScore.get())
    cb_2_9_score.set(cb_setScore.get())

# クルーバトルの左チームメンバーを事前入力データからセットする関数
def cbSetLMember(event):
    cb_1_1.delete(0, tk.END)
    cb_1_2.delete(0, tk.END)
    cb_1_3.delete(0, tk.END)
    cb_1_4.delete(0, tk.END)
    cb_1_5.delete(0, tk.END)
    cb_1_6.delete(0, tk.END)
    cb_1_7.delete(0, tk.END)
    cb_1_8.delete(0, tk.END)
    cb_1_9.delete(0, tk.END)
    if (combo_selectLteam.get() == "TEAM1"):
        cb_1_1.insert(tk.END, inad_1[0].get())
        cb_1_2.insert(tk.END, inad_1[1].get())
        cb_1_3.insert(tk.END, inad_1[2].get())
        cb_1_4.insert(tk.END, inad_1[3].get())
        cb_1_5.insert(tk.END, inad_1[4].get())
        cb_1_6.insert(tk.END, inad_1[5].get())
        cb_1_7.insert(tk.END, inad_1[6].get())
        cb_1_8.insert(tk.END, inad_1[7].get())
        cb_1_9.insert(tk.END, inad_1[8].get())
    elif (combo_selectLteam.get() == "TEAM2"):
        cb_1_1.insert(tk.END, inad_2[0].get())
        cb_1_2.insert(tk.END, inad_2[1].get())
        cb_1_3.insert(tk.END, inad_2[2].get())
        cb_1_4.insert(tk.END, inad_2[3].get())
        cb_1_5.insert(tk.END, inad_2[4].get())
        cb_1_6.insert(tk.END, inad_2[5].get())
        cb_1_7.insert(tk.END, inad_2[6].get())
        cb_1_8.insert(tk.END, inad_2[7].get())
        cb_1_9.insert(tk.END, inad_2[8].get())
    elif (combo_selectLteam.get() == "TEAM3"):
        cb_1_1.insert(tk.END, inad_3[0].get())
        cb_1_2.insert(tk.END, inad_3[1].get())
        cb_1_3.insert(tk.END, inad_3[2].get())
        cb_1_4.insert(tk.END, inad_3[3].get())
        cb_1_5.insert(tk.END, inad_3[4].get())
        cb_1_6.insert(tk.END, inad_3[5].get())
        cb_1_7.insert(tk.END, inad_3[6].get())
        cb_1_8.insert(tk.END, inad_3[7].get())
        cb_1_9.insert(tk.END, inad_3[8].get())
    else:
        cb_1_1.insert(tk.END, inad_4[0].get())
        cb_1_2.insert(tk.END, inad_4[1].get())
        cb_1_3.insert(tk.END, inad_4[2].get())
        cb_1_4.insert(tk.END, inad_4[3].get())
        cb_1_5.insert(tk.END, inad_4[4].get())
        cb_1_6.insert(tk.END, inad_4[5].get())
        cb_1_7.insert(tk.END, inad_4[6].get())
        cb_1_8.insert(tk.END, inad_4[7].get())
        cb_1_9.insert(tk.END, inad_4[8].get())

# クルーバトルの右チームメンバーを事前入力データからセットする関数
def cbSetRMember(event):
    cb_2_1.delete(0, tk.END)
    cb_2_2.delete(0, tk.END)
    cb_2_3.delete(0, tk.END)
    cb_2_4.delete(0, tk.END)
    cb_2_5.delete(0, tk.END)
    cb_2_6.delete(0, tk.END)
    cb_2_7.delete(0, tk.END)
    cb_2_8.delete(0, tk.END)
    cb_2_9.delete(0, tk.END)
    if (combo_selectRteam.get() == "TEAM1"):
        cb_2_1.insert(tk.END, inad_1[0].get())
        cb_2_2.insert(tk.END, inad_1[1].get())
        cb_2_3.insert(tk.END, inad_1[2].get())
        cb_2_4.insert(tk.END, inad_1[3].get())
        cb_2_5.insert(tk.END, inad_1[4].get())
        cb_2_6.insert(tk.END, inad_1[5].get())
        cb_2_7.insert(tk.END, inad_1[6].get())
        cb_2_8.insert(tk.END, inad_1[7].get())
        cb_2_9.insert(tk.END, inad_1[8].get())
    elif (combo_selectRteam.get() == "TEAM2"):
        cb_2_1.insert(tk.END, inad_2[0].get())
        cb_2_2.insert(tk.END, inad_2[1].get())
        cb_2_3.insert(tk.END, inad_2[2].get())
        cb_2_4.insert(tk.END, inad_2[3].get())
        cb_2_5.insert(tk.END, inad_2[4].get())
        cb_2_6.insert(tk.END, inad_2[5].get())
        cb_2_7.insert(tk.END, inad_2[6].get())
        cb_2_8.insert(tk.END, inad_2[7].get())
        cb_2_9.insert(tk.END, inad_2[8].get())
    elif (combo_selectRteam.get() == "TEAM3"):
        cb_2_1.insert(tk.END, inad_3[0].get())
        cb_2_2.insert(tk.END, inad_3[1].get())
        cb_2_3.insert(tk.END, inad_3[2].get())
        cb_2_4.insert(tk.END, inad_3[3].get())
        cb_2_5.insert(tk.END, inad_3[4].get())
        cb_2_6.insert(tk.END, inad_3[5].get())
        cb_2_7.insert(tk.END, inad_3[6].get())
        cb_2_8.insert(tk.END, inad_3[7].get())
        cb_2_9.insert(tk.END, inad_3[8].get())
    else:
        cb_2_1.insert(tk.END, inad_4[0].get())
        cb_2_2.insert(tk.END, inad_4[1].get())
        cb_2_3.insert(tk.END, inad_4[2].get())
        cb_2_4.insert(tk.END, inad_4[3].get())
        cb_2_5.insert(tk.END, inad_4[4].get())
        cb_2_6.insert(tk.END, inad_4[5].get())
        cb_2_7.insert(tk.END, inad_4[6].get())
        cb_2_8.insert(tk.END, inad_4[7].get())
        cb_2_9.insert(tk.END, inad_4[8].get())

# クルーバトルの左右データを入れ替える関数
def cbSwap(event):
    exchangeVal = cb_team1.get()
    cb_team1.delete(0, tk.END)
    cb_team1.insert(tk.END, cb_team2.get())
    cb_team2.delete(0, tk.END)
    cb_team2.insert(tk.END, exchangeVal)
    exchangeVal = cb_team1_score.get()
    cb_team1_score.set(cb_team2_score.get())
    cb_team2_score.set(exchangeVal)
    exchangeVal = cb_1_1.get()
    cb_1_1.delete(0, tk.END)
    cb_1_1.insert(tk.END, cb_2_1.get())
    cb_2_1.delete(0, tk.END)
    cb_2_1.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_2.get()
    cb_1_2.delete(0, tk.END)
    cb_1_2.insert(tk.END, cb_2_2.get())
    cb_2_2.delete(0, tk.END)
    cb_2_2.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_3.get()
    cb_1_3.delete(0, tk.END)
    cb_1_3.insert(tk.END, cb_2_3.get())
    cb_2_3.delete(0, tk.END)
    cb_2_3.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_4.get()
    cb_1_4.delete(0, tk.END)
    cb_1_4.insert(tk.END, cb_2_4.get())
    cb_2_4.delete(0, tk.END)
    cb_2_4.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_5.get()
    cb_1_5.delete(0, tk.END)
    cb_1_5.insert(tk.END, cb_2_5.get())
    cb_2_5.delete(0, tk.END)
    cb_2_5.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_6.get()
    cb_1_6.delete(0, tk.END)
    cb_1_6.insert(tk.END, cb_2_6.get())
    cb_2_6.delete(0, tk.END)
    cb_2_6.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_7.get()
    cb_1_7.delete(0, tk.END)
    cb_1_7.insert(tk.END, cb_2_7.get())
    cb_2_7.delete(0, tk.END)
    cb_2_7.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_8.get()
    cb_1_8.delete(0, tk.END)
    cb_1_8.insert(tk.END, cb_2_8.get())
    cb_2_8.delete(0, tk.END)
    cb_2_8.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_9.get()
    cb_1_9.delete(0, tk.END)
    cb_1_9.insert(tk.END, cb_2_9.get())
    cb_2_9.delete(0, tk.END)
    cb_2_9.insert(tk.END, exchangeVal)
    exchangeVal = cb_1_1_score.get()
    cb_1_1_score.set(cb_2_1_score.get())
    cb_2_1_score.set(exchangeVal)
    exchangeVal = cb_1_2_score.get()
    cb_1_2_score.set(cb_2_2_score.get())
    cb_2_2_score.set(exchangeVal)
    exchangeVal = cb_1_3_score.get()
    cb_1_3_score.set(cb_2_3_score.get())
    cb_2_3_score.set(exchangeVal)
    exchangeVal = cb_1_4_score.get()
    cb_1_4_score.set(cb_2_4_score.get())
    cb_2_4_score.set(exchangeVal)
    exchangeVal = cb_1_5_score.get()
    cb_1_5_score.set(cb_2_5_score.get())
    cb_2_5_score.set(exchangeVal)
    exchangeVal = cb_1_6_score.get()
    cb_1_6_score.set(cb_2_6_score.get())
    cb_2_6_score.set(exchangeVal)
    exchangeVal = cb_1_7_score.get()
    cb_1_7_score.set(cb_2_7_score.get())
    cb_2_7_score.set(exchangeVal)
    exchangeVal = cb_1_8_score.get()
    cb_1_8_score.set(cb_2_8_score.get())
    cb_2_8_score.set(exchangeVal)
    exchangeVal = cb_1_9_score.get()
    cb_1_9_score.set(cb_2_9_score.get())
    cb_2_9_score.set(exchangeVal)

# スコアボードのデータをクリアする関数
def sbClear(event):
    pName1.delete(0, tk.END)
    pName2.delete(0, tk.END)
    pTeam1.delete(0, tk.END)
    pTeam2.delete(0, tk.END)
    game1_var.set(1)
    game2_var.set(1)
    game3_var.set(1)
    game4_var.set(1)
    game5_var.set(1)

# スコアボードの左右データを入れ替える関数
def sbSwap(event):
    exchangeVal = pName1.get()
    pName1.delete(0, tk.END)
    pName1.insert(tk.END, pName2.get())
    pName2.delete(0, tk.END)
    pName2.insert(tk.END, exchangeVal)
    exchangeVal = pTeam1.get()
    pTeam1.delete(0, tk.END)
    pTeam1.insert(tk.END, pTeam2.get())
    pTeam2.delete(0, tk.END)
    pTeam2.insert(tk.END, exchangeVal)
    if (game1_var.get() == 0):
        game1_var.set(2)
    elif (game1_var.get() == 2):
        game1_var.set(0)

    if (game2_var.get() == 0):
        game2_var.set(2)
    elif (game2_var.get() == 2):
        game2_var.set(0)

    if (game3_var.get() == 0):
        game3_var.set(2)
    elif (game3_var.get() == 2):
        game3_var.set(0)

    if (game4_var.get() == 0):
        game4_var.set(2)
    elif (game4_var.get() == 2):
        game4_var.set(0)

    if (game5_var.get() == 0):
        game5_var.set(2)
    elif (game5_var.get() == 2):
        game5_var.set(0)

# TOP8ブラケットの全データをクリアする関数
def top8ClearAll(event):
    top8_1_1.delete(0, tk.END)
    top8_1_2.delete(0, tk.END)
    top8_1_3.delete(0, tk.END)
    top8_1_4.delete(0, tk.END)
    top8_1_5.delete(0, tk.END)
    top8_1_6.delete(0, tk.END)
    top8_1_7.delete(0, tk.END)
    top8_1_8.delete(0, tk.END)
    top8_2_1.delete(0, tk.END)
    top8_2_2.delete(0, tk.END)
    top8_2_3.delete(0, tk.END)
    top8_2_4.delete(0, tk.END)
    top8_2_5.delete(0, tk.END)
    top8_2_6.delete(0, tk.END)
    top8_3_1.delete(0, tk.END)
    top8_3_2.delete(0, tk.END)
    top8_3_3.delete(0, tk.END)
    top8_3_4.delete(0, tk.END)
    top8_4_3.delete(0, tk.END)
    top8_4_4.delete(0, tk.END)
    top8_1_1_score.set(0)
    top8_1_2_score.set(0)
    top8_1_3_score.set(0)
    top8_1_4_score.set(0)
    top8_1_5_score.set(0)
    top8_1_6_score.set(0)
    top8_1_7_score.set(0)
    top8_1_8_score.set(0)
    top8_2_1_score.set(0)
    top8_2_2_score.set(0)
    top8_2_3_score.set(0)
    top8_2_4_score.set(0)
    top8_2_5_score.set(0)
    top8_2_6_score.set(0)
    top8_3_1_score.set(0)
    top8_3_2_score.set(0)
    top8_3_3_score.set(0)
    top8_3_4_score.set(0)
    top8_4_3_score.set(0)
    top8_4_4_score.set(0)

# 事前入力データをクリアする関数
def inad1Clear(event):
    for i in range(9):
        inad_1[i].delete(0, tk.END)

def inad2Clear(event):
    for i in range(9):
        inad_2[i].delete(0, tk.END)

def inad3Clear(event):
    for i in range(9):
        inad_3[i].delete(0, tk.END)

def inad4Clear(event):
    for i in range(9):
        inad_4[i].delete(0, tk.END)

# 3人総当たりのデータをクリアする関数
def rrClear(event):
    rr_pool.delete(0, tk.END)
    rr_p1.delete(0, tk.END)
    rr_p2.delete(0, tk.END)
    rr_p3.delete(0, tk.END)
    rr_p1_h.delete(0, tk.END)
    rr_p2_h.delete(0, tk.END)
    rr_p3_h.delete(0, tk.END)
    rr_p1_rank.set(0)
    rr_p2_rank.set(0)
    rr_p3_rank.set(0)
    rr_1vs2_1.set(0)
    rr_1vs2_2.set(0)
    rr_1vs3_1.set(0)
    rr_1vs3_3.set(0)
    rr_2vs3_2.set(0)
    rr_2vs3_3.set(0)

# LatteCon.exeを最前面に固定する関数
def alwaysOnTop():
    root.attributes("-topmost", always_top_value.get())

# メニューバーの作成
menubar = tk.Menu(root)
root.config(menu=menubar)
config_menu = tk.Menu(menubar, tearoff=False)
always_top_value = tk.BooleanVar()
config_menu.add_checkbutton(label = "常に最前面に表示する", variable=always_top_value, command=alwaysOnTop)
menubar.add_cascade(label="設定", menu=config_menu)

# Notebookウィジェットの作成
notebook = ttk.Notebook(root)

# タブの作成
scoreboard = tk.Frame(notebook)
mc = tk.Frame(notebook)
TOP8 = tk.Frame(notebook)
crewbattle = tk.Frame(notebook)
inadvance = tk.Frame(notebook)
roundrobin = tk.Frame(notebook)

# notebookにタブを追加
notebook.add(scoreboard, text="スコアボード")
notebook.add(mc, text="MC")
notebook.add(TOP8, text="TOP8")
notebook.add(crewbattle, text="クルーバトル")
notebook.add(inadvance, text="事前入力")
notebook.add(roundrobin, text="3人総当たり")

# ウィンドウ上部に配置するウィジェットの作成
Button_save = tk.Button(text=u'適用する')
Button_save.bind("<Button-1>",SetJSON) 

Button_save.pack(anchor = tk.NW)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

# -------------スコアボード-------------
# ラベル
stage_info_text = ['R1','R2','R3','R4','R5','R6','R7','QF','SF',' F','GF','GF2','予選']
for i in range(len(stage_info_text)):
    label_stage_info = ttk.Label(scoreboard, text=stage_info_text[i])
    if (i <= 10):
        label_stage_info.place(x=55 + (i *24), y=0)
    elif (i == 11):
        label_stage_info.place(x=315, y=0)
    elif (i == 12):
        label_stage_info.place(x=339, y=0)

label_stage_top = ttk.Label(scoreboard, text="勝者側")
label_stage_top.place(x=10, y=15)

label_stage_bottom = ttk.Label(scoreboard, text="敗者側")
label_stage_bottom.place(x=10, y=35)

label_stage_typing = ttk.Label(scoreboard, text="直接入力")
label_stage_typing.place(x=5, y=55)

label_tournament_name = ttk.Label(scoreboard, text="大会名")
label_tournament_name.place(x=5, y=90)
label_tournament_name = ttk.Label(scoreboard, text="(scoreboard-type2のみ)")
label_tournament_name.place(x=5, y=110)

label_BESTOF = ttk.Label(scoreboard, text="BEST OF ~")
label_BESTOF.place(x=250, y=90)

label_setstory = ttk.Label(scoreboard, text="SET STORY")
label_setstory.place(x=250, y=125)

label_tournament_name = ttk.Label(scoreboard, text="P1 Team")
label_tournament_name.place(x=5, y=160)
label_tournament_name = ttk.Label(scoreboard, text="P1 Name")
label_tournament_name.place(x=85, y=160)
label_tournament_name = ttk.Label(scoreboard, text="P2 Team")
label_tournament_name.place(x=245, y=160)
label_tournament_name = ttk.Label(scoreboard, text="P2 Name")
label_tournament_name.place(x=325, y=160)

label_game1 = ttk.Label(scoreboard, text="P1   -   P2")
label_game1.place(x=185, y=210)

label_game1 = ttk.Label(scoreboard, text="GAME1")
label_game1.place(x=140, y=225)
label_game2 = ttk.Label(scoreboard, text="GAME2")
label_game2.place(x=140, y=250)
label_game3 = ttk.Label(scoreboard, text="GAME3")
label_game3.place(x=140, y=275)
label_game4 = ttk.Label(scoreboard, text="GAME4")
label_game4.place(x=140, y=300)
label_game5 = ttk.Label(scoreboard, text="GAME5")
label_game5.place(x=140, y=325)

# ウィジェット
stage_text = [
    'WINNERS ROUND1',
    'WINNERS ROUND2',
    'WINNERS ROUND3',
    'WINNERS ROUND4',
    'WINNERS ROUND5',
    'WINNERS ROUND6',
    'WINNERS ROUND7',
    'WINNERS QUARTER-FINAL',
    'WINNERS SEMI-FINAL',
    'WINNERS FINAL',
    'GRAND FINAL',
    'GRAND FINAL RESET',
    'POOLS',
    'LOSERS ROUND1',
    'LOSERS ROUND2',
    'LOSERS ROUND3',
    'LOSERS ROUND4',
    'LOSERS ROUND5',
    'LOSERS ROUND6',
    'LOSERS ROUND7',
    'LOSERS QUARTER-FINAL',
    'LOSERS SEMI-FINAL',
    'LOSERS FINAL',
    'stage_typing'
]
stage_var = tk.IntVar()
stage_var.set(0)
for i in range(len(stage_text)):
    stage = ttk.Radiobutton(scoreboard, value=i, variable=stage_var)
    if (i <= 12):
        stage.place(x=55 + (i *24), y=15)
    elif (i <= 22):
        stage.place(x=55 + ((i - 13) *24), y=35)
    else:
        stage.place(x=55, y=55)

stage_typing = ttk.Entry(scoreboard, width=20)
stage_typing.place(x=80, y=55)

tournament_name = ttk.Entry(scoreboard, width=20)
tournament_name.place(x=80, y=90)

bestofN = ttk.Entry(scoreboard, width=13)
# bestofN.insert(tk.END,"BEST OF 3")
bestofN.place(x=320, y=90)

option_setstory = ('BO3', 'BO5')
setstory_variable = tk.StringVar()
combo_setstory = ttk.Combobox(scoreboard, values=option_setstory, textvariable=setstory_variable, state="readonly", width=10)
combo_setstory.set(option_setstory[0])
combo_setstory.place(x=320, y=125)

pName1 = ttk.Entry(scoreboard, width=20)
# pName1.insert(tk.END,"プレイヤー1")
pName1.place(x=55, y=180)

pName2 = ttk.Entry(scoreboard, width=20)
# pName2.insert(tk.END,"プレイヤー2")
pName2.place(x=295, y=180)

pTeam1 = ttk.Entry(scoreboard, width=7)
# pTeam1.insert(tk.END,"TEAM")
pTeam1.place(x=5, y=180)

pTeam2 = ttk.Entry(scoreboard, width=7)
# pTeam2.insert(tk.END,"TEAM")
pTeam2.place(x=245, y=180)

Button_sb_change = ttk.Button(scoreboard, text=u'⇔', width=7)
Button_sb_change.bind("<Button-1>",sbSwap) 
Button_sb_change.place(x=187, y=178)

Button_sb_clear = ttk.Button(scoreboard, text=u'Clear', width=7)
Button_sb_clear.bind("<Button-1>",sbClear) 
Button_sb_clear.place(x=185, y=350)

game_text = ['p1', 'no', 'p2']
game1_var = tk.IntVar()
game1_var.set(1)
for i in range(len(game_text)):
    game1 = ttk.Radiobutton(scoreboard, value=i, variable=game1_var)
    game1.place(x=185 + (i *18), y=225)

game2_var = tk.IntVar()
game2_var.set(1)
for i in range(len(game_text)):
    game2 = ttk.Radiobutton(scoreboard, value=i, variable=game2_var)
    game2.place(x=185 + (i *18), y=250)

game3_var = tk.IntVar()
game3_var.set(1)
for i in range(len(game_text)):
    game3 = ttk.Radiobutton(scoreboard, value=i, variable=game3_var)
    game3.place(x=185 + (i *18), y=275)

game4_var = tk.IntVar()
game4_var.set(1)
for i in range(len(game_text)):
    game4 = ttk.Radiobutton(scoreboard, value=i, variable=game4_var)
    game4.place(x=185 + (i *18), y=300)

game5_var = tk.IntVar()
game5_var.set(1)
for i in range(len(game_text)):
    game5 = ttk.Radiobutton(scoreboard, value=i, variable=game5_var)
    game5.place(x=185 + (i *18), y=325)

option_GF_WL1 = ('GF時に使用する項目', '[W]', '[L]')
GF_WL1_variable = tk.StringVar()
combo_GF_WL1 = ttk.Combobox(scoreboard, values=option_GF_WL1, textvariable=GF_WL1_variable, state="readonly", width=17)
combo_GF_WL1.set(option_GF_WL1[0])
combo_GF_WL1.place(x=5, y=210)

option_GF_WL2 = ('GF時に使用する項目', '[W]', '[L]')
GF_WL2_variable = tk.StringVar()
combo_GF_WL2 = ttk.Combobox(scoreboard, values=option_GF_WL2, textvariable=GF_WL2_variable, state="readonly", width=17)
combo_GF_WL2.set(option_GF_WL1[0])
combo_GF_WL2.place(x=295, y=210)

# ------------- MC -------------
# ラベル
label_mc_name = ttk.Label(mc, text="MC NAME")
label_mc_name.place(x=90, y=20)
label_mc_xid = ttk.Label(mc, text="MC TwitterID")
label_mc_xid.place(x=225, y=20)

label_mc_name1 = ttk.Label(mc, text="■ MC 1")
label_mc_name1.place(x=10, y=40)

label_mc_name2 = ttk.Label(mc, text="■ MC 2")
label_mc_name2.place(x=10, y=70)

# ウィジェット
mc_name1 = ttk.Entry(mc, width=20)
mc_name1.place(x=60, y=40)
mc_xid1 = ttk.Entry(mc, width=20)
mc_xid1.place(x=200, y=40)

mc_name2 = ttk.Entry(mc, width=20)
mc_name2.place(x=60, y=70)
mc_xid2 = ttk.Entry(mc, width=20)
mc_xid2.place(x=200, y=70)

# ------------- TOP8 -------------
# ラベル
label = ttk.Label(TOP8, text="Winners SF")
label.place(x=5, y=5)
label = ttk.Label(TOP8, text="TOP8 Losers")
label.place(x=5, y=155)
label = ttk.Label(TOP8, text="Winners Final")
label.place(x=265, y=20)
label = ttk.Label(TOP8, text="Losers QF")
label.place(x=135, y=155)
label = ttk.Label(TOP8, text="Grand Final")
label.place(x=395, y=20)
label = ttk.Label(TOP8, text="Losers SF")
label.place(x=265, y=170)
label = ttk.Label(TOP8, text="Losers Final")
label.place(x=395, y=170)

label = ttk.Label(TOP8, text="┓")
label.place(x=115, y=25)
label = ttk.Label(TOP8, text="┠━━━━━━━━━━━")
label.place(x=115, y=40)
label = ttk.Label(TOP8, text="┛")
label.place(x=115, y=55)

label = ttk.Label(TOP8, text="┓")
label.place(x=115, y=85)
label = ttk.Label(TOP8, text="┠━━━━━━━━━━━")
label.place(x=115, y=100)
label = ttk.Label(TOP8, text="┛")
label.place(x=115, y=115)

label = ttk.Label(TOP8, text="┓")
label.place(x=115, y=175)
label = ttk.Label(TOP8, text="┃")
label.place(x=115, y=190)
label = ttk.Label(TOP8, text="┻")
label.place(x=115, y=205)

label = ttk.Label(TOP8, text="┓")
label.place(x=115, y=235)
label = ttk.Label(TOP8, text="┃")
label.place(x=115, y=250)
label = ttk.Label(TOP8, text="┻")
label.place(x=115, y=265)

label = ttk.Label(TOP8, text="┳")
label.place(x=375, y=40)
label = ttk.Label(TOP8, text="┃")
label.place(x=375, y=55)
label = ttk.Label(TOP8, text="┃")
label.place(x=375, y=70)
label = ttk.Label(TOP8, text="┃")
label.place(x=375, y=85)
label = ttk.Label(TOP8, text="┛")
label.place(x=375, y=100)

label = ttk.Label(TOP8, text="┓")
label.place(x=245, y=175)
label = ttk.Label(TOP8, text="┠")
label.place(x=245, y=190)
label = ttk.Label(TOP8, text="┛")
label.place(x=245, y=205)

label = ttk.Label(TOP8, text="┓")
label.place(x=245, y=235)
label = ttk.Label(TOP8, text="┠")
label.place(x=245, y=250)
label = ttk.Label(TOP8, text="┛")
label.place(x=245, y=265)

label = ttk.Label(TOP8, text="┓")
label.place(x=375, y=190)
label = ttk.Label(TOP8, text="┃")
label.place(x=375, y=205)
label = ttk.Label(TOP8, text="┃")
label.place(x=375, y=220)
label = ttk.Label(TOP8, text="┃")
label.place(x=375, y=235)
label = ttk.Label(TOP8, text="┻")
label.place(x=375, y=250)

# ウィジェット
top8_1_1 = ttk.Entry(TOP8, width=10)
top8_1_1.place(x=5, y=25)
top8_1_2 = ttk.Entry(TOP8, width=10)
top8_1_2.place(x=5, y=55)
top8_1_3 = ttk.Entry(TOP8, width=10)
top8_1_3.place(x=5, y=85)
top8_1_4 = ttk.Entry(TOP8, width=10)
top8_1_4.place(x=5, y=115)

top8_1_1_score = tk.IntVar()
top8_1_1_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_1_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=25)

top8_1_2_score = tk.IntVar()
top8_1_2_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_2_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=55)

top8_1_3_score = tk.IntVar()
top8_1_3_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_3_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=85)

top8_1_4_score = tk.IntVar()
top8_1_4_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_4_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=115)

top8_1_5 = ttk.Entry(TOP8, width=10)
top8_1_5.place(x=5, y=175)
top8_1_6 = ttk.Entry(TOP8, width=10)
top8_1_6.place(x=5, y=205)
top8_1_7 = ttk.Entry(TOP8, width=10)
top8_1_7.place(x=5, y=235)
top8_1_8 = ttk.Entry(TOP8, width=10)
top8_1_8.place(x=5, y=265)

top8_1_5_score = tk.IntVar()
top8_1_5_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_5_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=175)

top8_1_6_score = tk.IntVar()
top8_1_6_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_6_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=205)

top8_1_7_score = tk.IntVar()
top8_1_7_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_7_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=235)

top8_1_8_score = tk.IntVar()
top8_1_8_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_1_8_score, from_=0, to=99, increment=1, width=3)
s.place(x=75, y=265)

top8_2_1 = ttk.Entry(TOP8, width=10)
top8_2_1.place(x=265, y=40)
top8_2_2 = ttk.Entry(TOP8, width=10)
top8_2_2.place(x=265, y=100)

top8_2_1_score = tk.IntVar()
top8_2_1_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_2_1_score, from_=0, to=99, increment=1, width=3)
s.place(x=335, y=40)

top8_2_2_score = tk.IntVar()
top8_2_2_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_2_2_score, from_=0, to=99, increment=1, width=3)
s.place(x=335, y=100)

top8_2_3 = ttk.Entry(TOP8, width=10)
top8_2_3.place(x=135, y=175)
top8_2_4 = ttk.Entry(TOP8, width=10)
top8_2_4.place(x=135, y=205)
top8_2_5 = ttk.Entry(TOP8, width=10)
top8_2_5.place(x=135, y=235)
top8_2_6 = ttk.Entry(TOP8, width=10)
top8_2_6.place(x=135, y=265)

top8_2_3_score = tk.IntVar()
top8_2_3_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_2_3_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=175)

top8_2_4_score = tk.IntVar()
top8_2_4_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_2_4_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=205)

top8_2_5_score = tk.IntVar()
top8_2_5_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_2_5_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=235)

top8_2_6_score = tk.IntVar()
top8_2_6_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_2_6_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=265)

top8_3_1 = ttk.Entry(TOP8, width=10)
top8_3_1.place(x=395, y=40)
top8_3_2 = ttk.Entry(TOP8, width=10)
top8_3_2.place(x=395, y=100)

top8_3_1_score = tk.IntVar()
top8_3_1_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_3_1_score, from_=0, to=99, increment=1, width=3)
s.place(x=465, y=40)

top8_3_2_score = tk.IntVar()
top8_3_2_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_3_2_score, from_=0, to=99, increment=1, width=3)
s.place(x=465, y=100)

top8_3_3 = ttk.Entry(TOP8, width=10)
top8_3_3.place(x=265, y=190)
top8_3_4 = ttk.Entry(TOP8, width=10)
top8_3_4.place(x=265, y=250)

top8_3_3_score = tk.IntVar()
top8_3_3_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_3_3_score, from_=0, to=99, increment=1, width=3)
s.place(x=335, y=190)

top8_3_4_score = tk.IntVar()
top8_3_4_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_3_4_score, from_=0, to=99, increment=1, width=3)
s.place(x=335, y=250)

top8_4_3 = ttk.Entry(TOP8, width=10)
top8_4_3.place(x=395, y=190)
top8_4_4 = ttk.Entry(TOP8, width=10)
top8_4_4.place(x=395, y=250)

top8_4_3_score = tk.IntVar()
top8_4_3_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_4_3_score, from_=0, to=99, increment=1, width=3)
s.place(x=465, y=190)

top8_4_4_score = tk.IntVar()
top8_4_4_score.set(0)
s = ttk.Spinbox(TOP8, textvariable=top8_4_4_score, from_=0, to=99, increment=1, width=3)
s.place(x=465, y=250)

Button_top8_AllClear = ttk.Button(TOP8, text=u'AllClear')
Button_top8_AllClear.bind("<Button-1>",top8ClearAll) 
Button_top8_AllClear.place(x=5, y=330)

# ------------- クルーバトル -------------
# ラベル
label = ttk.Label(crewbattle, text="LEFT TEAM")
label.place(x=5, y=53)
label = ttk.Label(crewbattle, text="RIGHT TEAM")
label.place(x=245, y=53)

label = ttk.Label(crewbattle, text="メンバー数")
label.place(x=5, y=105)

label = ttk.Label(crewbattle, text="now?")
label.place(x=5, y=130)
label = ttk.Label(crewbattle, text="now?")
label.place(x=345, y=130)
label = ttk.Label(crewbattle, text="LEFT MEMBER")
label.place(x=45, y=130)
label = ttk.Label(crewbattle, text="残ストック")
label.place(x=165, y=130)
label = ttk.Label(crewbattle, text="RIGHT MEMBER")
label.place(x=250, y=130)
label = ttk.Label(crewbattle, text="P1")
label.place(x=180, y=150)
label = ttk.Label(crewbattle, text="P2")
label.place(x=180, y=175)
label = ttk.Label(crewbattle, text="P3")
label.place(x=180, y=200)
label = ttk.Label(crewbattle, text="P4")
label.place(x=180, y=225)
label = ttk.Label(crewbattle, text="P5")
label.place(x=180, y=250)
label = ttk.Label(crewbattle, text="P6")
label.place(x=180, y=275)
label = ttk.Label(crewbattle, text="P7")
label.place(x=180, y=300)
label = ttk.Label(crewbattle, text="P8")
label.place(x=180, y=325)
label = ttk.Label(crewbattle, text="P9")
label.place(x=180, y=350)
label = ttk.Label(crewbattle, text="NO SELECT")
label.place(x=35, y=375)
label = ttk.Label(crewbattle, text="NO SELECT")
label.place(x=280, y=375)

# ウィジェット
cb_upperleft = ttk.Entry(crewbattle, width=20)
# cb_upperleft.insert(tk.END,"CREW BATTLE")
cb_upperleft.place(x=5, y=25)

cb_upperright = ttk.Entry(crewbattle, width=20)
# cb_upperright.insert(tk.END,"クルーバトル")
cb_upperright.place(x=245, y=25)

cb_team1 = ttk.Entry(crewbattle, width=20)
# cb_team1.insert(tk.END,"LEFT TEAM")
cb_team1.place(x=5, y=70)

cb_team2 = ttk.Entry(crewbattle, width=20)
# cb_team2.insert(tk.END,"RIGHT TEAM")
cb_team2.place(x=245, y=70)

cb_team1_score = tk.IntVar()
cb_team1_score.set(0)
s = ttk.Spinbox(crewbattle, textvariable=cb_team1_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=70)

cb_team2_score = tk.IntVar()
cb_team2_score.set(0)
s = ttk.Spinbox(crewbattle, textvariable=cb_team2_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=70)

cb_memberNum = tk.IntVar()
# cb_memberNum.set(9)
s = ttk.Spinbox(crewbattle, textvariable=cb_memberNum, from_=1, to=9, increment=1, width=3)
s.place(x=60, y=105)

cb_autocalcVal = tk.BooleanVar()
cb_autocalcVal.set(True)
c = ttk.Checkbutton(crewbattle, text=u"チーム残ストック自動計算", variable=cb_autocalcVal)
c.place(x=205, y=105)

cb_1_1 = ttk.Entry(crewbattle, width=15)
cb_1_1.place(x=35, y=150)
cb_1_2 = ttk.Entry(crewbattle, width=15)
cb_1_2.place(x=35, y=175)
cb_1_3 = ttk.Entry(crewbattle, width=15)
cb_1_3.place(x=35, y=200)
cb_1_4 = ttk.Entry(crewbattle, width=15)
cb_1_4.place(x=35, y=225)
cb_1_5 = ttk.Entry(crewbattle, width=15)
cb_1_5.place(x=35, y=250)
cb_1_6 = ttk.Entry(crewbattle, width=15)
cb_1_6.place(x=35, y=275)
cb_1_7 = ttk.Entry(crewbattle, width=15)
cb_1_7.place(x=35, y=300)
cb_1_8 = ttk.Entry(crewbattle, width=15)
cb_1_8.place(x=35, y=325)
cb_1_9 = ttk.Entry(crewbattle, width=15)
cb_1_9.place(x=35, y=350)

cb_2_1 = ttk.Entry(crewbattle, width=15)
cb_2_1.place(x=245, y=150)
cb_2_2 = ttk.Entry(crewbattle, width=15)
cb_2_2.place(x=245, y=175)
cb_2_3 = ttk.Entry(crewbattle, width=15)
cb_2_3.place(x=245, y=200)
cb_2_4 = ttk.Entry(crewbattle, width=15)
cb_2_4.place(x=245, y=225)
cb_2_5 = ttk.Entry(crewbattle, width=15)
cb_2_5.place(x=245, y=250)
cb_2_6 = ttk.Entry(crewbattle, width=15)
cb_2_6.place(x=245, y=275)
cb_2_7 = ttk.Entry(crewbattle, width=15)
cb_2_7.place(x=245, y=300)
cb_2_8 = ttk.Entry(crewbattle, width=15)
cb_2_8.place(x=245, y=325)
cb_2_9 = ttk.Entry(crewbattle, width=15)
cb_2_9.place(x=245, y=350)

cb_1_1_score = tk.IntVar()
cb_1_2_score = tk.IntVar()
cb_1_3_score = tk.IntVar()
cb_1_4_score = tk.IntVar()
cb_1_5_score = tk.IntVar()
cb_1_6_score = tk.IntVar()
cb_1_7_score = tk.IntVar()
cb_1_8_score = tk.IntVar()
cb_1_9_score = tk.IntVar()
cb_2_1_score = tk.IntVar()
cb_2_2_score = tk.IntVar()
cb_2_3_score = tk.IntVar()
cb_2_4_score = tk.IntVar()
cb_2_5_score = tk.IntVar()
cb_2_6_score = tk.IntVar()
cb_2_7_score = tk.IntVar()
cb_2_8_score = tk.IntVar()
cb_2_9_score = tk.IntVar()

cb_1_1_score.set(3)
cb_1_2_score.set(3)
cb_1_3_score.set(3)
cb_1_4_score.set(3)
cb_1_5_score.set(3)
cb_1_6_score.set(3)
cb_1_7_score.set(3)
cb_1_8_score.set(3)
cb_1_9_score.set(3)
cb_2_1_score.set(3)
cb_2_2_score.set(3)
cb_2_3_score.set(3)
cb_2_4_score.set(3)
cb_2_5_score.set(3)
cb_2_6_score.set(3)
cb_2_7_score.set(3)
cb_2_8_score.set(3)
cb_2_9_score.set(3)

s = ttk.Spinbox(crewbattle, textvariable=cb_1_1_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=150)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_2_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=175)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_3_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=200)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_4_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=225)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_5_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=250)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_6_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=275)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_7_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=300)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_8_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=325)
s = ttk.Spinbox(crewbattle, textvariable=cb_1_9_score, from_=0, to=99, increment=1, width=3)
s.place(x=135, y=350)

s = ttk.Spinbox(crewbattle, textvariable=cb_2_1_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=150)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_2_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=175)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_3_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=200)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_4_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=225)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_5_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=250)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_6_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=275)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_7_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=300)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_8_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=325)
s = ttk.Spinbox(crewbattle, textvariable=cb_2_9_score, from_=0, to=99, increment=1, width=3)
s.place(x=205, y=350)

cb_member_text = ['1','2','3','4','5','6','7','8','9','0']
Lmember_var = tk.IntVar()
Lmember_var.set(9)
Rmember_var = tk.IntVar()
Rmember_var.set(9)
for i in range(len(cb_member_text)):
    member = ttk.Radiobutton(crewbattle, value=i, variable=Lmember_var)
    member.place(x=10, y=150 + (i *25))
    member = ttk.Radiobutton(crewbattle, value=i, variable=Rmember_var)
    member.place(x=350, y=150 + (i *25))

for i in range(45):
    label = ttk.Label(crewbattle, text="|")
    label.place(x=390, y=0 + (i *10))

label = ttk.Label(crewbattle, text="事前入力データ読込")
label.place(x=400, y=80)
label = ttk.Label(crewbattle, text="LEFT TEAM")
label.place(x=400, y=105)
option_team= ('TEAM1', 'TEAM2', 'TEAM3', 'TEAM4')
selectLteam_variable = tk.StringVar()
combo_selectLteam = ttk.Combobox(crewbattle, values=option_team, textvariable=selectLteam_variable, state="readonly", width=7)
combo_selectLteam.set(option_team[0])
combo_selectLteam.place(x=400, y=125)
Button_cb_SetLMember = ttk.Button(crewbattle, text=u'SetLMember')
Button_cb_SetLMember.bind("<Button-1>",cbSetLMember) 
Button_cb_SetLMember.place(x=400, y=150)

label = ttk.Label(crewbattle, text="RIGHT TEAM")
label.place(x=400, y=185)
selectRteam_variable = tk.StringVar()
combo_selectRteam = ttk.Combobox(crewbattle, values=option_team, textvariable=selectRteam_variable, state="readonly", width=7)
combo_selectRteam.set(option_team[0])
combo_selectRteam.place(x=400, y=205)
Button_cb_SetRMember = ttk.Button(crewbattle, text=u'SetRMember')
Button_cb_SetRMember.bind("<Button-1>",cbSetRMember) 
Button_cb_SetRMember.place(x=400, y=230)

label = ttk.Label(crewbattle, text="メンバー名をクリア")
label.place(x=400, y=265)
Button_cb_AllClear = ttk.Button(crewbattle, text=u'Clear')
Button_cb_AllClear.bind("<Button-1>",cbClearAllName) 
Button_cb_AllClear.place(x=400, y=285)

label = ttk.Label(crewbattle, text="スコアをセット")
label.place(x=400, y=320)
Button_cb_SetScore = ttk.Button(crewbattle, text=u'Set', width=7)
Button_cb_SetScore.bind("<Button-1>",cbSetAllScore) 
Button_cb_SetScore.place(x=400, y=340)
cb_setScore = tk.IntVar()
cb_setScore.set(3)
s = ttk.Spinbox(crewbattle, textvariable=cb_setScore, from_=0, to=99, increment=1, width=3)
s.place(x=455, y=343)

Button_cb_swap = ttk.Button(crewbattle, text=u'⇐ Swap ⇒', width=17)
Button_cb_swap.bind("<Button-1>",cbSwap) 
Button_cb_swap.place(x=135, y=380)

# ------------- 事前入力 -------------
label = ttk.Label(inadvance, text="■クルーバトルメンバー事前入力")
label.place(x=5, y=5)

label = ttk.Label(inadvance, text="TEAM1")
label.place(x=5, y=55)
label = ttk.Label(inadvance, text="TEAM2")
label.place(x=120, y=55)
label = ttk.Label(inadvance, text="TEAM3")
label.place(x=235, y=55)
label = ttk.Label(inadvance, text="TEAM4")
label.place(x=350, y=55)

inad_1 = []
inad_2 = []
inad_3 = []
inad_4 = []

for i in range(9):
    inad_1.append(ttk.Entry(inadvance, width=15))
    inad_2.append(ttk.Entry(inadvance, width=15))
    inad_3.append(ttk.Entry(inadvance, width=15))
    inad_4.append(ttk.Entry(inadvance, width=15))
    inad_1[i].place(x=5, y=75 + (i * 25))
    inad_2[i].place(x=120, y=75 + (i * 25))
    inad_3[i].place(x=235, y=75 + (i * 25))
    inad_4[i].place(x=350, y=75 + (i * 25))

Button_inad1Clear = ttk.Button(inadvance, text=u'Clear', width=14)
Button_inad1Clear.bind("<Button-1>",inad1Clear) 
Button_inad1Clear.place(x=5, y=310)

Button_inad2Clear = ttk.Button(inadvance, text=u'Clear', width=14)
Button_inad2Clear.bind("<Button-1>",inad2Clear) 
Button_inad2Clear.place(x=120, y=310)

Button_inad3Clear = ttk.Button(inadvance, text=u'Clear', width=14)
Button_inad3Clear.bind("<Button-1>",inad3Clear) 
Button_inad3Clear.place(x=235, y=310)

Button_inad4Clear = ttk.Button(inadvance, text=u'Clear', width=14)
Button_inad4Clear.bind("<Button-1>",inad4Clear) 
Button_inad4Clear.place(x=350, y=310)

# 3人総当たり
label = ttk.Label(roundrobin, text="------------------------------------------------------------------------------------------------")
label.place(x=5, y=50)
label = ttk.Label(roundrobin, text="------------------------------------------------------------------------------------------------")
label.place(x=5, y=90)
label = ttk.Label(roundrobin, text="------------------------------------------------------------------------------------------------")
label.place(x=5, y=130)

for i in range(14):
    label = ttk.Label(roundrobin, text="|")
    label.place(x=110, y=25 + (i *10))
    label = ttk.Label(roundrobin, text="|")
    label.place(x=220, y=25 + (i *10))
    label = ttk.Label(roundrobin, text="|")
    label.place(x=330, y=25 + (i *10))
    label = ttk.Label(roundrobin, text="|")
    label.place(x=440, y=25 + (i *10))


rr_pool = ttk.Entry(roundrobin, width=15)
rr_pool.place(x=10, y=30)
rr_p1 = ttk.Entry(roundrobin, width=15)
rr_p1.place(x=10, y=70)
rr_p2 = ttk.Entry(roundrobin, width=15)
rr_p2.place(x=10, y=110)
rr_p3 = ttk.Entry(roundrobin, width=15)
rr_p3.place(x=10, y=150)

label = ttk.Label(roundrobin, text="1列目の欄を入力・適用すると以下の欄は自動で入力されます")
label.place(x=120, y=0)
label = ttk.Label(roundrobin, text="↓")
label.place(x=160, y=15)
label = ttk.Label(roundrobin, text="↓")
label.place(x=270, y=15)
label = ttk.Label(roundrobin, text="↓")
label.place(x=380, y=15)

label = ttk.Label(roundrobin, text="ー")
label.place(x=163, y=110)
label = ttk.Label(roundrobin, text="ー")
label.place(x=163, y=150)
label = ttk.Label(roundrobin, text="ー")
label.place(x=273, y=70)
label = ttk.Label(roundrobin, text="ー")
label.place(x=273, y=150)
label = ttk.Label(roundrobin, text="ー")
label.place(x=383, y=70)
label = ttk.Label(roundrobin, text="ー")
label.place(x=383, y=110)

rr_p1_h = ttk.Entry(roundrobin, width=15)
rr_p1_h.place(x=120, y=30)
rr_p2_h = ttk.Entry(roundrobin, width=15)
rr_p2_h.place(x=230, y=30)
rr_p3_h = ttk.Entry(roundrobin, width=15)
rr_p3_h.place(x=340, y=30)

label = ttk.Label(roundrobin, text="順位")
label.place(x=450, y=30)

rr_1vs2_1 = tk.IntVar()
rr_1vs2_1.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs2_1, from_=0, to=99, increment=1, width=3)
s.place(x=230, y=70)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs2_1, from_=0, to=99, increment=1, width=3)
s.place(x=180, y=110)

rr_1vs2_2 = tk.IntVar()
rr_1vs2_2.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs2_2, from_=0, to=99, increment=1, width=3)
s.place(x=290, y=70)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs2_2, from_=0, to=99, increment=1, width=3)
s.place(x=120, y=110)

rr_1vs3_1 = tk.IntVar()
rr_1vs3_1.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs3_1, from_=0, to=99, increment=1, width=3)
s.place(x=340, y=70)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs3_1, from_=0, to=99, increment=1, width=3)
s.place(x=180, y=150)

rr_1vs3_3 = tk.IntVar()
rr_1vs3_3.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs3_3, from_=0, to=99, increment=1, width=3)
s.place(x=400, y=70)
s = ttk.Spinbox(roundrobin, textvariable=rr_1vs3_3, from_=0, to=99, increment=1, width=3)
s.place(x=120, y=150)

rr_2vs3_2 = tk.IntVar()
rr_2vs3_2.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_2vs3_2, from_=0, to=99, increment=1, width=3)
s.place(x=340, y=110)
s = ttk.Spinbox(roundrobin, textvariable=rr_2vs3_2, from_=0, to=99, increment=1, width=3)
s.place(x=290, y=150)

rr_2vs3_3 = tk.IntVar()
rr_2vs3_3.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_2vs3_3, from_=0, to=99, increment=1, width=3)
s.place(x=400, y=110)
s = ttk.Spinbox(roundrobin, textvariable=rr_2vs3_3, from_=0, to=99, increment=1, width=3)
s.place(x=230, y=150)

rr_p1_rank = tk.IntVar()
rr_p1_rank.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_p1_rank, from_=0, to=99, increment=1, width=3)
s.place(x=450, y=70)

rr_p2_rank = tk.IntVar()
rr_p2_rank.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_p2_rank, from_=0, to=99, increment=1, width=3)
s.place(x=450, y=110)

rr_p3_rank = tk.IntVar()
rr_p3_rank.set(0)
s = ttk.Spinbox(roundrobin, textvariable=rr_p3_rank, from_=0, to=99, increment=1, width=3)
s.place(x=450, y=150)

label = ttk.Label(roundrobin, text="NAME")
label.place(x=120, y=220)
label = ttk.Label(roundrobin, text="TwitterID")
label.place(x=255, y=220)

label = ttk.Label(roundrobin, text="■ Player1")
label.place(x=10, y=240)

label = ttk.Label(roundrobin, text="■ Player2")
label.place(x=10, y=270)

label = ttk.Label(roundrobin, text="■ Player3")
label.place(x=10, y=300)

rr_pl_p1 = ttk.Entry(roundrobin, width=20)
rr_pl_p1.place(x=80, y=240)
rr_pl_p1_xid = ttk.Entry(roundrobin, width=20)
rr_pl_p1_xid.place(x=220, y=240)

rr_pl_p2 = ttk.Entry(roundrobin, width=20)
rr_pl_p2.place(x=80, y=270)
rr_pl_p2_xid = ttk.Entry(roundrobin, width=20)
rr_pl_p2_xid.place(x=220, y=270)

rr_pl_p3 = ttk.Entry(roundrobin, width=20)
rr_pl_p3.place(x=80, y=300)
rr_pl_p3_xid = ttk.Entry(roundrobin, width=20)
rr_pl_p3_xid.place(x=220, y=300)

Button_rr_clear = ttk.Button(roundrobin, text=u'AllClear', width=14)
Button_rr_clear.bind("<Button-1>",rrClear) 
Button_rr_clear.place(x=10, y=190)

#----------------------------------------------------------------------------------
#
#                           jsonファイルの読み込み処理
#
#----------------------------------------------------------------------------------
jsonfile = "datafile/LatteCon.json"
jsonfile_open = open(jsonfile, "r", encoding="utf-8")
jsonfile_load = json.load(jsonfile_open)
jsonfile_open.close()

# スコアボード
pName1.insert(tk.END, jsonfile_load["pName1"])
pName2.insert(tk.END, jsonfile_load["pName2"])
pTeam1.insert(tk.END, jsonfile_load["pTeam1"])
pTeam2.insert(tk.END, jsonfile_load["pTeam2"])
stage_var.set(stage_text.index(jsonfile_load["stage"]))
stage_typing.insert(tk.END, jsonfile_load["stage_typing"])
bestofN.insert(tk.END, jsonfile_load["bestofN"])
combo_setstory.set(jsonfile_load["boN"].upper())
game1_var.set(game_text.index(jsonfile_load["game1"]))
game2_var.set(game_text.index(jsonfile_load["game2"]))
game3_var.set(game_text.index(jsonfile_load["game3"]))
game4_var.set(game_text.index(jsonfile_load["game4"]))
game5_var.set(game_text.index(jsonfile_load["game5"]))
set_gfwl1 = jsonfile_load["GF-WL1"]
set_gfwl2 = jsonfile_load["GF-WL2"]
if (jsonfile_load["GF-WL1"] == "no"):
    set_gfwl1 = "GF時に使用する項目"
elif (jsonfile_load["GF-WL1"] == "W"):
    set_gfwl1 = "[W]"
else:
    set_gfwl1 = "[L]"

if (jsonfile_load["GF-WL2"] == "no"):
    set_gfwl2 = "GF時に使用する項目"
elif (jsonfile_load["GF-WL2"] == "W"):
    set_gfwl2 = "[W]"
else:
    set_gfwl2 = "[L]"

combo_GF_WL1.set(set_gfwl1)
combo_GF_WL2.set(set_gfwl2)

tournament_name.insert(tk.END, jsonfile_load["tournament_name"])

# MC
mc_name1.insert(tk.END, jsonfile_load["mc_name1"])
mc_name2.insert(tk.END, jsonfile_load["mc_name2"])
mc_xid1.insert(tk.END, jsonfile_load["mc_xid1"])
mc_xid2.insert(tk.END, jsonfile_load["mc_xid2"])

# TOP8
top8_1_1.insert(tk.END, jsonfile_load["top8_1_1"])
top8_1_2.insert(tk.END, jsonfile_load["top8_1_2"])
top8_1_3.insert(tk.END, jsonfile_load["top8_1_3"])
top8_1_4.insert(tk.END, jsonfile_load["top8_1_4"])
top8_1_5.insert(tk.END, jsonfile_load["top8_1_5"])
top8_1_6.insert(tk.END, jsonfile_load["top8_1_6"])
top8_1_7.insert(tk.END, jsonfile_load["top8_1_7"])
top8_1_8.insert(tk.END, jsonfile_load["top8_1_8"])
top8_2_1.insert(tk.END, jsonfile_load["top8_2_1"])
top8_2_2.insert(tk.END, jsonfile_load["top8_2_2"])
top8_2_3.insert(tk.END, jsonfile_load["top8_2_3"])
top8_2_4.insert(tk.END, jsonfile_load["top8_2_4"])
top8_2_5.insert(tk.END, jsonfile_load["top8_2_5"])
top8_2_6.insert(tk.END, jsonfile_load["top8_2_6"])
top8_3_1.insert(tk.END, jsonfile_load["top8_3_1"])
top8_3_2.insert(tk.END, jsonfile_load["top8_3_2"])
top8_3_3.insert(tk.END, jsonfile_load["top8_3_3"])
top8_3_4.insert(tk.END, jsonfile_load["top8_3_4"])
top8_4_3.insert(tk.END, jsonfile_load["top8_4_3"])
top8_4_4.insert(tk.END, jsonfile_load["top8_4_4"])
top8_1_1_score.set(int(jsonfile_load["top8_1_1_score"]))
top8_1_2_score.set(int(jsonfile_load["top8_1_2_score"]))
top8_1_3_score.set(int(jsonfile_load["top8_1_3_score"]))
top8_1_4_score.set(int(jsonfile_load["top8_1_4_score"]))
top8_1_5_score.set(int(jsonfile_load["top8_1_5_score"]))
top8_1_6_score.set(int(jsonfile_load["top8_1_6_score"]))
top8_1_7_score.set(int(jsonfile_load["top8_1_7_score"]))
top8_1_8_score.set(int(jsonfile_load["top8_1_8_score"]))
top8_2_1_score.set(int(jsonfile_load["top8_2_1_score"]))
top8_2_2_score.set(int(jsonfile_load["top8_2_2_score"]))
top8_2_3_score.set(int(jsonfile_load["top8_2_3_score"]))
top8_2_4_score.set(int(jsonfile_load["top8_2_4_score"]))
top8_2_5_score.set(int(jsonfile_load["top8_2_5_score"]))
top8_2_6_score.set(int(jsonfile_load["top8_2_6_score"]))
top8_3_1_score.set(int(jsonfile_load["top8_3_1_score"]))
top8_3_2_score.set(int(jsonfile_load["top8_3_2_score"]))
top8_3_3_score.set(int(jsonfile_load["top8_3_3_score"]))
top8_3_4_score.set(int(jsonfile_load["top8_3_4_score"]))
top8_4_3_score.set(int(jsonfile_load["top8_4_3_score"]))
top8_4_4_score.set(int(jsonfile_load["top8_4_4_score"]))

# クルーバトル
cb_memberNum.set(int(jsonfile_load["cb_memberNum"]))
if (jsonfile_load["cb_autocalc"] == "1"):
    cb_autocalcVal.set(True)
else:
    cb_autocalcVal.set(False)

cb_upperleft.insert(tk.END, jsonfile_load["cb_upperleft"])
cb_upperright.insert(tk.END, jsonfile_load["cb_upperright"])
cb_team1.insert(tk.END, jsonfile_load["cb_team1"])
cb_team2.insert(tk.END, jsonfile_load["cb_team2"])
cb_team1_score.set(int(jsonfile_load["cb_team1_score"]))
cb_team2_score.set(int(jsonfile_load["cb_team2_score"]))
Lmember_var.set(cb_member_text.index(jsonfile_load["select_Lmember"]))
Rmember_var.set(cb_member_text.index(jsonfile_load["select_Rmember"]))
cb_1_1.insert(tk.END, jsonfile_load["cb_1_1"])
cb_1_2.insert(tk.END, jsonfile_load["cb_1_2"])
cb_1_3.insert(tk.END, jsonfile_load["cb_1_3"])
cb_1_4.insert(tk.END, jsonfile_load["cb_1_4"])
cb_1_5.insert(tk.END, jsonfile_load["cb_1_5"])
cb_1_6.insert(tk.END, jsonfile_load["cb_1_6"])
cb_1_7.insert(tk.END, jsonfile_load["cb_1_7"])
cb_1_8.insert(tk.END, jsonfile_load["cb_1_8"])
cb_1_9.insert(tk.END, jsonfile_load["cb_1_9"])
cb_2_1.insert(tk.END, jsonfile_load["cb_2_1"])
cb_2_2.insert(tk.END, jsonfile_load["cb_2_2"])
cb_2_3.insert(tk.END, jsonfile_load["cb_2_3"])
cb_2_4.insert(tk.END, jsonfile_load["cb_2_4"])
cb_2_5.insert(tk.END, jsonfile_load["cb_2_5"])
cb_2_6.insert(tk.END, jsonfile_load["cb_2_6"])
cb_2_7.insert(tk.END, jsonfile_load["cb_2_7"])
cb_2_8.insert(tk.END, jsonfile_load["cb_2_8"])
cb_2_9.insert(tk.END, jsonfile_load["cb_2_9"])
cb_1_1_score.set(int(jsonfile_load["cb_1_1_score"]))
cb_1_2_score.set(int(jsonfile_load["cb_1_2_score"]))
cb_1_3_score.set(int(jsonfile_load["cb_1_3_score"]))
cb_1_4_score.set(int(jsonfile_load["cb_1_4_score"]))
cb_1_5_score.set(int(jsonfile_load["cb_1_5_score"]))
cb_1_6_score.set(int(jsonfile_load["cb_1_6_score"]))
cb_1_7_score.set(int(jsonfile_load["cb_1_7_score"]))
cb_1_8_score.set(int(jsonfile_load["cb_1_8_score"]))
cb_1_9_score.set(int(jsonfile_load["cb_1_9_score"]))
cb_2_1_score.set(int(jsonfile_load["cb_2_1_score"]))
cb_2_2_score.set(int(jsonfile_load["cb_2_2_score"]))
cb_2_3_score.set(int(jsonfile_load["cb_2_3_score"]))
cb_2_4_score.set(int(jsonfile_load["cb_2_4_score"]))
cb_2_5_score.set(int(jsonfile_load["cb_2_5_score"]))
cb_2_6_score.set(int(jsonfile_load["cb_2_6_score"]))
cb_2_7_score.set(int(jsonfile_load["cb_2_7_score"]))
cb_2_8_score.set(int(jsonfile_load["cb_2_8_score"]))
cb_2_9_score.set(int(jsonfile_load["cb_2_9_score"]))

# 事前入力
for i in range(9):
    inad_1[i].insert(tk.END, jsonfile_load["inad_1_" + str(i+1)])
    inad_2[i].insert(tk.END, jsonfile_load["inad_2_" + str(i+1)])
    inad_3[i].insert(tk.END, jsonfile_load["inad_3_" + str(i+1)])
    inad_4[i].insert(tk.END, jsonfile_load["inad_4_" + str(i+1)])

# 3人総当たり
rr_pool.insert(tk.END, jsonfile_load["rr_pool"])
rr_p1.insert(tk.END, jsonfile_load["rr_p1"])
rr_p2.insert(tk.END, jsonfile_load["rr_p2"])
rr_p3.insert(tk.END, jsonfile_load["rr_p3"])
rr_p1_h.insert(tk.END, jsonfile_load["rr_p1"])
rr_p2_h.insert(tk.END, jsonfile_load["rr_p2"])
rr_p3_h.insert(tk.END, jsonfile_load["rr_p3"])
rr_1vs2_1.set(int(jsonfile_load["rr_1vs2_1"]))
rr_1vs2_2.set(int(jsonfile_load["rr_1vs2_2"]))
rr_1vs3_1.set(int(jsonfile_load["rr_1vs3_1"]))
rr_1vs3_3.set(int(jsonfile_load["rr_1vs3_3"]))
rr_2vs3_2.set(int(jsonfile_load["rr_2vs3_2"]))
rr_2vs3_3.set(int(jsonfile_load["rr_2vs3_3"]))
rr_pl_p1.insert(tk.END, jsonfile_load["rr_pl_p1"])
rr_pl_p2.insert(tk.END, jsonfile_load["rr_pl_p2"])
rr_pl_p3.insert(tk.END, jsonfile_load["rr_pl_p3"])
rr_pl_p1_xid.insert(tk.END, jsonfile_load["rr_pl_p1_xid"])
rr_pl_p2_xid.insert(tk.END, jsonfile_load["rr_pl_p2_xid"])
rr_pl_p3_xid.insert(tk.END, jsonfile_load["rr_pl_p3_xid"])
rr_p1_rank.set(int(jsonfile_load["rr_p1_rank"]))
rr_p2_rank.set(int(jsonfile_load["rr_p2_rank"]))
rr_p3_rank.set(int(jsonfile_load["rr_p3_rank"]))

root.mainloop()