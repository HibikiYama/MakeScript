# MakeScript.py

**PRIME観測scriptを作成するツール**。インタラクティブに観測scriptを作成できるCustom-Making modeと、あらかじめ用意したファイルから自動で観測scriptを作成するAuto-Making modeが選べる。
- ## 観測script  
  Goddard softwareでは**csv形式**の観測scriptが使用される。scriptに必要な情報は以下の20個。  
```
 Priority        : 0から順に数字が小さいほど優先される
 BlockID         : 観測ターゲットのID（現在はテキトーに連番でつく）
 Observer        : 観測者
 ObjectName      : ターゲットの名
 ObjectType      : ターゲットのタイプ
 RA              : ターゲットのRA (h:m:s)
 DEC             : ターゲットのDEC (d:m:s)
 RAoffset        : RAにオフセットを加える (")
 DECoffset       : DECにオフセットを加える (")
 ROToffset       : ローテーターの回転角にオフセットを加える
 Filter1         : Filter1を指定        # Filter1    : Open, Z, NB, Dark
 Filter2         : Filter2を指定        # Filter2    : Open, Y, J, H
 DitherType      : Ditheringの種類を指定 # DitherType : None, Circle, Random
 DitherRadius    : Ditheringの半径を指定 (")
 DitherPhase     : Ditheringの開始角度を指定（Circle Ditheringのみ）
 DitherTotal     : Ditheringの回数を指定 (1以上、NINT=DitherTotal*Images)
 Images          : 撮影枚数を指定 (1以上)
 IntegrationTime : 露光時間を指定
 Comment1        : コメント欄1
 Comment2        : コメント欄2
 ```

- ## How to use  
  script作成のoffsetとして使用するファイルを必ず指定して実行する。作成された観測scriptは Script/ 以下に置かれる。  

  - **Custom-Making mode** （-offset offset_name）   
  引数にoffsetとして使用するファイルを指定して流す。**インタラクティブ**に操作できる。新規作成、追加作成（Custom-Adding mode）が選択できる。  
  ```bash
  python MakeScript.py -offset standard.txt  
  ```
  - **Auto-Making mode** （-offset offset_name -list list_name -lb or -rd）  
  **観測提案スクリプトを観測スクリプトに変換する際はこのmodeを使用。**  
  引数にoffsetとして使用するファイルと事前に準備したtargetの情報が入ったファイルを指定する（standard.txtを推奨）。また、targetが銀河系座標なら-lb、赤道座標なら-rdを引数につけて実行。あとは**自動でscriptを作成**する。*ver1.4~ はtargetの情報が入ったファイルとして観測提案スクリプトを指定。基本的には-rdで実行。またobjectNameがAll-sky-gridもしくはBulge-gridの場合、各targetの位置と最適gird（RAoffset, DECoffsetも考慮）が表示されるので、観測者は問題がないか確認してEnterをし次に進む。
  ```bash
  python MakeScript.py -offset standard.txt -list testlist.txt -rd 
  ```
    - **Auto-Adding mode** （-offset offset_name -list list_name -add script_name -lb or -rd）  
    Auto-Making modeのオプションモード。引数に既存のscriptを指定すると自動で新たな観測ターゲットを追加する。基本的な機能はAuto-Making modeを参照。
    ```bash  
    python MakeScript.py -offset standard.txt -list testlist.txt -add obslist.csv -rd
    ```

# SelectScript.py

**選択したscript（例えばgrid）の中から指定した座標に近いターゲットを選び新たなscriptを作成する**。
- ## How to use  
  引数にはscript名、指定するRA、指定するDECを必ず入れる。作成された観測scriptは Script/ 以下に置かれる。デフォルトでは指定した座標に近い20個のターゲットを選ぶが、選びたいターゲット数を引数に入れることでカスタム可能。
  ```bash
  python SelectScript.py -script scriptname.csv -RA hh:mm:ss -DEC dd:mm:ss (-num 30)
  ```

# Required files
- ## offset (.txt, .list, .csv)  
Offset/ 以下に置いておく。観測scriptを作成する際に使用するoffset値の入ったファイル。観測するターゲットのタイプに合わせて作っておくと便利。デフォルトではList/ にstandard.txtとbulge.txtが入っている。
- ## List (.txt, .list, .csv)
List/ 以下に置いておく。観測targetの情報が入ったファイル。ver1.4~ は観測提案スクリプトに対応。
```bash
GB1 3.919806 2.706028
GB2 2.718806 2.706028
GB3 1.517806 2.706028
GB4 0.316806 2.706028
```

# Features

# Requirement

# Installation

# Usage

# Note
- ## ROToffset
ローテーターのオフセットは引数に-lbをつけると検出器が銀河系座標に、-rdをつけると検出器が赤道座標に沿うように自動で数値が入る。
# Author

* Hibiki Yama（山 響）
* 大阪大学 赤外線天文学
* yama@iral.ess.sci.osaka-u.ac.jp

# License

