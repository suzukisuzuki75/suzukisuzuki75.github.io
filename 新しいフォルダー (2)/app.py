from lib2to3.pgen2.pgen import DFAState
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pydeck as pdk

st.title("卒業共同制作")
st.header('１.河合勝彦ゼミの二大野球好きである金森と鈴木によるMLBのデータビジュアライゼーション')
st.write('MLBにはAL(アメリカンリーグ)NL(ナショナルリーグ)の2つのリーグが存在する。今回はNYY(ニューヨークヤンキース)のアーロンジャッジ選手とLAA(ロサンゼルスエンゼルス)の大谷翔平選手が所属するALMVPをセイバーメトリクスの観点から分析する。MLBのMVPは全米野球記者協会BBWAAの記者30名によって選出される。リーグの1位から10位まで順位をつけ投票し順位に応じた合計点数が最も高かった選手がMVPとなる。MVPはAL、NLから一名ずつ選出され日本人選手の選出は2001年のイチロー選手と2021年の大谷翔平選手の二名のみである。')
st.header('２.データと指標の紹介')
st.write("はじめに2019〜2022年の成績を中心に予測・比較を行なっていく。なお2020年は新型コロナウイルスの影響から試合数が大幅に縮小しての開催のためデータからは除外した。")
st.write("（※指標の説明　　PLAYER選手名　TEAM所属チーム名　G	出場試合数 　AB打数　R　得点数Hヒット数 　2B2塁打数　3B3塁打数　 HRホームラン数 　RBI打点数 　BB	四球数 　SO	三振数 　SB 盗塁数 　CS	盗塁失敗の数 　AVG打率 　OBP出塁率 　SLG 長打率 　OPS出塁率＋長打率 　WAR 選手の貢献度）")


##データを表示をボタンで切り替え
df = [pd.read_csv('Bstats_' + str(yr) + '.csv')for yr in (2019, 2021, 2022)]

col = st.columns(3)
show_2019 = col[0].button('2019year')
show_2021 = col[1].button('2021year')
show_2022 = col[2].button('2022year')

if show_2019:
    st.write(df[0])
elif show_2021:
    st.write(df[1]) 
elif show_2022:
    st.write(df[2])
st.header('３.過去のMVP受賞者とその成績')
    
st.write("2019年はLAAのマイクトラウト選手、2021年はLAAの大谷翔平選手が受賞している。2019年はマイクトラウト、アレックスブレグマン、マーカスセミエンの3選手がファイナリストである。")

df = pd.read_csv('Bstats_2019.csv')
st.write(df.iloc[[53,25,1],:].style.highlight_max(axis=0),width=500,height=500)

st.write("全体的な成績の見栄えはブレグマン選手が優勢とみられていたが、長打率と出塁率を足した現代野球で最も重要な指標の一つと言われているOPSで大差のトラウトが受賞した。ブレグマンのMVPに影を及ぼしたと言われているのは2017年に所属していた球団でのサイン盗み問題である。2019年の成績には関係していないが投票権を持つ記者の心情に影響が少なからずあったといえるかもしれない。")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("マイクトラウト")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqG_n0ND9uG8AHUnFY7DOmHx-qK-uBwRgV2zHOq-IlH8YOB8NY-I9wJbEU6z3eT4y0oOjsoG_g_KsZX_maIM5uUAGkrdwYy4wFUTvtfcefQK4w0I-e_n58ZGTPtupBWquV5lJxzYeIiMhmst8w1S2m-5AyOkItzHjvAQDWwZc7gnhbNWFKvYkUQInLfd3eX6fIWRgSNROpaiNKPOq8jwyP4fcggfheT3VZvQQXUlSp7Xonn29HIvYMWz9h5nUCimyTjHRm7-O8t5aW-4ll4jOaBN4pGPzOsHkpFXcxVdHI1Bo8djPo5-pisdzlzboJURcY_Onh_JEV7Q6iKpK6gcB9Vebycc9xqVVYKgjlBXfvHufA_F4sq3eAFdyrsNDDqbuFdxgzZb7NReef3Yu7oAdFqAKgaYppVBSOxHclRY-iFw6-SeBhT-xjjwyT8Vq3PcpU2g==/hi-res-557e693d77a591c355e630931a3ae4a6_crop_north.jpg?errorImage=false", use_column_width=True)

with col2:
    st.write("アレックスブレグマン")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqG0-odoPbBlzrJGs2yRctR9ArUNJPYNP-FmLFgaJayJz-zstkl7qJLSCAd485Uc3vYByGuCP4vA_xUSkPxDz3XEsw3exgTuq17LMmqbONjPTjd0XRgvS1dkUzsTp1yDMALJHZmgPtaX0gjl4H1ZIydpnP6AYgQIWwNzUqKoGbJGr_IfampeGnsMMd9dfEnKck56pYXLtC5e0hEWkMT0VkcQ9jxzmkMVgKDeRgyrT3gCZkfrHW7s8TeEWPW1CX056crQ==/201802112029209f3.jpg?errorImage=false", use_column_width=True)
    
with col3:
    st.write("マーカスセミエン")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqG5Me91eiZ7L5p6EFNFM5pygL90Iciq6hrmbrsiTzU68k5b9UG-chcGcHJnagxcbw3c1es1Y4fvvpwMOIz5ulGrbU628LMAr8T0s67HZNakMvDVU65JtgtaBC06R_z_Dv7mhOPlvbjxAe-g_GQ_t4p8y1Mr9QwDY_LdaqWvvM8BocXb3fcur85f3ir_Y5RHXqL_QFDL5ozf9axRWRRWbWUC9AvpqRXQYmADfXjzLsEZoMK6vIA8nlo3nOR5ACF20DDtXObIzxeONKC8Wu-E_sjg4=/1632040298-465062483-scaled.jpg?errorImage=false", use_column_width=True)

st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 

st.write("2021年はLAAの大谷翔平選手が満票でのMVP受賞となった。ファイナリストには大谷翔平、ウラジミール・ゲレーロ・ジュニア、マーカスセミエンが名を連ねた。大谷選手の所属するLAAは勝率5割に満たない弱いチームであったが投打での活躍が評価され満票でのMVP選出となった。")    
st.write("")    

df = pd.read_csv('Bstats_2021.csv')
st.write(df.iloc[[35,9,1],:].style.highlight_max(axis=0),width=500,height=500)
st.caption('大谷翔平の投手成績')
df = pd.read_csv('Pstats_2021.csv')
st.write(df)
st.caption('(※投手指標の説明　PLAYER選手名　TEAM所属チーム名　W勝利数　 L敗北数　ERA防御率　G登板試合数　GS先発登板数　CG完投数　SHO完封数　SVセーブ数　SVOセーブ機会数　IP投球回数　H被安打数　R失点数　ER自責点数　HR被本塁打数 　HB与死球数 　BB与四球数 　SO奪三振数 　WHIP投球回あたり与四球・被安打数合計 　AVG被安打率 　WAR選手の貢献度 　CYAサイヤング賞獲得数)')

col1, col2, col3 = st.columns(3)
with col1:
    st.write("大谷翔平")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqGzusZuH1tDPomPcf_UdBNLBh6orhLKGkvqTyO7KG9STGQ_W3SX9CL9W-Nq99KoxDphmcTMpBkIyuwSOcGIVr2t3sOmEm4m6KWHSMej0Cavtwm_LJ4s0xO1yYsTTiPGBZQ4Bv5Z-ZZZuWNoZx-LX9pnVjLGvhWP1LTQmBvPm95jhW1-ZC01AkaxZlI0kVPQp2okwyuzu9b_jaOebfKL6LZbNUqHcjdjydqj-o3EPHHy3MsFKezIth0CVBL9FdH76ftalFCRgpJ_evJwSWEYWBeP7fwshIkMhj65sG_BxPnrMT/20221117s00001007070000p_view.webp?errorImage=false", use_column_width=True)

with col2:
    st.write("ウラジミール・ゲレーロ・ジュニア")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqGxaQRRI8gBz4coOvQoxc8kDQTc5aZrbGI9eAcsYivygcWgovkGs5fjIDchrX6xqr4UGCBSouTFr0Un8CfUtywL94m8wWyf7I9tx7PLoTIK-nZisRL9bbUqIIOAZlgO8Y21LOhIKSG8aa45pQPBRcrsb77CunY9tMHkiht8iE8FJ_mTZWBUPN8dTa1yysjKhs9ZRinq80UdaLiaq4x3ut8b0uGF5szQyh_zJvU4kJVRWPEezeh5CYUsPtUYv2pzZA8Eb7tWEBT5TYfsg9X8geFeZ8JjTf8IJdMTGZ1aUQcd0v_QKMPGmJ6RW_PrGsuHjUb4KZq_7YIKtTRQJZu4c1phRRplTY-LIbS6OXHlvQG0nq9C6TBnB39df-XBxxMghfAA==/-guerrero_ep4h4nbzlekw1k18wwwkqbbmh.jpg?errorImage=false", use_column_width=True)
    
with col3:
    st.write("マーカスセミエン")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqG5Me91eiZ7L5p6EFNFM5pygL90Iciq6hrmbrsiTzU68k5b9UG-chcGcHJnagxcbw3c1es1Y4fvvpwMOIz5ulGrbU628LMAr8T0s67HZNakMvDVU65JtgtaBC06R_z_Dv7mhOPlvbjxAe-g_GQ_t4p8y1Mr9QwDY_LdaqWvvM8BocXb3fcur85f3ir_Y5RHXqL_QFDL5ozf9axRWRRWbWUC9AvpqRXQYmADfXjzLsEZoMK6vIA8nlo3nOR5ACF20DDtXObIzxeONKC8Wu-E_sjg4=/1632040298-465062483-scaled.jpg?errorImage=false", use_column_width=True)

st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 


st.write("")
st.header('４.MVP予想')

st.write("2022年アメリカンリーグMVPのファイナリストは大谷翔平、アーロンジャッジ、ヨルダンアルバレスの3名に絞られた(11/7発表)。")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("アーロンジャッジ")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqG7HPek0SOe2g_rpjpG26QUc66GlkxGj_Zx-vsMdiJ5DBaEeD0UOe8AUJVvg6cbjfo-NoVf84VzvxiPSiOEpXQ1RflMDj_IBE-eNmriqcHnpCHoNtb7gyWFe2pu89Qc6CutyMVlZqs9AvmVxtUHwNz9JfkUqIN3mDx47az20FAOvQV4e8nm7CSuc2qrDHwOSEY15eFW_Xh99Yos_glToXqwvapZV_DeFrd3NbgOJV2kTz/0ac3c8a3-9d0c-6cd1-0077-d5ac1aca08ac.jpg?errorImage=false", use_column_width=True)

with col2:
    st.write("大谷翔平")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqGzusZuH1tDPomPcf_UdBNLBh6orhLKGkvqTyO7KG9STGQ_W3SX9CL9W-Nq99KoxDphmcTMpBkIyuwSOcGIVr2t3sOmEm4m6KWHSMej0Cavtwm_LJ4s0xO1yYsTTiPGBZQ4Bv5Z-ZZZuWNoZx-LX9pnVjLGvhWP1LTQmBvPm95jhW1-ZC01AkaxZlI0kVPQp2okwyuzu9b_jaOebfKL6LZbNUqHcjdjydqj-o3EPHHy3MsFKezIth0CVBL9FdH76ftalFCRgpJ_evJwSWEYWBeP7fwshIkMhj65sG_BxPnrMT/20221117s00001007070000p_view.webp?errorImage=false", use_column_width=True)
    
with col3:
    st.write("ヨルダンアルバレス")
    st.image("https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqGzusZuH1tDPomPcf_UdBNLBh6orhLKGkvqTyO7KG9STG2AXabtvPv_XuHVYZLE0-AScQ5DJPrqG_dHJmzblr7PvE3mbD000P-YBEPJ8vG3MfeZIEpx1IohthycWgJj_jWl5AIkF5ufravNJxcETSXVTMk_gM2zaSl-eKP5bxZPkZAzRdtyBmG097KqR3xWc9NBZ37IZFBR3KSLXK62xzepVOWI3h24Z2C8HwYKbsya0yXhZOsYxF7FggwqZLWsugoXdsTWAzp8uKDeWDwG9Rjh-ydJ19tAKJ58gdvjptwpMO/20190610s00001007188000p_view.jpg?errorImage=false", use_column_width=True)

df = pd.read_csv('Bstats_2022.csv')
st.write(df.iloc[[15,13,57],:].style.highlight_max(axis=0),width=500,height=500)
st.caption('大谷翔平の投手成績')
df = pd.read_csv('Pstats_2022.csv')
st.write(df)

st.write('11/5に事前に行われた選手間でのMVPではジャッジ選手が年間最優秀選手とアメリカンリーグ最優秀選手の2冠を達成しており、実際にプレーする者たちからも高い評価を得ていることがわかる。また今年はボールが変わったといわれ投高打低といわれる投手有利なシーズンであった。その中で62本という傑出した成績を残し、リーグ記録を更新したアーロンジャッジ選手がMVPを獲得するのではないかと予想する。MVPはチームの順位が考慮される。アーロンジャッジの所属するヤンキースは地区優勝を果たしている一方、大谷翔平の所属するエンゼルスはプレーオフ進出すら叶っていない。またアーロンジャッジがALのホームラン記録を62年ぶりに更新したことも大きな要因であると考えられる。しかし昨年の大谷翔平選手のような満票でのMVP獲得はないと思われる。大谷選手自体昨年度よりHRの数こそ減ったものの成績を軒並み伸ばしているからだ。')

st.write("") 
st.write("") 
st.write("") 

st.write('アメリカの野球評論家がこのようなことを言っていた。「もし大谷がヤンキースでジャッジがエンゼルスだったら確実に大谷がMVPだ。」これは本当なのだろうか。そこで人気球団とMVPの相関があるかを検討してみる。フォーブス誌が毎年発表する価値のある球団のランキングに基づいて検討する。')

col1, col2  = st.columns(2)

with col1:
      MVP = pd.read_csv('MVP_30.csv')   
      st.caption('過去30年のALMVP受賞者所属チーム')
      st.write(MVP) 
with col2:      
      AL = pd.read_csv('AL_popular.csv')
      st.caption('AL資産価値の高いチーム')
      st.write(AL)

st.write('その結果ヤンキースはAL、NLの全30球団で最も価値のある球団であるが過去30年のALMVPの受賞者を見てみるとヤンキースは2回の受賞であるのに対してエンゼルスは5回でALのトップタイである。この結果からは人気度とMVP受賞には相関は見られない。あくまで人気球団は全米での中継が多く行われたりニュースに取り上げられたりすることが比較的多く、人々の目に留まりやすいため注目の的になることを言っているのかもしれない。')

st.header("５.さらなる予測")

st.write("ここまでの予測では不十分であると感じたため過去30年のMVP受賞者の成績を見比べて予測を立ててみる。なおMLBでは投手のMVPとしてサイヤング賞がある。相方の金森君が今回サイヤング賞を分析してくれているということもあり、今回はピッチャーのMVP受賞者は除外して分析してみる。(1990~2121年のうち1992年と2011年は投手がMVPを受賞したため除外）私が今回指標として軸にしたのはOPSだ。OPSは出塁率と長打率と足したものであり現代野球において野手の活躍度合いを見る指標として最も有効なものであるとされている。下に過去30年のALのMVP受賞者とOPSの成績を並べてみた。")

OPS = pd.read_csv('OPS.csv')
st.table(OPS)

st.write('基本的にOPSが最も高い選手がMVPになる理由として、OPSが基本的な指標を網羅しているからだ。打率や四球の数は出塁率として反映され、ホームラン数や二塁打の数は長打率に反映される。上の表を見てみても歴代MVPのほとんどがOPS0.900を超えており超えてない選手を見てみる。')
st.write('2001年のイチローはメジャー1年目にして新人ヒット記録を更新し新人王とMVPを受賞している。2002のミゲルテハダもシーズン2位の連続安打記録を記録、またチームでも20連勝を記録するなど、歴史的な記録を残したOPSで突出していなくとも何かしらの歴史的記録を達成した選手がMVPになる傾向にある。')

st.header('６.2022年度アメリカンリーグMVPは？？')
st.write("11月18日にアメリカンリーグMVPが発表された。結果はジャッジが大谷翔平をおさえてのMVP受賞となった。記者30人中28名がジャッジ、残り2名が大谷に1位票を入れた。なおこの2名はエンゼルスの担当記者である。ここでもう一度両選手の2022年度成績を比べてみる。")

st.caption('アーロンジャッジの成績')
df = pd.read_csv('Bstats_2022.csv')
st.write(df.iloc[[15],:])
st.caption('大谷翔平の野手成績')
df = pd.read_csv('Bstats_2022.csv')
st.write(df.iloc[[13],:])
st.caption('大谷翔平の投手成績')
df = pd.read_csv('Pstats_2022.csv')
st.write(df)

df = pd.read_csv('Bstats_2022.csv')
df2022 = pd.DataFrame(data = df,columns = df.columns)

fig1 = px.scatter(
            df2022,
            x = 'OPS',
            y = 'HR',
            text = 'PLAYER',
            color = 'TEAM',
            size_max=30,
            height=500,
            width=800,
            size = 'HR',
            color_discrete_map={
               'BOS' : '#c03832',
               'NYY' : '#cb483e',
               'TB' : '#01013b',
               'TOR' : '#436599',
               'BOL' : '#d67732',
               'CLE' : '#c9424a',
               'MIN' : '#a9333c',
               'DET' : '#001640',
               'CWS' : '#000000',
               'KC' : '#8b8143',
               'HOU' : '#fe6301',
               'OAK' : '#ecb233',
               'SEA' : '#195b4c',
               'LAA' : '#620000',
               'TEX' : '#aa343c',
            }
        )
st.write(fig1) 

st.write('両選手の成績を比べてみてわかることは、大谷翔平が野手に専念せず投手との二刀流をしているという事実をもってしてもアーロンジャッジの成績は圧巻であるということだ。ホームラン数、打点数の二冠に輝き打率でもリーグ2位ともう少しで三冠王に輝く成績を残している。また上のバブルチャートを見て一目瞭然であるがOPSは1.111と他2人をそしてリーグ全体を圧倒している。加えて所属チームのNYYを地区優勝に導いたという点でジャッジがMVPを受賞することに異論はない。')

st.header('７　まとめ')

st.write('今回はstreamlitというPythonのオープンソースフレームワークを用いてデータ分析、データビジュアライゼーションに挑戦した。機械学習によるMVP予想など当初の目標に達することはできなかったがほぼプログラミング初心者の私が(金森君の力を借りつつも)ひとつのWebサイトを作り上げることが出来たという達成感が大きい。来年の大谷翔平選手の活躍に期待している。')

condition = st.slider('大谷翔平選手が来年MVPを取る可能性は？？',0,100,50)
'？？:', condition


st.header('８　参考文献')
st.write('・鳥越規央(2014).『勝てる野球の統計学セイバーメトリクス』.岩波書店')
st.write("・【MLBアウォード】2019MVPはマイクトラウトとコディーべリンジャーに決定　https://www.mlb4journal.com/trout-and-bellinger-won-2019-mvp-award/")
st.write("・【MLB】選手間投票が発表…アーロン・ジャッジがMVP、大谷翔平は2年連続の受賞はならず　https://olympics.com/ja/news/mlb-ohtani-shohei-2022-players-choice-awars")
st.write('・メジャーリーグ球団市場価値　https://www.tsp21.com/sports/mlb/feature/teamvalue2022.html')
st.write('・MLB各球団の球場を旅しよう！　https://freelance32.net/google/earth/gearth-mlb/')
st.write('・メジャーリーグで投手の成績スタッツ表記の意味！　　https://baseball.w-pickup.com/post-796/#toc7')
st.write("・MLB 歴代MVP　https://nipponbaseball.web.fc2.com/title/mvp_mlb.html")
st.write('・ミゲル・テハダ　　https://www.weblio.jp/wkpja/content/%E3%83%9F%E3%82%B2%E3%83%AB%E3%83%BB%E3%83%86%E3%83%8F%E3%83%80_%E3%83%9F%E3%82%B2%E3%83%AB%E3%83%BB%E3%83%86%E3%83%8F%E3%83%80%E3%81%AE%E6%A6%82%E8%A6%81')