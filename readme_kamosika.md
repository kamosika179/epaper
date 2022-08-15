

## できること / What can I do

togglから今週の作業実行時間を取得し、画像を作成し、epaper(2.13inch)に表示します。

get day working time while this week from toggl working entity.

## 使い方 / How to use

・requestsを導入する / install requests module

'''
pip install requests
'''

・環境変数TOGGL_APIにAPIキーを設定する / setting environment variable "TOGGL_API=\[APIKEY\]"


・settingfile.txtを作成し、1行目にメールアドレス、2行目にワークスペースidを入力する。 / create settingfile.txt and put email adrress at line 1 and workspaceid at line 2.

・makeimage.pyのフォントの設定をする / setting font in makeimage.py

・eink2_13_show_toggltime.pyを実行する / run eink2_13_show_toggltime.py

