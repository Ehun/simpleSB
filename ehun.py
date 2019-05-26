# -*- coding: utf-8 -*-
from linepy import *
import json, time, random
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
import json, time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, urllib, urllib3, urllib.parse, traceback, atexit

cl = LineClient()
cl.log("Auth Token : " + str(cl.authToken))

print("success")

msg_dict = {}

poll = LinePoll(cl)
call = LineCall(cl)
mid = cl.profile.mid
Bots = [mid]
ABC = [cl]
Creator = ["u6d58abee35bdbc56834a366ef9498704","ub3808de9f7df35f57fb366d157f9790a"]
admin = ["u6d58abee35bdbc56834a366ef9498704","ub3808de9f7df35f57fb366d157f9790a"]
contact = cl.getProfile()
responsename = cl.getProfile().displayName

help ="""=================
By Ehun bot
==================
╔═══════════════
╠➩〘 Help 〙
╠➩〘 Help admin 〙
╠➩〘 Help Creator 〙
╠➩〘 Me 〙
╠➩〘 Mid 〙
╠➩〘 Mid @ 〙
╠➩〘 Ofsider 〙
╠➩〘 Id (id line) 〙
╠➩〘 Pic 〙
╠➩〘 Cover 〙
╠➩〘 Rtime 〙
╠➩〘 Kalender 〙
╠➩〘 Speed 〙
╠➩〘 Ginfo 〙
╠➩〘 Memlist 〙
╠➩〘 Glist 〙
╠➩〘 Creator 〙
╠➩〘 Adminlist 〙
╠➩〘 Banlist 〙
╚═══════════════
"""
help2 ="""=================
   ☄Help admin☄
==================
╔═══════════════
╠➩〘 K (on/off)(utk cek contact)
╠➩〘 J (on/ 〙
╠➩〘 Join 〙
╠➩〘 Bye 〙
╠➩〘 Gn: 〙
╠➩〘 Sider 〙
╠➩〘 Ofsider 〙
╠➩〘 Tagall 〙
╠➩〘 On (protect on) 〙
╠➩〘 Off (protect off) 〙
╠➩〘 Ban 〙
╠➩〘 Invite (contact) 〙
╠➩〘 Sinvite (spam invit contack) 〙
╠➩〘 Unban 〙
╠➩〘 Clearban 〙
╠➩〘 Kill 〙
╠➩〘 Kill ban 〙
╠➩〘 Clean invites 〙
╠➩〘 Buang 〙
╠➩〘 Respon on/off 〙
╠➩〘 Restart 〙
╠➩〘 Ivt (on/off) 〙
╠➩〘 # (kickall) 〙
╚═══════════════
"""
help3 ="""=================
 👉HELP CREATOR👈
==================
╔═══════════════
╠➩〘 Rom 〙
╠➩〘 Spam 〙
╠➩〘 Spm 〙
╠➩〘 ? 〙
╠➩〘 Bom 〙
╠➩〘 Code 〙
╠➩〘 K (on/off(utk cek contact) 〙
╠➩〘 J (on/off)(autohoin) 〙
╠➩〘 Kill 〙
╠➩〘 Admin add @ 〙
╠➩〘 Admindel @ 〙
╚═══════════════
"""
Ehun ="""
 @Echo offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.  
"""
wait={
    "comment":"Bot Auto Like ©By : Ehun\nnContact Me : 👉 line.me/ti/p/~sarehun",
    "message":"Trimakasih kakak sudah add aku",
    "Bot":True,
    "autoAdd":True,
    "AutoJoin":True,
    "LeaveRoom":True,
    "AutoJoinCancel":False,
    "memberscancel":7,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'invite':{},
    'sinvite':{},
    'ivt':False,
    'steal':{},
    'gift':{},
    'copy':{},
    'likeOn':True,
    'detectMention':True,
    'kickMention':False,
    'sticker':True,
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "wblacklist":False,
    "Qr":False,
    "Sider":False,
    "Contact":False,
    "Sambutan":False,
    "autoJoinTicket":True,
    "inviteprotect":False,
    "pname":{},
    "pro_name":{},
    "Simi":{},
    "lang":"JP",
    "BlGroup":{}
    }

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2={
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic={
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#while True:
def clBot(op):
    try:
            if op.type == 0:
                print("[ 0 ] Succes")
                pass

            if op.type == 5:
                if wait["autoAdd"] == True:
                    cl.findAndAddContactsByMid(op.param1)
                    if(wait["message"]in[""," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1,str(wait["message"]))

            if op.type == 22:
                cl.leaveRoom(op.param1)
            if op.type == 21:
                cl.leaveRoom(op.param1)
            if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Creator and op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
            if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
            if op.type == 13:
                if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in admin and op.param2 not in Creator:
                        cl.acceptGroupInvitation(op.param1)
            if op.type == 13:
                if mid in op.param3:
                    if wait["AutoJoinCancel"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) <= wait["memberscancel"]:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"Maaf " + cl.getContact(op.param2).displayName + "\nMember Kurang Dari 7 Orang\nUntuk Info, Silahkan Chat Creator Kami!")
                            cl.sendMessage(receiver, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'},contentType=13)
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")

            if op.type == 13:
                if mid in op.param3:
                    if wait["AutoJoin"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) <= wait["Members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(op.param1,"Halo")
                            
#cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                            pass
                else:
                    if wait["AutoCancel"] == True:
                        if op.param3 not in admin and op.param3 not in Creator and op.param3 not in Bots:
                            pass
                        else:
                            cl.cancelGroupInvitation(op.param1, [op.param3])
                    else:
                        if op.param3 not in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1, [op.param3])
                            cl.sendText(op.param1, "BlacklistDetected")
                        else:
                            Inviter = op.param3.replace("",',')
                            InviterX = Inviter.split(",")
                            matched_list = []
                            for tag in wait["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, InviterX)
                                if matched_list == []:
                                    pass
                                else:
                                    cl.cancelGroupInvitation(op.param1, matched_list)
   #--------------------------------------#
            if op.type == 19:
                if wait["ivt"] == True:
                    if op.param2 not in Bots:
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        pass

            if op.type == 19:
                if admin in op.param3:
                    if op.param2 in Creator:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] == True
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param1,admin)
                            cl.inviteIntoGroup(op.param1,[admin])
                        except:
                            pass


            if op.type == 13:
                if op.param2 in Creator:
                  if op.param2 in admin:
                    if op.param2 in Bots:
                      pass
                elif wait["inviteprotect"] == True:
                     wait["blacklist"][op.param2] = True
                     cl.cancelGroupInvitation(op.param1,[op.param3])
                     if op.param2 in Creator:
                       if op.param2 in admin:
                         if op.param2 in Bots:
                           cl.kickoutFromGroup(op.param1,[op.param2])
                           pass

            if op.type == 11:
                if wait["Qr"] == True:
                    if op.param2 not in Bots and op.param2 not in admin and op.param2 not in Creator:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "Kami Masukin Kedalam Blacklis Boss")
                        pass
                else:
                    pass

        #==========B A T A S ===========#

            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            cl.sendChatChecked(receiver, msg_id)
                            contact = cl.getContact(sender)
                            if text.lower() == 'me':
                              if msg._from in admin:
                                cl.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                              if msg._from in admin:
                                start = time.time()
                                cl.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                cl.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'pic' in text.lower():
                              if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).pictureStatus
                                    cl.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif 'cover' in text.lower():
                              if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif text.lower() == "creator":
                                cl.sendMessage(receiver, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'},contentType=13)
                                cl.sendText(receiver, "Itu Majikan Kami")
                            elif text.lower() == "virus":
                              if msg._from in Creator:
                                cl.sendMessage(receiver, None, contentMetadata={'mid': "BEBAS,'"},contentType=13)
                            elif text.lower() == "invite":
                              if msg._from in Creator:
                                wait["invite"] = True
                                cl.sendText(msg.to, "Kirim contak nya")
                            elif text.lower() == "sinvite":
                              if msg._from in Creator:
                                wait["dinvite"] = True
                                cl.sendText(msg.to, "Kirim contak nya")

                            elif 'Invit: ' in msg.text:
                              if msg._from in admin:
                                  midd = msg.text.replace("Invit: ","")
                                  cl.findAndAddContactsByMid(midd)
                                  cl.inviteIntoGroup(msg.to,[midd])
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == "halo":
                              if msg._from in admin:
                                  group = cl.getGroup(msg.to)
                                  aku = [Amid]
                                  cl.inviteIntoGroup(msg.to,aku)

                            elif text.lower() == 'tagall':
                              if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 20:
                                    cl.mention(msg.to, nama)
                                if jml > 20 and jml < 40:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, len(nama)):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                if jml > 40 and jml < 60:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                if jml > 60 and jml < 80:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                if jml > 80 and jml < 100:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    cl.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    cl.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    cl.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    cl.mention(msg.to, nm4)
                                    for m in range(81, len(nama)):
                                        nm5 += [nama[m]]
                                    cl.mention(msg.to, nm5)
                                if jml <= 100:
                                    cl.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'sider':
                              if msg._from in admin:
                                cl.sendText(msg.to,"Siap Boss")
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                            elif text.lower() == 'ofsider':
                              if msg._from in admin:
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    cl.sendText(msg.to,"Ok Off Boss")
                                else:
                                    cl.sendText(msg.to, "Heh belom di Set")
                            elif text.lower() == "mid":
                              if msg._from in admin:
                                cl.sendMessage(msg.to, msg._from)

                            elif text.lower() == 'help':
                              if msg._from in admin:
                                cl.sendText(msg.to,help)


                            elif text.lower() == 'help admin':
                              if msg._from in admin:
                                cl.sendText(msg.to,help2)
                            elif text.lower() == 'help creator':
                              if msg._from in admin:
                                cl.sendText(msg.to,help3)

                            elif "Mid @" in text:
                              if msg._from in admin:
                                _name = msg.text.replace("Mid @","")
                                _nametarget = _name.rstrip(' ')
                                gs = cl.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        cl.sendText(msg.to, g.mid)
                                    else:
                                        pass

                            elif text.lower() == "bot?":
                              if msg._from in admin:
                                cl.sendMessage(receiver, None, contentMetadata={'mid': mid},contentType = 13)

                            elif text.lower() == 'ourl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.preventJoinByTicket = False
                                    cl.updateGroup(X)
                                    cl.sendText(msg.to,"Url Sudah Di Aktifkan")
                                else:
                                    cl.sendText(msg.to,"Sudah di buka")
                            elif text.lower() == 'curl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.preventJoinByTicket = True
                                    cl.updateGroup(X)
                                    cl.sendText(msg.to,"Url Sudah Di Nonaktifkan")
                                else:
                                    cl.sendText(msg.to,"Sudah di tutup")
                            elif text.lower() == 'gurl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    x = cl.getGroup(msg.to)
                                    if x.preventJoinByTicket == True:
                                        x.preventJoinByTicket = False
                                        cl.updateGroup(x)
                                    gurl = cl.reissueGroupTicket(msg.to)
                                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                                else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Can't be used outside the group")
                                    else:
                                        cl.sendText(msg.to,"Not for use less than group")


                            elif ("Gn: " in msg.text):
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    X.name = msg.text.replace("Gn: ","")
                                    cl.updateGroup(X)
                                else:
                                    cl.sendText(msg.to,"It can't be usedbesides the group.")

                            elif text.lower() == "ginfo":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    ginfo = cl.getGroup(msg.to)
                                    try:
                                        gCreator = ginfo.creator.displayName
                                    except:
                                        gCreator = "Error"
                                    if wait["lang"] == "JP":
                                        if ginfo.invitee is None:
                                            sinvitee = "0"
                                        else:
                                            sinvitee = str(len(ginfo.invitee))
                                        if ginfo.preventJoinByTicket == True:
                                            u = "Tertutup"
                                        else:
                                            u = "Terbuka"
                                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "   Member\n\nPending:" + sinvitee + "Orang\n\nURL:" + u)
                                    else:
                                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                                else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Can not be used outside the group")
                                    else:
                                        cl.sendText(msg.to,"Not for use lessthan group")


                            elif 'Id ' in text:
                              if msg._from in Creator:
                                msgg = msg.text.replace('Id ',"")
                                conn = cl.findContactsByUserid(msgg)
                                if True:
                                   msg.contentType = 13
                                   msg.contentMetadata = {'mid': conn.mid}
                                   cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                                   cl.sendMessage(msg)
                            elif text.lower() == "on":
                              if msg._from in admin:
                                wait["AutoJoinCancel"] = True
                                wait["AutoJoin"] = True
                                wait["AutoCancel"] = True
                                wait["inviteprotect"] = True
                                wait["ivt"] = True
                                wait["Qr"] = True
                                cl.sendText(msg.to,"All Protect on")
                            elif text.lower() == "off":
                              if msg._from in admin:
                                wait["AutoJoinCancel"] = False
                                wait["AutoJoin"] = False
                                wait["AutoCancel"] = False
                                wait["inviteprotect"] = False
                                wait["ivt"] = False
                                wait["Qr"] = False
                                cl.sendText(msg.to,"All Protect off")

                            elif text.lower() == "status":
                              if msg._from in admin:
                                md = ""
                                if wait["ivt"] == True: md+="╠➩✔️ Auto ivt : On\n"
                                else: md+= "╠➩❌ Auto ivt : Off\n"
                                if wait["AutoCancel"] == True: md+="╠➩✔️ Auto Cancel : On\n"
                                else: md+= "╠➩❌ Auto Cancel : Off\n"
                                if wait["inviteprotect"] == True: md+="╠➩✔️ Invite Protect : On\n"
                                else: md+= "╠➩❌ Invite Protect : Off\n"
                                if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
                                else:md+="╠➩❌ Qr Protect : Off\n"
                                if wait["AutoJoinCancel"] == True: md+="╠➩✔️ AutoCancel : On\n"
                                else:md+="╠➩❌ JoinCancel : Off\n"
                                if wait["AutoJoin"] == True: md+="╠➩✔️ Join : On\n"
                                else:md+="╠➩❌ Join : Off\n"
                                cl.sendText(msg.to,"╔════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════\n"+md+"╚═════════════════")
                            elif text.lower() == 'j on':
                              if msg._from in Creator:
                                  wait["AutoJoin"] = True
                                  cl.sendText(msg.to, "join aktip")
                              else:
                                  cl.sendText(msg.to, "Sudah on")
                            elif text.lower() == 'j off':
                              if msg._from in Creator:
                                  wait["AutoJoin"] = False
                                  cl.sendText(msg.to, "join off")
                              else:
                                  cl.sendText(msg.to, "Blom on")
                            elif text.lower() == 'ivt on':
                              if msg._from in Creator:
                                 wait["ivt"] = True
                                 cl.sendText(msg.to,"Auto ivt di on")
                            elif text.lower() == 'ivt off':
                              if msg._from in Creator:
                                  wait["ivt"] = False
                                  cl.sendText(msg.to,"Auto ivt di off")

                            elif text.lower() == "code":
                              if msg._from in Creator:
                                cl.sendText(msg.to,"Bubar bubar")
                                cl.sendText(msg.to,Ehun)
                                cl.sendText(msg.to,"Success")
                            elif '#' in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                   print('Ok')
                                   _name = msg.text.replace("#","")
                                   gs = cl.getGroup(msg.to)
                                   targets = []
                                   for g in gs.members:
                                       if _name in g.displayName:
                                           targets.append(g.mid)
                                   if targets == []:
                                       cl.sendText(msg.to,"Not found.")
                                   else:
                                       for target in targets:
                                           wait["blacklist"][target] = True
                                           try:
                                               cl.kickoutFromGroup(msg.to,[target])
                                               print(msg.to,[g.mid])
                                           except Exception as e:
                                               cl.sendText(msg.to,str(e))
                            elif "? " in text:
                              if msg._from in admin:
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                      names = re.findall(r'@(\w+)', msg.text)
                                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                      mentionees = mention['MENTIONEES']
                                      for mention in mentionees:
                                          cl.kickoutFromGroup(msg.to,[mention['M']])
                            elif text.lower() == 'restart': 
                              if msg._from in admin:
                                  cl.sendText(receiver,"Ok bot di ulang")
                                  restart_program()
                              else:
                                  cl.sendText(msg.to,"Kuhsus admin")

                            elif "Rom" in msg.text:
                              if msg._from in Creator:
                                  thisgroup = cl.getGroups([msg.to])
                                  Mids = [contact.mid for contact in thisgroup[0].members]
                                  mi_d = Mids[:33]
                                  t = 20
                                  while(t):
                                    cl.createGroup("b̶o̶tডা‮‮─┅═ই", mi_d)
                                    t-=1
                                  cl.sendText(msg.to,"Success To b̶o̶tডা‮‮─┅═ই")
                              else:
                                  cl.sendText(msg.to,"Kusus Creator")

                            elif "Spam " in msg.text:
                              if msg._from in Creator:
                                  bctxt = msg.text.replace("Spam ","")
                                  t = 20
                                  while(t):
                                    cl.sendText(msg.to, (bctxt))
                                    t-=1
                            elif "Spam: " in msg.text:
                                try:
                                    group = msg.text.replace("Spam: ","")
                                    gid = group[:33]
                                    name = group.replace(grouptags[:34],"")
                                    cl.createGroup(gid,name)
                                    cl.sendText(msg.to,"We created an album" + name)
                                except:
                                    cl.sendText(msg.to,"Error")
                            elif "999+ " in msg.text:
                              if msg._from in Creator:
                                   bctxt = msg.text.replace("999+ ", "")
                                   t = cl.getAllContactIds()
                                   t = 3
                                   while(t):
                                      cl.sendText(msg.to, (bctxt))
                                      t-=1


                            elif "Spm @" in msg.text:
                              if msg._from in Creator:
                                  _name = msg.text.replace("Spm @","")
                                  _nametarget = _name.rstrip(' ')
                                  gs = cl.getGroup(msg.to)
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          cl.sendText(msg.to,"Yes")
                                          cl.sendText(g.mid,"Spammed")
                                          cl.sendText(msg.to,"Success")

                            elif text.lower() == 'kalender':
                                timeNow = datetime.now()
                                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                inihari = datetime.today()
                                hr = inihari.strftime('%A')
                                bln = inihari.strftime('%m')
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                cl.sendText(receiver,hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M%S') + " ]")
                            elif text.lower() == 'rtime':
                              if msg._from in admin:
                                eltime = time.time() - mulai
                                cl.sendText(receiver,"Ehun Bot Sudah BerjalanSelama :\n"+waktu(eltime))

                            elif "Setpoin" in msg.text:
                              if msg._from in admin:
                                cl.sendText(msg.to,"☆> Set <☆('・ω・') Jam [ " + datetime.today().strftime('%H:%M:%S') + " ]")
                                try:
                                    del wait2['readPoint'][msg.to]
                                    del wait2['readMember'][msg.to]
                                except:
                                    pass
                                now2 = datetime.now()
                                wait2['readPoint'][msg.to] = msg.id
                                wait2['readMember'][msg.to] = ""
                                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M:%S")
                                wait2['ROM'][msg.to] = {}
                            elif msg.text in ["Laspoin"]:
                              if msg._from in admin:
                                if msg.to in wait2['readPoint']:
                                   if wait2["ROM"][msg.to].items() == []:
                                        chiya = ""
                                   else:
                                        chiya = ""
                                        for rom in wait2["ROM"][msg.to].items():
                                            chiya += rom[1] + "\n"

                                   cl.sendText(msg.to,"      ||By : ✰Ehun bot✰||\n   Ini kak yang on tadi !!!\n-----------------------------------\n%s\n%s\nDoain sehat Ceria Semua ya kak (-_-)\n-----------------------------------\n    Setpoin ('・ω・')  Jam  [%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                                else:
                                   cl.sendText(msg.to,"Ktik 👉 Setpoin 👈 dulu")
                            elif text.lower() == 'left':
                              if msg._from in admin:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendText(msg.to, "izin left kakak semuanya\nBýe bye byeeeeeeeeeeeee\n" + str(ginfo.name) + "\nAssalamualaikum wr wb\nSampai jumpa lagi kakak semua nya")
                                  cl.leaveGroup(msg.to)
                              else:
                                  cl.sendText(msg.to,"Khusus admin")

                            elif 'Buang' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                         random.choice(ABC).cancelGroupInvitation(msg.to,[_mid])
                                         pass
#cl.sendText(msg.to,"Beres Boss")
                            elif 'Clean invites' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = cl.getGroup(msg.to)
                                    if X.invitee is not None:
                                        gInviMids = [contact.mid for contact in X.invitee]
                                        random.choice(ABC).cancelGroupInvitation(msg.to, gInviMids)
                                    else:
                                        if wait["lang"] == "JP":
                                            cl.sendText(msg.to,"No one is inviting。")
                                        else:
                                            cl.sendText(msg.to,"Sorry, nobody absent")
                                else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Can not be used")
                                    else:
                                        cl.sendText(msg.to,"Can not be used last group")
                            elif "Ban @" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    print("@Ban by mention")
                                    _name = msg.text.replace("Ban @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to,"Not found")
                                    else:
                                        for target in targets:
                                            if target not in Creator:
                                                try:
                                                    wait["blacklist"][target] = True
                                                    cl.sendText(msg.to,"Succes BosQ")
                                                except:
                                                    cl.sendText(msg.to,"Error")
                                            else:
                                                cl.sendText(msg.to,"Creator Detected~")
                            elif "Unban @" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    print("@Unban by mention")
                                    _name = msg.text.replace("Unban @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = cl.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to,"Not found")
                                    else:
                                        for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendText(msg.to,"Succes BosQ")
                                            except:
                                                cl.sendText(msg.to,"Succes BosQ")
                            elif text.lower() == 'banlist':
                              if msg._from in admin:
                                if wait["blacklist"] == {}:
                                    cl.sendText(msg.to,"Tidak Ada")
                                else:
                                    mc = ""
                                for mi_d in wait["blacklist"]:
                                    mc += "->" +cl.getContact(mi_d).displayName + "\n"
                                cl.sendText(msg.to,"===[Blacklist User]===\n"+mc)
                            elif text.lower() == 'kill':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                    for tag in wait["blacklist"]:
                                        matched_list+=filter(lambda str: str == tag, gMembMids)
                                    if matched_list == []:
                                        cl.sendText(msg.to,"Fuck You")
                                        pass
                                    for jj in matched_list:
                                        try:
                                            cl.kickoutFromGroup(msg.to,[jj])
                                            print(msg.to,[jj])
                                        except:
                                            pass
                            elif text.lower() == 'clearban':
                              if msg._from in admin:
                                  wait["blacklist"] = {}
                                  cl.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All")

                            elif text.lower() == 'memlist':
                              if msg._from in admin:
                                  kontak = cl.getGroup(msg.to)
                                  group = kontak.members
                                  num=1
                                  msgs="═════════List Member═�����═══════-"
                                  for ids in group:
                                      msgs+="\n[%i] %s" % (num, ids.displayName)
                                      num=(num+1)
                                  msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                                  cl.sendText(msg.to, msgs)
                            elif "Inpo "in msg.text:
                              if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = cl.getContact(key1)
                                cu = cl.getCover(key1)
                                try:
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                                except:
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
                            elif text.lower() == 'glist':
                              if msg._from in admin:
                                cl.sendText(msg.to, "Tunggu Sebentar. . .")
                                gid = cl.getGroupIdsJoined()
                                h = ""
                                jml = 0
                                for i in gid:
                                    h += "╠➩" + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                                    jml += 1
                                cl.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")
                            elif text.lower() == 'adminlist':
                              if admin == []:
                                  cl.sendText(msg.to,"The stafflist is empty")
                              else:
                                  cl.sendText(msg.to,"Tunggu...")
                                  mc = "||Admin Ehun Bot||\n=====================\n"
                                  for mi_d in admin:
                                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                                  cl.sendText(msg.to,mc)
                                  print("[Command]Stafflist executed")
                            elif text.lower() == 'k on':
                              if msg._from in admin:
                                wait["Contact"] = True
                                cl.sendText(msg.to,"Contact activ")
                            elif text.lower() == 'k off':
                              if msg._from in admin:
                                wait["Contact"] = False
                                cl.sendText(msg.to,"Contact di off")
                            elif text.lower() == 'bot on':
                              if msg._from in admin:
                                  wait["Bot"] = True
                                  cl.sendText(msg.to,"Bot di on")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'bot off':
                              if msg._from in admin:
                                  wait["Bot"] = False
                                  cl.sendText(msg.to,"Bot di off")
                              else:
                                  cl.sendText(msg.to,"Khusus admin")
                            elif text.lower() == 'respon on':
                              if msg._from in admin:
                                  wait['detectMention'] = True
                                  cl.sendText(msg.to,"Respon on")
                           
                            elif text.lower() == 'respon off':
                              if msg._from in admin:
                                  wait['detectMention'] = False
                                  cl.sendText(msg.to,"Respon off")
                            
                            elif "Admin add @" in msg.text:
                              if msg._from in Creator:
                                  print("[Command]Staff add executing")
                                  _name = msg.text.replace("Admin add @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = cl.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      cl.sendText(msg.to,"Contact not found")
                                  else:
                                      for target in targets:
                                          try:
                                              admin.append(target)
                                              cl.sendText(msg.to,"Admin Ditambahkan")
                                          except:
                                              pass
                              else:
                                  cl.sendText(msg.to,"Perintah Ditolak.\nHanya untuk Creator")
                            elif "Admindel @" in msg.text:
                              if msg._from in Creator:
                                  print("[Command]Staff remove executing")
                                  _name = msg.text.replace("Admindel @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = cl.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      cl.sendText(msg.to,"Contact not found")
                                  else:
                                      for target in targets:
                                           try:
                                              admin.remove(target)
                                              cl.sendText(msg.to,"Admin Dihapus")
                                           except:
                                               pass
                              else:
                                  cl.sendText(msg.to,"Perintah Ditolak.\nHanya untuk Creator")
                            elif "line://ti/g/" in msg.text.lower():
                              #if wait["Bot"] == True:
                                  if wait["autoJoinTicket"] == True:
                                      link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                      links = link_re.findall(text)
                                      n_links = []
                                      for l in links:
                                           if l not in n_links:
                                              n_links.append(l)
                                      for ticket_id in n_links:
                                          group = cl.findGroupByTicket(ticket_id)
                                          cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                          cl.sendMessage(msg.to, "Go b̶o̶tডা‮‮─┅═ই \n%s" % str(group.name))


                except:
                    pass
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Np = cl.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                cl.sendText(op.param1, str(random.choice(pref))+'👉'+Name+'👈')
                                cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass

            if op.type == 55:
                try:
                   if op.param1 in wait2['readPoint']:
                     Name = cl.getContact(op.param2).displayName
                     if Name in wait2['readMember'][op.param1]:
                        pass
                     else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name + "\nOn Jam : " + datetime.today().strftime('%H:%M:%S')
                        wait2['ROM'][op.param1][op.param2]
                   else:
                     cl.sendText
                except:
                    pass



            if op.type == 11:
                if op.param3 == '1':
                    if op.param1 in wait['pname']:
                        try:
                            G = cl.getGroup(op.param1)
                        except:
                            pass
                        G.name = wait['pro_name'][op.param1]
                        try:
                            cl.updateGroup(G)
                        except:
                            pass
                    else:
                        if op.param2 in Bots + Creator:
                            try:
                                cl.sendText(op.param1,"Hai kak" + cl.getContact(op.param2).displayName + "\nJangn Tukar Nama Group (-_-) \nMaaf Aku kick Kamu")
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass


            if op.type == 17:
              if wait["Sambutan"] == True:
                if op.param2 in Creator:
                    pass
                cl.sendMessage(to=op.param1, text=None, contentMetadata={'mid':op.param2}, contentType=13)
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).displayName
                cl.sendText(op.param1,"Jam  :" + datetime.today().strftime('%H:%M:%S') + "\nHallo kak" + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜ \nBudayakan Cek Note\nDan Semoga Betah di Sini . (p′︵‵。) 🤗 \nCreator>>" + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
                print("MEMBER JOIN TO GROUP")

            if op.type == 26:
                msg = op.message

                if 'MENTION' in msg.contentMetadata.keys() != None:
                     if wait["detectMention"] == True:
                         contact = cl.getContact(msg._from)
                         cName = contact.displayName
                         balas = ["Woi kak " + "☞ " + cName + " ☜" + "Jgn ngtag ngetag Admin bot \nHp ngebleng semmm kak", "Woi kak " + "☞ " + cName + " ☜" + "Kakak kangen ya?\nPm aja kak\nIni rahsia prusahaan ya kak(-_-)", "Woi kak " + "☞ " + cName + " ☜" + "ADmin bot gi sibuk\nKalo kangen bilang kak\nkak serius naksir Admin bot ya?"]
                         ret_ = random.choice(balas)
                         image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                         name = re.findall(r'@(\w+)', msg.text)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         for mention in mentionees:
                             if mention['M'] in admin:
                                 cl.sendText(msg.to,ret_)
                                 cl.sendImageWithURL(msg.to,image)
                                 break

            if op.type == 25:
                msg = op.message
                if msg.text in ["Bot on"]:
                    wait["Bot"] = True
                    cl.sendText(msg.to,"Bot Sudah On Kembali.")

            if op.type == 25:
              if wait["Bot"] == True:
                msg = op.message

                if msg.contentType == 13:
                    if wait["wblacklist"] == True:
                        if msg.contentMetadata["mid"] not in admin:
                            if msg.contentMetadata["mid"] in wait["blacklist"]:
                                cl.sendText(msg.to,"Sudah")
                                wait["wblacklist"] = False
                            else:
                                wait["blacklist"][msg.contentMetadata["mid"]] = True
                                cl.sendText(msg.to,"Ditambahkan")
                        else:
                            cl.sendText(msg.to,"Admin Detected~")
                    elif wait["Contact"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to, "Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                        
                    elif msg.contentType == 16:
                        if wait["Timeline"] == True:
                            msg.contentType = 0
                            cl.sendText(msg.to,"post URL\n" + msg.contentMetadata["postEndUrl"])
                    elif msg.contentType == 13:
                        if wait['invite'] == True:
                            _name = msg.contentMetadata["displayName"]
                            invite = msg.contentMetadata["mid"]
                            groups = cl.getGroup(msg.to)
                            pending = groups.invitee
                            targets = []
                            for s in groups.members:
                                if _name in s.displayName:
                                    cl.sendText(msg.to, _name + "Berada DiGrup Ini")
                                else:
                                    targets.append(invite)
                            if targets == []:
                               pass
                            else:
                               for target in targets:
                                   try:
                                       cl.findAndAddContactsByMid(target)
                                       cl.inviteIntoGroup(msg.to,[target])
                                       cl.sendText(msg.to,"Invite " + _name)
                                       wait['invite'] = False
                                       break
                                   except:
                                       cl.sendText(msg.to,"Limit Invite")
                                       wait['invite'] = False
                                       break
                        if wait['invite'] == True:
                            _name = msg.contentMetadata["displayName"]
                            invite = msg.contentMetadata["mid"]
                            groups = cl.getGroup(msg.to)
                            pending = groups.invitee
                            targets = []
                            for s in groups.members:
                                if _name in s.displayName:
                                    cl.sendText(msg.to, _name + "Berada DiGrup Ini")
                                else:
                                    targets.append(invite)
                            if targets == []:
                               pass
                            else:
                               for target in targets:
                                   try:
                                       cl.findAndAddContactsByMid(target)
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.createGroup(msg.to,[target])
                                       cl.sendText(msg.to,"Success " + _name)
                                       wait['sinvite'] = False
                                       break
                                   except:
                                       cl.sendText(msg.to,"Limit Invite")
                                       wait['sinvite'] = False
                                       break



    except:
        pass
while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops is not None:
           for op in ops:
                poll.setRevision(op.revision)
                clBot(op)
    except:
        pass
#Exception as e:
        #cl.log("[SEND_MESSAGE] ERROR : " + str(e))

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
        print("BYE")
atexit.register(atend)
