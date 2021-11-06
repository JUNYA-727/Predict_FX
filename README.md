# Description
LSTMを用いた時系列分析により､FX､株価､ビットコインといった価格予測に役立ち｡システムトレードに使えると思ったから作成に至った｡
 
# Requirement
 開発に使用したライブラリなど
 
* tensorflow 2.5.0
* TA-Lib 0.4.20
* numpy 1.19.2
* pandas 1.2.3
* tensorflow_addons 0.14.0

# Features
明日のGBPUSDの価格を予測してくれます｡また､予測をした際に大きく上昇､上昇､変化あまり無し､下落､大きく下落と5パターンに予測をします｡
例としてこのように出力されます｡

<img width="321" alt="スクリーンショット 2021-11-07 1 04 35" src="https://user-images.githubusercontent.com/61785070/140616062-b9072a7f-694f-49ff-a7ea-bc9f71e89223.png">

# Model Creation Procedure

* 2017年10月04日から2021年11月03日の1日ごとの終値､始値､安値､高値のデータを使用しました｡
* 特徴量としてテクニカル分析で使用している｡SMA､MACD､RSIも特徴量に加えて学習していきました｡
* optimizerとしては､学習率の最適化を行ったSGD,Adam,RAdamの3つからモデルを作成しました｡

![sgd (1)](https://user-images.githubusercontent.com/61785070/140616914-e6a0aec1-c975-4cdd-a94c-b4928b6088c3.jpg)
![adam (1)](https://user-images.githubusercontent.com/61785070/140616921-1762c669-e8b6-4d28-9ded-0e09dabc1b57.jpg)
![radam (1)](https://user-images.githubusercontent.com/61785070/140616916-5f086a4a-755b-4000-b291-e8db83c57c09.jpg)


# Installation
 
Requirementで列挙したライブラリなどのインストール方法(MacOS)
```bash
pip install tensorflow 
```
```bash
brew install ta-lib
pip install TA-Lib
```
```bash
pip install numpy
```
```bash
pip install pandas
```
```bash
pip install tensorflow-addons
```
# Note
csvファイルには､時系列でデータが記載されていますが､11月3日までしかデータが記載していないので､それ以降のデータは下に数値を入力して更新して使用ください｡

参考になるサイト
https://jp.investing.com/currencies/gbp-usd-historical-data

# Author
* k.junya0727@gmail.com
* 具体的な詳細であったり､質問等ございましたらご気軽に連絡ください
