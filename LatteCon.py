# インポート
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import json
import time
import math
import requests
import os
import shutil
import re

# rootメインウィンドウの設定
root = tk.Tk()
root.title("LatteCon")
root.geometry("530x500")

timestamp = math.floor(time.time())


#region 入力データをJSONに保存する関数
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
        # スコアボードタブ
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
        # 戦績タブ
        'st_pName1': st_pName1.get(),
        'st_pName2': st_pName2.get(),
        'st_p1_0_tournament_name': st_p1PlacementsInfo[0][0].get(),
        'st_p1_0_entrants': st_p1PlacementsInfo[0][1].get(),
        'st_p1_0_placement': st_p1PlacementsInfo[0][2].get(),
        'st_p1_1_tournament_name': st_p1PlacementsInfo[1][0].get(),
        'st_p1_1_entrants': st_p1PlacementsInfo[1][1].get(),
        'st_p1_1_placement': st_p1PlacementsInfo[1][2].get(),
        'st_p1_2_tournament_name': st_p1PlacementsInfo[2][0].get(),
        'st_p1_2_entrants': st_p1PlacementsInfo[2][1].get(),
        'st_p1_2_placement': st_p1PlacementsInfo[2][2].get(),
        'st_p1_3_tournament_name': st_p1PlacementsInfo[3][0].get(),
        'st_p1_3_entrants': st_p1PlacementsInfo[3][1].get(),
        'st_p1_3_placement': st_p1PlacementsInfo[3][2].get(),
        'st_p1_4_tournament_name': st_p1PlacementsInfo[4][0].get(),
        'st_p1_4_entrants': st_p1PlacementsInfo[4][1].get(),
        'st_p1_4_placement': st_p1PlacementsInfo[4][2].get(),
        'st_p2_0_tournament_name': st_p2PlacementsInfo[0][0].get(),
        'st_p2_0_entrants': st_p2PlacementsInfo[0][1].get(),
        'st_p2_0_placement': st_p2PlacementsInfo[0][2].get(),
        'st_p2_1_tournament_name': st_p2PlacementsInfo[1][0].get(),
        'st_p2_1_entrants': st_p2PlacementsInfo[1][1].get(),
        'st_p2_1_placement': st_p2PlacementsInfo[1][2].get(),
        'st_p2_2_tournament_name': st_p2PlacementsInfo[2][0].get(),
        'st_p2_2_entrants': st_p2PlacementsInfo[2][1].get(),
        'st_p2_2_placement': st_p2PlacementsInfo[2][2].get(),
        'st_p2_3_tournament_name': st_p2PlacementsInfo[3][0].get(),
        'st_p2_3_entrants': st_p2PlacementsInfo[3][1].get(),
        'st_p2_3_placement': st_p2PlacementsInfo[3][2].get(),
        'st_p2_4_tournament_name': st_p2PlacementsInfo[4][0].get(),
        'st_p2_4_entrants': st_p2PlacementsInfo[4][1].get(),
        'st_p2_4_placement': st_p2PlacementsInfo[4][2].get(),
        # MCタブ
        'mc_name1': mc_name1.get(),
        'mc_name2': mc_name2.get(),
        'mc_xid1': mc_xid1.get(),
        'mc_xid2': mc_xid2.get(),
        # TOP8タブ
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
        # クルーバトルタブ
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
        # 事前入力タブ
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
        # 3人総当たりタブ
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

#endregion

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

# (戦績出力タブ)大会ID取得用モーダレスを表示する関数
def createGetTournamentIDModeless(event):
    getTournamentID_modeless = tk.Toplevel()
    getTournamentID_modeless.title("大会ID取得") # ウィンドウタイトル
    getTournamentID_modeless.geometry("520x200") # ウィンドウサイズ(幅x高さ)

    modeless_label_1 = ttk.Label(getTournamentID_modeless, text="大会IDはstart.ggのURLから取得できます。")
    modeless_label_1.place(x=10, y=15)
    modeless_label_2 = ttk.Label(getTournamentID_modeless, text="例：「https://www.start.gg/tournament/10-kagaribi-10/events」なら「10-kagaribi-10」が大会ID")
    modeless_label_2.place(x=10, y=35)
    modeless_label_3 = ttk.Label(getTournamentID_modeless, text="以下の機能を使うことで、start.ggのURLから大会IDを取得することが可能です。")
    modeless_label_3.place(x=10, y=70)

    modeless_label_url = ttk.Label(getTournamentID_modeless, text="大会URL")
    modeless_label_url.place(x=10, y=100)
    modeless_textbox_url = ttk.Entry(getTournamentID_modeless, width=38)
    modeless_textbox_url.place(x=60, y=100)

    modeless_button_GetTournamentID = ttk.Button(getTournamentID_modeless, text=u'URLから大会IDを取得', width=20)
    modeless_button_GetTournamentID.place(x=300, y=97)

    modeless_label_id = ttk.Label(getTournamentID_modeless, text="大会ID")
    modeless_label_id.place(x=10, y=145)
    modeless_textbox_id = ttk.Entry(getTournamentID_modeless, width=38)
    modeless_textbox_id.place(x=60, y=145)

    modeless_button_SetTournamentID = ttk.Button(getTournamentID_modeless, text=u'大会IDをセット', width=20)
    modeless_button_SetTournamentID.place(x=300, y=142)

    # (大会ID取得用モーダレス)URLから大会IDを取得する関数
    def getTournamentIDfromURL(event):
        url = modeless_textbox_url.get()
        if url == "":
            messagebox.showerror("エラー", "URLを入力してください。")
            return
        
        pattern = r"^https://www\.start\.gg/tournament/([^/]+)"
        m = re.match(pattern, url)
        if m:
            result = m.group(1)
            modeless_textbox_id.delete(0, tk.END)
            modeless_textbox_id.insert(tk.END, result)
        else:
            messagebox.showerror("エラー", "入力されたURLが正しい形式ではありません。")

    # (大会ID取得用モーダレス)大会IDをセットする関数
    def setTournamentID(event):
        if modeless_textbox_id.get() == "":
            messagebox.showerror("エラー", "大会IDが入力されていません。")
            return
        
        api_tournamentID.delete(0, tk.END)
        api_tournamentID.insert(tk.END, modeless_textbox_id.get())
        messagebox.showinfo("確認", "大会IDをセットしました。")
    
    modeless_button_GetTournamentID.bind("<Button-1>", getTournamentIDfromURL)
    modeless_button_SetTournamentID.bind("<Button-1>", setTournamentID)

# (戦績出力タブ)大会IDからイベントIDを取得する関数
def apiGetEventID(event):
    # トークンが未入力の場合はエラー
    if api_token.get() == "":
        messagebox.showerror("エラー", "①start.ggトークンを入力してください。")
        return
    # 大会IDが未入力の場合はエラー
    if api_tournamentID.get() == "":
        messagebox.showerror("エラー", "②大会IDを入力してください。")
        return

    url = "https://api.start.gg/gql/alpha"
    headers = {
        "Authorization": "Bearer " + api_token.get(),
        "Content-Type": "application/json"
    }

    query = """
    query GetTournamentEvents($slug: String!) {
    tournament(slug: $slug) {
        id
        name
        events {
        id
        name
        }
    }
    }
    """
    variables = {"slug": api_tournamentID.get()}  # 大会のIDを入力
    response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
    # APIレスポンスを整形
    data = response.json()
    events = data.get("data", {}).get("tournament", {}).get("events", [])
    # 確認用に大会名も取得しておく
    tournament_name = data.get("data", {}).get("tournament", {}).get("name")
    if events:
        # 正常にresponseが得られた場合のみAPIトークンをjsonに保存
        token_json = {
            "token": api_token.get()
        }
        with open("datafile/token.json", "w", encoding="utf-8") as f:
            json.dump(token_json, f, ensure_ascii=False, indent=4)
        
        eventsInfo = []
        events_json = []
        for event in events:
            eventID = str(event.get("id")) + "/" + event.get("name")
            eventsInfo.append(eventID)
            events_json.append({
                "event_name": event.get("name"),
                "event_id": str(event.get("id"))
            })
        
        api_eventID["values"] = eventsInfo
        api_eventID.set("")
        messagebox.showinfo("確認", "正常にイベントIDを取得しました。")

        # 作成するディレクトリのパスを指定
        dir_path = "./datafile/" + api_tournamentID.get()
        # ディレクトリが存在するか確認
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        # 大会情報をjsonに記録
        with open("datafile/tournaments.json", "r", encoding="utf-8") as f:
            tournaments_json = json.load(f)
        
        tournament_exists_fg = False
        for tournament in tournaments_json:
            if tournament.get("tournament_id") == api_tournamentID.get():
                tournament_exists_fg = True
                break
        
        if not tournament_exists_fg:
            tournaments_json.append({
                "tournament_name": tournament_name,
                "tournament_id": api_tournamentID.get(),
                "events": events_json
            })
            with open("datafile/tournaments.json", "w", encoding="utf-8") as f:
                json.dump(tournaments_json, f, ensure_ascii=False, indent=4)
            # 戦績タブの大会コンボボックスを更新
            current_tournamentInfoCombo = list(st_tournamentInfo["values"])
            tournamentInfo = tournament_name + "/" + api_tournamentID.get()
            current_tournamentInfoCombo.append(tournamentInfo)
            st_tournamentInfo["values"] = current_tournamentInfoCombo
    
# (戦績出力タブ)イベントIDからイベント参加者一覧を取得する関数
def apiGetEntrants(event):
    # トークンが未入力の場合はエラー
    if api_token.get() == "":
        messagebox.showerror("エラー", "①start.ggトークンを入力してください。")
        return
    # 大会を選択してない場合はエラー
    if api_eventID.get() == "":
        messagebox.showerror("エラー", "①から大会を選択してください。")
        return

    url = "https://api.start.gg/gql/alpha"
    headers = {
        "Authorization": "Bearer " + api_token.get(),
        "Content-Type": "application/json"
    }

    query = """
    query GetEventEntrants($eventId: ID!, $page: Int!) {
    event(id: $eventId) {
        id
        name
        entrants(query: {page: $page, perPage: 512}) {
        pageInfo {
            totalPages
        }
        nodes {
            name
            participants {
            gamerTag
            user {
                player {
                    id
                }
            }
            }
        }
        }
    }
    }
    """
    event_id = api_eventID.get().split('/')[0]
    variables = {"eventId": event_id, "page": 1}
    response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
    # APIレスポンスを整形
    data = response.json()
    players = data.get("data", {}).get("event", {}).get("entrants", {}).get("nodes", [])
    if players:
        listbox_entrants.delete(0, tk.END)
        listbox_done_entrants.delete(0, tk.END)
        for player in players:
            name = player.get("participants", [])[0].get("gamerTag")
            player_id = player.get("participants", [])[0].get("user", {}).get("player", {}).get("id")
            listbox_entrants.insert(tk.END, name + "-" + str(player_id))

# (戦績出力タブ)参加者一覧リストボックスの選択上限チェック
def apiListboxSelected(event):
    max_selection = 10
    selected_players_index = listbox_entrants.curselection()
    if len(selected_players_index) > max_selection:
        messagebox.showerror("エラー", "10人以上の選択はできません。")
        # 最後に選んだ要素を解除
        listbox_entrants.selection_clear(selected_players_index[-1])

# (戦績出力タブ)選択したプレイヤーの大会戦績を取得する関数
def apiGetPlacements(event):
    # トークンが未入力の場合はエラー
    if api_token.get() == "":
        messagebox.showerror("エラー", "①start.ggトークンを入力してください。")
        return
    
    selected_players_index = listbox_entrants.curselection()

    if len(selected_players_index) == 0:
        messagebox.showerror("エラー", "⑥参加者一覧から戦績を出力したい人を選択してください。")
        return

    url = "https://api.start.gg/gql/alpha"
    headers = {
        "Authorization": "Bearer " + api_token.get(),
        "Content-Type": "application/json"
    }
    query = """
    query PlayerTournamentResults($playerId: ID!) {
        player(id: $playerId) {
            recentStandings(limit: 5) {
                placement
                entrant {
                    name
                    event {
                        name
                        numEntrants
                        tournament {
                            name
                            numAttendees
                        }
                    }
                }
            }
        }
    }
    """
    
    for index in selected_players_index:
        # プレイヤー名にハイフンが入る場合を考慮して配列の一番後ろを取得
        selected_player = listbox_entrants.get(index)
        player_id = selected_player.split('-')[-1]
        player_name = selected_player[0:len(selected_player)-len(player_id)-1].replace('/', '／')
        variables = {"playerId": player_id}
        response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
        # APIレスポンスを整形
        data = response.json()
        standings = data.get("data", {}).get("player", {}).get("recentStandings", [])
        results = []
        if standings:
            for standing in standings:
                tournament_name = standing.get("entrant", {}).get("event", {}).get("tournament", {}).get("name")
                entrants_num = standing.get("entrant", {}).get("event", {}).get("numEntrants")
                placement = standing.get("placement")
                results.append({
                    "tournament_name": tournament_name,
                    "entrants": entrants_num,
                    "placement": placement
                })
            # 戦績をjsonに出力
            with open("datafile/" + api_tournamentID.get() +"/" + player_name + ".json", "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=4)
            listbox_done_entrants.insert(tk.END, selected_player)

# (戦績出力タブ)リストボックスの選択解除
def apiClearSelect(event):
    listbox_entrants.selection_clear(0, tk.END)

# (戦績タブ)大会コンボボックス選択時のイベント
def stChangeTournamentCombo(event):
    tournament_id = st_tournamentInfo.get().split('/')[-1]
    folder_path = "datafile/" + tournament_id

    # 指定した大会のフォルダが存在しない場合は作成する
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    st_listbox_entrants.delete(0, tk.END)
    for file in files:
        file_name = file.split('.')[0]
        st_listbox_entrants.insert(tk.END, file_name)

# (戦績タブ)大会情報削除ボタン押下時
def stRemoveFolder(event):
    # 大会を選択してない場合はエラー
    if st_tournamentInfo.get() == "":
        messagebox.showerror("エラー", "①から大会を選択してください。")
        return

    ret = messagebox.askyesno('確認', 'この大会情報を削除しますか？\nこの大会情報に紐づくプレイヤーの戦績も削除されます。')
    if ret == True:
        tournament_id = st_tournamentInfo.get().split('/')[-1]
        folder_path = "datafile/" + tournament_id
        # フォルダの削除
        shutil.rmtree(folder_path)
        # リストボックスのクリア
        st_listbox_entrants.delete(0, tk.END)

        try:
            with open("datafile/tournaments.json", "r", encoding="utf-8") as f:
                tournaments_json = json.load(f)
            # 戦績タブのコンボボックス用リスト
            tournamentsInfo = []
            # tournaments.json書き換え用リスト
            update_tournaments_json = []
            for tournament in tournaments_json:
                if tournament.get("tournament_id") != tournament_id:
                    tournamentInfo = tournament.get("tournament_name") + "/" + tournament.get("tournament_id")
                    tournamentsInfo.append(tournamentInfo)
                    update_tournaments_json.append(tournament)
            
            st_tournamentInfo["values"] = tournamentsInfo
            # 戦績タブのコンボボックスを何も選んでいない状態にする
            st_tournamentInfo.set("")

            # tournaments.jsonから大会情報を削除
            with open("datafile/tournaments.json", "w", encoding="utf-8") as f:
                json.dump(update_tournaments_json, f, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            tournaments_json = []
            with open("datafile/tournaments.json", "w", encoding="utf-8") as f:
                json.dump(tournaments_json, f, ensure_ascii=False, indent=4)
            messagebox.showerror("エラー", "予期せぬエラーが発生しました。")
            return

# (戦績タブ)両プレイヤーの戦績取得
def stGetPlacements(event):
    # 大会を選択してない場合はエラー
    if st_tournamentInfo.get() == "":
        messagebox.showerror("エラー", "①から大会を選択してください。")
        return
    
    tournament_id = st_tournamentInfo.get().split('/')[-1]

    p1Name = st_pName1.get().replace('/', '／')
    p2Name = st_pName2.get().replace('/', '／')
    p1file_name = "datafile/" + tournament_id + "/" + p1Name + ".json"
    p2file_name = "datafile/" + tournament_id + "/" + p2Name + ".json"

    try:
        with open(p1file_name, "r", encoding="utf-8") as f:
            p1Placements = json.load(f)
        with open(p2file_name, "r", encoding="utf-8") as f:
            p2Placements = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("エラー", "このプレイヤーは戦績が出力されていません。\n戦績出力タブから戦績を出力してください。")
        return

    for i in range(5):
        for j in range(3):
            st_p1PlacementsInfo[i][j].delete(0, tk.END)
            st_p2PlacementsInfo[i][j].delete(0, tk.END)
    
    for i in range(len(p1Placements)):
        st_p1PlacementsInfo[i][0].insert(tk.END, p1Placements[i].get("tournament_name"))
        st_p1PlacementsInfo[i][1].insert(tk.END, p1Placements[i].get("entrants"))
        st_p1PlacementsInfo[i][2].insert(tk.END, p1Placements[i].get("placement"))
    
    for i in range(len(p2Placements)):
        st_p2PlacementsInfo[i][0].insert(tk.END, p2Placements[i].get("tournament_name"))
        st_p2PlacementsInfo[i][1].insert(tk.END, p2Placements[i].get("entrants"))
        st_p2PlacementsInfo[i][2].insert(tk.END, p2Placements[i].get("placement"))

# (戦績タブ)プレイヤー1の戦績取得ボタン押下時
def stGetP1Placements(event):
    # 大会を選択してない場合はエラー
    if st_tournamentInfo.get() == "":
        messagebox.showerror("エラー", "①から大会を選択してください。")
        return
    # プレイヤー名が未入力の場合はエラー
    if st_pName1.get() == "":
        messagebox.showerror("エラー", "プレイヤー名が未入力です。")
        return
    
    tournament_id = st_tournamentInfo.get().split('/')[-1]

    p1Name = st_pName1.get().replace('/', '／')
    p1file_name = "datafile/" + tournament_id + "/" + p1Name + ".json"

    try:
        with open(p1file_name, "r", encoding="utf-8") as f:
            p1Placements = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("エラー", "このプレイヤーは戦績が出力されていません。\n戦績出力タブから戦績を出力してください。")
        return
    
    for i in range(5):
        for j in range(3):
            st_p1PlacementsInfo[i][j].delete(0, tk.END)
    
    for i in range(len(p1Placements)):
        st_p1PlacementsInfo[i][0].insert(tk.END, p1Placements[i].get("tournament_name"))
        st_p1PlacementsInfo[i][1].insert(tk.END, p1Placements[i].get("entrants"))
        st_p1PlacementsInfo[i][2].insert(tk.END, p1Placements[i].get("placement"))

# (戦績タブ)プレイヤー2の戦績取得ボタン押下時
def stGetP2Placements(event):
    # 大会を選択してない場合はエラー
    if st_tournamentInfo.get() == "":
        messagebox.showerror("エラー", "①から大会を選択してください。")
        return
    # プレイヤー名が未入力の場合はエラー
    if st_pName2.get() == "":
        messagebox.showerror("エラー", "プレイヤー名が未入力です。")
        return
    
    tournament_id = st_tournamentInfo.get().split('/')[-1]

    p2Name = st_pName2.get().replace('/', '／')
    p2file_name = "datafile/" + tournament_id + "/" + p2Name + ".json"

    try:
        with open(p2file_name, "r", encoding="utf-8") as f:
            p2Placements = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("エラー", "このプレイヤーは戦績が出力されていません。\n戦績出力タブから戦績を出力してください。")
        return
    
    for i in range(5):
        for j in range(3):
            st_p2PlacementsInfo[i][j].delete(0, tk.END)
    
    for i in range(len(p2Placements)):
        st_p2PlacementsInfo[i][0].insert(tk.END, p2Placements[i].get("tournament_name"))
        st_p2PlacementsInfo[i][1].insert(tk.END, p2Placements[i].get("entrants"))
        st_p2PlacementsInfo[i][2].insert(tk.END, p2Placements[i].get("placement"))

# (戦績タブ)リストボックスで選択したプレイヤー名をP1にセットする関数
def stSetP1Name(event):
    if len(st_listbox_entrants.curselection()) == 0:
        messagebox.showerror("エラー", "②からプレイヤーを選択してください。")
        return
    
    st_pName1.delete(0, tk.END)
    st_pName1.insert(tk.END, st_listbox_entrants.get(st_listbox_entrants.curselection()[0]))
    for i in range(5):
        for j in range(3):
            st_p1PlacementsInfo[i][j].delete(0, tk.END)
    
    if st_autoSetVal.get() == True:
        stGetP1Placements(None)

# (戦績タブ)リストボックスで選択したプレイヤー名をP2にセットする関数
def stSetP2Name(event):
    if len(st_listbox_entrants.curselection()) == 0:
        messagebox.showerror("エラー", "②からプレイヤーを選択してください。")
        return
    
    st_pName2.delete(0, tk.END)
    st_pName2.insert(tk.END, st_listbox_entrants.get(st_listbox_entrants.curselection()[0]))
    for i in range(5):
        for j in range(3):
            st_p2PlacementsInfo[i][j].delete(0, tk.END)
    
    if st_autoSetVal.get() == True:
        stGetP2Placements(None)

# (戦績タブ)スコアボードに入力されているプレイヤー名をセットする関数
def stSetNamesFromScoreBoard(event):
    if pName1.get() == "" or pName2.get() == "":
        messagebox.showerror("エラー", "スコアボードにプレイヤー名が入力されていません。")
        return

    st_pName1.delete(0, tk.END)
    st_pName1.insert(tk.END, pName1.get())
    st_pName2.delete(0, tk.END)
    st_pName2.insert(tk.END, pName2.get())
    for i in range(5):
        for j in range(3):
            st_p1PlacementsInfo[i][j].delete(0, tk.END)
            st_p2PlacementsInfo[i][j].delete(0, tk.END)
    
    if st_autoSetVal.get() == True:
        stGetPlacements(None)

# (戦績タブ)戦績タブの左右データを入れ替える関数
def stSwap(event):
    swapVal = st_pName1.get()
    st_pName1.delete(0, tk.END)
    st_pName1.insert(tk.END, st_pName2.get())
    st_pName2.delete(0, tk.END)
    st_pName2.insert(tk.END, swapVal)

    for i in range(5):
        for j in range(3):
            swapVal = st_p1PlacementsInfo[i][j].get()
            st_p1PlacementsInfo[i][j].delete(0, tk.END)
            st_p1PlacementsInfo[i][j].insert(tk.END, st_p2PlacementsInfo[i][j].get())
            st_p2PlacementsInfo[i][j].delete(0, tk.END)
            st_p2PlacementsInfo[i][j].insert(tk.END, swapVal)

# (戦績タブ)戦績データをクリアする関数
def stClear(event):
    st_pName1.delete(0, tk.END)
    st_pName2.delete(0, tk.END)

    for i in range(5):
        for j in range(3):
            st_p1PlacementsInfo[i][j].delete(0, tk.END)
            st_p2PlacementsInfo[i][j].delete(0, tk.END)

# LatteCon.exeを最前面に固定する関数
def alwaysOnTop():
    root.attributes("-topmost", always_top_value.get())

# 左プレイヤーのスコアをプラス1する関数
def incrementLeftScore(event):
    if (game1_var.get() == 1):
        game1_var.set(0)
    elif (game2_var.get() == 1):
        game2_var.set(0)
    elif (game3_var.get() == 1):
        game3_var.set(0)
    elif (game4_var.get() == 1):
        game4_var.set(0)
    elif (game5_var.get() == 1):
        game5_var.set(0)
    
    SetJSON(None)

# 右プレイヤーのスコアをプラス1する関数
def incrementRightScore(event):
    if (game1_var.get() == 1):
        game1_var.set(2)
    elif (game2_var.get() == 1):
        game2_var.set(2)
    elif (game3_var.get() == 1):
        game3_var.set(2)
    elif (game4_var.get() == 1):
        game4_var.set(2)
    elif (game5_var.get() == 1):
        game5_var.set(2)
    
    SetJSON(None)

# ショートカットキー情報モーダレスを表示する関数
def createShortCutInfoKeyModeless():
    shortcut_modeless = tk.Toplevel()
    shortcut_modeless.title("ショートカットキー情報") # ウィンドウタイトル
    shortcut_modeless.geometry("300x200") # ウィンドウサイズ(幅x高さ)
    label_ctrlS = ttk.Label(shortcut_modeless, text="・Ctrl + S → 更新")
    label_ctrlS.place(x=10, y=15)
    label_ctrlL = ttk.Label(shortcut_modeless, text="・Ctrl + L → 左プレイヤーのスコアをプラス１後に更新")
    label_ctrlL.place(x=10, y=30)
    label_ctrlR = ttk.Label(shortcut_modeless, text="・Ctrl + R → 右プレイヤーのスコアをプラス１後に更新")
    label_ctrlR.place(x=10, y=45)

# ショートカットキーの設定
# Ctrl + S → スコアボードの更新
root.bind("<Control-s>", SetJSON)
root.bind("<Control-S>", SetJSON)

# Ctrl + L → 左プレイヤーのスコアをプラス1
root.bind("<Control-l>", incrementLeftScore)
root.bind("<Control-L>", incrementLeftScore)

# Ctrl + R → 右プレイヤーのスコアをプラス1
root.bind("<Control-r>", incrementRightScore)
root.bind("<Control-R>", incrementRightScore)

#region スコアボードの設定

# メニューバーの作成
menubar = tk.Menu(root)
root.config(menu=menubar)
# 設定メニューの作成
config_menu = tk.Menu(menubar, tearoff=False)
always_top_value = tk.BooleanVar()
config_menu.add_checkbutton(label = "常に最前面に表示する", variable=always_top_value, command=alwaysOnTop)
menubar.add_cascade(label="設定", menu=config_menu)
# ヘルプメニューの作成
help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(label = "ショートカットキー情報", command = createShortCutInfoKeyModeless)
menubar.add_cascade(label="ヘルプ", menu=help_menu)

# Notebookウィジェットの作成
notebook = ttk.Notebook(root)

# タブの作成
scoreboard = tk.Frame(notebook)
standing = tk.Frame(notebook)
api = tk.Frame(notebook)
mc = tk.Frame(notebook)
TOP8 = tk.Frame(notebook)
crewbattle = tk.Frame(notebook)
inadvance = tk.Frame(notebook)
roundrobin = tk.Frame(notebook)

# notebookにタブを追加
notebook.add(scoreboard, text="スコアボード")
notebook.add(standing, text="戦績")
notebook.add(api, text="戦績出力")
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

#region スコアボードタブ
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

#endregion

#region 戦績タブ

# イベントIDコンボボックス
st_label_eventID = ttk.Label(standing, text="①大会選択")
st_label_eventID.place(x=5, y=5)
st_tournamentInfo = ttk.Combobox(standing, state="readonly", width=40)
st_tournamentInfo.place(x=5, y=25)
st_tournamentInfo.bind("<<ComboboxSelected>>", stChangeTournamentCombo)

# 大会フォルダ削除ボタン
Button_st_removeFolder = ttk.Button(standing, text=u'削除', width=5)
Button_st_removeFolder.bind("<Button-1>",stRemoveFolder)
Button_st_removeFolder.place(x=280, y=23)

# 参加者一覧リストボックス
st_label_entrants = ttk.Label(standing, text="②戦績出力済プレイヤー")
st_label_entrants.place(x=5, y=55)
st_listbox_entrants = tk.Listbox(standing, width=20, height=21)
st_listbox_entrants.place(x=5, y=75)

st_label_entrants = ttk.Label(standing, text="③プレイヤー名, 戦績のセット")
st_label_entrants.place(x=150, y=55)

# 各種プレイヤー名セットボタン
Button_st_SetP1Name = ttk.Button(standing, text=u'選択したプレイヤー名をP1にセット', width=26)
Button_st_SetP1Name.bind("<Button-1>",stSetP1Name)
Button_st_SetP1Name.place(x=150, y=75)

Button_st_SetP2Name = ttk.Button(standing, text=u'選択したプレイヤー名をP2にセット', width=26)
Button_st_SetP2Name.bind("<Button-1>",stSetP2Name)
Button_st_SetP2Name.place(x=335, y=75)

Button_st_SetNameFromScoreBoard = ttk.Button(standing, text=u'スコアボードからプレイヤー名をセット', width=57)
Button_st_SetNameFromScoreBoard.bind("<Button-1>",stSetNamesFromScoreBoard)
Button_st_SetNameFromScoreBoard.place(x=150, y=105)

# プレイヤー名セット時の戦績自動セットチェックボックス
st_autoSetVal = tk.BooleanVar()
st_autoSetVal.set(True)
st_autoSetCheckbox = ttk.Checkbutton(standing, text=u"プレイヤー名セット時の戦績自動セット", variable=st_autoSetVal)
st_autoSetCheckbox.place(x=150, y=135)

# 左プレイヤー名
st_label_pName1 = ttk.Label(standing, text="P1 Name")
st_label_pName1.place(x=150, y=185)
st_pName1 = ttk.Entry(standing, width=24)
st_pName1.place(x=150, y=205)

# 右プレイヤー名
st_label_pName2 = ttk.Label(standing, text="P2 Name")
st_label_pName2.place(x=350, y=185)
st_pName2 = ttk.Entry(standing, width=24)
st_pName2.place(x=350, y=205)

# プレイヤー名と戦績を入れ替えるボタン
Button_st_swap = ttk.Button(standing, text=u'⇔', width=5)
Button_st_swap.bind("<Button-1>",stSwap)
Button_st_swap.place(x=306, y=202)

# プレイヤー1戦績取得ボタン
Button_st_GetP1Placements = ttk.Button(standing, text=u'戦績取得', width=23)
Button_st_GetP1Placements.bind("<Button-1>",stGetP1Placements)
Button_st_GetP1Placements.place(x=150, y=232)

# 戦績データクリアボタン
Button_st_clear = ttk.Button(standing, text=u'Clear', width=5)
Button_st_clear.bind("<Button-1>",stClear)
Button_st_clear.place(x=306, y=232)

# プレイヤー2戦績取得ボタン
Button_st_GetP2Placements = ttk.Button(standing, text=u'戦績取得', width=24)
Button_st_GetP2Placements.bind("<Button-1>",stGetP2Placements)
Button_st_GetP2Placements.place(x=350, y=232)

# 戦績
st_label_p1tournamentName = ttk.Label(standing, text="大会名")
st_label_p1tournamentName.place(x=150, y=265)
st_label_p1entrants = ttk.Label(standing, text="人数")
st_label_p1entrants.place(x=247, y=265)
st_label_p1placement = ttk.Label(standing, text="順位")
st_label_p1placement.place(x=277, y=265)

st_label_p2tournamentName = ttk.Label(standing, text="大会名")
st_label_p2tournamentName.place(x=350, y=265)
st_label_p2entrants = ttk.Label(standing, text="人数")
st_label_p2entrants.place(x=447, y=265)
st_label_p2placement = ttk.Label(standing, text="順位")
st_label_p2placement.place(x=477, y=265)

st_p1PlacementsInfo = []
st_p2PlacementsInfo = []

st_tournament_width = 15
st_placement_width = 3
st_p1_base_x = 150
st_p1_base_y = 285
st_p2_base_x = 350
st_p2_base_y = 285
for i in range(5):
    st_p1Info = []
    st_p1Info.append(ttk.Entry(standing, width=st_tournament_width))
    st_p1Info.append(ttk.Entry(standing, width=st_placement_width))
    st_p1Info.append(ttk.Entry(standing, width=st_placement_width))

    st_p2Info = []
    st_p2Info.append(ttk.Entry(standing, width=st_tournament_width))
    st_p2Info.append(ttk.Entry(standing, width=st_placement_width))
    st_p2Info.append(ttk.Entry(standing, width=st_placement_width))

    for j in range(3):
        if j == 0:
            st_p1Info[j].place(x=st_p1_base_x, y=st_p1_base_y)
            st_p2Info[j].place(x=st_p2_base_x, y=st_p2_base_y)
        else:
            st_p1Info[j].place(x=st_p1_base_x + 100 + ((j - 1) * 28), y=st_p1_base_y)
            st_p2Info[j].place(x=st_p2_base_x + 100 + ((j - 1) * 28), y=st_p2_base_y)
    
    st_p1_base_y = st_p1_base_y + 30
    st_p2_base_y = st_p2_base_y + 30

    st_p1PlacementsInfo.append(st_p1Info)
    st_p2PlacementsInfo.append(st_p2Info)

#endregion

#region 戦績出力タブ

# トークン入力欄
label_token = ttk.Label(api, text="①start.ggトークン")
label_token.place(x=5, y=5)
api_token = ttk.Entry(api, width=38)
api_token.place(x=5, y=25)

# 大会ID入力欄
label_tournamentID = ttk.Label(api, text="②大会ID")
label_tournamentID.place(x=5, y=55)
api_tournamentID = ttk.Entry(api, width=20)
api_tournamentID.place(x=5, y=75)

# 大会ID取得ボタン
Button_api_GetTournamentID = ttk.Button(api, text=u'大会ID取得', width=15)
Button_api_GetTournamentID.bind("<Button-1>", createGetTournamentIDModeless) 
Button_api_GetTournamentID.place(x=140, y=72)

# イベントID取得ボタン
Button_api_GetEventID = ttk.Button(api, text=u'③イベントID取得', width=15)
Button_api_GetEventID.bind("<Button-1>",apiGetEventID) 
Button_api_GetEventID.place(x=250, y=72)

# イベントIDコンボボックス
label_eventID = ttk.Label(api, text="④イベントID")
label_eventID.place(x=5, y=105)
api_eventID = ttk.Combobox(api, state="readonly", width=35)
api_eventID.place(x=5, y=125)

# 参加者出力ボタン
Button_api_GetEntrants = ttk.Button(api, text=u'⑤参加者出力', width=15)
Button_api_GetEntrants.bind("<Button-1>",apiGetEntrants)
Button_api_GetEntrants.place(x=250, y=122)

# 参加者一覧リストボックス
label_entrants = ttk.Label(api, text="⑥参加者一覧")
label_entrants.place(x=5, y=155)
listbox_entrants = tk.Listbox(api, width=16, height=15, selectmode="multiple")
listbox_entrants.place(x=5, y=175)
listbox_entrants.bind("<<ListboxSelect>>", apiListboxSelected)

# 戦績出力ボタン
Button_api_GetPlacements = ttk.Button(api, text=u'⑦戦績出力', width=18)
Button_api_GetPlacements.bind("<Button-1>",apiGetPlacements)
Button_api_GetPlacements.place(x=118, y=175)
api_label_caution1 = ttk.Label(api, text="一度に10人まで出力可")
api_label_caution1.place(x=118, y=205)

# 選択解除ボタン
Button_api_ClearSelect = ttk.Button(api, text=u'選択解除', width=18)
Button_api_ClearSelect.bind("<Button-1>",apiClearSelect)
Button_api_ClearSelect.place(x=118, y=245)

# 戦績出力済み参加者一覧リストボックス
label_done_entrants = ttk.Label(api, text="⑧戦績出力済み")
label_done_entrants.place(x=250, y=155)
listbox_done_entrants = tk.Listbox(api, width=16, height=15)
listbox_done_entrants.place(x=250, y=175)

# セパレータ
for i in range(45):
    label = ttk.Label(api, text="|")
    label.place(x=360, y=0 + (i *10))

# 手順
api_label_process0 = ttk.Label(api, text="■ 戦績出力手順")
api_label_process0.place(x=365, y=5)
api_label_process1 = ttk.Label(api, text="1. ①を入力")
api_label_process1.place(x=365, y=25)
api_label_process2 = ttk.Label(api, text="2. ②を入力")
api_label_process2.place(x=365, y=45)
api_label_process3 = ttk.Label(api, text="3. ③をクリック")
api_label_process3.place(x=365, y=65)
api_label_process4 = ttk.Label(api, text="4. ④からイベントを選択")
api_label_process4.place(x=365, y=85)
api_label_process5 = ttk.Label(api, text="5. ⑤をクリック")
api_label_process5.place(x=365, y=105)
api_label_process6 = ttk.Label(api, text="6. ⑥から参加者を選択")
api_label_process6.place(x=365, y=125)
api_label_process7 = ttk.Label(api, text="7. ⑦をクリック")
api_label_process7.place(x=365, y=145)

#endregion

#region MCタブ
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

#endregion

#region TOP8 
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

#endregion

#region クルーバトル
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

#endregion

#region 事前入力
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

#endregion

#region 3人総当たりタブ
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

#endregion

#endregion

#region jsonファイルの読み込み処理

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

# 戦績
try:
    with open("datafile/tournaments.json", "r", encoding="utf-8") as f:
        tournaments_json = json.load(f)
    tournamentsInfo = []

    for tournament in tournaments_json:
        tournamentInfo = tournament.get("tournament_name") + "/" + tournament.get("tournament_id")
        tournamentsInfo.append(tournamentInfo)
    st_tournamentInfo["values"] = tournamentsInfo

except FileNotFoundError:
    tournaments_json = []
    with open("datafile/tournaments.json", "w", encoding="utf-8") as f:
        json.dump(tournaments_json, f, ensure_ascii=False, indent=4)

st_pName1.insert(tk.END, jsonfile_load["st_pName1"])
st_pName2.insert(tk.END, jsonfile_load["st_pName2"])

for i in range(5):
    st_p1PlacementsInfo[i][0].insert(tk.END, jsonfile_load["st_p1_" + str(i) + "_tournament_name"])
    st_p1PlacementsInfo[i][1].insert(tk.END, jsonfile_load["st_p1_" + str(i) + "_entrants"])
    st_p1PlacementsInfo[i][2].insert(tk.END, jsonfile_load["st_p1_" + str(i) + "_placement"])
    st_p2PlacementsInfo[i][0].insert(tk.END, jsonfile_load["st_p2_" + str(i) + "_tournament_name"])
    st_p2PlacementsInfo[i][1].insert(tk.END, jsonfile_load["st_p2_" + str(i) + "_entrants"])
    st_p2PlacementsInfo[i][2].insert(tk.END, jsonfile_load["st_p2_" + str(i) + "_placement"])

# 戦績出力
try:
    with open("datafile/token.json", "r", encoding="utf-8") as f:
        token_json = json.load(f)
    api_token.insert(tk.END, token_json["token"])
except FileNotFoundError:
    token_json = {
        "token": ""
    }
    with open("datafile/token.json", "w", encoding="utf-8") as f:
        json.dump(token_json, f, ensure_ascii=False, indent=4)
    api_token.insert(tk.END, "")


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

#endregion

root.mainloop()