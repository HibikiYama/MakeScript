# MakeScript.py

**PRIME観測scriptを作成するツール。**インタラクティブに観測scriptを作成できるCustom-Making modeと、あらかじめ用意したファイルから自動で観測scriptを作成するAuto-Making modeが選べる。
- ## 観測script  
  Goddard softwareでは**csv形式**の観測scriptが使用される。scriptに必要な情報は以下の20個。  
```
 Priority        : 0から順に数字が小さいほど優先される
 BlockID         : 観測ターゲットのID（現在はテキトーに連番でつく）
 Observer        : 観測者
 ObjectName      : ターゲットの名
 ObjectType      : ターゲットのタイプ
 RA              : ターゲットのRA
 DEC             : ターゲットのDEC
 RAoffset        : RAにオフセットを加える
 DECoffset       : DECにオフセットを加える
 ROToffset       : ローテーターの回転角にオフセットを加える
 Filter1         : Filter1を指定        # Filter1    : Open, Z, NB, Dark
 Filter2         : Filter2を指定        # Filter2    : Open, Y, J, H
 DitherType      : Ditheringの種類を指定 # DitherType : None, Circle, Random
 DitherRadius    : Ditheringの半径を指定
 DitherPhase     : Ditheringの開始角度を指定（Circle Ditheringのみ）
 DitherTotal     : Ditheringの回数を指定
 Images          : 撮影枚数を指定
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
  引数にoffsetとして使用するファイルと事前に準備したtargetの情報が入ったファイルを指定する。また、targetが銀河系座標なら-lb、赤道座標なら-rdを引数につけて実行。あとは**自動でscriptを作成**する。
  ```bash
  python MakeScript.py -offset standard.txt -list testlist.txt -rd 
  ```
    - **Auto-Adding mode** （-offset offset_name -list list_name -add script_name -lb or -rd）  
    Auto-Making modeのオプションモード。引数に既存のscriptを指定すると自動で新たな観測ターゲットを追加する。
    ```bash  
    python MakeScript.py -offset standard.txt -list testlist.txt -add obslist.csv -rd
    ```


# Required files
- ## offset (.txt, .list, .csv)  
Offset/ 以下に置いておく。観測scriptを作成する際に使用するoffset値の入ったファイル。観測するターゲットのタイプに合わせて作っておくと便利。デフォルトではList/ にstandard.txtとbulge.txtが入っている。
- ## List (.txt, .list, .csv)
List/ 以下に置いておく。観測targetの情報が入ったファイル。現在（2023/7/5~）はtarget名、RA or l、DEC or bに対応。（ローテーターのoffsetに対応予定）
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

# Author

* Hibiki Yama（山 響）
* 大阪大学 赤外線天文学
* yama@iral.ess.sci.osaka-u.ac.jp

# License

