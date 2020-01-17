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

# 参考文献
定番の教科書として以下のものがあります。オンライン版(英語)は、なんと無料です。
* [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book.html), Richard S. Sutton and Andrew G. Barto著, 邦訳:[強化学習](https://www.morikita.co.jp/books/book/1990)

最近出た以下の教科書も前半に基本的な事項がまとまっていて読みやすいです。最近の高度な話題も書いてあるようです。
* [これからの強化学習](https://www.morikita.co.jp/books/book/3034), 牧野貴樹さん他(編著), 浅田稔さん他(共著)

迷路の環境や、REINFORCEアルゴリズムでは以下の本を参考にしました。
* [最強囲碁AI アルファ碁 解体新書 増補改訂版 アルファ碁ゼロ対応 深層学習、モンテカルロ木探索、強化学習から見たその仕組み](https://www.shoeisha.co.jp/book/detail/9784798157771),　三宅陽一郎さん(監修), 大槻知史さん著

強化学習の基礎的な部分については以下の教科書の後半部分に多くを学ばせていただきました
* [これならわかる深層学習入門(機械学習スタートアップシリーズ)](https://www.kspub.co.jp/book/detail/1538283.html), 瀧雅人さん著
