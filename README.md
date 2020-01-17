# HPC-Phys_tutorial_and_hands-on

[第6回 High Performance Computing Physics (HPC-Phys) 勉強会](http://hpc-phys.kek.jp/workshop/workshop200131.html)で行う予定のチュートリアル/ハンズオン用のリポジトリです。このリポジトリごとダウンロードしておいてください。当日は
* [section1_handson.ipynb](https://github.com/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/section1_handson.ipynb)
* [section2_handson.ipynb](https://github.com/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/section2_handson.ipynb)
* [section3_handson.ipynb](https://github.com/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/section3_handson.ipynb)

を使います。python環境がない人は[GoogleColabでの当日用](https://colab.research.google.com/github/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/handson_for_colab.ipynb)を使ってください。こちらは実行にはGoogleアカウントが必要です。jupyter notebookと同じように、各セルは`shift`+`enter`で実行できますし、スマートフォンなどからでも▶ボタンをクリックすれば実行できます。

GoogleColabでそのまま実行しようとすると
>警告: このノートブックは Google が作成したものではありません。<br>
このノートブックは GitHub から読み込まれています。Google に保存されているデータへのアクセスが求められたり、他のセッションからデータや認証情報が読み取られたりする場合があります。このノートブックを実行する前にソースコードをご確認ください。

と出るかと思いますが、そのまま実行でもいいですし、この警告が気になる方は左上のメニューにある「ドライブにコピー」した後、自分のドライブから開くのが良いと思います。

# 内容

[GoogleColab](https://colab.research.google.com/github/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/for_colab.ipynb)からも見れます。

### **[Section1:マルコフ決定過程](https://github.com/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/section1.ipynb)**

 用語などを実例を交え解説します。

### **[Section2:価値推定に基づく学習アルゴリズム](https://github.com/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/section2.ipynb)**

 価値関数とよばれる関数を推定する強化学習の手法を説明をします。

### **[Section3:方策最適化に基づく学習アルゴリズム](https://github.com/AkinoriTanaka-phys/HPC-Phys_tutorial_and_hands-on/blob/master/section3.ipynb)**

方策を直接最適化しにかかる強化学習の手法を説明します。

# 環境
一応私の環境を書いておきますと
```
$ python
Python 3.5.1 |Anaconda custom (x86_64)| (default, Jun 15 2016, 16:14:02) 
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
です。anacondaが入っていれば動くと思います。
